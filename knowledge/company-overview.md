# Company Overview

## Purpose

This document provides an overview of the engineering platform, technology stack, development workflow, architecture, and engineering standards used across the organization.

The goal is to help engineers understand how the platform works and provide context for onboarding, development, troubleshooting, and architectural decisions.

---

# Engineering Platform

The engineering platform is built using a modern frontend architecture that supports multiple brands and multiple engineering teams.

The platform emphasizes:

- Scalability
- Reusability
- Maintainability
- Performance
- Independent deployments
- Shared engineering standards

---

# Technology Stack

## Frontend

- Vue 2
- Vue 3
- Vuex
- JavaScript
- TypeScript
- HTML5
- CSS3

## Backend

- Backend For Frontend (BFF)
- REST APIs

## Build Tools

- Webpack
- Vite

## Testing

- Jest

## Version Control

- Git
- GitHub

## CI/CD

- GitHub Actions
- Jenkins

## Deployment

- Akamai CDN

## Infrastructure

- Docker
- Rancher Desktop
- Kubernetes

## Authentication

- OAuth 2.0
- JWT Authentication

---

# Engineering Principles

The engineering team follows several core principles:

- Write clean and maintainable code.
- Prefer reusable components over duplicated code.
- Keep Pull Requests focused and small.
- Build reusable utilities whenever possible.
- Write unit tests for business logic.
- Follow coding standards.
- Review code before merging.
- Optimize for performance.
- Maintain backward compatibility for shared components.

---

# Development Workflow

Typical engineering workflow:

1. Receive a Jira ticket.
2. Understand the business requirement.
3. Discuss architecture if needed.
4. Create a feature branch.
5. Implement the feature.
6. Write unit tests.
7. Perform local testing.
8. Open a Pull Request.
9. Receive code review.
10. Address review comments.
11. Merge into the target branch.
12. GitHub Actions validates the code.
13. Jenkins builds the application.
14. Deploy to Akamai.
15. QA verifies the deployment.
16. Release to Production.

---

# Architecture Overview

The platform uses a Micro Frontend architecture.

Characteristics include:

- Multiple frontend applications
- Independent deployments
- Shared component libraries
- Shared utilities
- Shared design system
- Shared configuration

The backend uses a Backend For Frontend (BFF) layer to simplify communication between frontend applications and backend services.

---

# Monorepo

The frontend applications are maintained in a monorepo.

Advantages include:

- Shared packages
- Shared utilities
- Easier dependency management
- Consistent coding standards
- Shared build configuration
- Shared testing strategy

---

# Multiple Brands

The platform supports multiple brands.

Each brand may have:

- Different configuration
- Different assets
- Different themes
- Different feature flags
- Different deployment pipelines

Shared code should remain brand-independent whenever possible.

---

# Shared Components

Shared components are used across multiple applications and brands.

Goals:

- Avoid duplicate implementations.
- Ensure consistent user experience.
- Improve maintainability.
- Reduce development effort.

Shared components should be:

- Reusable
- Configurable
- Well tested
- Backward compatible

---

# Repository Structure

The engineering ecosystem consists of multiple repositories.

Examples include:

- Frontend Monorepo
- Backend Services
- Shared Component Library
- Shared Utilities
- Brand Configuration Repository
- Shoppable Display Repository
- CI/CD Repository

Each repository has a clearly defined responsibility.

---

# Company Standards

Developers should follow these standards:

- Use meaningful variable names.
- Keep functions small.
- Prefer composition over duplication.
- Write readable code.
- Document complex logic.
- Avoid unnecessary abstractions.
- Keep Pull Requests focused.
- Follow project coding conventions.

---

# Pull Request Guidelines

Before opening a Pull Request:

- Ensure the application builds successfully.
- Run tests.
- Verify linting passes.
- Test affected functionality.
- Keep commits meaningful.
- Add screenshots if UI changes exist.
- Request reviewers.

---

# Code Review Expectations

Reviewers should verify:

- Correctness
- Readability
- Maintainability
- Performance
- Security
- Testing coverage
- Reusability
- Architecture consistency

---

# Deployment Overview

Typical deployment flow:

Developer

↓

GitHub

↓

GitHub Actions

↓

Jenkins

↓

Build

↓

Akamai

↓

QA

↓

Production

---

# Performance Goals

Engineers should optimize for:

- Fast page loads
- Small bundle sizes
- Efficient rendering
- Lazy loading
- Code splitting
- Caching
- Minimal network requests

---

# Security Principles

Always:

- Validate user input.
- Protect authentication tokens.
- Never commit secrets.
- Follow OAuth best practices.
- Use HTTPS.
- Protect against XSS and CSRF.

---

# Engineering Culture

The engineering team values:

- Collaboration
- Knowledge sharing
- Code quality
- Continuous learning
- Automation
- Documentation
- Ownership
- Innovation

---

# AI Assistant Usage

The Engineering Intelligence Assistant should:

- Help onboard engineers.
- Explain architecture.
- Answer engineering questions.
- Explain company workflows.
- Analyze Jira requirements.
- Suggest engineering best practices.
- Help troubleshoot technical issues.
- Teach engineering concepts.
- Distinguish between company documentation and general software engineering knowledge.

If company-specific information is unavailable, clearly state that the answer is based on general engineering best practices rather than internal documentation.