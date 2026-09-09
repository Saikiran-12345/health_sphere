import React, { useState } from 'react';
import { Outlet, useNavigate, useLocation } from 'react-router-dom';
import { 
  Activity, Users, Settings, LogOut, Menu, X, Bed, Home, Package, CreditCard, 
  Truck, Video, Bell, Search, Stethoscope, Calendar, FileText, ShieldCheck, Lock, ArrowLeft
} from 'lucide-react';
import { useAuth } from '../auth/AuthProvider';

interface MenuItem {
  label: string;
  icon: React.ReactNode;
  path: string;
  badge?: string;
}

export const DashboardLayout: React.FC = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');

  const allMenuItems: MenuItem[] = [
    { label: 'Overview', icon: <Home size={20} />, path: '/dashboard' },
    { label: 'Doctors & Specialists', icon: <Stethoscope size={20} />, path: '/dashboard/doctors' },
    { label: 'Patients Registry', icon: <Users size={20} />, path: '/dashboard/patients' },
    { label: 'Appointments & Queue', icon: <Calendar size={20} />, path: '/dashboard/appointments' },
    { label: 'ICU & Bed Census', icon: <Bed size={20} />, path: '/dashboard/admissions', badge: 'ICU' },
    { label: 'EHR Medical Records', icon: <FileText size={20} />, path: '/dashboard/records' },
    { label: 'Pharmacy & Stock', icon: <Package size={20} />, path: '/dashboard/pharmacy' },
    { label: 'Billing & Finance', icon: <CreditCard size={20} />, path: '/dashboard/billing' },
    { label: 'Ambulance Dispatch', icon: <Truck size={20} />, path: '/dashboard/ambulance', badge: 'LIVE' },
    { label: 'Telemedicine Consults', icon: <Video size={20} />, path: '/dashboard/telemedicine' },
    { label: 'AI Vitals Telemetry', icon: <Activity size={20} />, path: '/dashboard/analytics', badge: 'AI' },
    { label: 'System Settings', icon: <Settings size={20} />, path: '/dashboard/settings' },
  ];

  const userRole = user?.role || 'ADMIN';

  // Allowed Paths per Role
  const getAllowedPaths = (role: string) => {
    switch (role) {
      case 'ADMIN': 
        return allMenuItems.map(m => m.path);
      case 'DOCTOR': 
        return ['/dashboard', '/dashboard/doctors', '/dashboard/patients', '/dashboard/appointments', '/dashboard/records', '/dashboard/telemedicine', '/dashboard/analytics'];
      case 'NURSE_ICU': 
        return ['/dashboard', '/dashboard/admissions', '/dashboard/patients', '/dashboard/records', '/dashboard/analytics'];
      case 'PHARMACIST': 
        return ['/dashboard', '/dashboard/pharmacy', '/dashboard/patients'];
      case 'FINANCE': 
        return ['/dashboard', '/dashboard/billing', '/dashboard/patients'];
      case 'DISPATCHER': 
        return ['/dashboard', '/dashboard/ambulance', '/dashboard/patients'];
      case 'LAB_TECH': 
        return ['/dashboard', '/dashboard/analytics', '/dashboard/records', '/dashboard/patients'];
      default: 
        return ['/dashboard'];
    }
  };

  const allowedPaths = getAllowedPaths(userRole);
  const menuItems = allMenuItems.filter(item => allowedPaths.includes(item.path));
  const isCurrentPathAllowed = allowedPaths.includes(location.pathname);

  const getRoleColor = (role: string) => {
    switch (role) {
      case 'ADMIN': return { bg: '#e0f2fe', color: '#0284c7', label: 'Hospital Admin', home: '/dashboard' };
      case 'DOCTOR': return { bg: '#ccfbf1', color: '#0d9488', label: 'Cardiology Specialist', home: '/dashboard/doctors' };
      case 'NURSE_ICU': return { bg: '#fee2e2', color: '#dc2626', label: 'ICU Charge Nurse', home: '/dashboard/admissions' };
      case 'PHARMACIST': return { bg: '#fef3c7', color: '#d97706', label: 'Pharmacy Manager', home: '/dashboard/pharmacy' };
      case 'FINANCE': return { bg: '#e0e7ff', color: '#4f46e5', label: 'Finance Controller', home: '/dashboard/billing' };
      case 'DISPATCHER': return { bg: '#ffedd5', color: '#ea580c', label: 'Fleet Controller', home: '/dashboard/ambulance' };
      case 'LAB_TECH': return { bg: '#ede9fe', color: '#8b5cf6', label: 'Lab Diagnostics', home: '/dashboard/analytics' };
      default: return { bg: '#e0f2fe', color: '#0284c7', label: role, home: '/dashboard' };
    }
  };

  const roleStyle = getRoleColor(userRole);

  return (
    <div style={{ display: 'flex', minHeight: '100vh', width: '100%', background: '#f8fafc', fontFamily: 'Inter, system-ui, sans-serif' }}>
      
      {/* Fixed Sidebar */}
      <aside 
        style={{
          width: sidebarOpen ? 260 : 80,
          background: '#0f172a',
          color: '#94a3b8',
          display: 'flex',
          flexDirection: 'column',
          position: 'fixed',
          top: 0,
          left: 0,
          bottom: 0,
          zIndex: 100,
          transition: 'width 0.25s cubic-bezier(0.4, 0, 0.2, 1)',
          boxShadow: '4px 0 24px rgba(15, 23, 42, 0.15)',
          overflowX: 'hidden'
        }}
      >
        {/* Brand Header */}
        <div 
          style={{
            height: 70,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            padding: '0 1.25rem',
            borderBottom: '1px solid #1e293b',
            background: '#090d16'
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', overflow: 'hidden' }}>
            <div style={{ width: 36, height: 36, borderRadius: 10, background: 'linear-gradient(135deg, #0284c7, #0369a1)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'white', flexShrink: 0 }}>
              <Activity size={22} />
            </div>
            {sidebarOpen && (
              <div>
                <span style={{ fontWeight: 900, fontSize: '1.25rem', color: '#ffffff', letterSpacing: '-0.02em' }}>HealthSphere</span>
                <div style={{ fontSize: '0.7rem', color: '#38bdf8', fontWeight: 700, letterSpacing: '0.05em', textTransform: 'uppercase' }}>Hospital OS</div>
              </div>
            )}
          </div>
          
          <button 
            onClick={() => setSidebarOpen(!sidebarOpen)}
            style={{ background: 'none', border: 'none', color: '#64748b', cursor: 'pointer', padding: 4, display: 'flex', borderRadius: 6 }}
          >
            {sidebarOpen ? <X size={20} /> : <Menu size={20} />}
          </button>
        </div>

        {/* User Department Badge in Sidebar */}
        {sidebarOpen && (
          <div style={{ padding: '1rem 1.25rem 0.5rem 1.25rem' }}>
            <div style={{ padding: '0.75rem', borderRadius: 10, background: '#1e293b', border: '1px solid #334155', display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
              <div style={{ width: 34, height: 34, borderRadius: '50%', background: roleStyle.color, color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 800, fontSize: '0.85rem' }}>
                {user?.first_name?.charAt(0) || 'U'}
              </div>
              <div style={{ overflow: 'hidden' }}>
                <div style={{ color: '#f8fafc', fontWeight: 700, fontSize: '0.875rem', whiteSpace: 'nowrap', textOverflow: 'ellipsis', overflow: 'hidden' }}>
                  {user?.first_name ? `${user.first_name} ${user.last_name || ''}` : 'Hospital Staff'}
                </div>
                <div style={{ display: 'inline-block', fontSize: '0.7rem', fontWeight: 700, color: roleStyle.color, background: 'rgba(255,255,255,0.06)', padding: '2px 6px', borderRadius: 4, marginTop: 2 }}>
                  {roleStyle.label}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Navigation Links (Role Scoped Only) */}
        <nav style={{ flex: 1, padding: '0.75rem 0.75rem', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: 4 }}>
          {menuItems.map((item, idx) => {
            const isActive = location.pathname === item.path || (item.path !== '/dashboard' && location.pathname.startsWith(item.path));
            return (
              <button
                key={idx}
                onClick={() => navigate(item.path)}
                title={!sidebarOpen ? item.label : ''}
                style={{
                  width: '100%',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '0.875rem',
                  padding: '0.75rem 1rem',
                  borderRadius: 10,
                  border: 'none',
                  background: isActive ? '#0284c7' : 'transparent',
                  color: isActive ? '#ffffff' : '#94a3b8',
                  fontWeight: isActive ? 700 : 500,
                  fontSize: '0.9rem',
                  cursor: 'pointer',
                  transition: 'all 0.15s ease',
                  textAlign: 'left'
                }}
              >
                <div style={{ color: isActive ? '#ffffff' : '#64748b', display: 'flex', flexShrink: 0 }}>
                  {item.icon}
                </div>

                {sidebarOpen && (
                  <div style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'space-between', whiteSpace: 'nowrap', overflow: 'hidden' }}>
                    <span>{item.label}</span>
                    {item.badge && (
                      <span style={{ fontSize: '0.65rem', fontWeight: 800, padding: '2px 6px', borderRadius: 4, background: isActive ? '#0369a1' : '#334155', color: '#ffffff' }}>
                        {item.badge}
                      </span>
                    )}
                  </div>
                )}
              </button>
            );
          })}
        </nav>

        {/* Sign Out Button */}
        <div style={{ padding: '0.75rem', borderTop: '1px solid #1e293b', background: '#090d16' }}>
          <button 
            onClick={() => {
              logout();
              navigate('/login');
            }}
            style={{
              width: '100%',
              display: 'flex',
              alignItems: 'center',
              gap: '0.875rem',
              padding: '0.75rem 1rem',
              borderRadius: 10,
              border: 'none',
              background: 'rgba(239, 68, 68, 0.1)',
              color: '#f87171',
              fontWeight: 700,
              fontSize: '0.875rem',
              cursor: 'pointer'
            }}
          >
            <LogOut size={18} />
            {sidebarOpen && <span>Sign Out</span>}
          </button>
        </div>
      </aside>

      {/* Main Content Layout Container */}
      <div 
        style={{
          flex: 1,
          marginLeft: sidebarOpen ? 260 : 80,
          transition: 'margin-left 0.25s cubic-bezier(0.4, 0, 0.2, 1)',
          display: 'flex',
          flexDirection: 'column',
          minHeight: '100vh',
          width: `calc(100% - ${sidebarOpen ? 260 : 80}px)`
        }}
      >
        {/* Top Header */}
        <header 
          style={{
            height: 70,
            background: '#ffffff',
            borderBottom: '1px solid #e2e8f0',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            padding: '0 2rem',
            position: 'sticky',
            top: 0,
            zIndex: 90,
            boxShadow: '0 1px 3px rgba(0,0,0,0.03)'
          }}
        >
          {/* Search Input */}
          <div style={{ position: 'relative', width: 360 }}>
            <Search size={16} style={{ position: 'absolute', left: 14, top: '50%', transform: 'translateY(-50%)', color: '#94a3b8' }} />
            <input 
              type="text"
              placeholder="Search patients, doctors, records..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              style={{
                width: '100%',
                padding: '0.55rem 1rem 0.55rem 2.5rem',
                borderRadius: 20,
                border: '1px solid #cbd5e1',
                background: '#f8fafc',
                fontSize: '0.875rem',
                outline: 'none',
                color: '#1e293b'
              }}
            />
          </div>

          {/* Top Right Actions */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '1.25rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', padding: '0.4rem 0.85rem', background: roleStyle.bg, border: `1px solid ${roleStyle.color}40`, borderRadius: 20 }}>
              <ShieldCheck size={16} color={roleStyle.color} />
              <span style={{ fontSize: '0.8rem', fontWeight: 800, color: roleStyle.color }}>
                {user?.department || roleStyle.label}
              </span>
            </div>

            <button style={{ position: 'relative', background: '#f1f5f9', border: 'none', width: 38, height: 38, borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#64748b' }}>
              <Bell size={18} />
              <span style={{ position: 'absolute', top: 8, right: 8, width: 8, height: 8, borderRadius: '50%', background: '#ef4444' }}></span>
            </button>

            <div style={{ width: 1, height: 24, background: '#e2e8f0' }}></div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
              <div style={{ width: 38, height: 38, borderRadius: '50%', background: roleStyle.color, color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 800, fontSize: '0.9rem' }}>
                {user?.first_name?.charAt(0) || 'A'}
              </div>
              <div>
                <div style={{ fontWeight: 800, fontSize: '0.875rem', color: '#0f172a', lineHeight: 1.2 }}>
                  {user?.first_name ? `${user.first_name} ${user.last_name || ''}` : 'Administrator'}
                </div>
                <div style={{ fontSize: '0.75rem', color: '#64748b', fontWeight: 600 }}>
                  {user?.title || userRole}
                </div>
              </div>
            </div>
          </div>
        </header>

        {/* Main Dashboard Content View with Security Isolation Filter */}
        <main style={{ flex: 1, padding: '2rem', background: '#f8fafc' }}>
          {isCurrentPathAllowed ? (
            <Outlet />
          ) : (
            <div style={{ maxWidth: 540, margin: '4rem auto', padding: '2.5rem', background: 'white', borderRadius: 16, border: '1px solid #fee2e2', boxShadow: '0 10px 25px rgba(220, 38, 38, 0.08)', textAlign: 'center' }}>
              <div style={{ width: 64, height: 64, borderRadius: '50%', background: '#fee2e2', color: '#dc2626', display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto 1.25rem' }}>
                <Lock size={32} />
              </div>
              <h2 style={{ fontSize: '1.5rem', fontWeight: 900, color: '#0f172a', marginBottom: '0.5rem' }}>Access Restricted</h2>
              <p style={{ color: '#64748b', fontSize: '0.95rem', lineHeight: 1.6, marginBottom: '1.75rem' }}>
                You are currently logged in under <strong>{user?.department || roleStyle.label}</strong>. Unnecessary modules are restricted to enforce HIPAA compliance.
              </p>
              <button 
                onClick={() => navigate(roleStyle.home)} 
                style={{ background: roleStyle.color, color: 'white', padding: '0.75rem 1.5rem', borderRadius: 10, border: 'none', fontWeight: 800, fontSize: '0.95rem', cursor: 'pointer', display: 'inline-flex', alignItems: 'center', gap: '0.5rem' }}
              >
                <ArrowLeft size={18} /> Return to {roleStyle.label} Home
              </button>
            </div>
          )}
        </main>
      </div>
    </div>
  );
};
