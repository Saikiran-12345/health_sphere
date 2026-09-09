import React from 'react';
import { Activity, Shield, Users, ArrowRight, HeartPulse, Stethoscope, Clock, CheckCircle } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export const LandingPage = () => {
  const navigate = useNavigate();

  return (
    <div style={{ minHeight: '100vh', background: '#f8fafc', fontFamily: 'Inter, system-ui, sans-serif' }}>
      {/* Navigation Bar */}
      <nav style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '1.25rem 2.5rem', background: 'white', borderBottom: '1px solid #e2e8f0', boxShadow: '0 1px 3px rgba(0,0,0,0.05)' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', cursor: 'pointer' }} onClick={() => navigate('/')}>
          <div style={{ width: 36, height: 36, borderRadius: 8, background: '#0284c7', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'white' }}>
            <Activity size={22} />
          </div>
          <span style={{ fontSize: '1.5rem', fontWeight: 900, color: '#0f172a', letterSpacing: '-0.02em' }}>HealthSphere</span>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '2rem', fontSize: '0.95rem', fontWeight: 600, color: '#64748b' }}>
          <a href="#features" style={{ textDecoration: 'none', color: '#475569' }}>Features</a>
          <a href="#solutions" style={{ textDecoration: 'none', color: '#475569' }}>Solutions</a>
          <a href="#departments" style={{ textDecoration: 'none', color: '#475569' }}>Departments</a>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
          <button 
            onClick={() => navigate('/login')}
            style={{ padding: '0.625rem 1.25rem', background: 'transparent', border: '1px solid #0284c7', color: '#0284c7', borderRadius: 8, fontWeight: 700, cursor: 'pointer', fontSize: '0.9rem' }}
          >
            Department Sign In
          </button>
          <button 
            onClick={() => navigate('/dashboard')}
            style={{ padding: '0.625rem 1.5rem', background: 'linear-gradient(135deg, #0284c7, #0369a1)', color: 'white', border: 'none', borderRadius: 8, fontWeight: 700, cursor: 'pointer', fontSize: '0.9rem', boxShadow: '0 4px 14px rgba(2, 132, 199, 0.35)' }}
          >
            Launch Command Center
          </button>
        </div>
      </nav>

      {/* Hero Section */}
      <header style={{ padding: '5rem 2rem 6rem', textAlign: 'center', background: 'linear-gradient(180deg, #ffffff 0%, #f0f9ff 100%)', borderBottom: '1px solid #e2e8f0' }}>
        <div style={{ maxWidth: 860, margin: '0 auto' }}>
          <div style={{ display: 'inline-flex', alignItems: 'center', gap: 8, padding: '0.5rem 1.25rem', borderRadius: 9999, background: '#e0f2fe', color: '#0284c7', fontSize: '0.875rem', fontWeight: 700, marginBottom: '1.5rem', border: '1px solid #bae6fd' }}>
            <span style={{ width: 8, height: 8, borderRadius: '50%', background: '#0284c7' }}></span>
            Enterprise Medical Operating System 2.0
          </div>
          
          <h1 style={{ fontSize: '3.5rem', fontWeight: 900, color: '#0f172a', lineHeight: 1.15, letterSpacing: '-0.03em', marginBottom: '1.5rem' }}>
            Connected Care. Smarter Healthcare. <br />
            <span style={{ background: 'linear-gradient(135deg, #0284c7, #0d9488)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
              Better Outcomes.
            </span>
          </h1>

          <p style={{ fontSize: '1.2rem', color: '#64748b', lineHeight: 1.6, maxWidth: 680, margin: '0 auto 2.5rem' }}>
            Unify clinical queues, patient admissions, ICU vitals telemetry, pharmacy inventory, and AI risk predictions into one ridiculously fast hospital platform.
          </p>

          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '1rem' }}>
            <button 
              onClick={() => navigate('/login')}
              style={{ padding: '0.9rem 2rem', background: '#0f172a', color: 'white', border: 'none', borderRadius: 10, fontWeight: 700, fontSize: '1rem', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 8, boxShadow: '0 10px 25px rgba(15,23,42,0.2)' }}
            >
              Access Department Portal <ArrowRight size={18} />
            </button>
            <button 
              onClick={() => navigate('/dashboard')}
              style={{ padding: '0.9rem 2rem', background: 'white', color: '#0284c7', border: '2px solid #0284c7', borderRadius: 10, fontWeight: 700, fontSize: '1rem', cursor: 'pointer' }}
            >
              Explore Live Dashboard
            </button>
          </div>
        </div>
      </header>

      {/* Features Grid */}
      <section id="features" style={{ padding: '5rem 2rem', maxWidth: 1200, margin: '0 auto' }}>
        <div style={{ textAlign: 'center', marginBottom: '3.5rem' }}>
          <h2 style={{ fontSize: '2.25rem', fontWeight: 900, color: '#0f172a', marginBottom: '0.5rem' }}>
            Built for Doctors, Nurses, and Administrators
          </h2>
          <p style={{ color: '#64748b', fontSize: '1.1rem' }}>Enterprise-grade clinical infrastructure designed for modern hospital workflows</p>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '2rem' }}>
          <div style={{ padding: '2rem', background: 'white', borderRadius: 16, border: '1px solid #e2e8f0', boxShadow: '0 4px 6px -1px rgba(0,0,0,0.05)' }}>
            <div style={{ width: 48, height: 48, borderRadius: 12, background: '#e0f2fe', color: '#0284c7', display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: '1.25rem' }}>
              <HeartPulse size={26} />
            </div>
            <h3 style={{ fontSize: '1.25rem', fontWeight: 800, color: '#0f172a', marginBottom: '0.75rem' }}>AI Patient Risk Engine</h3>
            <p style={{ color: '#64748b', lineHeight: 1.6 }}>Predict 30-day readmission risks, cardiac vitals anomalies, and sepsis warnings using integrated Scikit-learn Random Forest models.</p>
          </div>

          <div style={{ padding: '2rem', background: 'white', borderRadius: 16, border: '1px solid #e2e8f0', boxShadow: '0 4px 6px -1px rgba(0,0,0,0.05)' }}>
            <div style={{ width: 48, height: 48, borderRadius: 12, background: '#ccfbf1', color: '#0d9488', display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: '1.25rem' }}>
              <Stethoscope size={26} />
            </div>
            <h3 style={{ fontSize: '1.25rem', fontWeight: 800, color: '#0f172a', marginBottom: '0.75rem' }}>Unified EMR & Records</h3>
            <p style={{ color: '#64748b', lineHeight: 1.6 }}>Lightning-fast patient timeline tracking prescriptions, lab telemetry, DICOM X-ray scans, and physician consultation notes.</p>
          </div>

          <div style={{ padding: '2rem', background: 'white', borderRadius: 16, border: '1px solid #e2e8f0', boxShadow: '0 4px 6px -1px rgba(0,0,0,0.05)' }}>
            <div style={{ width: 48, height: 48, borderRadius: 12, background: '#ede9fe', color: '#8b5cf6', display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: '1.25rem' }}>
              <Clock size={26} />
            </div>
            <h3 style={{ fontSize: '1.25rem', fontWeight: 800, color: '#0f172a', marginBottom: '0.75rem' }}>Real-time Telemedicine</h3>
            <p style={{ color: '#64748b', lineHeight: 1.6 }}>Conduct remote video consultations, WebSocket live clinical chat, and automated appointment scheduling effortlessly.</p>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer style={{ background: '#0f172a', padding: '3rem 2rem', color: '#94a3b8', textAlign: 'center', borderTop: '1px solid #1e293b' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem', marginBottom: '1rem', color: 'white' }}>
          <Activity size={24} color="#38bdf8" />
          <span style={{ fontSize: '1.25rem', fontWeight: 900 }}>HealthSphere Enterprise</span>
        </div>
        <p style={{ fontSize: '0.9rem' }}>&copy; 2026 HealthSphere Enterprise Inc. All rights reserved. HIPAA Compliant System.</p>
      </footer>
    </div>
  );
};
