import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Activity, Eye, EyeOff, ArrowRight, Building2, Stethoscope, Bed, Pill, CreditCard, Truck, Microscope, ShieldCheck, CheckCircle2, Key } from 'lucide-react';
import { useAuth } from '../auth/AuthProvider';

export const departments = [
  {
    id: 'ADMIN',
    name: 'Hospital Administration',
    email: 'admin@healthsphere.com',
    password: 'admin123',
    user: { id: 'ADMIN-001', first_name: 'Saikiran', last_name: 'Reddy', role: 'ADMIN', department: 'Executive Administration', title: 'Chief Administrator' },
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
    password: 'cardiology123',
    user: { id: 'DOC-101', first_name: 'Priya', last_name: 'Nair', role: 'DOCTOR', department: 'Cardiology & OPD', title: 'Senior Cardiologist' },
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
    password: 'icu123',
    user: { id: 'NURSE-202', first_name: 'Anjali', last_name: 'Sharma', role: 'NURSE_ICU', department: 'ICU & Inpatient', title: 'ICU Charge Nurse' },
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
    password: 'pharmacy123',
    user: { id: 'PHARM-303', first_name: 'Ramesh', last_name: 'Kumar', role: 'PHARMACIST', department: 'Pharmacy & Supplies', title: 'Chief Pharmacist' },
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
    password: 'billing123',
    user: { id: 'FIN-404', first_name: 'Sunita', last_name: 'Rao', role: 'FINANCE', department: 'Billing & Accounts', title: 'Finance Controller' },
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
    password: 'emergency123',
    user: { id: 'DISP-505', first_name: 'Raju', last_name: 'Sharma', role: 'DISPATCHER', department: 'Emergency & Fleet', title: 'Fleet Controller' },
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
    password: 'lab123',
    user: { id: 'LAB-606', first_name: 'Amit', last_name: 'Shah', role: 'LAB_TECH', department: 'Diagnostics & ML', title: 'Lab Diagnostics Director' },
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
  const [password, setPassword] = useState(departments[0].password);
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSelectDept = (dept: typeof departments[0]) => {
    setSelectedDept(dept);
    setEmail(dept.email);
    setPassword(dept.password);
  };

  const handleQuickLogin = (dept: typeof departments[0]) => {
    setSelectedDept(dept);
    setEmail(dept.email);
    setPassword(dept.password);
    setLoading(true);
    setTimeout(() => {
      login({
        id: dept.user.id,
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
        id: selectedDept.user.id,
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
      <div style={{ width: '38%', padding: '3.5rem 3rem', background: 'linear-gradient(135deg, #0284c7 0%, #0369a1 50%, #0f172a 100%)', color: 'white', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', position: 'relative', overflow: 'hidden' }}>
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
            7 Department <br />
            <span style={{ color: '#38bdf8' }}>Isolated Logins</span>
          </h2>
          <p style={{ color: '#bae6fd', lineHeight: 1.7, fontSize: '0.95rem', maxWidth: 440, marginBottom: '2rem' }}>
            Role-Based Access Control (RBAC) active. Each staff login unlocks only features relevant to their department.
          </p>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.85rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', background: 'rgba(255,255,255,0.08)', padding: '0.75rem 1rem', borderRadius: 10, border: '1px solid rgba(255,255,255,0.12)' }}>
              <CheckCircle2 size={20} color="#38bdf8" />
              <span style={{ fontSize: '0.875rem', fontWeight: 600 }}>7 Strict Role-Isolated Portals</span>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', background: 'rgba(255,255,255,0.08)', padding: '0.75rem 1rem', borderRadius: 10, border: '1px solid rgba(255,255,255,0.12)' }}>
              <ShieldCheck size={20} color="#34d399" />
              <span style={{ fontSize: '0.875rem', fontWeight: 600 }}>Unrelated Features Hidden Automatically</span>
            </div>
          </div>
        </div>

        <p style={{ color: '#7dd3fc', fontSize: '0.85rem', position: 'relative', zIndex: 1 }}>
          &copy; 2026 HealthSphere Enterprise Inc.
        </p>
      </div>

      {/* Right Form & Demo Credentials Cheat-Sheet */}
      <div style={{ flex: 1, padding: '3rem', overflowY: 'auto', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
        <div style={{ maxWidth: 720, margin: '0 auto', width: '100%' }}>
          
          <div style={{ marginBottom: '1.25rem' }}>
            <h1 style={{ fontSize: '2rem', fontWeight: 900, color: '#0f172a', letterSpacing: '-0.02em', marginBottom: '0.35rem' }}>
              Department Staff Sign In
            </h1>
            <p style={{ color: '#64748b', fontSize: '0.95rem' }}>
              Select a department card below or use the <strong>Demo Credentials Cheat-Sheet</strong>:
            </p>
          </div>

          {/* Department Selection Cards */}
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(210px, 1fr))', gap: '0.75rem', marginBottom: '1.25rem' }}>
            {departments.map((dept) => {
              const Icon = dept.icon;
              const isSelected = selectedDept.id === dept.id;
              return (
                <div
                  key={dept.id}
                  onClick={() => handleSelectDept(dept)}
                  style={{
                    padding: '0.85rem',
                    borderRadius: 10,
                    border: isSelected ? `2px solid ${dept.color}` : '1px solid #cbd5e1',
                    background: isSelected ? dept.bg : 'white',
                    cursor: 'pointer',
                    transition: 'all 0.2s ease',
                    boxShadow: isSelected ? '0 4px 14px rgba(0,0,0,0.08)' : '0 1px 3px rgba(0,0,0,0.03)'
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: 4 }}>
                    <div style={{ width: 28, height: 28, borderRadius: 6, background: dept.color, color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                      <Icon size={16} />
                    </div>
                    <span style={{ fontSize: '0.85rem', fontWeight: 800, color: '#0f172a', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                      {dept.name.split(' ')[0]}
                    </span>
                  </div>
                  <div style={{ fontSize: '0.75rem', color: '#475569', fontWeight: 600 }}>
                    {dept.user.first_name} ({dept.user.role})
                  </div>
                </div>
              );
            })}
          </div>

          {/* Active Selected Department Banner */}
          <div style={{ padding: '0.85rem 1rem', background: selectedDept.bg, border: `1.5px solid ${selectedDept.color}`, borderRadius: 10, marginBottom: '1.25rem', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
              <div style={{ width: 38, height: 38, borderRadius: 8, background: selectedDept.color, color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                <selectedDept.icon size={20} />
              </div>
              <div>
                <div style={{ fontWeight: 800, fontSize: '0.95rem', color: '#0f172a' }}>{selectedDept.name}</div>
                <div style={{ fontSize: '0.8rem', color: '#475569' }}>
                  Staff: <strong>{selectedDept.user.first_name} {selectedDept.user.last_name}</strong> &bull; {selectedDept.user.title}
                </div>
              </div>
            </div>
            <button 
              type="button" 
              onClick={() => handleQuickLogin(selectedDept)}
              style={{ background: selectedDept.color, color: 'white', padding: '0.4rem 0.85rem', borderRadius: 8, border: 'none', fontWeight: 800, fontSize: '0.8rem', cursor: 'pointer' }}
            >
              1-Click Demo Login &rarr;
            </button>
          </div>

          {/* Login Form */}
          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <div>
              <label style={{ display: 'block', fontSize: '0.85rem', fontWeight: 700, color: '#334155', marginBottom: '0.35rem' }}>
                Department Email Address
              </label>
              <input 
                className="form-control" 
                type="email" 
                value={email} 
                onChange={e => setEmail(e.target.value)} 
                required 
                style={{ padding: '0.65rem 0.85rem', fontSize: '0.9rem' }}
              />
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '0.85rem', fontWeight: 700, color: '#334155', marginBottom: '0.35rem' }}>
                Password
              </label>
              <div style={{ position: 'relative' }}>
                <input 
                  className="form-control" 
                  type={showPassword ? 'text' : 'password'} 
                  value={password} 
                  onChange={e => setPassword(e.target.value)} 
                  required 
                  style={{ padding: '0.65rem 0.85rem', paddingRight: '3rem', fontSize: '0.9rem' }}
                />
                <button 
                  type="button" 
                  onClick={() => setShowPassword(!showPassword)} 
                  style={{ position: 'absolute', right: '0.85rem', top: '50%', transform: 'translateY(-50%)', background: 'none', border: 'none', cursor: 'pointer', color: '#94a3b8' }}
                >
                  {showPassword ? <EyeOff size={16} /> : <Eye size={16} />}
                </button>
              </div>
            </div>

            <button 
              type="submit" 
              className="btn btn-block" 
              disabled={loading} 
              style={{ background: selectedDept.color, color: 'white', padding: '0.75rem', fontSize: '0.95rem', borderRadius: 8, fontWeight: 800, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}
            >
              {loading ? <span>Logging in...</span> : <><span>Sign In to {selectedDept.name.split(' ')[0]}</span> <ArrowRight size={16} /></>}
            </button>
          </form>

          {/* Demo Credentials Cheat-Sheet Card */}
          <div style={{ marginTop: '1.5rem', padding: '1rem', background: '#f1f5f9', borderRadius: 12, border: '1px solid #cbd5e1' }}>
            <div style={{ fontSize: '0.875rem', fontWeight: 800, color: '#0f172a', marginBottom: '0.75rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <Key size={16} color="#0284c7" /> Official Department Demo Credentials
            </div>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(210px, 1fr))', gap: '0.5rem' }}>
              {departments.map(d => (
                <div key={d.id} onClick={() => handleSelectDept(d)} style={{ background: 'white', padding: '0.5rem 0.65rem', borderRadius: 6, border: '1px solid #e2e8f0', cursor: 'pointer' }}>
                  <div style={{ fontWeight: 800, fontSize: '0.775rem', color: d.color }}>{d.name.split(' ')[0]} ({d.user.role})</div>
                  <div style={{ fontSize: '0.725rem', color: '#334155', fontFamily: 'monospace' }}>{d.email}</div>
                  <div style={{ fontSize: '0.725rem', color: '#64748b' }}>Pass: <strong style={{ color: '#0284c7' }}>{d.password}</strong></div>
                </div>
              ))}
            </div>
          </div>

        </div>
      </div>
    </div>
  );
};
