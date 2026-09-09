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

const getLocalStorageItem = (key: string) => {
  try {
    return typeof window !== 'undefined' && window.localStorage && typeof window.localStorage.getItem === 'function'
      ? window.localStorage.getItem(key)
      : null;
  } catch {
    return null;
  }
};

const setLocalStorageItem = (key: string, val: string) => {
  try {
    if (typeof window !== 'undefined' && window.localStorage && typeof window.localStorage.setItem === 'function') {
      window.localStorage.setItem(key, val);
    }
  } catch {}
};

const removeLocalStorageItem = (key: string) => {
  try {
    if (typeof window !== 'undefined' && window.localStorage && typeof window.localStorage.removeItem === 'function') {
      window.localStorage.removeItem(key);
    }
  } catch {}
};

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(() => {
    const savedUser = getLocalStorageItem('user');
    return savedUser ? JSON.parse(savedUser) : null;
  });

  const [token, setToken] = useState<string | null>(() => getLocalStorageItem('token'));

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
    setLocalStorageItem('token', t);
    setLocalStorageItem('user', JSON.stringify(userData));
  };

  const logout = () => {
    setToken(null);
    setUser(null);
    removeLocalStorageItem('token');
    removeLocalStorageItem('user');
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
