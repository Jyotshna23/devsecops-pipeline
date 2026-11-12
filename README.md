# 🔐 DevSecOps CI/CD Pipeline

`Pipeline: Passing` • `Python 3.9 / 3.10` • `Security: Bandit SAST` • `Container Scan: Aqua Trivy` • `Tests: Pytest` • `Docker: Alpine`

**An automated Shift-Left DevSecOps pipeline built with GitHub Actions that enforces static security analysis, unit testing, container vulnerability scanning, and runtime health checks on every code push.**

---

## 🚨 Problem Statement

In modern software delivery, security vulnerabilities cost organizations millions of dollars every year. Traditional development workflows treat security as an afterthought — developers write code, ship it, and only discover critical flaws after reaching production.

This project solves that challenge by embedding automated **Security Gates (SAST + Container Scanning)** and **Quality Gates (Unit + Smoke Tests)** directly into the CI/CD pipeline, ensuring every single commit is verified before deployment.

---

## ⚡ What This Project Does

Every time code is pushed to `main` or opened as a pull request, **GitHub Actions** automatically executes a 6-stage verification workflow with zero human intervention:

- ✅ **Checks out the repository** and configures an isolated Python environment with `pip` caching for fast builds.
- ✅ **Runs Bandit SAST (`bandit -r app.py -f txt -ll`)** to detect common Python security flaws and fails the build immediately on `MEDIUM` or `HIGH` severity issues.
- ✅ **Executes automated unit tests (`pytest test_app.py -v`)** to verify API responses, system telemetry, and error handling.
- ✅ **Builds a lightweight Docker image** using `python:3.10-alpine` with optimized layer caching.
- ✅ **Audits the container image with Aqua Trivy** to detect `CRITICAL` and `HIGH` CVEs across OS packages and Python libraries.
- ✅ **Performs live container smoke tests** by starting the container on port `5000`, verifying `/health` and `/metrics` via `curl --fail`, and cleaning up resources.

---

## 🏗️ Pipeline Architecture

```text
  Git Push / Pull Request (main)
               │
               ▼
  [1. Environment Setup]   ──► Python + cached pip dependencies
               │
               ▼
  [2. SAST Security Gate]  ──► Bandit scan (-ll blocks MEDIUM/HIGH risks)
               │
               ▼
  [3. Unit Testing]        ──► Pytest verbose test suite (test_app.py)
               │
               ▼
  [4. Container Build]     ──► Docker image (python:3.10-alpine)
               │
               ▼
  [5. CVE Vulnerability]   ──► Aqua Trivy scan (CRITICAL & HIGH audit)
               │
               ▼
  [6. Runtime Smoke Test]  ──► Live container check on /health & /metrics
```

---

## 🔌 Microservice API Endpoints

| Method | Endpoint | Description | Sample JSON Response |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Root service health banner | `{"message": "DevSecOps Pipeline Running!", "status": "healthy"}` |
| `GET` | `/health` | Container liveness probe | `{"status": "ok"}` |
| `GET` | `/metrics` | Live CPU & memory usage (`psutil`) | `{"cpu_percent": 4.2, "memory_percent": 38.5}` |

---

## 🛠️ Tech Stack & Security Tooling

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **CI/CD Automation** | GitHub Actions (`pipeline.yml`) | Automated build, test, and security gate orchestration |
| **Static Security (SAST)** | Bandit (`1.7.8`) | Scans Python source code for insecure functions & patterns |
| **Container Security** | Aqua Security Trivy | Scans Docker Alpine OS & dependencies for known CVEs |
| **Containerization** | Docker (`python:3.10-alpine`) | Minimal-footprint container packaging |
| **Backend Microservice** | Python, Flask (`3.0.2`), `psutil` (`5.9.8`) | Hardened REST API with structured JSON error handling |
| **Automated Testing** | Pytest (`8.0.2`), `curl` | Unit testing and post-build container runtime verification |

---

## 📂 Repository Structure

```text
devsecops-pipeline/
├── .github/
│   └── workflows/
│       └── pipeline.yml    # Automated 6-stage GitHub Actions DevSecOps workflow
├── Dockerfile              # Lightweight python:3.10-alpine container image
├── app.py                  # Hardened Flask microservice (/health, /metrics, error handlers)
├── test_app.py             # Pytest unit and API endpoint test suite
├── requirements.txt        # Pinned application and security scanning dependencies
└── README.md               # Project documentation
```

---

## 🚀 Quick Start (Local & Docker)

### Run Locally with Python

```bash
# 1. Clone the repository
git clone https://github.com
cd devsecops-pipeline

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run SAST security scan & unit tests
bandit -r app.py -f txt -ll
pytest test_app.py -v

# 4. Start the Flask microservice
python app.py
```

### Build & Test with Docker

```bash
# Build the Alpine Docker image
docker build -t devsecops-pipeline:latest .

# Run the container
docker run -d -p 5000:5000 --name devsecops-app devsecops-pipeline:latest

# Verify endpoints
curl http://localhost:5000/health
curl http://localhost:5000/metrics
```

---

## 👩‍💻 Author

**Jyotshna Pogiri** — Python, Cloud & DevSecOps Enthusiast
- **GitHub:** ://github.com
- **LinkedIn:** ://linkedin.com
- **Email:** jahnavipogiri3@gmail.com
