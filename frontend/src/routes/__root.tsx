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
