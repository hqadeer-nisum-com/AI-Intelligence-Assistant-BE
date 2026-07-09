# JavaScript

## Purpose

This document provides a comprehensive guide to JavaScript fundamentals and advanced concepts used throughout the engineering platform.

It serves as a learning resource for onboarding, interview preparation, debugging, and day-to-day frontend development.

---

# What is JavaScript?

JavaScript is a high-level, interpreted programming language primarily used to build interactive web applications.

It runs in browsers and server-side environments such as Node.js.

JavaScript powers modern frontend frameworks including Vue.

---

# Why We Use JavaScript

JavaScript allows developers to:

- Build dynamic user interfaces
- Handle user interactions
- Communicate with APIs
- Manipulate the DOM
- Manage application state
- Build reusable components
- Create full-stack applications

---

# Variables

JavaScript provides three ways to declare variables.

## var

- Function scoped
- Can be redeclared
- Avoid in modern applications

Example

```javascript
var name = "John";
```

---

## let

- Block scoped
- Can be reassigned
- Preferred for mutable values

```javascript
let count = 1;
count++;
```

---

## const

- Block scoped
- Cannot be reassigned
- Preferred by default

```javascript
const API_URL = "/api/products";
```

---

# Data Types

Primitive Types

- String
- Number
- Boolean
- Null
- Undefined
- Symbol
- BigInt

Reference Types

- Object
- Array
- Function
- Date
- Map
- Set

---

# Operators

- Arithmetic
- Comparison
- Logical
- Assignment
- Ternary
- Nullish Coalescing (??)
- Optional Chaining (?.)

Example

```javascript
user?.address?.city
```

---

# Functions

## Function Declaration

```javascript
function greet(name) {
    return "Hello " + name;
}
```

---

## Arrow Function

```javascript
const greet = (name) => {
    return `Hello ${name}`;
};
```

---

## Callback Functions

Functions passed as arguments.

```javascript
items.forEach(item => console.log(item));
```

---

# Scope

JavaScript has:

- Global Scope
- Function Scope
- Block Scope

Understanding scope helps prevent bugs.

---

# Hoisting

JavaScript moves declarations to the top of their scope before execution.

Best Practice:

- Use let and const.
- Avoid relying on hoisting.

---

# Closures

A closure is a function that remembers variables from its outer scope.

Example

```javascript
function counter() {
    let value = 0;

    return function () {
        value++;
        return value;
    };
}
```

Closures are commonly used for:

- Private variables
- Event handlers
- Memoization

---

# this Keyword

The value of `this` depends on how a function is called.

Examples:

- Global object
- Object methods
- Classes
- Arrow functions

Arrow functions do not create their own `this`.

---

# Objects

Objects store key-value pairs.

```javascript
const user = {
    name: "Ali",
    age: 25
};
```

---

# Arrays

Common methods:

- map()
- filter()
- reduce()
- find()
- some()
- every()
- sort()
- includes()

Example

```javascript
const names = users.map(user => user.name);
```

---

# Destructuring

Object

```javascript
const { name, age } = user;
```

Array

```javascript
const [first, second] = items;
```

---

# Spread Operator

```javascript
const copy = [...items];
```

```javascript
const updated = {
    ...user,
    age: 30
};
```

---

# Rest Operator

```javascript
function sum(...numbers) {}
```

---

# Template Literals

```javascript
const message = `Hello ${name}`;
```

---

# Promises

Promises represent asynchronous operations.

States:

- Pending
- Fulfilled
- Rejected

Example

```javascript
fetch("/api/products")
```

---

# Async / Await

Preferred way to write asynchronous code.

```javascript
async function loadProducts() {
    const response = await fetch("/api/products");
}
```

---

# Event Loop

JavaScript is single-threaded.

The Event Loop allows asynchronous operations using:

- Call Stack
- Web APIs
- Callback Queue
- Microtask Queue

Understanding the Event Loop helps debug asynchronous issues.

---

# Fetch API

Example

```javascript
const response = await fetch("/api/products");
const data = await response.json();
```

---

# Modules

Export

```javascript
export function loadProducts() {}
```

Import

```javascript
import { loadProducts } from "./api";
```

---

# Error Handling

```javascript
try {
   ...
}
catch(error) {
   console.error(error);
}
finally {
   ...
}
```

Always handle API errors gracefully.

---

# DOM Manipulation

Examples

- querySelector()
- addEventListener()
- classList
- appendChild()

Modern frameworks like Vue reduce direct DOM manipulation.

---

# ES6+ Features

- Arrow Functions
- let / const
- Template Literals
- Destructuring
- Spread Operator
- Rest Operator
- Optional Chaining
- Nullish Coalescing
- Modules
- Async/Await

---

# Performance Tips

- Avoid unnecessary loops.
- Minimize DOM updates.
- Debounce search inputs.
- Throttle scroll events.
- Cache repeated calculations.
- Lazy load resources.
- Use efficient array methods.

---

# Common Mistakes

- Using var
- Mutating objects unintentionally
- Forgetting await
- Nested callbacks
- Memory leaks
- Infinite loops
- Comparing with == instead of ===

---

# Debugging

Useful tools:

- Browser DevTools
- Console
- Breakpoints
- Network Tab
- Performance Tab

---

# Best Practices

- Use const by default.
- Prefer let over var.
- Write small functions.
- Use meaningful variable names.
- Keep functions pure where possible.
- Avoid global variables.
- Handle errors properly.
- Use modern ES6+ syntax.
- Write readable code.

---

# Company Notes

General recommendations:

- Use modern JavaScript syntax.
- Prefer async/await.
- Avoid callback hell.
- Follow project linting rules.
- Keep business logic reusable.
- Write maintainable code.

---

# Interview Questions

- Difference between let, const, and var?
- What is hoisting?
- What is a closure?
- Explain the Event Loop.
- What are Promises?
- What is async/await?
- Difference between == and ===?
- Explain this keyword.
- What is event delegation?
- Difference between map(), filter(), and reduce()?
- What are template literals?
- Explain destructuring.
- What is the spread operator?
- What are modules?

---

# Resources

Official Documentation

https://developer.mozilla.org/en-US/docs/Web/JavaScript

ECMAScript

https://tc39.es/

JavaScript Info

https://javascript.info/