import React from 'react';
import { Truck, MapPin, Phone, ShieldCheck, Plus } from 'lucide-react';

const fleet = [
  { id: 'AMB-101', driver: 'Raju Sharma', phone: '+91 98765 88881', location: 'MG Road Junction', eta: '4 min', type: 'Advanced Life Support (ALS)', status: 'Dispatched' },
  { id: 'AMB-102', driver: 'Suresh Kumar', phone: '+91 98765 88882', location: 'Indiranagar Hub', eta: 'Available', type: 'Basic Life Support (BLS)', status: 'Standby' },
  { id: 'AMB-103', driver: 'Mahesh Reddy', phone: '+91 98765 88883', location: 'Koramangala 4th Block', eta: '9 min', type: 'Neonatal ICU Ambulance', status: 'En Route Hospital' },
];

export const AmbulanceDispatch = () => {
  return (
    <div>
      <div className="page-header">
        <div className="page-title">
          <h2>Emergency Ambulance Dispatch</h2>
          <p>Real-time fleet tracking, emergency vehicle dispatch, and driver coordination</p>
        </div>
        <button className="btn btn-primary" style={{ background: '#dc2626' }}><Plus size={16} /> Dispatch Emergency Ambulance</button>
      </div>

      <div className="dashboard-grid">
        <div className="card-summary"><div className="card-summary-info"><h3>Total Fleet</h3><p>{fleet.length}</p></div><div className="card-summary-icon" style={{ background: '#ffedd5', color: '#ea580c' }}><Truck size={24} /></div></div>
        <div className="card-summary"><div className="card-summary-info"><h3>On Dispatch</h3><p style={{ color: '#dc2626' }}>2</p></div><div className="card-summary-icon" style={{ background: '#fee2e2', color: '#dc2626' }}><MapPin size={24} /></div></div>
        <div className="card-summary"><div className="card-summary-info"><h3>Standby Available</h3><p style={{ color: '#16a34a' }}>1</p></div><div className="card-summary-icon" style={{ background: '#dcfce7', color: '#16a34a' }}><CheckCircle size={24} /></div></div>
      </div>

      <div className="data-table-container">
        <div className="table-header"><h3>Active Fleet Status (09 Sep 2026)</h3></div>
        <table className="data-table">
          <thead><tr><th>Ambulance ID</th><th>Driver Name</th><th>Contact</th><th>Current Location</th><th>ETA to Destination</th><th>Vehicle Type</th><th>Status</th></tr></thead>
          <tbody>
            {fleet.map(item => (
              <tr key={item.id}>
                <td style={{ fontWeight: 700, color: '#ea580c' }}>{item.id}</td>
                <td style={{ fontWeight: 700 }}>{item.driver}</td>
                <td style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>{item.phone}</td>
                <td style={{ fontWeight: 600, display: 'flex', alignItems: 'center', gap: 4 }}>
                  <MapPin size={14} color="#dc2626" /> {item.location}
                </td>
                <td style={{ fontWeight: 700, color: 'var(--primary-color)' }}>{item.eta}</td>
                <td><span className="badge badge-primary">{item.type}</span></td>
                <td>
                  <span className={`badge ${item.status === 'Standby' ? 'badge-stable' : 'badge-critical'}`}>
                    {item.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
