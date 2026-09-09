import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Layouts
create_file('frontend/src/layouts/DashboardLayout.tsx', """
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
""")

# 2. Reusable UI Components
create_file('frontend/src/components/ui/Card.tsx', """
import React from 'react';

export const Card: React.FC<{ children: React.ReactNode; className?: string }> = ({ children, className = '' }) => (
  <div className={`bg-white rounded-lg shadow p-6 ${className}`}>
    {children}
  </div>
);
""")

create_file('frontend/src/components/ui/StatsCard.tsx', """
import React from 'react';
import { Card } from './Card';

interface StatsCardProps {
  title: string;
  value: string | number;
  icon: React.ReactNode;
  trend?: string;
  trendUp?: boolean;
}

export const StatsCard: React.FC<StatsCardProps> = ({ title, value, icon, trend, trendUp }) => (
  <Card className="flex items-center justify-between">
    <div>
      <p className="text-gray-500 text-sm font-medium uppercase tracking-wide">{title}</p>
      <h3 className="mt-2 text-3xl font-bold text-gray-900">{value}</h3>
      {trend && (
        <p className={`mt-2 text-sm font-medium ${trendUp ? 'text-green-600' : 'text-red-600'}`}>
          {trendUp ? '↑' : '↓'} {trend}
        </p>
      )}
    </div>
    <div className="p-4 bg-blue-50 text-blue-600 rounded-full">
      {icon}
    </div>
  </Card>
);
""")

# 3. Dashboards
create_file('frontend/src/pages/dashboards/AdminDashboard.tsx', """
import React from 'react';
import { StatsCard } from '../../components/ui/StatsCard';
import { Users, Calendar, Activity, Bed } from 'lucide-react';
import { ResponsiveContainer, AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';

const dummyChartData = [
  { name: 'Mon', admissions: 12, appointments: 45 },
  { name: 'Tue', admissions: 19, appointments: 52 },
  { name: 'Wed', admissions: 15, appointments: 38 },
  { name: 'Thu', admissions: 22, appointments: 65 },
  { name: 'Fri', admissions: 18, appointments: 48 },
  { name: 'Sat', admissions: 8, appointments: 25 },
  { name: 'Sun', admissions: 5, appointments: 15 },
];

export const AdminDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-gray-800">Hospital Administration</h2>
      
      {/* Top Stats */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <StatsCard title="Total Patients" value="12,450" icon={<Users size={24} />} trend="12% from last month" trendUp={true} />
        <StatsCard title="Today's Appointments" value="142" icon={<Calendar size={24} />} trend="4% from yesterday" trendUp={true} />
        <StatsCard title="Current Admissions" value="89" icon={<Bed size={24} />} trend="2% from last week" trendUp={false} />
        <StatsCard title="AI Risk Alerts" value="7" icon={<Activity size={24} />} trend="High priority" trendUp={false} />
      </div>

      {/* Analytics Chart */}
      <div className="bg-white p-6 rounded-lg shadow">
        <h3 className="text-lg font-bold text-gray-800 mb-4">Weekly Operational Overview</h3>
        <div className="h-80">
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={dummyChartData}>
              <defs>
                <linearGradient id="colorAppts" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.8}/>
                  <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" vertical={false} />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Area type="monotone" dataKey="appointments" stroke="#3b82f6" fillOpacity={1} fill="url(#colorAppts)" />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
};
""")

print("Frontend Core UI Generated.")
