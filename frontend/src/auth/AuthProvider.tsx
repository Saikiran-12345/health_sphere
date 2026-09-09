import React, { createContext, useContext, useState, useEffect } from 'react';
import axios from 'axios';

export interface User {
  id: string;
  email: string;
  first_name: string;
  last_name?: string;
  role: 'ADMIN' | 'DOCTOR' | 'NURSE_ICU' | 'PHARMACIST' | 'FINANCE' | 'DISPATCHER' | 'LAB_TECH' | string;
  department?: string;
  title?: string;
}

interface AuthContextType {
  user: User | null;
  token: string | null;
  login: (userData: User, token?: string) => void;
  logout: () => void;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | null>(null);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(() => {
    try {
      const savedUser = localStorage.getItem('user');
      return savedUser ? JSON.parse(savedUser) : null;
    } catch {
      return null;
    }
  });

  const [token, setToken] = useState<string | null>(() => localStorage.getItem('token'));

  useEffect(() => {
    if (token) {
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    } else {
      delete axios.defaults.headers.common['Authorization'];
    }
  }, [token]);

  const login = (userData: User, newToken?: string) => {
    const t = newToken || `demo-jwt-token-${userData.id.toLowerCase()}`;
    setToken(t);
    setUser(userData);
    localStorage.setItem('token', t);
    localStorage.setItem('user', JSON.stringify(userData));
  };

  const logout = () => {
    setToken(null);
    setUser(null);
    localStorage.removeItem('token');
    localStorage.removeItem('user');
  };

  return (
    <AuthContext.Provider value={{ user, token, login, logout, isAuthenticated: !!token }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error("useAuth must be used within an AuthProvider");
  return context;
};
