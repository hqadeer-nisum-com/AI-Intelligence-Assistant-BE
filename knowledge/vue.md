# Vue

## Purpose

This document provides an overview of Vue.js, including Vue 2, Vue 3, application architecture, state management, routing, lifecycle hooks, Composition API, performance optimization, debugging, and best practices.

The goal is to help engineers understand how Vue applications are built and maintained within our engineering platform.

---

# What is Vue?

Vue.js is a progressive JavaScript framework used to build modern web applications.

It is component-based, lightweight, and designed for building reusable user interfaces.

Our engineering platform currently supports both Vue 2 and Vue 3.

---

# Why We Use Vue

Vue provides:

- Component-based architecture
- Reactive data binding
- Excellent developer experience
- High performance
- Easy learning curve
- Strong ecosystem
- TypeScript support
- Scalable application architecture

---

# Vue 2

## Overview

Vue 2 is used in many legacy applications.

Most Vue 2 applications use:

- Options API
- Vuex
- Vue Router

Example:

```javascript
export default {
  data() {
    return {
      count: 0
    };
  },

  methods: {
    increment() {
      this.count++;
    }
  }
}
```

---

# Vue 3

## Overview

Vue 3 introduces major improvements.

Features include:

- Composition API
- Better TypeScript support
- Faster rendering
- Smaller bundle size
- Improved reactivity system

Most new applications should use Vue 3.

Example:

```javascript
import { ref } from "vue";

const count = ref(0);

function increment() {
  count.value++;
}
```

---

# Options API

The Options API organizes code into sections.

Common options include:

- data
- methods
- computed
- watch
- props
- emits
- lifecycle hooks

Example:

```javascript
export default {
  data() {
    return {
      name: ""
    };
  },

  methods: {
    save() {}
  }
}
```

---

# Composition API

The Composition API groups related logic together.

Benefits:

- Better code organization
- Easier reuse
- Better TypeScript support
- Simpler testing

Common functions:

- ref()
- reactive()
- computed()
- watch()
- onMounted()
- provide()
- inject()

Example:

```javascript
const count = ref(0);

const double = computed(() => count.value * 2);
```

---

# Reactivity

Vue automatically updates the UI when reactive data changes.

Common APIs:

- ref()
- reactive()
- computed()
- watch()

Use:

ref()

for primitive values.

Use:

reactive()

for objects.

---

# Lifecycle Hooks

Vue components go through several lifecycle stages.

Common hooks:

Vue 2

- beforeCreate
- created
- beforeMount
- mounted
- beforeUpdate
- updated
- beforeDestroy
- destroyed

Vue 3

- onBeforeMount
- onMounted
- onUpdated
- onUnmounted

Example:

```javascript
onMounted(() => {
  loadProducts();
});
```

---

# Props

Props allow parent components to pass data to child components.

Example:

```javascript
defineProps({
  title: String
});
```

Best Practices:

- Keep props immutable.
- Validate prop types.
- Keep APIs simple.

---

# Emits

Child components communicate with parents using events.

Example:

```javascript
const emit = defineEmits(["save"]);

emit("save");
```

---

# Computed Properties

Computed values automatically update when dependencies change.

Example:

```javascript
const fullName = computed(() => {
  return first.value + " " + last.value;
});
```

Use computed instead of methods whenever possible for derived values.

---

# Watch

Watch is used when reacting to state changes.

Example:

```javascript
watch(search, () => {
  loadProducts();
});
```

Use watch only for side effects.

---

# Composables

Composables are reusable functions built with the Composition API.

Example:

```
useAuth()
useApi()
useCart()
useProducts()
```

Benefits:

- Reusable logic
- Cleaner components
- Better testing

---

# Vue Router

Vue Router manages navigation.

Example:

```
/
products
/cart
/profile
```

Features:

- Dynamic routes
- Nested routes
- Route guards
- Lazy loading

---

# State Management

Vue applications commonly use Vuex.

State examples:

- Authentication
- User
- Cart
- Products
- Feature flags

Keep global state minimal.

---

# Component Design

Good components should be:

- Small
- Reusable
- Testable
- Independent

Avoid components that handle too many responsibilities.

---

# Folder Structure

Typical structure:

```
components/
views/
pages/
router/
store/
services/
composables/
assets/
utils/
types/
```

---

# API Integration

API calls should be placed inside services.

Avoid calling APIs directly from UI components.

Example:

```
services/
    product.service.js
```

---

# Error Handling

Handle:

- Network errors
- API failures
- Loading states
- Empty states

Always provide meaningful user feedback.

---

# Performance

Optimize by using:

- Lazy loading
- Async components
- Code splitting
- Tree shaking
- Virtual scrolling
- Image optimization

Avoid:

- Large components
- Deep watchers
- Unnecessary renders

---

# Accessibility

Components should support:

- Keyboard navigation
- Screen readers
- Semantic HTML
- ARIA attributes

Accessibility should be considered from the beginning.

---

# Testing

Test:

- Components
- Props
- Events
- API calls
- User interactions

Recommended tool:

- Jest

---

# Common Problems

Examples:

- Prop mutation
- Missing keys
- Infinite watchers
- Incorrect reactive state
- Memory leaks
- Lifecycle issues

---

# Debugging

Useful techniques:

- Vue DevTools
- Browser DevTools
- Console logging
- Network tab
- Component inspection

---

# Best Practices

- Prefer Vue 3 for new projects.
- Prefer Composition API.
- Keep components small.
- Reuse composables.
- Avoid duplicated logic.
- Write meaningful component names.
- Use TypeScript when possible.
- Separate business logic from UI.
- Avoid unnecessary watchers.
- Write unit tests.

---

# Company Notes

General recommendations:

- Legacy applications may still use Vue 2.
- New features should preferably use Vue 3.
- Shared components should remain reusable.
- Avoid brand-specific logic inside shared components.
- Follow project coding standards.
- Use configuration rather than hardcoded values.

---

# Interview Questions

- What is Vue?
- Difference between Vue 2 and Vue 3?
- What is the Composition API?
- What is the Options API?
- Difference between ref() and reactive()?
- What is computed()?
- What is watch()?
- What are lifecycle hooks?
- How does Vue reactivity work?
- What are composables?
- How do props work?
- How do emits work?
- How would you optimize a Vue application?
- How do you organize a large Vue project?

---

# Resources

Official Documentation

https://vuejs.org/

Vue Router

https://router.vuejs.org/

Vuex

https://vuex.vuejs.org/

Vue DevTools

https://devtools.vuejs.org/