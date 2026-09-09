import React, { useState } from 'react';
import { Search, Plus } from 'lucide-react';
import { useHospitalData, type Doctor } from '../../context/DataContext';

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
      email: email || `${name.toLowerCase().replace(/\s+/g, '')}@healthsphere.com`,
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
