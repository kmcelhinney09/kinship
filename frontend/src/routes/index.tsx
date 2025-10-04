import * as React from 'react'
import { createFileRoute } from '@tanstack/react-router'

function HomePage(): JSX.Element {
  return (
    <div>
      <h1>Kinship Frontend</h1>
      <p>Home route is working.</p>
    </div>
  )
}

export const Route = createFileRoute('/')({
  component: HomePage,
})
