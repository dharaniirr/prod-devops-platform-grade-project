Production-Grade CI Pipeline for Containerized Applications

This repository demonstrates a production-style Continuous Integration (CI) pipeline for a containerized backend service, focusing on build reliability, security, and artifact readiness rather than automated deployment.

The application itself is intentionally simple; the emphasis is on DevOps correctness and system design.

Overview

The project implements a CI workflow that automatically:

Builds a Docker image using a multi-stage Dockerfile

Scans the image for security vulnerabilities

Publishes versioned, deployable artifacts to a container registry

Deployment is intentionally manual and controlled, aligning with common production practices.

Architecture

Application

FastAPI backend

PostgreSQL database

/health endpoint validates real database connectivity

Containerization

Multi-stage Dockerfile

Non-root runtime user

Clear separation between build and runtime layers

Local Orchestration

Docker Compose

PostgreSQL health checks

API starts only after database is healthy

Environment-based configuration using env_file

Continuous Integration (CI)

CI is implemented using GitHub Actions and is triggered on every push to the main branch.

CI Pipeline Steps

Checkout source code

Build Docker image

Scan image using Trivy

Pipeline fails on HIGH or CRITICAL vulnerabilities

Tag image with:

latest

commit SHA

Publish image to GitHub Container Registry (GHCR)

This ensures that every commit produces a secure, versioned, deployable artifact.

Container Registry

Docker images are published automatically to:

ghcr.io/dharaniirr/prod-devops-platform-grade-project


Available tags:

latest

<commit-sha>

Deployment Model

This project follows a CI-only model.

Builds and artifact publishing are fully automated

Deployment is manual and controlled

Runtime environments pull images directly from the registry

This approach reflects how many real production systems operate, especially where change control or audits are required.

What This Project Demonstrates

Production-style CI pipeline design

Secure container build practices

Vulnerability scanning with enforced failure thresholds

Artifact versioning and registry publishing

Environment-driven configuration

Practical debugging of container, build, and runtime issues

What This Project Does Not Do (By Design)

No automated deployment (no CD)

No infrastructure provisioning

No Kubernetes or GitOps

These are intentional exclusions to keep the scope focused and accurate.

Future Enhancements (Optional)

Add controlled CD via SSH-based deployment

Infrastructure provisioning with Terraform

Kubernetes-based deployment with GitOps tools

Observability (metrics and logging)

Key Takeaway

Continuous Integration is about producing trusted, deployable artifacts.
Deployment should be deliberate, observable, and controlled.

