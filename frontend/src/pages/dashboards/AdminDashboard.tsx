import React, { useState } from 'react';
import { Users, Calendar, Bed, Activity, TrendingUp, Clock, AlertTriangle, ArrowUpRight, ArrowDownRight, Filter } from 'lucide-react';
import { useHospitalData } from '../../context/DataContext';

export const AdminDashboard = () => {
  const { patients, appointments, doctors } = useHospitalData();
  const [dateFilter, setDateFilter] = useState('today');

  const todayStr = '09 Sep 2026';

  return (
    <div>
      {/* Top Banner with Date Selector & Live Status */}
      <div className="page-header">
        <div className="page-title">
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <h2>Hospital Executive Command Center</h2>
            <span className="badge badge-completed" style={{ display: 'inline-flex', alignItems: 'center', gap: 6 }}>
              <span style={{ width: 8, height: 8, borderRadius: '50%', background: '#16a34a', animation: 'pulse 1.5s infinite' }}></span>
              LIVE TELEMETRY
            </span>
          </div>
          <p>Real-time clinical operations, bed occupancy, and patient queue metrics</p>
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

      {/* Stat Cards */}
      <div className="dashboard-grid">
        <div className="card-summary">
          <div className="card-summary-info">
            <h3>Total Patients</h3>
            <p>{patients.length * (dateFilter === 'month' ? 4 : dateFilter === 'week' ? 2 : 1)}</p>
            <div className="card-summary-change up"><ArrowUpRight size={14} /> +12.4% vs last period</div>
          </div>
          <div className="card-summary-icon" style={{ background: '#e0f2fe', color: '#0284c7' }}><Users size={24} /></div>
        </div>

        <div className="card-summary">
          <div className="card-summary-info">
            <h3>Today's Appointments</h3>
            <p>{appointments.length}</p>
            <div className="card-summary-change up"><ArrowUpRight size={14} /> +8.1% on schedule</div>
          </div>
          <div className="card-summary-icon" style={{ background: '#ede9fe', color: '#8b5cf6' }}><Calendar size={24} /></div>
        </div>

        <div className="card-summary">
          <div className="card-summary-info">
            <h3>ICU Bed Occupancy</h3>
            <p>84%</p>
            <div className="card-summary-change down"><ArrowDownRight size={14} /> 4 ICU beds available</div>
          </div>
          <div className="card-summary-icon" style={{ background: '#fee2e2', color: '#dc2626' }}><Bed size={24} /></div>
        </div>

        <div className="card-summary">
          <div className="card-summary-info">
            <h3>Avg ER Wait Time</h3>
            <p>14 min</p>
            <div className="card-summary-change up"><ArrowUpRight size={14} /> 3 min faster than target</div>
          </div>
          <div className="card-summary-icon" style={{ background: '#ccfbf1', color: '#0d9488' }}><Activity size={24} /></div>
        </div>
      </div>

      {/* Two Grid Tables */}
      <div className="grid-2">
        {/* Recent Registered Patients */}
        <div className="data-table-container">
          <div className="table-header">
            <h3>Recent Patient Registrations</h3>
            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Updated 1 min ago</span>
          </div>
          <table className="data-table">
            <thead><tr><th>Patient ID</th><th>Name</th><th>Diagnosis</th><th>Reg. Date</th><th>Status</th></tr></thead>
            <tbody>
              {patients.slice(0, 5).map(p => (
                <tr key={p.id}>
                  <td style={{ fontWeight: 600, color: 'var(--primary-color)' }}>{p.id}</td>
                  <td style={{ fontWeight: 600 }}>{p.name}</td>
                  <td style={{ color: 'var(--text-muted)' }}>{p.condition}</td>
                  <td style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>09 Sep 2026, 09:30 AM</td>
                  <td>
                    <span className={`badge ${p.status === 'critical' ? 'badge-critical' : p.status === 'admitted' ? 'badge-inqueue' : 'badge-primary'}`}>
                      {p.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Today's Doctor Roster */}
        <div className="data-table-container">
          <div className="table-header">
            <h3>Consulting Specialists Roster</h3>
            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>09 Sep 2026 Shift</span>
          </div>
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
