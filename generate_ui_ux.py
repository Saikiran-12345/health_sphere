import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Update Frontend Package to include Framer Motion
path_pkg = "frontend/package.json"
with open(path_pkg, "r") as f:
    pkg_content = f.read()

if "framer-motion" not in pkg_content:
    pkg_content = pkg_content.replace(
        '"react-router-dom": "^6.22.3"',
        '"react-router-dom": "^6.22.3",\n    "framer-motion": "^11.0.8",\n    "clsx": "^2.1.0",\n    "tailwind-merge": "^2.2.1"'
    )
    with open(path_pkg, "w") as f:
        f.write(pkg_content)

# 2. Utility for class merging (very common in real react codebases)
create_file('frontend/src/utils/cn.ts', """
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
""")

# 3. Framer Motion Animated Page Wrapper
create_file('frontend/src/components/AnimatedPage.tsx', """
import React from 'react';
import { motion } from 'framer-motion';

const animations = {
  initial: { opacity: 0, y: 15 },
  animate: { opacity: 1, y: 0 },
  exit: { opacity: 0, y: -15 },
};

export const AnimatedPage = ({ children }: { children: React.ReactNode }) => {
  return (
    <motion.div
      variants={animations}
      initial="initial"
      animate="animate"
      exit="exit"
      transition={{ duration: 0.3, ease: "easeOut" }}
      className="h-full w-full"
    >
      {children}
    </motion.div>
  );
};
""")

# 4. Polish the Dashboard Layout (Add User Menu, Search, Smooth styling)
create_file('frontend/src/layouts/DashboardLayout.tsx', """
import React, { useState } from 'react';
import { Outlet, useNavigate, useLocation } from 'react-router-dom';
import { Activity, Users, Settings, LogOut, Menu, X, Bed, Home, Package, CreditCard, Truck, Video, Bell, Search } from 'lucide-react';
import { useAuth } from '../auth/AuthProvider';
import { AnimatedPage } from '../components/AnimatedPage';

export const DashboardLayout: React.FC = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const [sidebarOpen, setSidebarOpen] = useState(true);

  const menuItems = [
    { label: 'Overview', icon: <Home size={20} />, path: '/dashboard' },
    { label: 'Patients', icon: <Users size={20} />, path: '/dashboard/patients' },
    { label: 'Admissions & Beds', icon: <Bed size={20} />, path: '/dashboard/admissions' },
    { label: 'Telemedicine', icon: <Video size={20} />, path: '/dashboard/telemedicine' },
    { label: 'Pharmacy', icon: <Package size={20} />, path: '/dashboard/pharmacy' },
    { label: 'Billing', icon: <CreditCard size={20} />, path: '/dashboard/billing' },
    { label: 'Ambulance', icon: <Truck size={20} />, path: '/dashboard/ambulance' },
  ];

  return (
    <div className="flex h-screen bg-slate-50 font-sans overflow-hidden">
      
      {/* Sidebar */}
      <aside className={`bg-slate-900 text-slate-300 transition-all duration-300 ease-in-out flex flex-col ${sidebarOpen ? 'w-64' : 'w-20'}`}>
        <div className="h-16 flex items-center justify-between px-4 border-b border-slate-800 bg-slate-950">
          <div className="flex items-center gap-3 overflow-hidden whitespace-nowrap">
            <Activity className="text-blue-500 min-w-[24px]" size={24}/>
            {sidebarOpen && <span className="font-bold text-lg text-white tracking-wide">HealthSphere</span>}
          </div>
          <button onClick={() => setSidebarOpen(!sidebarOpen)} className="text-slate-400 hover:text-white transition-colors">
            {sidebarOpen ? <X size={20}/> : <Menu size={20}/>}
          </button>
        </div>

        <nav className="flex-1 py-6 px-3 space-y-1 overflow-y-auto custom-scrollbar">
          {menuItems.map((item, idx) => {
            const isActive = location.pathname === item.path;
            return (
              <button
                key={idx}
                onClick={() => navigate(item.path)}
                className={`w-full flex items-center gap-4 px-3 py-3 rounded-lg transition-all duration-200 group
                  ${isActive ? 'bg-blue-600 text-white shadow-md shadow-blue-900/50' : 'hover:bg-slate-800 hover:text-white'}`}
                title={!sidebarOpen ? item.label : ''}
              >
                <div className={`${isActive ? 'text-white' : 'text-slate-400 group-hover:text-white'}`}>
                  {item.icon}
                </div>
                {sidebarOpen && <span className="font-medium text-sm whitespace-nowrap">{item.label}</span>}
              </button>
            );
          })}
        </nav>

        <div className="p-4 border-t border-slate-800">
          <button onClick={logout} className="w-full flex items-center gap-4 px-3 py-2 rounded-lg text-red-400 hover:bg-red-500/10 hover:text-red-300 transition-colors">
            <LogOut size={20} />
            {sidebarOpen && <span className="font-medium text-sm">Sign Out</span>}
          </button>
        </div>
      </aside>

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col h-screen overflow-hidden relative">
        
        {/* Top Header */}
        <header className="h-16 bg-white border-b border-slate-200 flex items-center justify-between px-8 z-10 shadow-sm">
          <div className="flex items-center bg-slate-100 rounded-full px-4 py-2 w-96 border border-slate-200 focus-within:border-blue-500 focus-within:bg-white transition-all">
            <Search size={18} className="text-slate-400 mr-2" />
            <input type="text" placeholder="Search patients, doctors, or records..." className="bg-transparent border-none outline-none text-sm w-full text-slate-700" />
          </div>
          
          <div className="flex items-center gap-6">
            <button className="relative text-slate-400 hover:text-slate-600 transition-colors">
              <Bell size={20} />
              <span className="absolute -top-1 -right-1 w-2.5 h-2.5 bg-red-500 rounded-full border-2 border-white"></span>
            </button>
            <div className="h-8 w-px bg-slate-200"></div>
            <div className="flex items-center gap-3 cursor-pointer">
              <div className="w-9 h-9 rounded-full bg-gradient-to-tr from-blue-600 to-cyan-500 text-white flex items-center justify-center font-bold text-sm shadow-sm">
                {user?.first_name?.charAt(0) || 'D'}
              </div>
              <div className="hidden md:block text-sm">
                <p className="font-bold text-slate-800 leading-tight">Dr. {user?.last_name || 'Admin'}</p>
                <p className="text-slate-500 text-xs">{user?.role || 'Administrator'}</p>
              </div>
            </div>
          </div>
        </header>

        {/* Page Content with Framer Motion */}
        <main className="flex-1 overflow-x-hidden overflow-y-auto bg-slate-50 p-8">
          <AnimatedPage>
            <Outlet />
          </AnimatedPage>
        </main>
      </div>
    </div>
  );
};
""")

