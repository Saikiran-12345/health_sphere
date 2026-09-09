import os

BASE = r"C:\Users\saikiran\Desktop\eliteiq project zips\5 loc project\HEALTHSPHERE"

def w(rel_path, content):
    path = os.path.join(BASE, rel_path)
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. DataContext
w('frontend/src/context/DataContext.tsx', '''
import React, { createContext, useContext, useState, useEffect } from 'react';

export interface Doctor {
  id: string;
  name: string;
  spec: string;
  dept: string;
  phone: string;
  email: string;
  status: string;
  patientsCount: number;
}

export interface Patient {
  id: string;
  name: string;
  age: number;
  gender: string;
  phone: string;
  blood: string;
  condition: string;
  doctor: string;
  admitted: string;
  status: string;
}

export interface Appointment {
  id: string;
  patient: string;
  doctor: string;
  dept: string;
  date: string;
  time: string;
  status: string;
}

interface DataContextType {
  doctors: Doctor[];
  patients: Patient[];
  appointments: Appointment[];
  addDoctor: (doc: Doctor) => void;
  addPatient: (pat: Patient) => void;
  addAppointment: (apt: Appointment) => void;
}

const initialDoctors: Doctor[] = [
  { id: 'DOC-101', name: 'Dr. Saikiran Reddy', spec: 'Cardiology', dept: 'Cardiology', phone: '+91 98765 11111', email: 'saikiran@healthsphere.com', status: 'Active', patientsCount: 142 },
  { id: 'DOC-102', name: 'Dr. Priya Nair', spec: 'Neurology', dept: 'Neurology', phone: '+91 98765 22222', email: 'priya@healthsphere.com', status: 'Active', patientsCount: 98 },
  { id: 'DOC-103', name: 'Dr. Neha Gupta', spec: 'Gynecology & Obstetrics', dept: 'Maternity', phone: '+91 98765 33333', email: 'neha@healthsphere.com', status: 'Active', patientsCount: 115 },
  { id: 'DOC-104', name: 'Dr. Amit Shah', spec: 'General Medicine & Dialysis', dept: 'General', phone: '+91 98765 44444', email: 'amit@healthsphere.com', status: 'Active', patientsCount: 160 },
  { id: 'DOC-105', name: 'Dr. Vikramaditya Rao', spec: 'Orthopedics & Surgery', dept: 'Surgery', phone: '+91 98765 55555', email: 'vikram@healthsphere.com', status: 'On Leave', patientsCount: 74 },
];

const initialPatients: Patient[] = [
  { id: 'P-1001', name: 'Arun Kumar', age: 45, gender: 'Male', phone: '+91 98765 43210', blood: 'O+', condition: 'Hypertension', doctor: 'Dr. Saikiran Reddy', admitted: '2024-01-15', status: 'admitted' },
  { id: 'P-1002', name: 'Priya Sharma', age: 32, gender: 'Female', phone: '+91 87654 32109', blood: 'A+', condition: 'Pregnancy (32 weeks)', doctor: 'Dr. Neha Gupta', admitted: '2024-01-18', status: 'admitted' },
  { id: 'P-1003', name: 'Raj Patel', age: 58, gender: 'Male', phone: '+91 76543 21098', blood: 'B+', condition: 'Type 2 Diabetes', doctor: 'Dr. Amit Shah', admitted: '-', status: 'outpatient' },
  { id: 'P-1004', name: 'Meera Reddy', age: 28, gender: 'Female', phone: '+91 65432 10987', blood: 'AB+', condition: 'Appendicitis', doctor: 'Dr. Saikiran Reddy', admitted: '2024-01-20', status: 'discharged' },
  { id: 'P-1005', name: 'Vikram Singh', age: 67, gender: 'Male', phone: '+91 54321 09876', blood: 'O-', condition: 'Coronary Artery Disease', doctor: 'Dr. Priya Nair', admitted: '2024-01-12', status: 'critical' },
  { id: 'P-1006', name: 'Sunita Rao', age: 41, gender: 'Female', phone: '+91 43210 98765', blood: 'A-', condition: 'Migraine', doctor: 'Dr. Neha Gupta', admitted: '-', status: 'outpatient' },
  { id: 'P-1007', name: 'Deepak Mishra', age: 53, gender: 'Male', phone: '+91 32109 87654', blood: 'B-', condition: 'Chronic Kidney Disease', doctor: 'Dr. Amit Shah', admitted: '2024-01-19', status: 'admitted' },
  { id: 'P-1008', name: 'Latha Krishnan', age: 36, gender: 'Female', phone: '+91 21098 76543', blood: 'AB-', condition: 'Thyroid Disorder', doctor: 'Dr. Priya Nair', admitted: '-', status: 'outpatient' },
];

const initialAppointments: Appointment[] = [
  { id: 'APT-301', patient: 'Anita Desai', doctor: 'Dr. Saikiran Reddy', dept: 'Cardiology', date: '2024-01-22', time: '9:00 AM', status: 'confirmed' },
  { id: 'APT-302', patient: 'Rahul Verma', doctor: 'Dr. Priya Nair', dept: 'Neurology', date: '2024-01-22', time: '9:30 AM', status: 'confirmed' },
  { id: 'APT-303', patient: 'Kiran Joshi', doctor: 'Dr. Saikiran Reddy', dept: 'Cardiology', date: '2024-01-22', time: '10:00 AM', status: 'in_progress' },
  { id: 'APT-304', patient: 'Sunita Rao', doctor: 'Dr. Amit Shah', dept: 'General', date: '2024-01-22', time: '10:30 AM', status: 'scheduled' },
  { id: 'APT-305', patient: 'Deepak Mishra', doctor: 'Dr. Neha Gupta', dept: 'Oncology', date: '2024-01-22', time: '11:00 AM', status: 'scheduled' },
  { id: 'APT-306', patient: 'Latha Krishnan', doctor: 'Dr. Priya Nair', dept: 'Neurology', date: '2024-01-22', time: '11:30 AM', status: 'completed' },
  { id: 'APT-307', patient: 'Pooja Thakur', doctor: 'Dr. Saikiran Reddy', dept: 'Cardiology', date: '2024-01-22', time: '2:00 PM', status: 'cancelled' },
];

const DataContext = createContext<DataContextType>({
  doctors: [],
  patients: [],
  appointments: [],
  addDoctor: () => {},
  addPatient: () => {},
  addAppointment: () => {},
});

export const useHospitalData = () => useContext(DataContext);

export const DataProvider = ({ children }: { children: React.ReactNode }) => {
  const [doctors, setDoctors] = useState<Doctor[]>(() => {
    const s = localStorage.getItem('hs_doctors');
    return s ? JSON.parse(s) : initialDoctors;
  });

  const [patients, setPatients] = useState<Patient[]>(() => {
    const s = localStorage.getItem('hs_patients');
    return s ? JSON.parse(s) : initialPatients;
  });

  const [appointments, setAppointments] = useState<Appointment[]>(() => {
    const s = localStorage.getItem('hs_appointments');
    return s ? JSON.parse(s) : initialAppointments;
  });

  useEffect(() => { localStorage.setItem('hs_doctors', JSON.stringify(doctors)); }, [doctors]);
  useEffect(() => { localStorage.setItem('hs_patients', JSON.stringify(patients)); }, [patients]);
  useEffect(() => { localStorage.setItem('hs_appointments', JSON.stringify(appointments)); }, [appointments]);

  const addDoctor = (doc: Doctor) => setDoctors(prev => [doc, ...prev]);
  const addPatient = (pat: Patient) => setPatients(prev => [pat, ...prev]);
  const addAppointment = (apt: Appointment) => setAppointments(prev => [apt, ...prev]);

  return (
    <DataContext.Provider value={{ doctors, patients, appointments, addDoctor, addPatient, addAppointment }}>
      {children}
    </DataContext.Provider>
  );
};
''')

