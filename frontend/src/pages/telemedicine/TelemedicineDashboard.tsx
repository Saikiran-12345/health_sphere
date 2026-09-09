import React from 'react';
import { Video, Calendar, Clock, UserCheck, Plus } from 'lucide-react';

const consultations = [
  { id: 'TELE-501', patient: 'Anita Desai', doctor: 'Dr. Saikiran Reddy', dept: 'Cardiology', time: '10:30 AM', duration: '20 min', status: 'Connecting' },
  { id: 'TELE-502', patient: 'Sunita Rao', doctor: 'Dr. Neha Gupta', dept: 'Gynecology', time: '11:15 AM', duration: '15 min', status: 'Scheduled' },
  { id: 'TELE-503', patient: 'Latha Krishnan', doctor: 'Dr. Priya Nair', dept: 'Neurology', time: '09:00 AM', duration: '25 min', status: 'Completed' },
];

export const TelemedicineDashboard = () => {
  return (
    <div>
      <div className="page-header">
        <div className="page-title">
          <h2>Telemedicine & Virtual Consultations</h2>
          <p>HD video consultations, remote patient monitoring, and digital prescriptions</p>
        </div>
        <button className="btn btn-primary"><Plus size={16} /> Start Instant Call</button>
      </div>

      <div className="dashboard-grid">
        <div className="card-summary"><div className="card-summary-info"><h3>Virtual Today</h3><p>{consultations.length}</p></div><div className="card-summary-icon" style={{ background: '#e0f2fe', color: '#0284c7' }}><Video size={24} /></div></div>
        <div className="card-summary"><div className="card-summary-info"><h3>Active Call</h3><p style={{ color: '#16a34a' }}>1</p></div><div className="card-summary-icon" style={{ background: '#dcfce7', color: '#16a34a' }}><UserCheck size={24} /></div></div>
        <div className="card-summary"><div className="card-summary-info"><h3>Upcoming</h3><p style={{ color: '#d97706' }}>1</p></div><div className="card-summary-icon" style={{ background: '#fef3c7', color: '#d97706' }}><Clock size={24} /></div></div>
      </div>

      <div className="data-table-container">
        <div className="table-header"><h3>Telehealth Queue (09 Sep 2026)</h3></div>
        <table className="data-table">
          <thead><tr><th>Session ID</th><th>Patient Name</th><th>Specialist</th><th>Department</th><th>Scheduled Time</th><th>Duration</th><th>Action</th></tr></thead>
          <tbody>
            {consultations.map(c => (
              <tr key={c.id}>
                <td style={{ fontWeight: 600, color: 'var(--primary-color)' }}>{c.id}</td>
                <td style={{ fontWeight: 700 }}>{c.patient}</td>
                <td>{c.doctor}</td>
                <td>{c.dept}</td>
                <td style={{ fontWeight: 600 }}>{c.time}</td>
                <td>{c.duration}</td>
                <td>
                  <button className={`btn ${c.status === 'Connecting' ? 'btn-primary' : 'btn-outline'}`} style={{ padding: '4px 12px', fontSize: '0.8rem' }}>
                    <Video size={14} /> {c.status === 'Connecting' ? 'Join Call' : c.status}
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
