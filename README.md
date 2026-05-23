# 🔐 DevSecOps CI/CD Pipeline

![Pipeline Status](https://github.com/Jyotshna23/devsecops-pipeline/actions/workflows/pipeline.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.9-blue)
![Security](https://img.shields.io/badge/Security-Bandit-red)
![Tests](https://img.shields.io/badge/Tests-Pytest-green)

## 🚨 Problem Statement

In modern software development, security vulnerabilities cost companies millions of dollars every year. Traditional development workflows treat security as an afterthought — developers write code, ship it, and only discover vulnerabilities after a breach occurs. This project solves that problem by integrating security scanning and automated testing directly into the development pipeline, so every single line of code is automatically scanned for vulnerabilities before it reaches production.

## ⚡ What This Project Does

This is a fully automated DevSecOps pipeline built with GitHub Actions. Every time a developer pushes code, the pipeline automatically triggers and runs through the following stages without any human intervention:

- ✅ Pulls the latest code from the repository
- ✅ Sets up a clean Python environment
- ✅ Installs all required dependencies
- ✅ Runs Bandit security scanner to detect vulnerabilities like SQL injection, hardcoded passwords, and insecure functions
- ✅ Runs all automated test cases using Pytest
- ✅ Reports Pass or Fail within seconds

The entire process completes in under 20 seconds, replacing what would otherwise take a developer hours to do manually.

## 🌍 Real World Applications

**🏥 Healthcare** — Hospitals use DevSecOps pipelines to protect patient data and comply with HIPAA regulations. A single vulnerability can expose thousands of patient records.

**🏦 Banking & Fintech** — Banks use automated security scanning to prevent data breaches. The average cost of a data breach in the financial sector is over $5 million.

**🏛️ Government** — Defense organizations use compliance pipelines to ensure every deployment meets strict security standards automatically.

**🚀 Startups** — Small teams use CI/CD pipelines to ship features faster without sacrificing code quality.

## 🏗️ Technical Architecture
Developer pushes code to GitHub
            |
            v
   GitHub Actions triggered
            |
            v
   Environment setup (Python 3.9)
            |
            v
   Dependencies installed
            |
            v
   Bandit Security Scan
   - Scans for 30+ vulnerability types
   - Detects hardcoded secrets
   - Identifies insecure function usage
            |
            v
   Pytest Automated Tests
   - Tests all API endpoints
   - Validates response codes
   - Ensures application health
            |
            v
   Pipeline Result: Pass or Fail

## 📊 Pipeline Metrics

| Metric | Value |
|--------|-------|
| Lines of code scanned | 10 |
| Vulnerability types checked | 30+ |
| Automated test cases | 2 |
| Average pipeline duration | 17 seconds |
| Manual effort replaced | 2-3 hours per deployment |

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| GitHub Actions | CI/CD automation engine |
| Bandit | Python static security analysis |
| Pytest | Automated testing framework |
| Flask | Web application layer |
| Python 3.9 | Runtime environment |

## 🚀 How To Run Locally

git clone https://github.com/Jyotshna23/devsecops-pipeline.git
cd devsecops-pipeline
pip install -r requirements.txt
python app.py
pytest test_app.py -v

## 📁 Project Structure

devsecops-pipeline/
├── app.py                        
├── test_app.py                   
├── requirements.txt              
└── .github/
    └── workflows/
        └── pipeline.yml          

## 👩‍💻 Author

**Jyotshna Pogiri** — Software Engineer | DevSecOps Enthusiast

GitHub: https://github.com/Jyotshna23
Email: jahnavipogiri3@gmail.com
