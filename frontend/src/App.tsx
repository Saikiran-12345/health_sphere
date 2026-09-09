import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './auth/AuthProvider';
import { Login } from './pages/Login';
import { DashboardLayout } from './layouts/DashboardLayout';
import { AdminDashboard } from './pages/dashboards/AdminDashboard';
import { PatientsList } from './pages/patients/PatientsList';

const ProtectedRoute = ({ children, allowedRoles }: { children: React.ReactNode, allowedRoles?: string[] }) => {
  const { isAuthenticated, user } = useAuth();
  
  if (!isAuthenticated) return <Navigate to="/login" replace />;
  if (allowedRoles && user && !allowedRoles.includes(user.role)) return <Navigate to="/unauthorized" replace />;
  
  return <>{children}</>;
};

function AppRoutes() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/" element={<Navigate to="/dashboard" replace />} />
      
      {/* Protected Layout */}
      <Route element={<ProtectedRoute><DashboardLayout /></ProtectedRoute>}>
        <Route path="/dashboard" element={<AdminDashboard />} />
        {/* Placeholder Routes for later */}
        <Route path="/patients" element={<PatientsList />} />
        <Route path="/appointments" element={<div className="p-6">Appointments Module Coming Soon</div>} />
        <Route path="/records" element={<div className="p-6">Medical Records Module Coming Soon</div>} />
        <Route path="/admissions" element={<div className="p-6">Admissions & Beds Module Coming Soon</div>} />
        <Route path="/analytics" element={<div className="p-6">AI Analytics Module Coming Soon</div>} />
        <Route path="/settings" element={<div className="p-6">Settings Module Coming Soon</div>} />
      </Route>
      
      <Route path="*" element={<div className="p-12 text-center text-2xl font-bold">404 Not Found</div>} />
    </Routes>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <AppRoutes />
      </BrowserRouter>
    </AuthProvider>
  );
}
