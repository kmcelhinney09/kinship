## Frontend: Getting started tasks (React + TypeScript + TanStack)

Purpose
-------
This document lists a detailed, ordered task list to scaffold and configure the frontend inside `./frontend` so you can start building a React + TypeScript app using TanStack Query (React Query). It includes shell commands and full code snippets for each file the tasks reference.

High-level checklist
--------------------
- [x] Create Vite React+TS scaffold in `./frontend`
- [x] Install runtime & dev dependencies (TanStack Query + TanStack Router, axios, ESLint, Prettier, Vitest, testing libs)
- [x] Add npm scripts (dev/build/preview/test/lint/format)
- [x] Add core app files: `src/main.tsx`, `src/index.css`, file-based routes `src/routes/__root.tsx`, `src/routes/index.tsx`
- [x] Wire Material UI (ThemeProvider + CssBaseline) and load Roboto font
- [ ] Add services: `src/services/apiClient.ts`, `src/services/queryClient.ts`
- [ ] Configure Vite dev proxy for backend and enable TanStack Router Vite plugin
- [ ] Add ESLint + Prettier configs
- [ ] Add basic Vitest test and config
- [ ] Commit scaffold and add CI step (lint/build/test)

Detailed tasks
--------------

Prerequisites / Notes
- These tasks assume you're running commands inside the devcontainer terminal with the workspace mounted at `/workspaces/kinship` (or from your local machine where Node and npm are available).
- If your devcontainer doesn't include Node/npm, update `.devcontainer/devcontainer.json` to include the Node feature and rebuild the container.

Task 1 — Scaffold the app (Vite + React + TypeScript)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Run from workspace root:

```bash
cd /workspaces/kinship
# Create the Vite scaffold in ./frontend (won't overwrite existing files)
npm create vite@latest frontend -- --template react-ts
cd frontend
npm install
```

Task 2 — Install runtime deps (TanStack Query + Router, axios) and dev tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

```bash
# runtime deps
npm install @tanstack/react-query @tanstack/react-router @tanstack/router-devtools axios

# dev/test/lint/format deps (includes router plugin for file-based routes)
npm install -D @tanstack/router-plugin eslint prettier @typescript-eslint/parser @typescript-eslint/eslint-plugin vitest jsdom @testing-library/react @testing-library/jest-dom
```

Task 3 — Add npm scripts
~~~~~~~~~~~~~~~~~~~~~~~~~
Open `package.json` and ensure the following scripts exist. Add or replace the `scripts` block with:

```json
"scripts": {
  "dev": "vite",
  "build": "vite build",
  "preview": "vite preview",
  "test": "vitest",
  "lint": "eslint . --ext .ts,.tsx",
  "format": "prettier --write ."
}
```

Task 4 — Core app files (with TanStack Router file-based routes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Create the following files and contents.

1) `src/main.tsx`

```tsx
import React from 'react'
import { createRoot } from 'react-dom/client'
import { QueryClientProvider } from '@tanstack/react-query'
import { createRouter, RouterProvider } from '@tanstack/react-router'
import { routeTree } from './routeTree.gen'
import { queryClient } from './services/queryClient'
import './index.css'

const router = createRouter({ routeTree, context: { queryClient } })

declare module '@tanstack/react-router' {
  interface Register {
    router: typeof router
  }
}

createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <RouterProvider router={router} />
    </QueryClientProvider>
  </React.StrictMode>,
)
```

2) `src/routes/__root.tsx`

```tsx
import * as React from 'react'
import { Outlet, createRootRoute } from '@tanstack/react-router'

/**
 * Root route providing the app shell and layout.
 */
export const Route = createRootRoute({
  component: function RootLayout(): JSX.Element {
    return (
      <div style={{ padding: 16 }}>
        <Outlet />
      </div>
    )
  },
})
```

3) `src/routes/index.tsx` (home route)

```tsx
import * as React from 'react'
import { createFileRoute } from '@tanstack/react-router'
import { useQuery } from '@tanstack/react-query'
import apiClient from '../services/apiClient'

async function fetchHello(): Promise<unknown> {
  const { data } = await apiClient.get('/api/hello')
  return data
}

function HomePage(): JSX.Element {
  const { data, isLoading, error } = useQuery({ queryKey: ['hello'], queryFn: fetchHello })
  if (isLoading) return <div>Loading…</div>
  if (error) return <div>Error</div>
  return (
    <div>
      <h1>Kinship Frontend</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  )
}

export const Route = createFileRoute('/')({
  // Preload data with loader (optional but recommended)
  loader: async ({ context: { queryClient } }) =>
    queryClient.ensureQueryData({ queryKey: ['hello'], queryFn: fetchHello }),
  component: HomePage,
})
```

4) `src/index.css` (basic reset)

