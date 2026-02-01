import { createRouter, createRoute, createRootRouteWithContext, Outlet, redirect } from '@tanstack/react-router'
// import { TanStackRouterDevtools } from '@tanstack/router-devtools'
import { Login } from './routes/login'
import { Register } from './routes/register'
import type { AuthContextType } from './context/auth'

interface MyRouterContext {
    auth: AuthContextType
}

const rootRoute = createRootRouteWithContext<MyRouterContext>()({
    component: () => (
        <>
            <div className="p-2 gap-2 flex justify-between items-center bg-gray-100">
                <h1 className="text-xl font-bold">Kinship</h1>
                {/* Simple logout button injection for now, ideally in a Header component */}
                {/* We can't easily access auth.logout here without hook, but we can render Outlet */}
            </div>
            <hr />
            <Outlet />
            {/* <TanStackRouterDevtools /> Disable for prod/cleanliness if needed, keeping for now */}
        </>
    ),
})

const indexRoute = createRoute({
    getParentRoute: () => rootRoute,
    path: '/',
    component: () => <div className="p-2"><h3>Dashboard</h3><p>Welcome to Kinship!</p></div>,
    beforeLoad: ({ context }) => {
        if (!context.auth.isAuthenticated) {
            throw redirect({
                to: '/login',
            })
        }
    },
})

const loginRoute = createRoute({
    getParentRoute: () => rootRoute,
    path: '/login',
    component: Login,
})

const registerRoute = createRoute({
    getParentRoute: () => rootRoute,
    path: '/register',
    component: Register,
})

const routeTree = rootRoute.addChildren([indexRoute, loginRoute, registerRoute])

export const router = createRouter({
    routeTree,
    context: {
        auth: undefined!, // Initial context value, will be populated by RouterProvider
    },
})

declare module '@tanstack/react-router' {
    interface Register {
        router: typeof router
    }
}
