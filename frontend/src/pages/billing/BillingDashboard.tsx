import React from 'react';
import { CreditCard, DollarSign, FileText, CheckCircle, Plus } from 'lucide-react';

const invoices = [
  { id: 'INV-8001', patient: 'Vikram Singh', item: 'ICU Stay & Cardiac Monitoring (3 days)', amount: '₹48,500', paid: '₹48,500', date: '09 Sep 2026', status: 'Paid' },
  { id: 'INV-8002', patient: 'Priya Sharma', item: 'Maternity Package & Ultrasound', amount: '₹32,000', paid: '₹20,000', date: '08 Sep 2026', status: 'Partial' },
  { id: 'INV-8003', patient: 'Arun Kumar', item: 'OPD Consultation & CBC Test', amount: '₹2,400', paid: '₹2,400', date: '09 Sep 2026', status: 'Paid' },
  { id: 'INV-8004', patient: 'Deepak Mishra', item: 'Hemodialysis Procedure (Session 1)', amount: '₹14,200', paid: '₹0', date: '08 Sep 2026', status: 'Pending' },
];

export const BillingDashboard = () => {
  return (
    <div>
      <div className="page-header">
        <div className="page-title">
          <h2>Patient Billing & Financial Operations</h2>
          <p>Generate patient invoices, track payments, insurance claims, and outstanding balances</p>
        </div>
        <button className="btn btn-primary"><Plus size={16} /> Create Invoice</button>
      </div>

      <div className="dashboard-grid">
        <div className="card-summary"><div className="card-summary-info"><h3>Today's Billing</h3><p>₹97,100</p></div><div className="card-summary-icon" style={{ background: '#e0f2fe', color: '#0284c7' }}><CreditCard size={24} /></div></div>
        <div className="card-summary"><div className="card-summary-info"><h3>Collected</h3><p style={{ color: '#16a34a' }}>₹70,900</p></div><div className="card-summary-icon" style={{ background: '#dcfce7', color: '#16a34a' }}><CheckCircle size={24} /></div></div>
        <div className="card-summary"><div className="card-summary-info"><h3>Pending Balance</h3><p style={{ color: '#d97706' }}>₹26,200</p></div><div className="card-summary-icon" style={{ background: '#fef3c7', color: '#d97706' }}><FileText size={24} /></div></div>
      </div>

      <div className="data-table-container">
        <div className="table-header"><h3>Recent Invoices (09 Sep 2026)</h3></div>
        <table className="data-table">
          <thead><tr><th>Invoice ID</th><th>Patient Name</th><th>Treatment / Service</th><th>Total Amount</th><th>Amount Paid</th><th>Date</th><th>Status</th></tr></thead>
          <tbody>
            {invoices.map(inv => (
              <tr key={inv.id}>
                <td style={{ fontWeight: 600, color: 'var(--primary-color)' }}>{inv.id}</td>
                <td style={{ fontWeight: 700, color: 'var(--text-main)' }}>{inv.patient}</td>
                <td>{inv.item}</td>
                <td style={{ fontWeight: 700 }}>{inv.amount}</td>
                <td style={{ color: '#16a34a', fontWeight: 600 }}>{inv.paid}</td>
                <td style={{ color: 'var(--text-muted)', fontSize: '0.85rem' }}>{inv.date}</td>
                <td>
                  <span className={`badge ${inv.status === 'Paid' ? 'badge-stable' : inv.status === 'Partial' ? 'badge-monitoring' : 'badge-critical'}`}>
                    {inv.status}
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
