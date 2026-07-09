# CI/CD, Deployment & Release Process

## Purpose

This document explains the Continuous Integration (CI), Continuous Deployment (CD), deployment pipeline, Jenkins, GitHub Actions, Akamai, and release workflow used in our engineering platform.

It helps engineers understand how code moves from development to production and how deployments are performed safely.

---

# What is CI/CD?

CI/CD stands for:

- Continuous Integration (CI)
- Continuous Deployment (CD)

CI automatically validates code after every change.

CD automatically or manually deploys validated code to different environments.

Benefits:

- Faster delivery
- Fewer production issues
- Automated testing
- Consistent deployments
- Reliable releases

---

# Deployment Workflow

Typical deployment flow:

```

Developer
↓
Jira Ticket
↓
Development
↓
Unit Testing
↓
Pull Request
↓
Code Review
↓
Merge
↓
GitHub Actions
↓
Jenkins Pipeline
↓
Build
↓
Artifact Generation
↓
Deployment
↓
Akamai
↓
QA
↓
Production

```

---

# Development Workflow

Typical engineering workflow:

1. Pick a Jira ticket.
2. Understand the requirement.
3. Create a feature branch.
4. Develop the feature.
5. Test locally.
6. Commit changes.
7. Push branch.
8. Create Pull Request.
9. Address review comments.
10. Merge code.
11. CI pipeline executes.
12. Deploy to QA.
13. Validate functionality.
14. Release to Production.

---

# GitHub Actions

## Purpose

GitHub Actions automates engineering workflows.

Common tasks:

- Install dependencies
- Run linting
- Run unit tests
- Build applications
- Trigger Jenkins
- Validate Pull Requests

---

## Benefits

- Automated validation
- Consistent builds
- Faster feedback
- Better code quality

---

# Jenkins

## What is Jenkins?

Jenkins is an automation server used for building, testing, and deploying applications.

It executes deployment pipelines.

---

## Responsibilities

Jenkins typically performs:

- Install dependencies
- Build applications
- Run tests
- Package artifacts
- Trigger deployments
- Publish build status

---

## Pipeline Stages

Typical stages:

Checkout

↓

Install

↓

Lint

↓

Test

↓

Build

↓

Package

↓

Deploy

↓

Notify

---

# Build Process

Typical frontend build:

Source Code

↓

Install Dependencies

↓

Compile

↓

Bundle

↓

Optimize

↓

Generate Assets

↓

Deploy

---

# Deployment Environments

Common environments include:

- Local
- Development
- QA
- UAT
- Staging
- Production

Each environment has different configurations.

---

# Environment Variables

Applications often require different configuration values.

Examples:

- API URLs
- Feature Flags
- Authentication Settings
- Analytics Keys

Never hardcode environment-specific values.

---

# Akamai

## What is Akamai?

Akamai is a Content Delivery Network (CDN).

It delivers static assets closer to end users.

---

## Why We Use Akamai

- Faster page loads
- Global distribution
- High availability
- Reduced origin traffic
- Improved performance

---

## Common Akamai Tasks

- Deploy frontend assets
- Cache static files
- Invalidate cache
- Verify deployment

---

# Cache Invalidation

Sometimes users continue seeing old files after deployment.

Reasons:

- Browser cache
- CDN cache
- Service Worker cache

Possible solutions:

- Purge CDN cache
- Hard refresh browser
- Verify deployed assets

---

# Rollback

If deployment fails:

1. Stop rollout.
2. Identify issue.
3. Deploy previous stable build.
4. Verify production.
5. Investigate root cause.

---

# Smoke Testing

After deployment verify:

- Homepage loads.
- Login works.
- Navigation works.
- APIs respond.
- Critical user journeys work.
- No console errors.
- No network failures.

---

# Deployment Checklist

Before deployment:

- Code reviewed
- Tests passed
- Build successful
- No lint errors
- Environment variables verified
- Feature flags checked
- Documentation updated

After deployment:

- Smoke testing completed
- Monitoring verified
- Logs checked
- Business validation completed

---

# Common Deployment Problems

## Build Failed

Possible reasons:

- Dependency issues
- Type errors
- Syntax errors
- Missing environment variables

---

## Deployment Failed

Possible reasons:

- Jenkins failure
- Incorrect configuration
- Network issue
- Invalid artifact

---

## Old UI Still Visible

Possible reasons:

- Browser cache
- Akamai cache
- CDN propagation

---

## API Errors

Possible reasons:

- Wrong environment
- Backend unavailable
- Authentication issues

---

# Troubleshooting

Build won't start

- Verify Jenkins.
- Check GitHub Actions.

Pipeline failed

- Review logs.
- Fix failed stage.

Deployment successful but UI unchanged

- Clear Akamai cache.
- Hard refresh browser.

Environment variables missing

- Verify deployment configuration.

---

# Best Practices

- Keep deployments small.
- Test locally first.
- Review Pull Requests carefully.
- Automate testing.
- Monitor deployments.
- Use feature flags.
- Avoid manual production changes.
- Keep rollback plan ready.

---

# Company Notes

General recommendations:

- GitHub Actions validates code before deployment.
- Jenkins executes deployment pipelines.
- Akamai serves frontend assets.
- QA validates releases before production.
- Production deployments should always be verified using smoke tests.

---

# Interview Questions

- What is CI?
- What is CD?
- Difference between CI and CD?
- Why use GitHub Actions?
- Why use Jenkins?
- What is a deployment pipeline?
- What is Akamai?
- What is cache invalidation?
- What is smoke testing?
- What is rollback?
- How do you debug a failed deployment?
- What should you verify after production deployment?

---

# Resources

GitHub Actions

https://docs.github.com/actions

Jenkins

https://www.jenkins.io/doc/

Akamai

https://techdocs.akamai.com/

CI/CD

https://martinfowler.com/articles/continuousIntegration.html