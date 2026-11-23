# 🔐 Cloud-Native Observability & DevSecOps CI/CD Pipeline

`Pipeline: Passing` • `Python 3.11` • `Observability: Prometheus & Grafana` • `Security: Bandit SAST & Aqua Trivy` • `Orchestration: Docker & Kubernetes`

**An end-to-end DevSecOps and Observability pipeline built with GitHub Actions, Prometheus, Grafana, Docker, and Kubernetes—enforcing automated security gates, runtime health checks, structured JSON logging, and threshold-based alerting.**

---

## 🚨 Problem Statement

Modern cloud-native services face two major operational risks: shipping insecure code to production and operating without real-time visibility into system health. Without automated security gates and proactive observability, teams discover vulnerabilities and resource bottlenecks only after service degradation occurs.

This project solves both challenges by combining:
1. **Shift-Left DevSecOps Gates:** Automated static analysis (Bandit), unit testing (Pytest), CVE container scanning (Aqua Trivy), and live runtime smoke tests on every push.
2. **Full-Stack Observability & Alerting:** Prometheus metric instrumentation (`/metrics`), structured JSON request logging, Grafana dashboards, and automated threshold alerting rules (`alerts.yml`).

---

## ⚡ What This Project Does

- ✅ **Automated 6-Stage CI/CD Pipeline:** Every push or pull request to `main` triggers GitHub Actions to run Bandit SAST, 8 Pytest unit tests, Docker image builds, Trivy CVE vulnerability scans, and live `curl` container smoke tests.
- ✅ **Prometheus Instrumentation (`/metrics`):** Exposes real-time application and system telemetry (`app_requests_total`, `app_request_latency_seconds`, `system_cpu_usage_percent`, `system_memory_usage_percent`) via `prometheus-client`.
- ✅ **Threshold-Based Alerting (`alerts.yml`):** Configures Prometheus alert rules to trigger warnings/critical alerts on high memory usage (`> 80%`), high CPU utilization (`> 85%`), or service downtime (`up == 0`).
- ✅ **Structured JSON Request Logging:** Emits machine-parseable JSON logs (`method`, `endpoint`, `status`, `latency_sec`) ready for centralized log aggregation pipelines.
- ✅ **Hardened Container & Kubernetes Ready:** Runs as a non-root user (`appuser`) on `python:3.11-slim` with Docker `HEALTHCHECK` and Kubernetes Deployment/Service manifests (2 replicas, liveness/readiness probes, CPU/memory limits).

---

## 🏗️ System & Pipeline Architecture

```text
  Git Push / Pull Request (main)
               │
               ▼
  [1. Environment Setup]   ──► Python 3.11 + cached pip dependencies
               │
               ▼
  [2. SAST Security Gate]  ──► Bandit scan (-ll blocks MEDIUM/HIGH risks)
               │
               ▼
  [3. Unit & API Testing]  ──► Pytest suite verifying routes & Prometheus metrics
               │
               ▼
  [4. Container Build]     ──► Hardened non-root Docker image (python:3.11-slim)
               │
               ▼
  [5. CVE Vulnerability]   ──► Aqua Trivy scan (CRITICAL & HIGH audit)
               │
               ▼
  [6. Runtime Smoke Test]  ──► Live container verification on /health & /metrics

  ──────────────────────────────────────────────────────────────────────────

  [Flask Microservice :5000] ──(/metrics)──► [Prometheus :9090] ──► [Grafana :3000]
                                                    │
                                             (alerts.yml rules)
                                                    ▼
                                        High CPU / Memory / Down Alerts
```

---

## 🔌 Microservice API Endpoints

| Method | Endpoint | Description | Response Format |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Root service status banner | `{"message": "DevSecOps & Observability Pipeline Running!", "status": "healthy"}` |
| `GET` | `/health` | Container & Kubernetes liveness/readiness probe | `{"status": "ok"}` |
| `GET` | `/metrics` | Prometheus-compatible CPU, memory, request count & latency metrics | `text/plain; version=0.0.4` (`system_cpu_usage_percent`, etc.) |

---

## 🛠️ Tech Stack & Tooling

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Observability & Alerting** | Prometheus, Grafana, `prometheus-client` | Metric scraping, visualization dashboards, and threshold alerts |
| **CI/CD Automation** | GitHub Actions (`pipeline.yml`) | Automated build, test, security, and smoke-test orchestration |
| **Containerization & Orchestration** | Docker, Docker Compose, Kubernetes | Non-root container packaging, local monitoring stack, and K8s manifests |
| **Static & Container Security** | Bandit (`1.7.8`), Aqua Trivy | Python SAST scanning and OS/library CVE vulnerability detection |
| **Backend & Logging** | Python `3.11`, Flask (`3.0.2`), Gunicorn, `psutil` | Production-grade REST API with structured JSON logging |
| **Automated Testing** | Pytest (`8.0.2`), `curl` | Unit testing and post-build container verification |

---

## 📂 Repository Structure

```text
devsecops-pipeline/
├── .github/
│   └── workflows/
│       └── pipeline.yml      # Automated 6-stage GitHub Actions DevSecOps workflow
├── k8s/
│   └── deployment.yaml       # Kubernetes Deployment (2 replicas, probes, limits) & Service
├── Dockerfile                # Hardened non-root python:3.11-slim container image
├── docker-compose.yml        # Multi-container stack: Flask App + Prometheus + Grafana
├── prometheus.yml            # Prometheus scrape configuration targeting Flask /metrics
├── alerts.yml                # Alerting rules for HighMemoryUsage, HighCPUUsage & ServiceDown
├── app.py                    # Flask microservice with Prometheus metrics & JSON logging
├── test_app.py               # Pytest unit and endpoint test suite
├── requirements.txt          # Pinned Python dependencies
└── README.md                 # Project documentation
```

---

## 🚀 Quick Start

### 1. Run Full Observability Stack (App + Prometheus + Grafana)

```bash
# Clone the repository
git clone https://github.com
cd devsecops-pipeline

# Start Flask service, Prometheus, and Grafana
docker-compose up --build -d
```

- **Flask API & Metrics:** `http://localhost:5000/metrics`
- **Prometheus UI & Alerts:** `http://localhost:9090`
- **Grafana Dashboards:** `http://localhost:3000` (Default login: `admin` / `admin`)

### 2. Run Security Scans & Unit Tests Locally

```bash
pip install -r requirements.txt
pip install pytest==8.0.2 bandit==1.7.8

# Run SAST security scan & unit tests
bandit -r app.py -f txt -ll
pytest test_app.py -v
```

---

## 👩‍💻 Author

**Jyotshna Pogiri** — Cloud, Infrastructure & DevSecOps Engineer
- **GitHub:** [github.com/Jyotshna23](https://github.com)
- **LinkedIn:** [://linkedin.com](https://www.://linkedin.com)
- **Email:** jahnavipogiri3@gmail.com
