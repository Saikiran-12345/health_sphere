import React, { useState } from 'react';
import { useAuth } from '../auth/AuthProvider';
import { useNavigate, Outlet, Link } from 'react-router-dom';
import { Activity, Calendar, Users, FileText, Settings, LogOut, Menu, X, Bed, Crosshair, Home } from 'lucide-react';

export const DashboardLayout: React.FC = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [sidebarOpen, setSidebarOpen] = useState(true);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const menuItems = [
    { label: 'Dashboard', icon: <Home size={20} />, path: '/dashboard' },
    { label: 'Patients', icon: <Users size={20} />, path: '/patients' },
    { label: 'Appointments', icon: <Calendar size={20} />, path: '/appointments' },
    { label: 'Medical Records', icon: <FileText size={20} />, path: '/records' },
    { label: 'Admissions & Beds', icon: <Bed size={20} />, path: '/admissions' },
    { label: 'AI Risk Analytics', icon: <Activity size={20} />, path: '/analytics' },
    { label: 'Settings', icon: <Settings size={20} />, path: '/settings' }
  ];

  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <aside className={`bg-slate-900 text-white transition-all duration-300 ${sidebarOpen ? 'w-64' : 'w-20'}`}>
        <div className="flex items-center justify-between p-4 border-b border-slate-800">
          <div className={`font-bold text-xl flex items-center gap-2 ${!sidebarOpen && 'hidden'}`}>
            <Crosshair className="text-blue-400" /> HealthSphere
          </div>
          <button onClick={() => setSidebarOpen(!sidebarOpen)} className="text-slate-400 hover:text-white">
            {sidebarOpen ? <X size={20} /> : <Menu size={20} />}
          </button>
        </div>
        
        <nav className="p-4 space-y-2">
          {menuItems.map((item, idx) => (
            <Link key={idx} to={item.path} className="flex items-center gap-4 p-3 rounded hover:bg-slate-800 transition-colors">
              <span className="text-blue-400">{item.icon}</span>
              {sidebarOpen && <span>{item.label}</span>}
            </Link>
          ))}
        </nav>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col overflow-hidden">
        {/* Top Header */}
        <header className="bg-white shadow-sm p-4 flex justify-between items-center">
          <h1 className="text-xl font-semibold text-gray-800">Welcome, {user?.first_name || 'Guest'}</h1>
          <div className="flex items-center gap-4">
            <span className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm font-medium">Role: {user?.role || 'N/A'}</span>
            <button onClick={handleLogout} className="flex items-center gap-2 text-red-600 hover:text-red-800 font-medium">
              <LogOut size={18} /> Logout
            </button>
          </div>
        </header>

        {/* Dynamic Route Content */}
        <div className="flex-1 overflow-auto p-6">
          <Outlet />
        </div>
      </main>
    </div>
  );
};
