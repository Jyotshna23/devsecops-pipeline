from flask import Flask, jsonify, Response, request
from prometheus_client import Counter, Gauge, Histogram, generate_latest, CONTENT_TYPE_LATEST
import psutil
import logging
import json
import time

app = Flask(__name__)

# Structured JSON logging for observability pipelines
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Prometheus Metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total HTTP requests', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'HTTP request latency in seconds', ['endpoint'])
CPU_USAGE = Gauge('system_cpu_usage_percent', 'Current system CPU usage percentage')
MEMORY_USAGE = Gauge('system_memory_usage_percent', 'Current system Memory usage percentage')


@app.before_request
def start_timer():
    request.start_time = time.time()


@app.after_request
def log_request(response):
    if hasattr(request, 'start_time'):
        latency = round(time.time() - request.start_time, 4)
        REQUEST_LATENCY.labels(endpoint=request.path).observe(latency)
        REQUEST_COUNT.labels(method=request.method, endpoint=request.path, status=response.status_code).inc()
        app.logger.info(json.dumps({
            "method": request.method,
            "endpoint": request.path,
            "status": response.status_code,
            "latency_sec": latency
        }))
    return response


@app.route('/')
def home():
    return jsonify({"message": "DevSecOps & Observability Pipeline Running!", "status": "healthy"})


@app.route('/health')
def health():
    return jsonify({"status": "ok"})


@app.route('/metrics')
def metrics():
    # Prometheus-compatible metrics exposition endpoint
    CPU_USAGE.set(psutil.cpu_percent(interval=0.1))
    MEMORY_USAGE.set(psutil.virtual_memory().percent)
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found", "status": 404}), 404


@app.errorhandler(500)
def server_error(error):
    # Never leak a raw stack trace to the client - log it server-side instead.
    app.logger.error(json.dumps({"error": "Internal server error", "details": str(error)}))
    return jsonify({"error": "Internal server error", "status": 500}), 500


if __name__ == '__main__':
    # Binding to 0.0.0.0 is intentional here - the app runs inside a Docker
    # container, and the container's own port mapping (not this bind) is
    # what controls what's actually reachable from outside.
    app.run(host='0.0.0.0', port=5000)  # nosec B104
