import React, { useState } from 'react';
import { Calendar, Clock, Plus, Filter } from 'lucide-react';
import { useHospitalData, type Appointment } from '../../context/DataContext';

const statusMap: any = {
  scheduled: { label: 'Scheduled', cls: 'badge-primary' },
  confirmed: { label: 'Confirmed', cls: 'badge-inqueue' },
  in_progress: { label: 'In Progress', cls: 'badge-completed' },
  completed: { label: 'Completed', cls: 'badge-stable' },
  cancelled: { label: 'Cancelled', cls: 'badge-critical' },
};

export const AppointmentsList = () => {
  const { appointments, addAppointment } = useHospitalData();
  const [showModal, setShowModal] = useState(false);

  const [patient, setPatient] = useState('');
  const [doctor, setDoctor] = useState('Dr. Saikiran Reddy');
  const [dept, setDept] = useState('Cardiology');
  const [date, setDate] = useState('09 Sep 2026');
  const [time, setTime] = useState('10:00 AM');

  const handleBookAppointment = (e: React.FormEvent) => {
    e.preventDefault();
    if (!patient) return;
    const newApt: Appointment = {
      id: `APT-${Math.floor(300 + Math.random() * 600)}`,
      patient, doctor, dept, date, time, status: 'confirmed'
    };
    addAppointment(newApt);
    setPatient('');
    setShowModal(false);
  };

  return (
    <div>
      <div className="page-header">
        <div className="page-title">
          <h2>Clinical Consultation Roster</h2>
          <p>Schedule, manage, and inspect patient appointments for today (09 Sep 2026)</p>
        </div>
        <button className="btn btn-primary" onClick={() => setShowModal(true)}>
          <Plus size={16} /> Book Appointment
        </button>
      </div>

      <div className="dashboard-grid">
        <div className="card-summary"><div className="card-summary-info"><h3>Total Scheduled</h3><p>{appointments.length}</p></div><div className="card-summary-icon" style={{ background: '#e0f2fe', color: '#0284c7' }}><Calendar size={24} /></div></div>
        <div className="card-summary"><div className="card-summary-info"><h3>Confirmed</h3><p style={{ color: '#16a34a' }}>{appointments.filter(a => a.status === 'confirmed').length}</p></div><div className="card-summary-icon" style={{ background: '#dcfce7', color: '#16a34a' }}><Clock size={24} /></div></div>
        <div className="card-summary"><div className="card-summary-info"><h3>In Consultation</h3><p style={{ color: '#8b5cf6' }}>{appointments.filter(a => a.status === 'in_progress').length}</p></div><div className="card-summary-icon" style={{ background: '#ede9fe', color: '#8b5cf6' }}><Clock size={24} /></div></div>
        <div className="card-summary"><div className="card-summary-info"><h3>Completed</h3><p style={{ color: '#0d9488' }}>{appointments.filter(a => a.status === 'completed').length}</p></div><div className="card-summary-icon" style={{ background: '#ccfbf1', color: '#0d9488' }}><Calendar size={24} /></div></div>
      </div>

      <div className="data-table-container">
        <div className="table-header"><h3>Active Appointments Schedule</h3></div>
        <table className="data-table">
          <thead><tr><th>Appointment ID</th><th>Patient Name</th><th>Consulting Specialist</th><th>Department</th><th>Date & Time</th><th>Status</th></tr></thead>
          <tbody>
            {appointments.map(a => (
              <tr key={a.id}>
                <td style={{ fontWeight: 600, color: 'var(--primary-color)' }}>{a.id}</td>
                <td style={{ fontWeight: 700, color: 'var(--text-main)' }}>{a.patient}</td>
                <td>{a.doctor}</td>
                <td>{a.dept}</td>
                <td style={{ color: 'var(--text-muted)', fontWeight: 500 }}>09 Sep 2026 ({a.time})</td>
                <td><span className={`badge ${statusMap[a.status]?.cls || 'badge-primary'}`}>{statusMap[a.status]?.label || a.status}</span></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {showModal && (
        <div className="modal-overlay">
          <div className="modal-content">
            <div className="modal-header"><h3>Book Consultation Slot</h3><button className="modal-close" onClick={() => setShowModal(false)}>&times;</button></div>
            <form onSubmit={handleBookAppointment}>
              <div className="modal-body">
                <div className="form-group"><label>Patient Full Name</label><input className="form-control" placeholder="e.g. Anita Desai" value={patient} onChange={e => setPatient(e.target.value)} required /></div>
                <div className="form-group"><label>Consulting Specialist</label><select className="form-control" value={doctor} onChange={e => setDoctor(e.target.value)}><option value="Dr. Saikiran Reddy">Dr. Saikiran Reddy (Cardiology)</option><option value="Dr. Priya Nair">Dr. Priya Nair (Neurology)</option><option value="Dr. Neha Gupta">Dr. Neha Gupta (Maternity)</option><option value="Dr. Amit Shah">Dr. Amit Shah (General)</option></select></div>
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
                  <div className="form-group"><label>Department</label><select className="form-control" value={dept} onChange={e => setDept(e.target.value)}><option value="Cardiology">Cardiology</option><option value="Neurology">Neurology</option><option value="Maternity">Maternity</option></select></div>
                  <div className="form-group"><label>Time Slot</label><input className="form-control" value={time} onChange={e => setTime(e.target.value)} required /></div>
                </div>
              </div>
              <div className="modal-footer"><button type="button" className="btn btn-outline" onClick={() => setShowModal(false)}>Cancel</button><button type="submit" className="btn btn-primary">Confirm Booking</button></div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
