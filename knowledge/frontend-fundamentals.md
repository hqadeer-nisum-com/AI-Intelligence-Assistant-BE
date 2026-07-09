# Frontend Fundamentals

## Purpose

This document provides a reference for the core frontend technologies used in web development. It covers HTML, CSS, Tailwind CSS, TypeScript, responsive design, accessibility, browser rendering, performance, and frontend best practices.

The goal is to help engineers understand how modern frontend applications are built and maintained.

---

# HTML

## What is HTML?

HTML (HyperText Markup Language) defines the structure of a web page.

Example elements:

- html
- head
- body
- header
- nav
- main
- section
- article
- aside
- footer

---

## Semantic HTML

Use semantic elements whenever possible.

Examples

- header
- nav
- main
- section
- article
- footer
- button
- form

Benefits

- Better accessibility
- Better SEO
- Easier maintenance

---

## Forms

Common elements

- input
- textarea
- select
- checkbox
- radio
- button

Always use labels.

Validate user input.

---

# CSS

## Purpose

CSS controls presentation and layout.

---

## Selectors

- Class
- ID
- Element
- Attribute
- Pseudo Class
- Pseudo Element

---

## Box Model

Every element contains

- Content
- Padding
- Border
- Margin

---

## Display

Common values

- block
- inline
- inline-block
- flex
- grid
- none

---

## Position

- static
- relative
- absolute
- fixed
- sticky

---

## Flexbox

Useful for one-dimensional layouts.

Common properties

Container

- display:flex
- justify-content
- align-items
- flex-wrap
- gap

Item

- flex
- align-self
- order

---

## CSS Grid

Useful for two-dimensional layouts.

Common properties

- grid-template-columns
- grid-template-rows
- gap
- grid-area

---

## Responsive Design

Use

- Relative units
- Media queries
- Flexible layouts
- Responsive images

Typical breakpoints

- Mobile
- Tablet
- Desktop

---

# Tailwind CSS

## What is Tailwind?

Tailwind CSS is a utility-first CSS framework.

Example

```
flex
items-center
justify-between
p-4
rounded-lg
shadow
```

---

## Benefits

- Faster development
- Reusable utility classes
- Consistent spacing
- Responsive utilities
- Easy customization

---

## Responsive Utilities

Examples

```
sm:
md:
lg:
xl:
2xl:
```

---

# TypeScript

## What is TypeScript?

TypeScript is JavaScript with static typing.

Benefits

- Better IDE support
- Early error detection
- Safer refactoring
- Improved maintainability

---

## Types

Examples

- string
- number
- boolean
- object
- array
- unknown
- never

---

## Interfaces

Interfaces define object shapes.

Example

```
interface User {
    id: number;
    name: string;
}
```

---

## Type Aliases

```
type Status = "active" | "inactive";
```

---

## Enums

Use enums for fixed values.

---

## Generics

Generics improve code reusability.

Example

```
function identity<T>(value:T):T
```

---

## Utility Types

Useful utility types

- Partial
- Required
- Pick
- Omit
- Record
- Readonly

---

# Accessibility (a11y)

Best practices

- Semantic HTML
- Keyboard navigation
- Alt text
- Labels
- Focus management
- Proper color contrast

---

# Browser Rendering

Typical flow

HTML

↓

DOM

↓

CSS

↓

CSSOM

↓

Render Tree

↓

Layout

↓

Paint

↓

Composite

---

# Performance

Improve performance by

- Lazy loading
- Code splitting
- Tree shaking
- Image optimization
- Bundle optimization
- Memoization
- Virtual scrolling (large lists)

---

# Responsive Design Best Practices

- Mobile-first approach
- Flexible layouts
- Avoid fixed widths
- Test multiple screen sizes
- Optimize images

---

# Clean Code

- Meaningful names
- Small functions
- Reusable components
- Avoid duplication
- Keep files organized
- Remove unused code

---

# Common Frontend Problems

Examples

- Layout breaking
- Overflow
- Z-index issues
- CSS specificity
- Responsive bugs
- Hydration mismatch
- Browser compatibility

---

# Debugging

Useful tools

- Browser DevTools
- Lighthouse
- Performance panel
- Accessibility inspector

---

# Best Practices

- Use semantic HTML.
- Prefer Flexbox/Grid over floats.
- Keep CSS modular.
- Write reusable TypeScript types.
- Avoid inline styles unless necessary.
- Optimize bundle size.
- Test responsiveness.
- Follow accessibility standards.

---

# Company Notes

General recommendations

- Prefer reusable components.
- Follow design system guidelines.
- Use TypeScript for new features.
- Build responsive interfaces.
- Consider accessibility during development.
- Optimize performance before production.

---

# Interview Questions

- What is semantic HTML?
- Explain the CSS Box Model.
- Flexbox vs Grid?
- What is responsive design?
- What is Tailwind CSS?
- Why use TypeScript?
- Interface vs Type?
- What are Generics?
- What are Utility Types?
- How does browser rendering work?
- What improves frontend performance?
- How do you build accessible web applications?

---

# Resources

HTML

https://developer.mozilla.org/en-US/docs/Web/HTML

CSS

https://developer.mozilla.org/en-US/docs/Web/CSS

Tailwind CSS

https://tailwindcss.com/docs

TypeScript

https://www.typescriptlang.org/docs/

Web Accessibility

https://www.w3.org/WAI/

Lighthouse

https://developer.chrome.com/docs/lighthouse/