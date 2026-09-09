import React, { createContext, useContext, useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './auth/AuthProvider';
import { DataProvider } from './context/DataContext';
import { ToastProvider } from './components/Toast';

import { LandingPage } from './pages/LandingPage';
import { Login } from './pages/Login';
import { DashboardLayout } from './layouts/DashboardLayout';

import { AdminDashboard } from './pages/dashboards/AdminDashboard';
import { DoctorsList } from './pages/doctors/DoctorsList';
import { PatientsList } from './pages/patients/PatientsList';
import { AppointmentsList } from './pages/appointments/AppointmentsList';
import { MedicalRecords } from './pages/records/MedicalRecords';
import { BedManagement } from './pages/admissions/BedManagement';
import { AIAnalytics } from './pages/analytics/AIAnalytics';
import { PharmacyInventory } from './pages/pharmacy/PharmacyInventory';
import { BillingDashboard } from './pages/billing/BillingDashboard';
import { AmbulanceDispatch } from './pages/ambulance/AmbulanceDispatch';
import { TelemedicineDashboard } from './pages/telemedicine/TelemedicineDashboard';
import { SettingsPage } from './pages/settings/SettingsPage';

// Inline ThemeProvider to guarantee zero import/reference errors
const ThemeContext = createContext({ theme: 'light', setTheme: (t: string) => {} });
const ThemeProvider = ({ children }: { children: React.ReactNode; defaultTheme?: string; storageKey?: string }) => {
  const [theme, setTheme] = useState('light');
  useEffect(() => {
    document.documentElement.classList.remove('dark');
    document.documentElement.classList.add('light');
  }, []);
  return <ThemeContext.Provider value={{ theme, setTheme }}>{children}</ThemeContext.Provider>;
};

const ProtectedRoute = ({ children }: { children: React.ReactNode }) => {
  const { isAuthenticated } = useAuth();
  if (!isAuthenticated) return <Navigate to="/login" replace />;
  return <>{children}</>;
};

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/login" element={<Login />} />

      <Route path="/dashboard" element={<ProtectedRoute><DashboardLayout /></ProtectedRoute>}>
        <Route index element={<AdminDashboard />} />
        <Route path="doctors" element={<DoctorsList />} />
        <Route path="patients" element={<PatientsList />} />
        <Route path="appointments" element={<AppointmentsList />} />
        <Route path="records" element={<MedicalRecords />} />
        <Route path="admissions" element={<BedManagement />} />
        <Route path="analytics" element={<AIAnalytics />} />
        <Route path="pharmacy" element={<PharmacyInventory />} />
        <Route path="billing" element={<BillingDashboard />} />
        <Route path="ambulance" element={<AmbulanceDispatch />} />
        <Route path="telemedicine" element={<TelemedicineDashboard />} />
        <Route path="settings" element={<SettingsPage />} />
      </Route>

      <Route path="*" element={
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100vh', fontFamily: 'Inter, sans-serif' }}>
          <h1 style={{ fontSize: '4rem', color: '#0284c7', fontWeight: 900 }}>404</h1>
          <p style={{ color: '#64748b', marginBottom: '2rem' }}>Page Not Found</p>
          <a href="/" style={{ background: '#0284c7', color: 'white', padding: '0.625rem 1.5rem', borderRadius: 6, textDecoration: 'none', fontWeight: 600 }}>Return Home</a>
        </div>
      } />
    </Routes>
  );
}

export default function App() {
  return (
    <ThemeProvider defaultTheme="light" storageKey="healthsphere-theme">
      <AuthProvider>
        <DataProvider>
          <ToastProvider>
            <BrowserRouter>
              <AppRoutes />
            </BrowserRouter>
          </ToastProvider>
        </DataProvider>
      </AuthProvider>
    </ThemeProvider>
  );
}