import React, { useState } from 'react';
import { useAuth } from '../auth/AuthProvider';
import { useNavigate } from 'react-router-dom';

export const Login: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      // API call would go here
      login("dummy_token", { id: "1", email, first_name: "Admin", last_name: "User", role: "ADMIN" });
      navigate('/dashboard');
    } catch (error) {
      console.error("Login failed", error);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Sign in to HealthSphere
          </h2>
        </div>
        <form className="mt-8 space-y-6" onSubmit={handleLogin}>
          <input type="email" value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" required className="block w-full px-3 py-2 border rounded-md" />
          <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" required className="block w-full px-3 py-2 border rounded-md" />
          <button type="submit" className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700">
            Sign In
          </button>
        </form>
      </div>
    </div>
  );
};