# 5. Fix App.tsx routing so all pages are rendered under the DashboardLayout path correctly
path_app = "frontend/src/App.tsx"
with open(path_app, "r") as f:
    app_content = f.read()

# We need to ensure nested routes are correctly using the layout.
app_content = app_content.replace(
    '<Route path="/patients" element={<PatientsList />} />',
    '<Route path="patients" element={<PatientsList />} />'
)
app_content = app_content.replace('<Route path="/analytics" element={<AIAnalytics />} />', '<Route path="analytics" element={<AIAnalytics />} />')
app_content = app_content.replace('<Route path="/pharmacy" element={<PharmacyInventory />} />', '<Route path="pharmacy" element={<PharmacyInventory />} />')
app_content = app_content.replace('<Route path="/appointments" element={<AppointmentsList />} />', '<Route path="appointments" element={<AppointmentsList />} />')
app_content = app_content.replace('<Route path="/records" element={<MedicalRecords />} />', '<Route path="records" element={<MedicalRecords />} />')
app_content = app_content.replace('<Route path="/admissions" element={<BedManagement />} />', '<Route path="admissions" element={<BedManagement />} />')
app_content = app_content.replace('<Route path="/billing" element={<BillingDashboard />} />', '<Route path="billing" element={<BillingDashboard />} />')
app_content = app_content.replace('<Route path="/ambulance" element={<AmbulanceDispatch />} />', '<Route path="ambulance" element={<AmbulanceDispatch />} />')
app_content = app_content.replace('<Route path="/telemedicine" element={<TelemedicineDashboard />} />', '<Route path="telemedicine" element={<TelemedicineDashboard />} />')

with open(path_app, "w") as f:
    f.write(app_content)

print("UI/UX Overhaul completed.")
