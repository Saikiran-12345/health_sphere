import React, { useState } from 'react';
import { CreditCard, DollarSign, FileText, CheckCircle } from 'lucide-react';

export const BillingDashboard: React.FC = () => {
  const [invoices] = useState([
    { id: 'INV-1001', patient: 'John Doe', date: '2026-09-01', amount: 1250.00, status: 'PAID' },
    { id: 'INV-1002', patient: 'Jane Smith', date: '2026-09-05', amount: 450.00, status: 'PENDING' },
    { id: 'INV-1003', patient: 'Robert Fox', date: '2026-09-08', amount: 3200.00, status: 'PARTIAL' },
  ]);

  return (
    <div className="bg-white rounded-lg shadow h-full flex flex-col p-6">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-gray-800 flex items-center gap-2">
          <CreditCard className="text-green-600"/> Billing & Invoicing
        </h2>
        <button className="bg-green-600 text-white px-4 py-2 rounded shadow-sm hover:bg-green-700">
          Create Invoice
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="p-4 rounded-lg bg-green-50 border border-green-200">
          <p className="text-sm font-medium text-green-600">Total Revenue (Month)</p>
          <h3 className="text-3xl font-bold text-green-800 mt-2">$45,200.00</h3>
        </div>
        <div className="p-4 rounded-lg bg-yellow-50 border border-yellow-200">
          <p className="text-sm font-medium text-yellow-600">Pending Payments</p>
          <h3 className="text-3xl font-bold text-yellow-800 mt-2">$12,450.00</h3>
        </div>
        <div className="p-4 rounded-lg bg-blue-50 border border-blue-200">
          <p className="text-sm font-medium text-blue-600">Insurance Claims Pending</p>
          <h3 className="text-3xl font-bold text-blue-800 mt-2">18 Claims</h3>
        </div>
      </div>

      <h3 className="text-lg font-bold text-gray-800 mb-4">Recent Invoices</h3>
      <table className="w-full text-left border-collapse">
        <thead>
          <tr className="bg-gray-50 text-gray-600 text-sm uppercase">
            <th className="p-4 border-b">Invoice ID</th>
            <th className="p-4 border-b">Patient</th>
            <th className="p-4 border-b">Date</th>
            <th className="p-4 border-b text-right">Amount</th>
            <th className="p-4 border-b">Status</th>
          </tr>
        </thead>
        <tbody>
          {invoices.map(inv => (
            <tr key={inv.id} className="border-b">
              <td className="p-4 font-medium text-gray-900">{inv.id}</td>
              <td className="p-4 text-gray-600">{inv.patient}</td>
              <td className="p-4 text-gray-600">{inv.date}</td>
              <td className="p-4 text-right font-medium text-gray-900">${inv.amount.toFixed(2)}</td>
              <td className="p-4">
                <span className={`px-2 py-1 text-xs font-bold rounded-full 
                  ${inv.status === 'PAID' ? 'bg-green-100 text-green-800' : 
                    inv.status === 'PENDING' ? 'bg-yellow-100 text-yellow-800' : 'bg-orange-100 text-orange-800'}`}>
                  {inv.status}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
