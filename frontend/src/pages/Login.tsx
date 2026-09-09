import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Activity, Eye, EyeOff, ArrowRight, Building2, Stethoscope, Bed, Pill, CreditCard, Truck, Microscope, ShieldCheck, CheckCircle2 } from 'lucide-react';
import { useAuth } from '../auth/AuthProvider';

export const departments = [
  {
    id: 'ADMIN',
    name: 'Hospital Administration',
    email: 'admin@healthsphere.com',
    user: { first_name: 'Saikiran', last_name: 'Reddy', role: 'ADMIN', department: 'Executive Administration', title: 'Chief Administrator' },
    icon: Building2,
    color: '#0284c7',
    bg: '#e0f2fe',
    desc: 'Full System Command & Operations',
    route: '/dashboard'
  },
  {
    id: 'CARDIOLOGY',
    name: 'Cardiology & Outpatient (OPD)',
    email: 'cardiology@healthsphere.com',
    user: { first_name: 'Priya', last_name: 'Nair', role: 'DOCTOR', department: 'Cardiology & OPD', title: 'Senior Cardiologist' },
    icon: Stethoscope,
    color: '#0d9488',
    bg: '#ccfbf1',
    desc: 'OPD Consultations & Clinical Roster',
    route: '/dashboard/doctors'
  },
  {
    id: 'ICU',
    name: 'ICU & Bed Admissions',
    email: 'icu@healthsphere.com',
    user: { first_name: 'Anjali', last_name: 'Sharma', role: 'NURSE_ICU', department: 'ICU & Inpatient', title: 'ICU Charge Nurse' },
    icon: Bed,
    color: '#dc2626',
    bg: '#fee2e2',
    desc: 'ICU Telemetry & Ward Census',
    route: '/dashboard/admissions'
  },
  {
    id: 'PHARMACY',
    name: 'Pharmacy & Supplies',
    email: 'pharmacy@healthsphere.com',
    user: { first_name: 'Ramesh', last_name: 'Kumar', role: 'PHARMACIST', department: 'Pharmacy & Supplies', title: 'Chief Pharmacist' },
    icon: Pill,
    color: '#d97706',
    bg: '#fef3c7',
    desc: 'Drug Inventory & Reorder Alerts',
    route: '/dashboard/pharmacy'
  },
  {
    id: 'BILLING',
    name: 'Billing & Finance',
    email: 'billing@healthsphere.com',
    user: { first_name: 'Sunita', last_name: 'Rao', role: 'FINANCE', department: 'Billing & Accounts', title: 'Finance Controller' },
    icon: CreditCard,
    color: '#4f46e5',
    bg: '#e0e7ff',
    desc: 'Invoices, Copays & EDI Claims',
    route: '/dashboard/billing'
  },
  {
    id: 'EMERGENCY',
    name: 'Ambulance & Emergency Dispatch',
    email: 'emergency@healthsphere.com',
    user: { first_name: 'Raju', last_name: 'Sharma', role: 'DISPATCHER', department: 'Emergency & Fleet', title: 'Fleet Controller' },
    icon: Truck,
    color: '#ea580c',
    bg: '#ffedd5',
    desc: 'Emergency Fleet & GPS Tracking',
    route: '/dashboard/ambulance'
  },
  {
    id: 'LAB',
    name: 'Diagnostics & Radiology',
    email: 'lab@healthsphere.com',
    user: { first_name: 'Amit', last_name: 'Shah', role: 'LAB_TECH', department: 'Diagnostics & ML', title: 'Lab Diagnostics Director' },
    icon: Microscope,
    color: '#8b5cf6',
    bg: '#ede9fe',
    desc: 'Lab Telemetry & AI Diagnostics',
    route: '/dashboard/analytics'
  }
];