# 2. Toast Component
w('frontend/src/components/Toast.tsx', '''
import React, { useState, createContext, useContext } from 'react';
import { CheckCircle, AlertTriangle, XCircle, X, Info } from 'lucide-react';

interface ToastItem {
  id: number;
  message: string;
  type: 'success' | 'error' | 'warning' | 'info';
}

interface ToastContextType {
  showToast: (message: string, type?: 'success' | 'error' | 'warning' | 'info') => void;
}

const ToastContext = createContext<ToastContextType>({ showToast: () => {} });
export const useToast = () => useContext(ToastContext);

const icons: any = { success: CheckCircle, error: XCircle, warning: AlertTriangle, info: Info };
const colors: any = {
  success: { bg: '#dcfce7', border: '#bbf7d0', color: '#16a34a' },
  error: { bg: '#fee2e2', border: '#fecaca', color: '#dc2626' },
  warning: { bg: '#fef3c7', border: '#fde68a', color: '#d97706' },
  info: { bg: '#e0f2fe', border: '#bae6fd', color: '#0284c7' },
};

export const ToastProvider = ({ children }: { children: React.ReactNode }) => {
  const [toasts, setToasts] = useState<ToastItem[]>([]);
  let counter = 0;

  const showToast = (message: string, type: 'success' | 'error' | 'warning' | 'info' = 'success') => {
    const id = Date.now() + (counter++);
    setToasts(prev => [...prev, { id, message, type }]);
    setTimeout(() => setToasts(prev => prev.filter(t => t.id !== id)), 4000);
  };

  const dismiss = (id: number) => setToasts(prev => prev.filter(t => t.id !== id));

  return (
    <ToastContext.Provider value={{ showToast }}>
      {children}
      <div style={{ position: 'fixed', top: 20, right: 20, zIndex: 9999, display: 'flex', flexDirection: 'column', gap: 8 }}>
        {toasts.map(toast => {
          const Icon = icons[toast.type];
          const c = colors[toast.type];
          return (
            <div key={toast.id} style={{
              display: 'flex', alignItems: 'center', gap: '0.75rem',
              padding: '0.85rem 1.25rem', borderRadius: 8,
              background: c.bg, border: '1px solid ' + c.border,
              boxShadow: '0 4px 12px rgba(0,0,0,0.1)',
              animation: 'slideIn 0.3s ease-out',
              minWidth: 300, maxWidth: 420
            }}>
              <Icon size={18} style={{ color: c.color, flexShrink: 0 }} />
              <span style={{ flex: 1, fontSize: '0.9rem', fontWeight: 500, color: '#1e293b' }}>{toast.message}</span>
              <button onClick={() => dismiss(toast.id)} style={{ background: 'none', border: 'none', cursor: 'pointer', color: '#94a3b8', padding: 2 }}><X size={16} /></button>
            </div>
          );
        })}
      </div>
    </ToastContext.Provider>
  );
};
''')

