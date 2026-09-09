import React, { useState } from 'react';
import { Pill, Package, AlertTriangle, Plus, Search } from 'lucide-react';

const inventory = [
  { code: 'MED-101', name: 'Paracetamol 650mg', category: 'Analgesic', stock: 450, unit: 'Tablets', price: '₹18.50', expiry: '2027-04-15', status: 'In Stock' },
  { code: 'MED-102', name: 'Amoxicillin 500mg', category: 'Antibiotic', stock: 120, unit: 'Capsules', price: '₹85.00', expiry: '2026-12-01', status: 'In Stock' },
  { code: 'MED-103', name: 'Atorvastatin 10mg', category: 'Cardiovascular', stock: 35, unit: 'Tablets', price: '₹140.00', expiry: '2026-11-20', status: 'Low Stock' },
  { code: 'MED-104', name: 'Omeprazole 20mg', category: 'Gastrointestinal', stock: 12, unit: 'Capsules', price: '₹62.00', expiry: '2026-10-10', status: 'Critical' },
  { code: 'MED-105', name: 'Metformin 500mg', category: 'Anti-Diabetic', stock: 310, unit: 'Tablets', price: '₹45.00', expiry: '2027-08-30', status: 'In Stock' },
];

export const PharmacyInventory = () => {
  const [search, setSearch] = useState('');
  const filtered = inventory.filter(i => i.name.toLowerCase().includes(search.toLowerCase()));

  return (
    <div>
      <div className="page-header">
        <div className="page-title">
          <h2>Pharmacy Stock & Dispensary</h2>
          <p>Monitor drug inventory, stock levels, expiration dates, and reorder alerts</p>
        </div>
        <button className="btn btn-primary"><Plus size={16} /> Add Medicine</button>
      </div>

      <div className="dashboard-grid">
        <div className="card-summary"><div className="card-summary-info"><h3>Total Drugs</h3><p>{inventory.length}</p></div><div className="card-summary-icon" style={{ background: '#e0f2fe', color: '#0284c7' }}><Pill size={24} /></div></div>
        <div className="card-summary"><div className="card-summary-info"><h3>In Stock</h3><p style={{ color: '#16a34a' }}>3</p></div><div className="card-summary-icon" style={{ background: '#dcfce7', color: '#16a34a' }}><Package size={24} /></div></div>
        <div className="card-summary"><div className="card-summary-info"><h3>Low Stock Alert</h3><p style={{ color: '#d97706' }}>1</p></div><div className="card-summary-icon" style={{ background: '#fef3c7', color: '#d97706' }}><AlertTriangle size={24} /></div></div>
        <div className="card-summary"><div className="card-summary-info"><h3>Critical Reorder</h3><p style={{ color: '#dc2626' }}>1</p></div><div className="card-summary-icon" style={{ background: '#fee2e2', color: '#dc2626' }}><AlertTriangle size={24} /></div></div>
      </div>

      <div style={{ marginBottom: '1.5rem', position: 'relative' }}>
        <Search size={16} style={{ position: 'absolute', left: 12, top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
        <input className="form-control" style={{ paddingLeft: '2.5rem' }} placeholder="Search medicine by name or category..." value={search} onChange={e => setSearch(e.target.value)} />
      </div>

      <div className="data-table-container">
        <div className="table-header"><h3>Medication Inventory</h3></div>
        <table className="data-table">
          <thead><tr><th>Drug Code</th><th>Medicine Name</th><th>Category</th><th>Stock Level</th><th>Unit Price</th><th>Expiry Date</th><th>Status</th></tr></thead>
          <tbody>
            {filtered.map(item => (
              <tr key={item.code}>
                <td style={{ fontWeight: 600, color: 'var(--primary-color)' }}>{item.code}</td>
                <td style={{ fontWeight: 700, color: 'var(--text-main)' }}>{item.name}</td>
                <td>{item.category}</td>
                <td style={{ fontWeight: 700 }}>{item.stock} {item.unit}</td>
                <td style={{ fontWeight: 600 }}>{item.price}</td>
                <td style={{ color: 'var(--text-muted)', fontSize: '0.85rem' }}>{item.expiry}</td>
                <td>
                  <span className={`badge ${item.status === 'In Stock' ? 'badge-stable' : item.status === 'Low Stock' ? 'badge-monitoring' : 'badge-critical'}`}>
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