export const Login = () => {
  const [selectedDept, setSelectedDept] = useState(departments[0]);
  const [email, setEmail] = useState(departments[0].email);
  const [password, setPassword] = useState('admin123');
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleQuickLogin = (dept: typeof departments[0]) => {
    setSelectedDept(dept);
    setEmail(dept.email);
    setLoading(true);
    setTimeout(() => {
      login({
        id: dept.id,
        email: dept.email,
        first_name: dept.user.first_name,
        last_name: dept.user.last_name,
        role: dept.user.role,
        department: dept.user.department,
        title: dept.user.title
      });
      navigate(dept.route);
    }, 400);
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setTimeout(() => {
      login({
        id: selectedDept.id,
        email: email,
        first_name: selectedDept.user.first_name,
        last_name: selectedDept.user.last_name,
        role: selectedDept.user.role,
        department: selectedDept.user.department,
        title: selectedDept.user.title
      });
      navigate(selectedDept.route);
    }, 400);
  };

  return (
    <div style={{ display: 'flex', minHeight: '100vh', width: '100%', fontFamily: 'Inter, system-ui, sans-serif', background: '#f8fafc' }}>
      {/* Left Branding Panel */}
      <div style={{ width: '40%', padding: '3.5rem 3rem', background: 'linear-gradient(135deg, #0284c7 0%, #0369a1 50%, #0f172a 100%)', color: 'white', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', position: 'relative', overflow: 'hidden' }}>
        <div style={{ position: 'absolute', width: 300, height: 300, borderRadius: '50%', background: 'rgba(56, 189, 248, 0.2)', filter: 'blur(80px)', top: -50, left: -50 }}></div>
        <div style={{ position: 'absolute', width: 350, height: 350, borderRadius: '50%', background: 'rgba(13, 148, 136, 0.2)', filter: 'blur(90px)', bottom: -50, right: -50 }}></div>

        <div style={{ position: 'relative', zIndex: 1 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '0.5rem' }}>
            <div style={{ width: 42, height: 42, borderRadius: 10, background: 'rgba(255,255,255,0.15)', display: 'flex', alignItems: 'center', justifyContent: 'center', backdropFilter: 'blur(10px)', border: '1px solid rgba(255,255,255,0.2)' }}>
              <Activity size={26} color="#ffffff" />
            </div>
            <span style={{ fontSize: '1.85rem', fontWeight: 900, letterSpacing: '-0.02em' }}>HealthSphere</span>
          </div>
          <p style={{ color: '#bae6fd', fontSize: '0.9rem', fontWeight: 600 }}>Multi-Department Hospital OS 2.0</p>
        </div>

        <div style={{ position: 'relative', zIndex: 1 }}>
          <h2 style={{ fontSize: '2.4rem', fontWeight: 900, lineHeight: 1.2, marginBottom: '1.25rem', letterSpacing: '-0.02em' }}>
            Department Staff <br />
            <span style={{ color: '#38bdf8' }}>Demo & Live Logins</span>
          </h2>
          <p style={{ color: '#bae6fd', lineHeight: 1.7, fontSize: '0.95rem', maxWidth: 440, marginBottom: '2rem' }}>
            Click any department below for 1-Click instant access to role-tailored clinical dashboards, bed telemetry, pharmacy stock, and billing.
          </p>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.85rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', background: 'rgba(255,255,255,0.08)', padding: '0.75rem 1rem', borderRadius: 10, border: '1px solid rgba(255,255,255,0.12)' }}>
              <CheckCircle2 size={20} color="#38bdf8" />
              <span style={{ fontSize: '0.875rem', fontWeight: 600 }}>7 Dedicated Department Login Portals</span>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', background: 'rgba(255,255,255,0.08)', padding: '0.75rem 1rem', borderRadius: 10, border: '1px solid rgba(255,255,255,0.12)' }}>
              <ShieldCheck size={20} color="#34d399" />
              <span style={{ fontSize: '0.875rem', fontWeight: 600 }}>Role-Based Navigation & Access Control</span>
            </div>
          </div>
        </div>

        <p style={{ color: '#7dd3fc', fontSize: '0.85rem', position: 'relative', zIndex: 1 }}>
          &copy; 2026 HealthSphere Enterprise Inc.
        </p>
      </div>

      {/* Right Login Form & Quick Demo Buttons */}
      <div style={{ flex: 1, padding: '3rem', overflowY: 'auto', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
        <div style={{ maxWidth: 680, margin: '0 auto', width: '100%' }}>
          
          <div style={{ marginBottom: '1.5rem' }}>
            <h1 style={{ fontSize: '2rem', fontWeight: 900, color: '#0f172a', letterSpacing: '-0.02em', marginBottom: '0.35rem' }}>
              Select Department to Sign In
            </h1>
            <p style={{ color: '#64748b', fontSize: '0.95rem' }}>
              Click any card below for <strong>1-Click Instant Demo Login</strong> directly to that department:
            </p>
          </div>

          {/* Department Quick Selection Grid */}
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))', gap: '0.85rem', marginBottom: '1.5rem' }}>
            {departments.map((dept) => {
              const Icon = dept.icon;
              const isSelected = selectedDept.id === dept.id;
              return (
                <div
                  key={dept.id}
                  onClick={() => handleQuickLogin(dept)}
                  style={{
                    padding: '1rem',
                    borderRadius: 12,
                    border: isSelected ? `2px solid ${dept.color}` : '1px solid #cbd5e1',
                    background: isSelected ? dept.bg : 'white',
                    cursor: 'pointer',
                    transition: 'all 0.2s ease',
                    boxShadow: isSelected ? '0 4px 14px rgba(0,0,0,0.08)' : '0 1px 3px rgba(0,0,0,0.03)'
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.625rem', marginBottom: 6 }}>
                    <div style={{ width: 32, height: 32, borderRadius: 8, background: dept.color, color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                      <Icon size={18} />
                    </div>
                    <span style={{ fontSize: '0.85rem', fontWeight: 800, color: '#0f172a', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                      {dept.name.split(' ')[0]}
                    </span>
                  </div>
                  <div style={{ fontSize: '0.775rem', color: '#475569', fontWeight: 600 }}>
                    {dept.user.first_name} ({dept.user.role})
                  </div>
                  <div style={{ fontSize: '0.7rem', color: dept.color, fontWeight: 700, marginTop: 4 }}>
                    Goes to &rarr; {dept.route.replace('/dashboard', 'Home')}
                  </div>
                </div>
              );
            })}
          </div>

          {/* Active Selected Department Banner */}
          <div style={{ padding: '1rem 1.25rem', background: selectedDept.bg, border: `1.5px solid ${selectedDept.color}`, borderRadius: 12, marginBottom: '1.5rem', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
              <div style={{ width: 44, height: 44, borderRadius: 10, background: selectedDept.color, color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 800 }}>
                <selectedDept.icon size={22} />
              </div>
              <div>
                <div style={{ fontWeight: 800, fontSize: '1rem', color: '#0f172a' }}>{selectedDept.name}</div>
                <div style={{ fontSize: '0.825rem', color: '#475569', marginTop: 2 }}>
                  Staff: <strong>{selectedDept.user.first_name} {selectedDept.user.last_name}</strong> &bull; {selectedDept.user.title}
                </div>
              </div>
            </div>
            <span style={{ background: selectedDept.color, color: 'white', padding: '0.35rem 0.75rem', borderRadius: 20, fontSize: '0.75rem', fontWeight: 800 }}>
              {selectedDept.user.role}
            </span>
          </div>

          {/* Login Form */}
          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
            <div>
              <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: 700, color: '#334155', marginBottom: '0.5rem' }}>
                Department Email Address
              </label>
              <input 
                className="form-control" 
                type="email" 
                value={email} 
                onChange={e => setEmail(e.target.value)} 
                required 
                style={{ padding: '0.75rem 1rem', fontSize: '0.95rem' }}
              />
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: 700, color: '#334155', marginBottom: '0.5rem' }}>
                Password
              </label>
              <div style={{ position: 'relative' }}>
                <input 
                  className="form-control" 
                  type={showPassword ? 'text' : 'password'} 
                  value={password} 
                  onChange={e => setPassword(e.target.value)} 
                  required 
                  style={{ padding: '0.75rem 1rem', paddingRight: '3rem', fontSize: '0.95rem' }}
                />
                <button 
                  type="button" 
                  onClick={() => setShowPassword(!showPassword)} 
                  style={{ position: 'absolute', right: '1rem', top: '50%', transform: 'translateY(-50%)', background: 'none', border: 'none', cursor: 'pointer', color: '#94a3b8' }}
                >
                  {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
                </button>
              </div>
            </div>

            <button 
              type="submit" 
              className="btn btn-block" 
              disabled={loading} 
              style={{ background: selectedDept.color, color: 'white', padding: '0.9rem', fontSize: '1rem', borderRadius: 10, fontWeight: 800, boxShadow: `0 4px 14px ${selectedDept.color}40`, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}
            >
              {loading ? <span>Logging in...</span> : <><span>Sign In to {selectedDept.name.split(' ')[0]} Dashboard</span> <ArrowRight size={18} /></>}
            </button>
          </form>

        </div>
      </div>
    </div>
  );
};
