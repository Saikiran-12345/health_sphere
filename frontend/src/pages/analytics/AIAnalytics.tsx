import React from 'react';
import { BarChart3, Brain, AlertTriangle, ShieldCheck } from 'lucide-react';

const predictions = [
  { patient: 'Vikram Singh', riskScore: '89%', category: 'High Cardiac Risk', model: 'Random Forest v2.4', action: 'Immediate ICU Monitoring' },
  { patient: 'Deepak Mishra', riskScore: '74%', category: 'Renal Complication', model: 'XGBoost Sepsis ML', action: 'Schedule Nephrology Consult' },
  { patient: 'Arun Kumar', riskScore: '18%', category: 'Low Readmission Risk', model: 'Prophet Census', action: 'Routine OPD Followup' },
  { patient: 'Priya Sharma', riskScore: '12%', category: 'Stable Obstetric', model: 'Clinical Decision Support', action: 'Standard Care' },
];

export const AIAnalytics = () => {
  return (
    <div>
      <div className="page-header">
        <div className="page-title">
          <h2>AI Clinical Diagnostics & Predictive Risk</h2>
          <p>Machine Learning patient risk scoring, readmission prediction, and automated clinical alerts</p>
        </div>
      </div>

      <div className="dashboard-grid">
        <div className="card-summary"><div className="card-summary-info"><h3>Active ML Models</h3><p>4 Models</p></div><div className="card-summary-icon" style={{ background: '#ede9fe', color: '#8b5cf6' }}><Brain size={24} /></div></div>
        <div className="card-summary"><div className="card-summary-info"><h3>High Risk Patients</h3><p style={{ color: '#dc2626' }}>2 Patients</p></div><div className="card-summary-icon" style={{ background: '#fee2e2', color: '#dc2626' }}><AlertTriangle size={24} /></div></div>
        <div className="card-summary"><div className="card-summary-info"><h3>Model Confidence</h3><p style={{ color: '#16a34a' }}>94.2%</p></div><div className="card-summary-icon" style={{ background: '#dcfce7', color: '#16a34a' }}><ShieldCheck size={24} /></div></div>
      </div>

      <div className="data-table-container">
        <div className="table-header"><h3>Real-Time AI Patient Risk Matrix (09 Sep 2026)</h3></div>
        <table className="data-table">
          <thead><tr><th>Patient Name</th><th>AI Risk Score</th><th>Risk Category</th><th>ML Algorithm</th><th>Recommended Clinical Action</th></tr></thead>
          <tbody>
            {predictions.map((p, idx) => (
              <tr key={idx}>
                <td style={{ fontWeight: 700, color: 'var(--text-main)' }}>{p.patient}</td>
                <td>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <div style={{ width: 100, height: 8, background: '#e2e8f0', borderRadius: 4, overflow: 'hidden' }}>
                      <div style={{ width: p.riskScore, height: '100%', background: parseInt(p.riskScore) > 70 ? '#dc2626' : parseInt(p.riskScore) > 40 ? '#d97706' : '#16a34a' }}></div>
                    </div>
                    <span style={{ fontWeight: 700, fontSize: '0.85rem' }}>{p.riskScore}</span>
                  </div>
                </td>
                <td>
                  <span className={`badge ${parseInt(p.riskScore) > 70 ? 'badge-critical' : parseInt(p.riskScore) > 40 ? 'badge-monitoring' : 'badge-stable'}`}>
                    {p.category}
                  </span>
                </td>
                <td style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>{p.model}</td>
                <td style={{ fontWeight: 600, color: 'var(--text-main)' }}>{p.action}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
