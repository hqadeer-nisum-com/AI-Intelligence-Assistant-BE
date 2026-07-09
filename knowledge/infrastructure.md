# Infrastructure

## Purpose

This document explains the infrastructure technologies used across our engineering platform.

It covers local development, containers, orchestration, deployment concepts, troubleshooting, and best practices.

The goal is to help engineers understand how applications run locally and in production.

---

# Infrastructure Overview

Our engineering platform uses:

- Docker
- Rancher Desktop
- Kubernetes
- Container Images
- Containers
- Namespaces
- Services
- Deployments
- ConfigMaps
- Secrets
- Ingress
- Load Balancers

---

# Docker

## What is Docker?

Docker is a container platform used to package applications together with their dependencies.

Benefits:

- Consistent environments
- Easy deployment
- Fast onboarding
- Reproducible builds

---

## Docker Concepts

- Image
- Container
- Volume
- Network
- Dockerfile
- Docker Compose

---

## Common Docker Commands

Build image

docker build -t app .

Run container

docker run -p 3000:3000 app

List containers

docker ps

Stop container

docker stop CONTAINER_ID

Remove container

docker rm CONTAINER_ID

List images

docker images

Remove image

docker rmi IMAGE_ID

---

## Docker Best Practices

- Keep images small.
- Use multi-stage builds.
- Don't run containers as root.
- Ignore unnecessary files.
- Pin image versions.
- Use environment variables.

---

# Rancher Desktop

## What is Rancher Desktop?

Rancher Desktop is a local development environment that provides:

- Kubernetes
- Container runtime
- Docker-compatible CLI
- Local container management

It allows developers to run Kubernetes locally without needing a cloud cluster.

---

## Why We Use Rancher Desktop

- Local Kubernetes development
- Local testing
- Container management
- Faster onboarding
- Production-like environment

---

## Components

- Kubernetes
- containerd
- Docker CLI compatibility
- kubectl

---

## Installation

Typical steps:

1. Install Rancher Desktop.
2. Enable Kubernetes.
3. Wait until Kubernetes starts.
4. Verify using kubectl.

---

## Verify Installation

kubectl version

kubectl get nodes

kubectl get pods

---

## Common Rancher Desktop Issues

Kubernetes won't start

Possible causes:

- Insufficient memory
- Port conflicts
- Corrupted cache

Docker CLI not working

Restart Rancher Desktop.

Verify PATH.

Cluster not responding

Restart Kubernetes.

---

# Kubernetes

## What is Kubernetes?

Kubernetes is a container orchestration platform.

It manages containers automatically.

---

## Why We Use Kubernetes

- Auto scaling
- Self healing
- Rolling deployments
- Service discovery
- High availability

---

## Kubernetes Architecture

Control Plane

↓

Worker Nodes

↓

Pods

↓

Containers

---

## Core Concepts

Pod

Smallest deployable unit.

Deployment

Manages Pods.

Service

Provides networking.

Namespace

Logical isolation.

ConfigMap

Stores configuration.

Secret

Stores sensitive data.

Ingress

Routes external traffic.

ReplicaSet

Maintains Pod count.

Persistent Volume

Stores persistent data.

---

## Common kubectl Commands

Get pods

kubectl get pods

Get deployments

kubectl get deployments

Get services

kubectl get svc

Describe pod

kubectl describe pod POD_NAME

View logs

kubectl logs POD_NAME

Delete pod

kubectl delete pod POD_NAME

Restart deployment

kubectl rollout restart deployment DEPLOYMENT_NAME

---

## Debugging Kubernetes

Check pod status

Check logs

Describe deployment

Check events

Verify ConfigMaps

Verify Secrets

Check Ingress

Verify Services

---

## Common Kubernetes Problems

CrashLoopBackOff

ImagePullBackOff

Pending Pods

OOMKilled

Failed Mount

Network Errors

---

## Best Practices

Use namespaces.

Avoid hardcoded configuration.

Store secrets securely.

Monitor logs.

Use health checks.

Use resource limits.

Use rolling deployments.

---

# Deployment Flow

Developer

↓

GitHub

↓

CI

↓

Container Build

↓

Docker Image

↓

Container Registry

↓

Kubernetes

↓

Service

↓

Ingress

↓

Production

---

# Company Notes

General recommendations:

- Rancher Desktop is used for local Kubernetes development.
- Containers should mirror production as closely as possible.
- Kubernetes deployments should be repeatable.
- Configuration should come from environment variables.
- Secrets should never be committed to Git.

---

# Troubleshooting

Docker won't start

Restart Docker or Rancher Desktop.

Pods are Pending

Check node resources.

ImagePullBackOff

Verify image name and registry access.

CrashLoopBackOff

Inspect container logs.

Service unreachable

Verify Service and Ingress configuration.

kubectl not found

Install kubectl and verify PATH.

---

# Interview Questions

- What is Docker?
- Difference between Image and Container?
- What is Rancher Desktop?
- Why do we use Rancher Desktop?
- What is Kubernetes?
- What is a Pod?
- Difference between Deployment and Pod?
- What is a Service?
- What is Ingress?
- What is ConfigMap?
- What are Secrets?
- Explain rolling deployments.
- Explain Kubernetes architecture.
- How do you debug a Pod?

---

# Resources

Docker

https://docs.docker.com/

Rancher Desktop

https://docs.rancherdesktop.io/

Kubernetes

https://kubernetes.io/docs/

kubectl

https://kubernetes.io/docs/reference/kubectl/