import React, { useState } from 'react';
import { 
  Users, Calendar, Bed, Activity, ArrowUpRight, ArrowDownRight, Filter, 
  Stethoscope, Pill, CreditCard, Truck, Microscope, ShieldCheck, MapPin, 
  AlertTriangle, CheckCircle2, Clock, FileText, Phone, DollarSign, Package
} from 'lucide-react';
import { useHospitalData } from '../../context/DataContext';
import { useAuth } from '../../auth/AuthProvider';

export const AdminDashboard = () => {
  const { patients, appointments, doctors } = useHospitalData();
  const { user } = useAuth();
  const [dateFilter, setDateFilter] = useState('today');

  const todayStr = '09 Sep 2026';
  const role = user?.role || 'ADMIN';

  // 1. AMBULANCE DISPATCHER DASHBOARD VIEW
  if (role === 'DISPATCHER') {
    const fleet = [
      { id: 'AMB-101', driver: 'Raju Sharma', phone: '+91 98765 88881', location: 'MG Road Junction', destination: 'City ER Ward A', eta: '4 min', type: 'Advanced Life Support (ALS)', status: 'En Route Hospital' },
      { id: 'AMB-102', driver: 'Suresh Kumar', phone: '+91 98765 88882', location: 'Indiranagar Fleet Depot', destination: 'Standby Base', eta: 'Ready', type: 'Basic Life Support (BLS)', status: 'Standby Available' },
      { id: 'AMB-103', driver: 'Mahesh Reddy', phone: '+91 98765 88883', location: 'Koramangala 4th Block', destination: 'Trauma ICU Unit', eta: '9 min', type: 'Neonatal ICU Ambulance', status: 'Dispatched to Scene' }
    ];

    const emergencyCalls = [
      { id: 'EMG-901', location: 'Commercial Street, Sector 4', caller: 'Anil Gupta', type: 'Acute Cardiac Distress', priority: 'CRITICAL', unit: 'AMB-101', status: 'Dispatched' },
      { id: 'EMG-902', location: 'Outer Ring Road Flyover', caller: 'Highway Patrol', type: 'Motor Collision Trauma', priority: 'CRITICAL', unit: 'AMB-103', status: 'En Route' },
      { id: 'EMG-903', location: 'Jayanagar 5th Main', caller: 'Saritha Rao', type: 'Severe Respiratory Distress', priority: 'HIGH', unit: 'AMB-102', status: 'Pending Assignment' }
    ];

    return (
      <div>
        <div style={{ padding: '0.85rem 1.25rem', background: '#ffedd5', border: '1px solid #ea580c', borderRadius: 10, marginBottom: '1.25rem', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <Truck size={20} color="#ea580c" />
            <span style={{ fontSize: '0.9rem', color: '#9a3412', fontWeight: 700 }}>
              Ambulance Dispatch Command &bull; Operator: <strong>{user?.first_name} {user?.last_name}</strong> (Fleet Controller)
            </span>
          </div>
          <span style={{ fontSize: '0.75rem', fontWeight: 800, background: '#ea580c', color: 'white', padding: '0.25rem 0.65rem', borderRadius: 6 }}>
            DISPATCHER PORTAL
          </span>
        </div>

        <div className="page-header">
          <div className="page-title">
            <h2>Emergency Ambulance & Fleet Telemetry</h2>
            <p>Live GPS vehicle dispatch, driver telemetry, and 911 emergency response tracking</p>
          </div>
          <button className="btn btn-primary" style={{ background: '#dc2626' }}><Truck size={16} /> Dispatch Emergency Ambulance</button>
        </div>

        {/* Fleet Stat Cards */}
        <div className="dashboard-grid">
          <div className="card-summary">
            <div className="card-summary-info"><h3>Total Ambulance Fleet</h3><p>3 Vehicles</p><div className="card-summary-change up"><ArrowUpRight size={14} /> 100% Operational</div></div>
            <div className="card-summary-icon" style={{ background: '#ffedd5', color: '#ea580c' }}><Truck size={24} /></div>
          </div>
          <div className="card-summary">
            <div className="card-summary-info"><h3>Active Dispatches</h3><p style={{ color: '#dc2626' }}>2 Units</p><div className="card-summary-change down"><AlertTriangle size={14} /> Critical Trauma En Route</div></div>
            <div className="card-summary-icon" style={{ background: '#fee2e2', color: '#dc2626' }}><MapPin size={24} /></div>
          </div>
          <div className="card-summary">
            <div className="card-summary-info"><h3>Standby Ready</h3><p style={{ color: '#16a34a' }}>1 Unit</p><div className="card-summary-change up"><CheckCircle2 size={14} /> Base Station Ready</div></div>
            <div className="card-summary-icon" style={{ background: '#dcfce7', color: '#16a34a' }}><CheckCircle2 size={24} /></div>
          </div>
          <div className="card-summary">
            <div className="card-summary-info"><h3>Avg Dispatch Time</h3><p>3.5 min</p><div className="card-summary-change up"><ArrowUpRight size={14} /> 1.5 min under target</div></div>
            <div className="card-summary-icon" style={{ background: '#e0f2fe', color: '#0284c7' }}><Clock size={24} /></div>
          </div>
        </div>

        {/* Dispatch Tables */}
        <div className="grid-2">
          <div className="data-table-container">
            <div className="table-header"><h3>Active Fleet Location Telemetry</h3><span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>GPS Live Updated</span></div>
            <table className="data-table">
              <thead><tr><th>Ambulance ID</th><th>Driver Name</th><th>Current GPS Location</th><th>ETA</th><th>Status</th></tr></thead>
              <tbody>
                {fleet.map(item => (
                  <tr key={item.id}>
                    <td style={{ fontWeight: 700, color: '#ea580c' }}>{item.id}</td>
                    <td style={{ fontWeight: 700 }}>{item.driver}</td>
                    <td style={{ fontWeight: 600, display: 'flex', alignItems: 'center', gap: 4 }}><MapPin size={14} color="#dc2626" /> {item.location}</td>
                    <td style={{ fontWeight: 700, color: '#0284c7' }}>{item.eta}</td>
                    <td><span className={`badge ${item.status === 'Standby Available' ? 'badge-stable' : 'badge-critical'}`}>{item.status}</span></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <div className="data-table-container">
            <div className="table-header"><h3>Emergency 911 Calls Queue</h3><span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>09 Sep 2026 Triage</span></div>
            <table className="data-table">
              <thead><tr><th>Call ID</th><th>Location</th><th>Emergency Type</th><th>Priority</th><th>Assigned Unit</th></tr></thead>
              <tbody>
                {emergencyCalls.map(call => (
                  <tr key={call.id}>
                    <td style={{ fontWeight: 700, color: '#0284c7' }}>{call.id}</td>
                    <td style={{ fontWeight: 600 }}>{call.location}</td>
                    <td style={{ color: 'var(--text-muted)' }}>{call.type}</td>
                    <td><span className={`badge ${call.priority === 'CRITICAL' ? 'badge-critical' : 'badge-inqueue'}`}>{call.priority}</span></td>
                    <td style={{ fontWeight: 700, color: '#ea580c' }}>{call.unit}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    );
  }

  // 2. PHARMACIST DASHBOARD VIEW
  if (role === 'PHARMACIST') {
    const stockAlerts = [
      { id: 'DRG-101', name: 'Paracetamol 500mg Injection', category: 'Analgesic', stock: 45, min: 100, status: 'LOW STOCK REORDER' },
      { id: 'DRG-104', name: 'Amoxicillin 500mg Capsules', category: 'Antibiotic', stock: 20, min: 80, status: 'CRITICAL LOW' },
      { id: 'DRG-108', name: 'Atorvastatin 10mg Tablets', category: 'Cardiovascular', stock: 310, min: 100, status: 'OPTIMAL' },
      { id: 'DRG-112', name: 'Insulin Regular 100IU/ml', category: 'Endocrine', stock: 15, min: 50, status: 'CRITICAL LOW' }
    ];

    const rxOrders = [
      { id: 'RX-8801', patient: 'Rajesh Kumar', doctor: 'Dr. Priya Nair', meds: 'Amoxicillin 500mg, Paracetamol', status: 'Ready for Pickup' },
      { id: 'RX-8802', patient: 'Sunita Rao', doctor: 'Dr. Saikiran Reddy', meds: 'Atorvastatin 10mg', status: 'In Preparation' },
      { id: 'RX-8803', patient: 'Vikram Singh', doctor: 'Dr. Priya Nair', meds: 'Insulin Regular 100IU', status: 'Pending Verification' }
    ];

    return (
      <div>
        <div style={{ padding: '0.85rem 1.25rem', background: '#fef3c7', border: '1px solid #d97706', borderRadius: 10, marginBottom: '1.25rem', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <Pill size={20} color="#d97706" />
            <span style={{ fontSize: '0.9rem', color: '#92400e', fontWeight: 700 }}>
              Pharmacy & Medical Supplies Depot &bull; Pharmacist: <strong>{user?.first_name} {user?.last_name}</strong>
            </span>
          </div>
          <span style={{ fontSize: '0.75rem', fontWeight: 800, background: '#d97706', color: 'white', padding: '0.25rem 0.65rem', borderRadius: 6 }}>
            PHARMACY PORTAL
          </span>
        </div>

        <div className="page-header">
          <div className="page-title">
            <h2>Pharmacy Inventory & Dispensing Queue</h2>
            <p>Pharmaceutical stock monitoring, automated reorder alerts, and prescription fulfillment</p>
          </div>
          <button className="btn btn-primary" style={{ background: '#d97706' }}><Pill size={16} /> Dispense New Prescription</button>
        </div>

        <div className="dashboard-grid">
          <div className="card-summary"><div className="card-summary-info"><h3>Total Stock Items</h3><p>1,420 Items</p><div className="card-summary-change up"><ArrowUpRight size={14} /> Full Depot Census</div></div><div className="card-summary-icon" style={{ background: '#fef3c7', color: '#d97706' }}><Package size={24} /></div></div>
          <div className="card-summary"><div className="card-summary-info"><h3>Low Stock Reorder Alerts</h3><p style={{ color: '#d97706' }}>4 Drugs</p><div className="card-summary-change down"><AlertTriangle size={14} /> Auto-PO Sent</div></div><div className="card-summary-icon" style={{ background: '#fee2e2', color: '#dc2626' }}><AlertTriangle size={24} /></div></div>
          <div className="card-summary"><div className="card-summary-info"><h3>Prescriptions Today</h3><p style={{ color: '#16a34a' }}>84 Orders</p><div className="card-summary-change up"><CheckCircle2 size={14} /> 94% Fulfilled</div></div><div className="card-summary-icon" style={{ background: '#dcfce7', color: '#16a34a' }}><CheckCircle2 size={24} /></div></div>
          <div className="card-summary"><div className="card-summary-info"><h3>Controlled Substances</h3><p>12 Verified</p><div className="card-summary-change up"><ShieldCheck size={14} /> Vault Locked</div></div><div className="card-summary-icon" style={{ background: '#e0f2fe', color: '#0284c7' }}><ShieldCheck size={24} /></div></div>
        </div>

        <div className="grid-2">
          <div className="data-table-container">
            <div className="table-header"><h3>Critical Drug Stock & Reorder Alerts</h3></div>
            <table className="data-table">
              <thead><tr><th>Code</th><th>Medication Name</th><th>Stock Level</th><th>Min Limit</th><th>Reorder Status</th></tr></thead>
              <tbody>
                {stockAlerts.map(item => (
                  <tr key={item.id}>
                    <td style={{ fontWeight: 700, color: '#d97706' }}>{item.id}</td>
                    <td style={{ fontWeight: 700 }}>{item.name}</td>
                    <td style={{ fontWeight: 700, color: item.stock < item.min ? '#dc2626' : '#16a34a' }}>{item.stock} units</td>
                    <td>{item.min} units</td>
                    <td><span className={`badge ${item.stock < item.min ? 'badge-critical' : 'badge-stable'}`}>{item.status}</span></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <div className="data-table-container">
            <div className="table-header"><h3>Prescription Fulfillment Queue</h3></div>
            <table className="data-table">
              <thead><tr><th>Rx ID</th><th>Patient Name</th><th>Prescribing Doctor</th><th>Medications</th><th>Status</th></tr></thead>
              <tbody>
                {rxOrders.map(rx => (
                  <tr key={rx.id}>
                    <td style={{ fontWeight: 700, color: '#0284c7' }}>{rx.id}</td>
                    <td style={{ fontWeight: 700 }}>{rx.patient}</td>
                    <td style={{ color: 'var(--text-muted)' }}>{rx.doctor}</td>
                    <td style={{ fontSize: '0.85rem' }}>{rx.meds}</td>
                    <td><span className="badge badge-primary">{rx.status}</span></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    );
  }

  // 3. FINANCE & BILLING DASHBOARD VIEW
  if (role === 'FINANCE') {
    const invoices = [
      { id: 'INV-4011', patient: 'Amitabh Verma', dept: 'Cardiology OPD', amount: '₹14,500', status: 'Paid in Full' },
      { id: 'INV-4012', patient: 'Kavita Sharma', dept: 'ICU Admissions', amount: '₹84,200', status: 'Pending Copay' },
      { id: 'INV-4013', patient: 'Deepak Patel', dept: 'Emergency ER', amount: '₹6,800', status: 'Insurance EDI Claimed' }
    ];

    return (
      <div>
        <div style={{ padding: '0.85rem 1.25rem', background: '#e0e7ff', border: '1px solid #4f46e5', borderRadius: 10, marginBottom: '1.25rem', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <CreditCard size={20} color="#4f46e5" />
            <span style={{ fontSize: '0.9rem', color: '#3730a3', fontWeight: 700 }}>
              Billing & Financial Accounts Command &bull; Controller: <strong>{user?.first_name} {user?.last_name}</strong>
            </span>
          </div>
          <span style={{ fontSize: '0.75rem', fontWeight: 800, background: '#4f46e5', color: 'white', padding: '0.25rem 0.65rem', borderRadius: 6 }}>
            FINANCE PORTAL
          </span>
        </div>

        <div className="page-header">
          <div className="page-title">
            <h2>Billing & Revenue Audit Center</h2>
            <p>Patient copay collections, insurance EDI claims, invoice settlements, and financial audit</p>
          </div>
          <button className="btn btn-primary" style={{ background: '#4f46e5' }}><CreditCard size={16} /> Generate Patient Invoice</button>
        </div>

        <div className="dashboard-grid">
          <div className="card-summary"><div className="card-summary-info"><h3>Today's Revenue Collected</h3><p>₹1,84,500</p><div className="card-summary-change up"><ArrowUpRight size={14} /> +14.2% vs target</div></div><div className="card-summary-icon" style={{ background: '#e0e7ff', color: '#4f46e5' }}><CreditCard size={24} /></div></div>
          <div className="card-summary"><div className="card-summary-info"><h3>Pending Invoices</h3><p style={{ color: '#d97706' }}>14 Bills</p><div className="card-summary-change down"><Clock size={14} /> Follow-up Sent</div></div><div className="card-summary-icon" style={{ background: '#fef3c7', color: '#d97706' }}><Clock size={24} /></div></div>
          <div className="card-summary"><div className="card-summary-info"><h3>Insurance EDI Claims</h3><p style={{ color: '#16a34a' }}>38 Approved</p><div className="card-summary-change up"><CheckCircle2 size={14} /> 98% Cleared</div></div><div className="card-summary-icon" style={{ background: '#dcfce7', color: '#16a34a' }}><CheckCircle2 size={24} /></div></div>
          <div className="card-summary"><div className="card-summary-info"><h3>Avg Bill Settlement</h3><p>2.5 Hrs</p><div className="card-summary-change up"><ArrowUpRight size={14} /> Fast Discharge</div></div><div className="card-summary-icon" style={{ background: '#e0f2fe', color: '#0284c7' }}><Activity size={24} /></div></div>
        </div>

        <div className="data-table-container">
          <div className="table-header"><h3>Recent Patient Invoices & Copay Ledger</h3></div>
          <table className="data-table">
            <thead><tr><th>Invoice ID</th><th>Patient Name</th><th>Department</th><th>Billed Amount</th><th>Payment Status</th></tr></thead>
            <tbody>
              {invoices.map(inv => (
                <tr key={inv.id}>
                  <td style={{ fontWeight: 700, color: '#4f46e5' }}>{inv.id}</td>
                  <td style={{ fontWeight: 700 }}>{inv.patient}</td>
                  <td>{inv.dept}</td>
                  <td style={{ fontWeight: 800, color: '#0f172a' }}>{inv.amount}</td>
                  <td><span className={`badge ${inv.status === 'Paid in Full' ? 'badge-completed' : 'badge-inqueue'}`}>{inv.status}</span></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    );
  }

  // 4. ICU NURSE DASHBOARD VIEW
  if (role === 'NURSE_ICU') {
    const icuBeds = [
      { bed: 'ICU Bed 01', patient: 'Vikram Singh', condition: 'Acute Respiratory Distress', spO2: '94%', hr: '82 bpm', status: 'CRITICAL MONITORED' },
      { bed: 'ICU Bed 02', patient: 'Kavita Sharma', condition: 'Post-Op Coronary Bypass', spO2: '98%', hr: '74 bpm', status: 'STABLE ICU' },
      { bed: 'ICU Bed 03', patient: 'Anil Mehta', condition: 'Trauma Fracture Surge', spO2: '96%', hr: '88 bpm', status: 'OBSERVATION' }
    ];

    return (
      <div>
        <div style={{ padding: '0.85rem 1.25rem', background: '#fee2e2', border: '1px solid #dc2626', borderRadius: 10, marginBottom: '1.25rem', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <Bed size={20} color="#dc2626" />
            <span style={{ fontSize: '0.9rem', color: '#991b1b', fontWeight: 700 }}>
              ICU Inpatient & Telemetry Control &bull; Charge Nurse: <strong>{user?.first_name} {user?.last_name}</strong>
            </span>
          </div>
          <span style={{ fontSize: '0.75rem', fontWeight: 800, background: '#dc2626', color: 'white', padding: '0.25rem 0.65rem', borderRadius: 6 }}>
            ICU NURSE PORTAL
          </span>
        </div>

        <div className="page-header">
          <div className="page-title">
            <h2>ICU Bed Census & Critical Telemetry</h2>
            <p>Real-time patient vitals monitor, ICU bed allocation, ventilator telemetry, and emergency nursing</p>
          </div>
          <button className="btn btn-primary" style={{ background: '#dc2626' }}><Bed size={16} /> Assign ICU Bed</button>
        </div>

        <div className="dashboard-grid">
          <div className="card-summary"><div className="card-summary-info"><h3>ICU Bed Occupancy</h3><p style={{ color: '#dc2626' }}>84%</p><div className="card-summary-change down"><AlertTriangle size={14} /> 16 / 20 Occupied</div></div><div className="card-summary-icon" style={{ background: '#fee2e2', color: '#dc2626' }}><Bed size={24} /></div></div>
          <div className="card-summary"><div className="card-summary-info"><h3>Available ICU Beds</h3><p style={{ color: '#16a34a' }}>4 Beds</p><div className="card-summary-change up"><CheckCircle2 size={14} /> Ready for Triage</div></div><div className="card-summary-icon" style={{ background: '#dcfce7', color: '#16a34a' }}><CheckCircle2 size={24} /></div></div>
          <div className="card-summary"><div className="card-summary-info"><h3>Active Ventilators</h3><p>9 Units</p><div className="card-summary-change up"><Activity size={14} /> Pressure Normal</div></div><div className="card-summary-icon" style={{ background: '#e0f2fe', color: '#0284c7' }}><Activity size={24} /></div></div>
          <div className="card-summary"><div className="card-summary-info"><h3>Critical Vitals Alerts</h3><p style={{ color: '#dc2626' }}>2 Patients</p><div className="card-summary-change down"><AlertTriangle size={14} /> High Nurse Priority</div></div><div className="card-summary-icon" style={{ background: '#fee2e2', color: '#dc2626' }}><AlertTriangle size={24} /></div></div>
        </div>

        <div className="data-table-container">
          <div className="table-header"><h3>Active ICU Bed Census & Live Telemetry</h3></div>
          <table className="data-table">
            <thead><tr><th>Bed No</th><th>Patient Name</th><th>Diagnosis / Condition</th><th>SpO2</th><th>Heart Rate</th><th>Monitoring Status</th></tr></thead>
            <tbody>
              {icuBeds.map(bed => (
                <tr key={bed.bed}>
                  <td style={{ fontWeight: 800, color: '#dc2626' }}>{bed.bed}</td>
                  <td style={{ fontWeight: 700 }}>{bed.patient}</td>
                  <td style={{ color: 'var(--text-muted)' }}>{bed.condition}</td>
                  <td style={{ fontWeight: 800, color: parseInt(bed.spO2) < 95 ? '#dc2626' : '#16a34a' }}>{bed.spO2}</td>
                  <td style={{ fontWeight: 700 }}>{bed.hr}</td>
                  <td><span className={`badge ${bed.status.includes('CRITICAL') ? 'badge-critical' : 'badge-stable'}`}>{bed.status}</span></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    );
  }

  // 5. CARDIOLOGY DOCTOR DASHBOARD VIEW
  if (role === 'DOCTOR') {
    return (
      <div>
        <div style={{ padding: '0.85rem 1.25rem', background: '#ccfbf1', border: '1px solid #0d9488', borderRadius: 10, marginBottom: '1.25rem', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <Stethoscope size={20} color="#0d9488" />
            <span style={{ fontSize: '0.9rem', color: '#115e59', fontWeight: 700 }}>
              Cardiology OPD Clinic &bull; Specialist: <strong>Dr. {user?.last_name || 'Nair'}</strong> ({user?.title})
            </span>
          </div>
          <span style={{ fontSize: '0.75rem', fontWeight: 800, background: '#0d9488', color: 'white', padding: '0.25rem 0.65rem', borderRadius: 6 }}>
            DOCTOR PORTAL
          </span>
        </div>

        <div className="page-header">
          <div className="page-title">
            <h2>Outpatient (OPD) Consultation Queue</h2>
            <p>Today's appointments, ECG telemetry, patient EHR medical histories, and consultations</p>
          </div>
          <button className="btn btn-primary" style={{ background: '#0d9488' }}><Stethoscope size={16} /> Call Next OPD Patient</button>
        </div>

        <div className="dashboard-grid">
          <div className="card-summary"><div className="card-summary-info"><h3>Today's OPD Patients</h3><p>18 Patients</p><div className="card-summary-change up"><ArrowUpRight size={14} /> +8.1% vs yesterday</div></div><div className="card-summary-icon" style={{ background: '#ccfbf1', color: '#0d9488' }}><Users size={24} /></div></div>
          <div className="card-summary"><div className="card-summary-info"><h3>Consultations Done</h3><p style={{ color: '#16a34a' }}>12 Completed</p><div className="card-summary-change up"><CheckCircle2 size={14} /> On Schedule</div></div><div className="card-summary-icon" style={{ background: '#dcfce7', color: '#16a34a' }}><CheckCircle2 size={24} /></div></div>
          <div className="card-summary"><div className="card-summary-info"><h3>Waiting in OPD Queue</h3><p style={{ color: '#0284c7' }}>6 Waiting</p><div className="card-summary-change up"><Clock size={14} /> Avg Wait: 8 min</div></div><div className="card-summary-icon" style={{ background: '#e0f2fe', color: '#0284c7' }}><Clock size={24} /></div></div>
          <div className="card-summary"><div className="card-summary-info"><h3>Critical ECG Alerts</h3><p style={{ color: '#dc2626' }}>1 Patient</p><div className="card-summary-change down"><AlertTriangle size={14} /> Triage Priority</div></div><div className="card-summary-icon" style={{ background: '#fee2e2', color: '#dc2626' }}><AlertTriangle size={24} /></div></div>
        </div>

        <div className="data-table-container">
          <div className="table-header"><h3>Cardiology OPD Active Queue</h3></div>
          <table className="data-table">
            <thead><tr><th>Patient ID</th><th>Patient Name</th><th>Condition / Complaint</th><th>Appointment Time</th><th>Status</th></tr></thead>
            <tbody>
              {patients.slice(0, 5).map(p => (
                <tr key={p.id}>
                  <td style={{ fontWeight: 700, color: '#0d9488' }}>{p.id}</td>
                  <td style={{ fontWeight: 700 }}>{p.name}</td>
                  <td style={{ color: 'var(--text-muted)' }}>{p.condition}</td>
                  <td style={{ fontSize: '0.85rem' }}>09 Sep 2026, 10:30 AM</td>
                  <td><span className="badge badge-primary">{p.status}</span></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    );
  }

  // 6. LAB TECH DASHBOARD VIEW
  if (role === 'LAB_TECH') {
    return (
      <div>
        <div style={{ padding: '0.85rem 1.25rem', background: '#ede9fe', border: '1px solid #8b5cf6', borderRadius: 10, marginBottom: '1.25rem', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <Microscope size={20} color="#8b5cf6" />
            <span style={{ fontSize: '0.9rem', color: '#5b21b6', fontWeight: 700 }}>
              Diagnostics & AI Radiology Laboratory &bull; Director: <strong>{user?.first_name} {user?.last_name}</strong>
            </span>
          </div>
          <span style={{ fontSize: '0.75rem', fontWeight: 800, background: '#8b5cf6', color: 'white', padding: '0.25rem 0.65rem', borderRadius: 6 }}>
            LAB PORTAL
          </span>
        </div>

        <div className="page-header">
          <div className="page-title">
            <h2>AI Radiology Scans & Pathology Queue</h2>
            <p>Automated AI telemetry analysis, MRI/CT radiology scans, and pathology report verification</p>
          </div>
          <button className="btn btn-primary" style={{ background: '#8b5cf6' }}><Microscope size={16} /> Run AI Scan Analysis</button>
        </div>

        <div className="dashboard-grid">
          <div className="card-summary"><div className="card-summary-info"><h3>Pending Lab Scans</h3><p style={{ color: '#8b5cf6' }}>12 Scans</p><div className="card-summary-change up"><Clock size={14} /> Queue Active</div></div><div className="card-summary-icon" style={{ background: '#ede9fe', color: '#8b5cf6' }}><Microscope size={24} /></div></div>
          <div className="card-summary"><div className="card-summary-info"><h3>AI Telemetry Accuracy</h3><p style={{ color: '#16a34a' }}>99.4%</p><div className="card-summary-change up"><CheckCircle2 size={14} /> High Precision</div></div><div className="card-summary-icon" style={{ background: '#dcfce7', color: '#16a34a' }}><CheckCircle2 size={24} /></div></div>
          <div className="card-summary"><div className="card-summary-info"><h3>Reports Completed Today</h3><p>45 Scans</p><div className="card-summary-change up"><ArrowUpRight size={14} /> Verified</div></div><div className="card-summary-icon" style={{ background: '#e0f2fe', color: '#0284c7' }}><FileText size={24} /></div></div>
          <div className="card-summary"><div className="card-summary-info"><h3>Critical Findings</h3><p style={{ color: '#dc2626' }}>1 Scan</p><div className="card-summary-change down"><AlertTriangle size={14} /> Doctor Alerted</div></div><div className="card-summary-icon" style={{ background: '#fee2e2', color: '#dc2626' }}><AlertTriangle size={24} /></div></div>
        </div>

        <div className="data-table-container">
          <div className="table-header"><h3>AI Diagnostic Scan Queue</h3></div>
          <table className="data-table">
            <thead><tr><th>Scan ID</th><th>Patient Name</th><th>Modality</th><th>AI Telemetry Finding</th><th>Status</th></tr></thead>
            <tbody>
              <tr><td style={{ fontWeight: 700, color: '#8b5cf6' }}>RAD-901</td><td style={{ fontWeight: 700 }}>Rajesh Kumar</td><td>Chest CT Scan</td><td>98% Normal Lung Field</td><td><span className="badge badge-completed">Verified</span></td></tr>
              <tr><td style={{ fontWeight: 700, color: '#8b5cf6' }}>RAD-902</td><td style={{ fontWeight: 700 }}>Vikram Singh</td><td>Cardiac MRI</td><td>Cardiomegaly AI Alert</td><td><span className="badge badge-critical">Critical Flag</span></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    );
  }

  // 7. EXECUTIVE ADMIN DASHBOARD VIEW
  return (
    <div>
      <div className="page-header">
        <div className="page-title">
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <h2>Hospital Executive Command Center</h2>
            <span className="badge badge-completed" style={{ display: 'inline-flex', alignItems: 'center', gap: 6 }}>
              <span style={{ width: 8, height: 8, borderRadius: '50%', background: '#16a34a' }}></span>
              FULL SYSTEM TELEMETRY
            </span>
          </div>
          <p>Real-time hospital-wide clinical operations, bed occupancy, and multi-department telemetry</p>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
          <Filter size={16} color="var(--text-muted)" />
          <select className="form-control" style={{ width: 'auto', fontWeight: 600 }} value={dateFilter} onChange={e => setDateFilter(e.target.value)}>
            <option value="today">Today ({todayStr})</option>
            <option value="week">This Week (07 Sep - 13 Sep)</option>
            <option value="month">September 2026</option>
            <option value="quarter">Q3 2026 Census</option>
          </select>
        </div>
      </div>

      <div className="dashboard-grid">
        <div className="card-summary"><div className="card-summary-info"><h3>Total Patients</h3><p>{patients.length * (dateFilter === 'month' ? 4 : dateFilter === 'week' ? 2 : 1)}</p><div className="card-summary-change up"><ArrowUpRight size={14} /> +12.4% vs last period</div></div><div className="card-summary-icon" style={{ background: '#e0f2fe', color: '#0284c7' }}><Users size={24} /></div></div>
        <div className="card-summary"><div className="card-summary-info"><h3>Today's Consultations</h3><p>{appointments.length}</p><div className="card-summary-change up"><ArrowUpRight size={14} /> +8.1% on schedule</div></div><div className="card-summary-icon" style={{ background: '#ede9fe', color: '#8b5cf6' }}><Calendar size={24} /></div></div>
        <div className="card-summary"><div className="card-summary-info"><h3>ICU Bed Occupancy</h3><p>84%</p><div className="card-summary-change down"><ArrowDownRight size={14} /> 4 ICU beds available</div></div><div className="card-summary-icon" style={{ background: '#fee2e2', color: '#dc2626' }}><Bed size={24} /></div></div>
        <div className="card-summary"><div className="card-summary-info"><h3>Avg ER Response</h3><p>14 min</p><div className="card-summary-change up"><ArrowUpRight size={14} /> 3 min faster than target</div></div><div className="card-summary-icon" style={{ background: '#ccfbf1', color: '#0d9488' }}><Activity size={24} /></div></div>
      </div>

      <div className="grid-2">
        <div className="data-table-container">
          <div className="table-header"><h3>Recent Registered Patients</h3></div>
          <table className="data-table">
            <thead><tr><th>Patient ID</th><th>Name</th><th>Condition</th><th>Reg. Date</th><th>Status</th></tr></thead>
            <tbody>
              {patients.slice(0, 5).map(p => (
                <tr key={p.id}>
                  <td style={{ fontWeight: 600, color: 'var(--primary-color)' }}>{p.id}</td>
                  <td style={{ fontWeight: 600 }}>{p.name}</td>
                  <td style={{ color: 'var(--text-muted)' }}>{p.condition}</td>
                  <td style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>09 Sep 2026, 09:30 AM</td>
                  <td><span className={`badge ${p.status === 'critical' ? 'badge-critical' : 'badge-primary'}`}>{p.status}</span></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <div className="data-table-container">
          <div className="table-header"><h3>Consulting Specialists Roster</h3></div>
          <table className="data-table">
            <thead><tr><th>Doctor</th><th>Specialty</th><th>Shift Date</th><th>Status</th></tr></thead>
            <tbody>
              {doctors.slice(0, 5).map(d => (
                <tr key={d.id}>
                  <td style={{ fontWeight: 700 }}>{d.name}</td>
                  <td><span className="badge badge-primary">{d.spec}</span></td>
                  <td style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>09 Sep 2026 (08:00 - 16:00)</td>
                  <td><span className={`badge ${d.status === 'Active' ? 'badge-stable' : 'badge-monitoring'}`}>{d.status}</span></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
