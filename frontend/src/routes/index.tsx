import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/')({
    component: Index,
})

function Index() {
    return (
        <div className="p-2">
            <h1 className="text-4xl font-bold text-primary">Welcome to Kinship</h1>
            <p className="mt-4 text-lg text-muted-foreground">
                Your Family Command Center
            </p>
        </div>
    )
}