# 3. DoctorsList
w('frontend/src/pages/doctors/DoctorsList.tsx', '''
import React, { useState } from 'react';
import { Search, Plus } from 'lucide-react';
import { useHospitalData, Doctor } from '../../context/DataContext';

export const DoctorsList = () => {
  const { doctors, addDoctor } = useHospitalData();
  const [search, setSearch] = useState('');
  const [showModal, setShowModal] = useState(false);

  const [name, setName] = useState('');
  const [spec, setSpec] = useState('');
  const [dept, setDept] = useState('Cardiology');
  const [phone, setPhone] = useState('');
  const [email, setEmail] = useState('');

  const filtered = doctors.filter(d => d.name.toLowerCase().includes(search.toLowerCase()) || d.spec.toLowerCase().includes(search.toLowerCase()));

  const handleAddDoctor = (e: React.FormEvent) => {
    e.preventDefault();
    if (!name || !spec) return;
    const newDoc: Doctor = {
      id: `DOC-${Math.floor(100 + Math.random() * 900)}`,
      name: name.startsWith('Dr.') ? name : `Dr. ${name}`,
      spec,
      dept,
      phone: phone || '+91 98765 00000',
      email: email || `${name.toLowerCase().replace(/\\s+/g, '')}@healthsphere.com`,
      status: 'Active',
      patientsCount: 0
    };
    addDoctor(newDoc);
    setName(''); setSpec(''); setPhone(''); setEmail('');
    setShowModal(false);
  };

  return (
    <div>
      <div className="page-header">
        <div className="page-title"><h2>Medical Staff Directory</h2><p>Manage hospital doctors and specialists</p></div>
        <button className="btn btn-primary" onClick={() => setShowModal(true)}><Plus size={16} /> Add Doctor</button>
      </div>

      <div style={{ display: 'flex', gap: '1rem', marginBottom: '1.5rem' }}>
        <div style={{ flex: 1, position: 'relative' }}>
          <Search size={16} style={{ position: 'absolute', left: 12, top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
          <input className="form-control" style={{ paddingLeft: '2.5rem' }} placeholder="Search doctor by name or specialty..." value={search} onChange={e => setSearch(e.target.value)} />
        </div>
      </div>

      <div className="data-table-container">
        <div className="table-header"><h3>Active Doctors ({filtered.length})</h3></div>
        <table className="data-table">
          <thead><tr><th>ID</th><th>Doctor Name</th><th>Specialty</th><th>Department</th><th>Contact</th><th>Status</th></tr></thead>
          <tbody>
            {filtered.map(d => (
              <tr key={d.id}>
                <td style={{ fontWeight: 600, color: 'var(--primary-color)' }}>{d.id}</td>
                <td style={{ fontWeight: 700 }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                    <div style={{ width: 32, height: 32, borderRadius: '50%', background: '#e0f2fe', color: '#0284c7', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 700, fontSize: '0.8rem' }}>
                      {d.name.split(' ').pop()?.charAt(0) || 'D'}
                    </div>
                    <div>
                      <div>{d.name}</div>
                      <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>{d.email}</div>
                    </div>
                  </div>
                </td>
                <td><span className="badge badge-primary">{d.spec}</span></td>
                <td>{d.dept}</td>
                <td style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>{d.phone}</td>
                <td><span className={`badge ${d.status === 'Active' ? 'badge-stable' : 'badge-monitoring'}`}>{d.status}</span></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {showModal && (
        <div className="modal-overlay">
          <div className="modal-content">
            <div className="modal-header"><h3>Add New Doctor</h3><button className="modal-close" onClick={() => setShowModal(false)}>&times;</button></div>
            <form onSubmit={handleAddDoctor}>
              <div className="modal-body">
                <div className="form-group"><label>Full Name</label><input className="form-control" placeholder="e.g. Dr. Rajesh Sharma" value={name} onChange={e => setName(e.target.value)} required /></div>
                <div className="form-group"><label>Specialization</label><input className="form-control" placeholder="e.g. Neurologist" value={spec} onChange={e => setSpec(e.target.value)} required /></div>
                <div className="form-group"><label>Department</label><select className="form-control" value={dept} onChange={e => setDept(e.target.value)}><option value="Cardiology">Cardiology</option><option value="Neurology">Neurology</option><option value="Maternity">Maternity</option><option value="General">General</option></select></div>
                <div className="form-group"><label>Phone</label><input className="form-control" placeholder="+91 98765 00000" value={phone} onChange={e => setPhone(e.target.value)} /></div>
                <div className="form-group"><label>Email</label><input className="form-control" type="email" placeholder="doctor@healthsphere.com" value={email} onChange={e => setEmail(e.target.value)} /></div>
              </div>
              <div className="modal-footer"><button type="button" className="btn btn-outline" onClick={() => setShowModal(false)}>Cancel</button><button type="submit" className="btn btn-primary">Save Doctor</button></div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
''')

