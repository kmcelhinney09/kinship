# GEMINI.md

## Project Overview

This is a web application called "kinship", designed to help families keep track of calendars, chores, grocery lists, and meal planning.

The project is a monorepo with a `frontend` and a `backend` directory. Currently, only the frontend is developed.

The frontend is a modern web application built with:

*   **React**: A JavaScript library for building user interfaces.
*   **TypeScript**: A typed superset of JavaScript that compiles to plain JavaScript.
*   **Vite**: A fast build tool and development server.
*   **TanStack Router**: A fully type-safe router for React.
*   **TanStack React Query**: A data-fetching and state management library.
*   **Material-UI (MUI)**: A popular React UI framework for faster and easier web development.

The backend is not yet implemented.

## Building and Running

The frontend application is managed with npm. The following commands are available in the `/frontend` directory:

*   **`npm install`**: Installs the dependencies.
*   **`npm run dev`**: Starts the development server with Hot Module Replacement (HMR).
*   **`npm run build`**: Builds the application for production.
*   **`npm run preview`**: Previews the production build locally.
*   **`npm run test`**: Runs the tests using `vitest`.
*   **`npm run lint`**: Lints the code using ESLint to find and fix problems.
*   **`npm run format`**: Formats the code using Prettier.

## Development Conventions

*   **TypeScript**: All new code should be written in TypeScript to ensure type safety.
*   **ESLint**: The project uses ESLint for static code analysis. Please run `npm run lint` before committing your changes.
*   **Prettier**: The project uses Prettier for code formatting. Please run `npm run format` to maintain a consistent code style.
*   **Components**: Components are organized in the `src/` directory.
*   **Routing**: Routing is handled by TanStack Router. Routes are defined in the `src/routes/` directory.
*   **Styling**: The project uses Material-UI for UI components and styling.
