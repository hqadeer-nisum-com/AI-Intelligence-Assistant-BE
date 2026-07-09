# Testing & Debugging

## Purpose

This document explains the testing strategy, debugging techniques, code quality practices, and troubleshooting process used across the engineering platform.

It helps engineers write reliable code, identify issues quickly, and maintain application quality throughout the development lifecycle.

---

# Why Testing Matters

Testing helps ensure that applications:

- Work as expected
- Prevent regressions
- Improve code quality
- Reduce production bugs
- Increase confidence during deployments

Testing should be part of every feature development.

---

# Types of Testing

## Unit Testing

Tests a single function, component, or module.

Examples:

- Vue component
- Utility function
- Composable
- Store action

Benefits

- Fast
- Easy to maintain
- Detects bugs early

---

## Integration Testing

Verifies that multiple modules work together.

Examples

- Component + API
- Component + Vuex
- Parent and Child Components

---

## End-to-End Testing

Tests the complete application from the user's perspective.

Example

Login

↓

Browse Products

↓

Add to Cart

↓

Checkout

---

## Regression Testing

Ensures existing functionality continues working after new changes.

Usually performed before releases.

---

## Smoke Testing

Quick validation after deployment.

Typical checks

- Application loads
- Login works
- Navigation works
- APIs respond
- No major console errors

---

# Jest

## What is Jest?

Jest is the testing framework commonly used for JavaScript and Vue applications.

Typical uses

- Unit testing
- Mocking
- Snapshot testing
- Code coverage

---

## Common Jest Features

- describe()
- test()
- expect()
- beforeEach()
- afterEach()
- mock()

---

## Example

```javascript
describe("sum", () => {
  test("adds numbers", () => {
    expect(sum(2, 3)).toBe(5);
  });
});
```

---

# Mocking

Mocking replaces external dependencies during testing.

Examples

- API requests
- Authentication
- Browser APIs
- Timers

Benefits

- Faster tests
- Predictable results
- Independent execution

---

# Code Coverage

Coverage measures how much code is tested.

Typical targets

- Statements
- Functions
- Branches
- Lines

High coverage does not always mean high-quality tests.

---

# Debugging

## Browser DevTools

Useful tabs

- Console
- Network
- Sources
- Performance
- Application

---

## Console Debugging

Useful methods

```javascript
console.log()

console.error()

console.warn()

console.table()

console.time()

console.timeEnd()
```

---

# Breakpoints

Breakpoints allow execution to pause so variables and application state can be inspected.

Useful for

- Event handlers
- API calls
- Vue lifecycle hooks
- Store actions

---

# Network Debugging

Verify

- Request URL
- HTTP Method
- Status Code
- Headers
- Request Payload
- Response Body

---

# Common HTTP Errors

## 400

Bad Request

Possible causes

- Invalid request data
- Missing required fields

---

## 401

Unauthorized

Possible causes

- Expired token
- Missing authentication

---

## 403

Forbidden

Possible causes

- User lacks permission

---

## 404

Not Found

Possible causes

- Incorrect endpoint
- Missing resource

---

## 500

Internal Server Error

Possible causes

- Backend issue
- Unexpected exception

---

## 503

Service Unavailable

Possible causes

- Server overloaded
- Maintenance
- Deployment in progress

---

# Vue Debugging

Common issues

- Missing props
- Incorrect reactivity
- Watchers not firing
- Lifecycle hook misuse
- State updates not reflected

---

# API Debugging

Verify

- Endpoint
- Request body
- Authorization header
- Response
- Environment variables

---

# Git Debugging

Common problems

- Merge conflicts
- Wrong branch
- Detached HEAD
- Incorrect rebase

---

# Build Debugging

Common issues

- Dependency conflicts
- Missing environment variables
- Type errors
- Lint failures
- Version mismatch

---

# Deployment Debugging

Check

- Jenkins logs
- GitHub Actions
- Build artifacts
- Akamai cache
- Browser cache

---

# Performance Debugging

Look for

- Large bundles
- Unnecessary API calls
- Repeated rendering
- Memory leaks
- Slow components

Useful tools

- Lighthouse
- Performance tab
- Vue DevTools

---

# Logging Best Practices

- Log meaningful information
- Avoid excessive logging
- Never log passwords or tokens
- Remove debug logs before production

---

# Troubleshooting Checklist

When something fails

1. Reproduce the issue.
2. Read the error message.
3. Check browser console.
4. Check network requests.
5. Review logs.
6. Verify configuration.
7. Test locally.
8. Identify root cause.
9. Fix the issue.
10. Verify the solution.

---

# Best Practices

- Test before committing.
- Keep tests independent.
- Mock external services.
- Write readable test names.
- Handle errors gracefully.
- Validate edge cases.
- Review logs before guessing.

---

# Company Notes

General recommendations

- Write unit tests for new functionality.
- Run tests before opening Pull Requests.
- Perform smoke testing after deployment.
- Investigate production issues using logs and monitoring tools.
- Ensure fixes do not introduce regressions.

---

# Interview Questions

- What is unit testing?
- What is integration testing?
- What is smoke testing?
- What is regression testing?
- What is Jest?
- Why use mocking?
- How do you debug API issues?
- How do you debug Vue applications?
- How do you debug production issues?
- What tools do you use for debugging?
- How do you investigate a failed deployment?

---

# Resources

Jest

https://jestjs.io/

Vue Test Utils

https://test-utils.vuejs.org/

Chrome DevTools

https://developer.chrome.com/docs/devtools/

MDN Debugging

https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Tools_and_setup/What_are_browser_developer_tools