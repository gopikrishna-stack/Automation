# Security Automation Project

## Overview
This project demonstrates an end-to-end DevSecOps pipeline that integrates
security checks into CI/CD using GitHub Actions.

## Tools Used
- GitHub
- GitHub Actions
- Semgrep (SAST)
- Docker
- Trivy (Container Security)
- OWASP ZAP (DAST)

## Pipeline Flow
1. Code pushed to GitHub
2. SAST scan using Semgrep
3. Docker image build
4. Container image scan using Trivy
5. Application runtime scan using OWASP ZAP

## Key Learnings
- Shift-left security
- CI/CD security automation
- SAST, Container, and DAST integration
