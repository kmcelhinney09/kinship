import { useState } from 'react'
import { useNavigate } from '@tanstack/react-router'
import axios from 'axios'

export function Register() {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [familyName, setFamilyName] = useState('')
    const [inviteCode, setInviteCode] = useState('')
    const [isJoining, setIsJoining] = useState(false)
    const navigate = useNavigate()

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()
        try {
            await axios.post('/api/auth/register', {
                email,
                password,
                username: email.split('@')[0], // derived username
                family_name: isJoining ? undefined : familyName,
                invite_code: isJoining ? inviteCode : undefined
            })
            navigate({ to: '/login' })
        } catch (err) {
            alert('Registration failed')
        }
    }

    return (
        <div className="flex flex-col items-center justify-center h-screen">
            <h2 className="text-2xl mb-4">Register</h2>
            <div className="mb-4">
                <button onClick={() => setIsJoining(false)} className={`mr-2 ${!isJoining && 'font-bold'}`}>Create Family</button>
                <button onClick={() => setIsJoining(true)} className={`${isJoining && 'font-bold'}`}>Join Family</button>
            </div>
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
                {!isJoining ? (
                    <input
                        type="text"
                        placeholder="Family Name"
                        value={familyName}
                        onChange={(e) => setFamilyName(e.target.value)}
                        className="border p-2 rounded"
                        required
                    />
                ) : (
                    <input
                        type="text"
                        placeholder="Invite Code"
                        value={inviteCode}
                        onChange={(e) => setInviteCode(e.target.value)}
                        className="border p-2 rounded"
                        required
                    />
                )}
                <button type="submit" className="bg-green-500 text-white p-2 rounded">Register</button>
            </form>
        </div>
    )
}
