---
applyTo: '**'
---
# GitHub Copilot Instructions for the "Kinship" Repository

You are an expert AI assistant for the "Kinship" project, a family management application. Your primary goal is to generate high-quality, consistent, and well-tested code that adheres strictly to the architectural and stylistic standards outlined below.

This is a monorepo with two main directories: `frontend/` and `backend/`. Your behavior and suggestions must adapt to the specific context of the directory you are working in.

## 1. Core Project & Architectural Principles

- **Project Goal:** Kinship helps families manage their lives with modules for a Shared Calendar, Grocery/Meal Planning, a Chore Chart with a Rewards System, and a Reminder System.
- **Monorepo Structure:** Be aware of the `frontend/` and `backend/` separation. Code and dependencies for each part of the stack are completely isolated within these directories.

---

## 2. Frontend Development (`frontend/`)

When working within the `frontend/` directory, you must adhere to the following rules:

### 2.1. Technology Stack
- **Framework:** React with TypeScript.
- **Routing:** TanStack Router.
- **State & Data Fetching:** TanStack Query for all server state management.
- **UI Components:** Material UI (MUI). Always prefer MUI components over custom or native HTML elements for UI construction.

### 2.2. Architecture & Code Structure
- **Route-centric Colocation:** The entire frontend architecture is organized around the TanStack Router file-based routes.
- When creating a new feature or route, you must colocate all related files. This includes the route definition, components specific to that route, data fetching logic (e.g., `loader` functions for TanStack Query), and tests.

### 2.3. Coding and Style Standards
- **Component Type:** All React components MUST be functional components using React Hooks. Do NOT generate class components.
- **File & Component Naming:** All file and component names MUST use `PascalCase` and be highly descriptive (e.g., `SharedCalendarView.tsx`, `ChoreRewardCard.tsx`).
- **Variable & Function Naming:** Use descriptive `camelCase` names for all variables and functions.
- **Documentation:** All exported functions and components MUST have a complete and descriptive TSDoc block explaining their purpose, props, and return values.
- **Formatting:** Strictly adhere to the project's ESLint and Prettier configurations. Ensure code is auto-formatted before concluding your work.

---

## 3. Backend Development (`backend/`)

When working within the `backend/` directory, you must adhere to the following rules:

### 3.1. Technology Stack
- **Framework:** Python with FastAPI.
- **Database:** PostgreSQL.
- **ORM:** SQLAlchemy is used for all database interactions.
- **Migrations:** Alembic is used for all database schema migrations. Generate new Alembic migration files for any model changes.

### 3.2. Architecture & Data Contracts
- **API Data Contract:** Pydantic models are the single source of truth for all API request and response schemas. All data entering or leaving the API MUST be validated and serialized through a Pydantic model. Do not use raw dictionaries in API routes.
- **Database Models:** Define all database tables as SQLAlchemy ORM models. Keep these models separate from the Pydantic API models to decouple the API contract from the database schema.
- **Business Logic:** Encapsulate business logic in service-layer functions that are called from the FastAPI route handlers. Keep route handlers thin and focused on HTTP concerns.

### 3.3. Coding and Style Standards
- **Type Hinting:** All functions, methods, and classes MUST include explicit Python type hints for all parameters and return values.
- **Docstrings:** All public modules, classes, and functions MUST have a comprehensive docstring following the **Google Style** format.
- **Best Practices:** Adhere strictly to PEP 8 and other industry-standard Python best practices. Keep imports clean and organized.
- **Comments:** Limit the use of inline comments. Only add them to explain complex algorithms or non-obvious business logic. Your code should be self-documenting through clear naming and structure.

---

## 4. Testing Standards (Crucial)

Generating tests is a critical part of your function. Do not generate code without also generating the corresponding tests.

- **Priority:** Focus on generating **Unit and Integration Tests**.
- **Coverage Target:** All new or modified code you generate MUST aim for a minimum of **80% test coverage**.
- **Frontend Testing (`frontend/`):**
    - **Framework:** Use **Vitest** for all tests.
    - **Location:** Test files MUST be named `*.test.tsx` or `*.test.ts` and placed in a `__tests__` subdirectory directly adjacent to the file being tested.
- **Backend Testing (`backend/`):**
    - **Framework:** Use **pytest** for all tests.
    - **Location:** All test files MUST be placed in the `backend/tests/` directory. The structure within `backend/tests/` should mirror the structure of the main application source code.

---

## 5. Custom Command Integration

When I provide a specific trigger phrase, you MUST use the content of the referenced file as your primary instructions for the response.

1.  **If I say:** `"I need a PRD for <feature name>"`
    **Then:** You MUST use the contents of `/workspaces/kinship/.github/prompts/prd.prompt.md` as your template and instructions for generating the Product Requirements Document.

2.  **If I say:** `"Generate tasks for this change"`
    **Then:** You MUST use the contents of `/workspaces/kinship/.github/prompts/generate-tasks.prompt.md` as your instructions to break down the request into a detailed implementation plan with actionable tasks.