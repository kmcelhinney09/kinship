import * as React from 'react'
import { Outlet, createRootRoute } from '@tanstack/react-router'
import { CssBaseline, ThemeProvider, createTheme, Container } from '@mui/material'

/**
 * Root route providing the app shell and layout.
 */
const theme = createTheme()

export const Route = createRootRoute({
  component: function RootLayout(): JSX.Element {
    return (
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Container maxWidth="md" sx={{ py: 2 }}>
          <Outlet />
        </Container>
      </ThemeProvider>
    )
  },
})