# 4. SettingsPage
w('frontend/src/pages/settings/SettingsPage.tsx', '''
import React, { useState } from 'react';
import { Save, Building, Globe, Shield, Bell } from 'lucide-react';

export const SettingsPage = () => {
  const [saved, setSaved] = useState(false);
  const handleSave = () => { setSaved(true); setTimeout(() => setSaved(false), 3000); };

  return (
    <div>
      <div className="page-header"><div className="page-title"><h2>System Settings</h2><p>Configure hospital preferences and security</p></div></div>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
        <div className="data-table-container">
          <div className="table-header"><h3 style={{ display: 'flex', alignItems: 'center', gap: 8 }}><Building size={18} /> Hospital Information</h3></div>
          <div style={{ padding: '1.5rem' }}>
            <div className="form-group"><label>Hospital Name</label><input className="form-control" defaultValue="HealthSphere General Hospital" /></div>
            <div className="form-group"><label>Registration No.</label><input className="form-control" defaultValue="HOSP-KA-2024-08741" /></div>
          </div>
        </div>
        <div className="data-table-container">
          <div className="table-header"><h3 style={{ display: 'flex', alignItems: 'center', gap: 8 }}><Globe size={18} /> Preferences</h3></div>
          <div style={{ padding: '1.5rem' }}>
            <div className="form-group"><label>Timezone</label><select className="form-control"><option>Asia/Kolkata (IST +5:30)</option><option>UTC</option></select></div>
          </div>
        </div>
      </div>
      <div style={{ marginTop: '1.5rem', display: 'flex', gap: '1rem', alignItems: 'center' }}>
        <button className="btn btn-primary" onClick={handleSave}><Save size={16} /> Save All Settings</button>
        {saved && <span style={{ color: '#16a34a', fontWeight: 600 }}>Settings saved successfully!</span>}
      </div>
    </div>
  );
};
''')

print("ALL MISSING FILES RECREATED SUCCESSFULLY!")
