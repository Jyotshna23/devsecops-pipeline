from flask import Flask, jsonify
import psutil

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"message": "DevSecOps Pipeline Running!", "status": "healthy"})


@app.route('/health')
def health():
    return jsonify({"status": "ok"})


@app.route('/metrics')
def metrics():
    # Basic resource visibility - useful for spotting a runaway process
    # before it takes the whole service down, not full observability.
    return jsonify({
        "cpu_percent": psutil.cpu_percent(interval=0.1),
        "memory_percent": psutil.virtual_memory().percent,
    })


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found", "status": 404}), 404


@app.errorhandler(500)
def server_error(error):
    # Never leak a raw stack trace to the client - log it server-side instead.
    app.logger.error(f"Internal server error: {error}")
    return jsonify({"error": "Internal server error", "status": 500}), 500


if __name__ == '__main__':
    # Binding to 0.0.0.0 is intentional here - the app runs inside a Docker
    # container, and the container's own port mapping (not this bind) is
    # what controls what's actually reachable from outside.
    app.run(host='0.0.0.0', port=5000)  # nosec B104
