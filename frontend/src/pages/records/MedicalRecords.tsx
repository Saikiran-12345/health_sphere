import React, { useState } from 'react';
import { FileText, Download, Eye, Search, Calendar } from 'lucide-react';

const records = [
  { id: 'REC-9001', patient: 'Vikram Singh', type: '12-Lead ECG Report', doctor: 'Dr. Saikiran Reddy', date: '09 Sep 2026, 08:30 AM', status: 'Abnormal (ST Elevation)', format: 'PDF' },
  { id: 'REC-9002', patient: 'Arun Kumar', type: 'Complete Blood Count (CBC)', doctor: 'Dr. Amit Shah', date: '09 Sep 2026, 07:15 AM', status: 'Normal', format: 'PDF' },
  { id: 'REC-9003', patient: 'Priya Sharma', type: 'Obstetric Ultrasound Scan', doctor: 'Dr. Neha Gupta', date: '08 Sep 2026, 16:45 PM', status: 'Normal (Fetal HR 142)', format: 'DICOM/PDF' },
  { id: 'REC-9004', patient: 'Deepak Mishra', type: 'Renal Function Panel (KFT)', doctor: 'Dr. Amit Shah', date: '08 Sep 2026, 11:20 AM', status: 'Elevated Creatinine', format: 'PDF' },
  { id: 'REC-9005', patient: 'Latha Krishnan', type: 'Chest X-Ray (PA View)', doctor: 'Dr. Priya Nair', date: '07 Sep 2026, 14:10 PM', status: 'Clear Lung Fields', format: 'DICOM' },
];

export const MedicalRecords = () => {
  const [search, setSearch] = useState('');
  const [dateFilter, setDateFilter] = useState('all');

  const filtered = records.filter(r => r.patient.toLowerCase().includes(search.toLowerCase()) || r.type.toLowerCase().includes(search.toLowerCase()));

  return (
    <div>
      <div className="page-header">
        <div className="page-title">
          <h2>Electronic Health Records & Lab Telemetry</h2>
          <p>Inspect diagnostic lab reports, imaging scans, and historical patient records</p>
        </div>
        <div style={{ display: 'flex', gap: '0.75rem' }}>
          <select className="form-control" style={{ width: 'auto', fontWeight: 600 }} value={dateFilter} onChange={e => setDateFilter(e.target.value)}>
            <option value="all">Date Range: All Records</option>
            <option value="today">Today (09 Sep 2026)</option>
            <option value="week">Past 7 Days</option>
          </select>
        </div>
      </div>

      <div style={{ display: 'flex', gap: '1rem', marginBottom: '1.5rem' }}>
        <div style={{ flex: 1, position: 'relative' }}>
          <Search size={16} style={{ position: 'absolute', left: 12, top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
          <input className="form-control" style={{ paddingLeft: '2.5rem' }} placeholder="Search records by patient name or lab report type..." value={search} onChange={e => setSearch(e.target.value)} />
        </div>
      </div>

      <div className="data-table-container">
        <div className="table-header"><h3>Diagnostic Lab & Imaging Reports ({filtered.length})</h3></div>
        <table className="data-table">
          <thead><tr><th>Record ID</th><th>Patient Name</th><th>Report Type</th><th>Ordering Doctor</th><th>Test Date & Time</th><th>Result Status</th><th>Download</th></tr></thead>
          <tbody>
            {filtered.map(r => (
              <tr key={r.id}>
                <td style={{ fontWeight: 600, color: 'var(--primary-color)' }}>{r.id}</td>
                <td style={{ fontWeight: 700 }}>{r.patient}</td>
                <td>{r.type}</td>
                <td style={{ color: 'var(--text-muted)' }}>{r.doctor}</td>
                <td style={{ fontWeight: 500, color: '#334155' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
                    <Calendar size={13} color="var(--primary-color)" /> {r.date}
                  </div>
                </td>
                <td>
                  <span className={`badge ${r.status.includes('Abnormal') || r.status.includes('Elevated') ? 'badge-critical' : 'badge-stable'}`}>
                    {r.status}
                  </span>
                </td>
                <td>
                  <button className="btn btn-outline" style={{ padding: '4px 8px', fontSize: '0.8rem' }}>
                    <Download size={14} /> {r.format}
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
