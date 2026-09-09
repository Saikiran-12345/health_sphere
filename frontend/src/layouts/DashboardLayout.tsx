import React, { useState } from 'react';
import { Outlet, useNavigate, useLocation } from 'react-router-dom';
import { 
  Activity, Users, Settings, LogOut, Menu, X, Bed, Home, Package, CreditCard, 
  Truck, Video, Bell, Search, Stethoscope, Calendar, FileText, ShieldCheck, ChevronRight, User
} from 'lucide-react';
import { useAuth } from '../auth/AuthProvider';

interface MenuItem {
  label: string;
  icon: React.ReactNode;
  path: string;
  roles?: string[];
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

  // Role-Based Navigation Filtering
  const userRole = user?.role || 'ADMIN';

  const menuItems = allMenuItems.filter(item => {
    if (userRole === 'ADMIN') return true;
    if (item.path === '/dashboard') return true;
    if (userRole === 'DOCTOR') return ['/dashboard/doctors', '/dashboard/patients', '/dashboard/appointments', '/dashboard/records', '/dashboard/telemedicine', '/dashboard/analytics'].includes(item.path);
    if (userRole === 'NURSE_ICU') return ['/dashboard/patients', '/dashboard/admissions', '/dashboard/records', '/dashboard/analytics'].includes(item.path);
    if (userRole === 'PHARMACIST') return ['/dashboard/pharmacy', '/dashboard/patients'].includes(item.path);
    if (userRole === 'FINANCE') return ['/dashboard/billing', '/dashboard/patients'].includes(item.path);
    if (userRole === 'DISPATCHER') return ['/dashboard/ambulance', '/dashboard/patients'].includes(item.path);
    if (userRole === 'LAB_TECH') return ['/dashboard/analytics', '/dashboard/records', '/dashboard/patients'].includes(item.path);
    return true;
  });

  const getRoleColor = (role: string) => {
    switch (role) {
      case 'ADMIN': return { bg: '#e0f2fe', color: '#0284c7', label: 'Hospital Admin' };
      case 'DOCTOR': return { bg: '#ccfbf1', color: '#0d9488', label: 'Cardiology Specialist' };
      case 'NURSE_ICU': return { bg: '#fee2e2', color: '#dc2626', label: 'ICU Charge Nurse' };
      case 'PHARMACIST': return { bg: '#fef3c7', color: '#d97706', label: 'Pharmacy Manager' };
      case 'FINANCE': return { bg: '#e0e7ff', color: '#4f46e5', label: 'Finance Controller' };
      case 'DISPATCHER': return { bg: '#ffedd5', color: '#ea580c', label: 'Fleet Controller' };
      case 'LAB_TECH': return { bg: '#ede9fe', color: '#8b5cf6', label: 'Lab Diagnostics' };
      default: return { bg: '#e0f2fe', color: '#0284c7', label: role };
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

        {/* Navigation Links */}
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
                  textAlign: 'left',
                  position: 'relative'
                }}
                onMouseEnter={(e) => {
                  if (!isActive) {
                    e.currentTarget.style.background = '#1e293b';
                    e.currentTarget.style.color = '#ffffff';
                  }
                }}
                onMouseLeave={(e) => {
                  if (!isActive) {
                    e.currentTarget.style.background = 'transparent';
                    e.currentTarget.style.color = '#94a3b8';
                  }
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
              cursor: 'pointer',
              transition: 'background 0.2s ease'
            }}
            onMouseEnter={(e) => e.currentTarget.style.background = 'rgba(239, 68, 68, 0.2)'}
            onMouseLeave={(e) => e.currentTarget.style.background = 'rgba(239, 68, 68, 0.1)'}
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
              placeholder="Search patients, doctors, records, or beds..."
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
            {/* Active Department Badge */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', padding: '0.4rem 0.85rem', background: roleStyle.bg, border: `1px solid ${roleStyle.color}40`, borderRadius: 20 }}>
              <ShieldCheck size={16} color={roleStyle.color} />
              <span style={{ fontSize: '0.8rem', fontWeight: 800, color: roleStyle.color }}>
                {user?.department || roleStyle.label}
              </span>
            </div>

            {/* Notification Bell */}
            <button 
              style={{
                position: 'relative',
                background: '#f1f5f9',
                border: 'none',
                width: 38,
                height: 38,
                borderRadius: '50%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                cursor: 'pointer',
                color: '#64748b'
              }}
            >
              <Bell size={18} />
              <span style={{ position: 'absolute', top: 8, right: 8, width: 8, height: 8, borderRadius: '50%', background: '#ef4444' }}></span>
            </button>

            <div style={{ width: 1, height: 24, background: '#e2e8f0' }}></div>

            {/* User Profile Info */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
              <div style={{ width: 38, height: 38, borderRadius: '50%', background: 'linear-gradient(135deg, #0284c7, #0d9488)', color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 800, fontSize: '0.9rem', boxShadow: '0 2px 8px rgba(2, 132, 199, 0.25)' }}>
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

        {/* Main Dashboard Content View */}
        <main style={{ flex: 1, padding: '2rem', background: '#f8fafc' }}>
          <Outlet />
        </main>
      </div>
    </div>
  );
};\n