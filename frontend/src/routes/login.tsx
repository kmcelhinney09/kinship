import { useState } from 'react'
import { useNavigate } from '@tanstack/react-router'
import { useAuth } from '../context/auth'
import axios from 'axios'

export function Login() {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [error, setError] = useState('')
    const navigate = useNavigate()
    const { login } = useAuth()

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()
        setError('')
        try {
            const formData = new FormData()
            formData.append('username', email)
            formData.append('password', password)

            const res = await axios.post('/api/auth/login', formData)

            // We need to decode the token or fetch user details separately since login only returns token
            // For MVP, let's assume we can fetch user details. 
            // OR update backend to return user details on login? 
            // Standard OAuth2 only returns token. Let's start with just setting token.

            const token = res.data.access_token
            // Temporary cheat: Create a dummy user object or fetch it.
            // Ideally we call /auth/me or similar.
            // Let's implement /auth/me on backend quickly or just redirect.

            login(token, { id: 'temp', email: email, role: 'member', family_id: 'temp' })
            navigate({ to: '/' })
        } catch (err) {
            setError('Invalid credentials')
        }
    }

    return (
        <div className="flex flex-col items-center justify-center h-screen">
            <h2 className="text-2xl mb-4">Login</h2>
            {error && <p className="text-red-500">{error}</p>}
            <form onSubmit={handleSubmit} className="flex flex-col gap-4 w-64">
                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="border p-2 rounded"
                    required
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="border p-2 rounded"
                    required
                />
                <button type="submit" className="bg-blue-500 text-white p-2 rounded">Login</button>
            </form>
        </div>
    )
}
