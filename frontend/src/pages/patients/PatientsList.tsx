import React, { useState } from 'react';
import { Search, Plus, Filter, Calendar } from 'lucide-react';
import { useHospitalData, type Patient } from '../../context/DataContext';

const statusMap: any = {
  admitted: { label: 'Admitted', cls: 'badge-inqueue' },
  outpatient: { label: 'Outpatient', cls: 'badge-primary' },
  discharged: { label: 'Discharged', cls: 'badge-completed' },
  critical: { label: 'Critical', cls: 'badge-critical' },
};

export const PatientsList = () => {
  const { patients, addPatient } = useHospitalData();
  const [search, setSearch] = useState('');
  const [showModal, setShowModal] = useState(false);

  const [name, setName] = useState('');
  const [age, setAge] = useState<number>(35);
  const [gender, setGender] = useState('Male');
  const [phone, setPhone] = useState('');
  const [blood, setBlood] = useState('O+');
  const [condition, setCondition] = useState('');
  const [doctor, setDoctor] = useState('Dr. Saikiran Reddy');
  const [status, setStatus] = useState('admitted');

  const filtered = patients.filter(p => p.name.toLowerCase().includes(search.toLowerCase()) || p.id.toLowerCase().includes(search.toLowerCase()));

  const handleAddPatient = (e: React.FormEvent) => {
    e.preventDefault();
    if (!name) return;
    const newPat: Patient = {
      id: `P-${Math.floor(1000 + Math.random() * 9000)}`,
      name,
      age: Number(age),
      gender,
      phone: phone || '+91 98765 00000',
      blood,
      condition: condition || 'General Checkup',
      doctor,
      admitted: status === 'admitted' || status === 'critical' ? '09 Sep 2026, 09:30 AM' : '-',
      status
    };
    addPatient(newPat);
    setName(''); setCondition(''); setPhone(''); setShowModal(false);
  };

  return (
    <div>
      <div className="page-header">
        <div className="page-title">
          <h2>Patient Registry Directory</h2>
          <p>Register, track, and manage all inpatient and outpatient health records</p>
        </div>
        <button className="btn btn-primary" onClick={() => setShowModal(true)}>
          <Plus size={16} /> Register Patient
        </button>
      </div>

      <div style={{ display: 'flex', gap: '1rem', marginBottom: '1.5rem' }}>
        <div style={{ flex: 1, position: 'relative' }}>
          <Search size={16} style={{ position: 'absolute', left: 12, top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
          <input className="form-control" style={{ paddingLeft: '2.5rem' }} placeholder="Search by patient name, ID, or phone number..." value={search} onChange={e => setSearch(e.target.value)} />
        </div>
      </div>

      <div className="data-table-container">
        <div className="table-header">
          <h3>Registered Patients ({filtered.length})</h3>
          <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Updated live</span>
        </div>
        <table className="data-table">
          <thead>
            <tr>
              <th>Patient ID</th><th>Full Name</th><th>Age / Gender</th><th>Blood</th><th>Diagnosis / Condition</th><th>Primary Specialist</th><th>Admission Date</th><th>Status</th>
            </tr>
          </thead>
          <tbody>
            {filtered.map(p => (
              <tr key={p.id}>
                <td style={{ fontWeight: 700, color: 'var(--primary-color)' }}>{p.id}</td>
                <td style={{ fontWeight: 700, color: 'var(--text-main)' }}>{p.name}</td>
                <td>{p.age} / {p.gender}</td>
                <td><span className="badge badge-primary">{p.blood}</span></td>
                <td>{p.condition}</td>
                <td style={{ color: 'var(--text-muted)', fontWeight: 500 }}>{p.doctor}</td>
                <td style={{ fontSize: '0.825rem', color: 'var(--text-muted)' }}>{p.admitted}</td>
                <td><span className={`badge ${statusMap[p.status]?.cls || 'badge-primary'}`}>{statusMap[p.status]?.label || p.status}</span></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {showModal && (
        <div className="modal-overlay">
          <div className="modal-content">
            <div className="modal-header">
              <h3>Register New Patient</h3>
              <button className="modal-close" onClick={() => setShowModal(false)}>&times;</button>
            </div>
            <form onSubmit={handleAddPatient}>
              <div className="modal-body">
                <div className="form-group"><label>Patient Full Name</label><input className="form-control" placeholder="e.g. Ramesh Reddy" value={name} onChange={e => setName(e.target.value)} required /></div>
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
                  <div className="form-group"><label>Age</label><input className="form-control" type="number" value={age} onChange={e => setAge(Number(e.target.value))} required /></div>
                  <div className="form-group"><label>Gender</label><select className="form-control" value={gender} onChange={e => setGender(e.target.value)}><option value="Male">Male</option><option value="Female">Female</option></select></div>
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
                  <div className="form-group"><label>Blood Group</label><select className="form-control" value={blood} onChange={e => setBlood(e.target.value)}><option value="O+">O+</option><option value="A+">A+</option><option value="B+">B+</option><option value="AB+">AB+</option><option value="O-">O-</option></select></div>
                  <div className="form-group"><label>Admission Status</label><select className="form-control" value={status} onChange={e => setStatus(e.target.value)}><option value="admitted">Admitted</option><option value="outpatient">Outpatient</option><option value="critical">Critical</option></select></div>
                </div>
                <div className="form-group"><label>Primary Diagnosis / Condition</label><input className="form-control" placeholder="e.g. Acute Coronary Syndrome" value={condition} onChange={e => setCondition(e.target.value)} /></div>
                <div className="form-group"><label>Assigned Specialist</label><select className="form-control" value={doctor} onChange={e => setDoctor(e.target.value)}><option value="Dr. Saikiran Reddy">Dr. Saikiran Reddy (Cardiology)</option><option value="Dr. Priya Nair">Dr. Priya Nair (Neurology)</option><option value="Dr. Neha Gupta">Dr. Neha Gupta (Maternity)</option><option value="Dr. Amit Shah">Dr. Amit Shah (General)</option></select></div>
              </div>
              <div className="modal-footer"><button type="button" className="btn btn-outline" onClick={() => setShowModal(false)}>Cancel</button><button type="submit" className="btn btn-primary">Register Patient</button></div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
