import React, { useState } from 'react';
import { Bed, AlertCircle, CheckCircle, Clock, Filter } from 'lucide-react';

const wards = [
  { id: 'icu', name: 'ICU Ward A', total: 12, occupied: 10, color: '#dc2626' },
  { id: 'general', name: 'General Ward B', total: 30, occupied: 22, color: '#0284c7' },
  { id: 'peds', name: 'Pediatric Ward C', total: 16, occupied: 9, color: '#8b5cf6' },
  { id: 'maternity', name: 'Maternity Ward D', total: 14, occupied: 11, color: '#0d9488' }
];

const bedGrid = [
  { bedNo: 'ICU-01', patient: 'Vikram Singh', admittedDate: '07 Sep 2026, 14:30', status: 'occupied', critical: true, vitals: 'BP 140/90 • HR 98' },
  { bedNo: 'ICU-02', patient: 'Deepak Mishra', admittedDate: '08 Sep 2026, 09:15', status: 'occupied', critical: false, vitals: 'BP 120/80 • HR 72' },
  { bedNo: 'ICU-03', patient: 'Arun Kumar', admittedDate: '09 Sep 2026, 06:45', status: 'occupied', critical: true, vitals: 'BP 155/95 • HR 104' },
  { bedNo: 'ICU-04', patient: 'Empty', admittedDate: '-', status: 'available', critical: false, vitals: 'Sanitized & Ready' },
  { bedNo: 'ICU-05', patient: 'Priya Sharma', admittedDate: '08 Sep 2026, 18:20', status: 'occupied', critical: false, vitals: 'BP 118/76 • HR 78' },
  { bedNo: 'ICU-06', patient: 'Empty', admittedDate: '-', status: 'available', critical: false, vitals: 'Sanitized & Ready' },
  { bedNo: 'ICU-07', patient: 'Raj Patel', admittedDate: '09 Sep 2026, 01:10', status: 'occupied', critical: false, vitals: 'BP 125/82 • HR 80' },
  { bedNo: 'ICU-08', patient: 'Empty', admittedDate: '-', status: 'available', critical: false, vitals: 'Sanitized & Ready' },
];

export const BedManagement = () => {
  const [selectedWard, setSelectedWard] = useState('icu');
  const [dateFilter, setDateFilter] = useState('today');

  return (
    <div>
      <div className="page-header">
        <div className="page-title">
          <h2>Inpatient Bed & Ward Census</h2>
          <p>Real-time bed availability matrix, patient admission dates, and live telemetry</p>
        </div>
        <div style={{ display: 'flex', gap: '0.75rem' }}>
          <select className="form-control" style={{ width: 'auto', fontWeight: 600 }} value={dateFilter} onChange={e => setDateFilter(e.target.value)}>
            <option value="today">Census Date: 09 Sep 2026</option>
            <option value="yesterday">Census Date: 08 Sep 2026</option>
          </select>
        </div>
      </div>

      <div className="dashboard-grid">
        {wards.map(w => (
          <div key={w.id} className="card-summary" style={{ borderLeft: `4px solid ${w.color}`, cursor: 'pointer' }} onClick={() => setSelectedWard(w.id)}>
            <div className="card-summary-info">
              <h3>{w.name}</h3>
              <p>{w.occupied} / {w.total}</p>
              <span className="badge" style={{ background: `${w.color}20`, color: w.color, marginTop: 4 }}>
                {Math.round((w.occupied / w.total) * 100)}% Occupied
              </span>
            </div>
            <div className="card-summary-icon" style={{ background: `${w.color}20`, color: w.color }}><Bed size={24} /></div>
          </div>
        ))}
      </div>

      <div className="data-table-container">
        <div className="table-header">
          <h3>Bed Allocation Matrix — ICU Ward A (Date: 09 Sep 2026)</h3>
          <span style={{ fontSize: '0.85rem', color: '#16a34a', fontWeight: 600, display: 'flex', alignItems: 'center', gap: 4 }}>
            <span style={{ width: 8, height: 8, borderRadius: '50%', background: '#16a34a' }}></span> Live Vitals Sync Active
          </span>
        </div>
        <div style={{ padding: '1.5rem', display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '1rem' }}>
          {bedGrid.map(bed => (
            <div key={bed.bedNo} style={{
              padding: '1.25rem', borderRadius: 10,
              border: bed.status === 'occupied' ? (bed.critical ? '2px solid #ef4444' : '1px solid #bae6fd') : '1px solid #bbf7d0',
              background: bed.status === 'occupied' ? (bed.critical ? '#fef2f2' : '#f0f9ff') : '#f0fdf4'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
                <span style={{ fontWeight: 800, fontSize: '1.1rem', color: '#1e293b' }}>{bed.bedNo}</span>
                <span className={`badge ${bed.status === 'occupied' ? (bed.critical ? 'badge-critical' : 'badge-primary') : 'badge-stable'}`}>
                  {bed.status === 'occupied' ? (bed.critical ? 'CRITICAL' : 'OCCUPIED') : 'AVAILABLE'}
                </span>
              </div>
              <div style={{ fontWeight: 700, fontSize: '0.95rem', color: '#0f172a' }}>{bed.patient}</div>
              <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginTop: 4, display: 'flex', alignItems: 'center', gap: 4 }}>
                <Clock size={12} /> Admitted: {bed.admittedDate}
              </div>
              <div style={{ marginTop: 8, fontSize: '0.8rem', fontWeight: 600, color: bed.critical ? '#dc2626' : '#0369a1', background: 'white', padding: '4px 8px', borderRadius: 4, border: '1px solid #e2e8f0' }}>
                {bed.vitals}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