```css
html,body,#root { height: 100%; margin: 0; font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; }
body { background: #f7f7fb; color: #111827; }
```

Task 5 — Services and query client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Create these helpers to centralize API and query config.

1) `src/services/apiClient.ts`

```ts
import axios from "axios";

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL ?? "/",
  headers: { "Content-Type": "application/json" },
});

// Example interceptor (attach auth token if you later add auth)
apiClient.interceptors.request.use((config) => {
  // const token = getAuthToken(); if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export default apiClient;
```

2) `src/services/queryClient.ts`

```ts
import { QueryClient } from "@tanstack/react-query";

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60, // 1 minute
      retry: 1,
      refetchOnWindowFocus: false,
    },
  },
});
```

Task 6 — Vite config + dev proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If your backend runs on a separate port (common: FastAPI on 8000), configure Vite dev server proxy so `fetch('/api/...')` forwards to backend.

Edit or create `vite.config.ts` with the Router plugin and proxy snippet:

```ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { TanStackRouterVite } from '@tanstack/router-plugin/vite'

export default defineConfig({
  plugins: [react(), TanStackRouterVite()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false,
      },
    },
  },
})
```

Task 7 — ESLint + Prettier configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Create an ESLint config file `.eslintrc.cjs`:

```js
module.exports = {
  parser: '@typescript-eslint/parser',
  extends: [
    'eslint:recommended',
    'plugin:react/recommended',
    'plugin:@typescript-eslint/recommended',
    'prettier'
  ],
  plugins: ['@typescript-eslint', 'react'],
  settings: { react: { version: 'detect' } },
  env: { browser: true, es2021: true },
  rules: {
    // project-specific rules
  },
};
```

Create a minimal `.prettierrc`:

```json
{
  "singleQuote": true,
  "trailingComma": "all",
  "printWidth": 100
}
```

Task 8 — Vitest config and a basic test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Create `vitest.config.ts` at project root (frontend) with the Router plugin so file-based routes are generated for tests:

```ts
import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'
import { TanStackRouterVite } from '@tanstack/router-plugin/vite'

export default defineConfig({
  plugins: [react(), TanStackRouterVite()],
  test: {
    environment: 'jsdom',
    globals: true,
  },
})
```

Create a simple test `src/__tests__/HomeRoute.test.tsx`:

```tsx
import { render, screen } from '@testing-library/react'
import { createRouter, RouterProvider } from '@tanstack/react-router'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { routeTree } from '../../routeTree.gen'

test('renders Kinship heading on home route', () => {
  const queryClient = new QueryClient()
  const router = createRouter({ routeTree, context: { queryClient } })

  render(
    <QueryClientProvider client={queryClient}>
      <RouterProvider router={router} />
    </QueryClientProvider>,
  )

  expect(screen.getByText(/Kinship Frontend/i)).toBeInTheDocument()
})
```

Task 9 — Commit and CI
~~~~~~~~~~~~~~~~~~~~~~
1. Commit initial scaffold and files:

```bash
git add frontend
git commit -m "chore(frontend): scaffold Vite React TypeScript app with React Query setup"
```

2. Add CI job (example GitHub Actions) to run lint, build and tests. Create `.github/workflows/frontend-ci.yml` (example):

```yaml
name: Frontend CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: cd frontend && npm ci
      - run: cd frontend && npm run lint
      - run: cd frontend && npm run build
      - run: cd frontend && npm run test -- --coverage

```

Task 10 — Optional sensible next steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Add Material UI (MUI): `npm install @mui/material @emotion/react @emotion/styled` and wrap your app with baseline/theme.
- Add Router Devtools in development to inspect routes: `import { RouterDevtools } from '@tanstack/router-devtools'` and include `<RouterDevtools />` inside the root layout.
- Add generator step for TypeScript models from backend Pydantic models later (datamodel-code-generator) and commit generated types into `src/types`.

Try it — quick run commands
---------------------------
After you finish Tasks 1–3 and create the files, run these to verify:

```bash
cd /workspaces/kinship/frontend
npm run dev       # starts Vite dev server
npm run test      # runs Vitest tests
npm run lint      # runs ESLint
```

Requirements coverage
---------------------
- Scaffold app: Task 1 — Done by following commands
- Install deps: Task 2 — Done by following commands
- Scripts: Task 3 — Add the provided `scripts` block
- Core files & services: Task 4 & 5 — Files and code snippets provided
- Vite proxy: Task 6 — Proxy snippet provided for `vite.config.ts`
- Lint/format/test: Task 7 & 8 — configs and example test provided
- Commit/CI: Task 9 — example CI file included

If you'd like, I can create these files in the repository now. Reply with "Create frontend files" and I'll add them and run the project checks. Otherwise follow the steps above in your devcontainer terminal.
