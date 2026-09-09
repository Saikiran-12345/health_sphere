import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Billing UI
create_file('frontend/src/pages/billing/BillingDashboard.tsx', """
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
""")

# 2. Ambulance UI
create_file('frontend/src/pages/ambulance/AmbulanceDispatch.tsx', """
import React, { useState } from 'react';
import { Truck, MapPin, AlertCircle, PhoneCall } from 'lucide-react';

export const AmbulanceDispatch: React.FC = () => {
  const [ambulances] = useState([
    { id: 'AMB-01', type: 'ICU', status: 'AVAILABLE', location: 'Base Station' },
    { id: 'AMB-02', type: 'ALS', status: 'EN_ROUTE', location: '123 Main St' },
    { id: 'AMB-03', type: 'BASIC', status: 'MAINTENANCE', location: 'Garage' },
  ]);

  return (
    <div className="bg-white rounded-lg shadow h-full flex flex-col p-6">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-gray-800 flex items-center gap-2">
          <Truck className="text-red-600"/> Ambulance Dispatch
        </h2>
        <button className="bg-red-600 text-white px-4 py-2 rounded shadow-sm flex items-center gap-2 hover:bg-red-700">
          <PhoneCall size={18}/> Emergency Dispatch
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {ambulances.map(amb => (
          <div key={amb.id} className={`p-6 rounded-lg border-2 ${
            amb.status === 'AVAILABLE' ? 'border-green-200 bg-green-50' :
            amb.status === 'EN_ROUTE' ? 'border-blue-200 bg-blue-50' : 'border-gray-200 bg-gray-50'
          }`}>
            <div className="flex justify-between items-start">
              <div>
                <h3 className="text-xl font-bold text-gray-900">{amb.id}</h3>
                <p className="text-sm font-medium text-gray-500">{amb.type} Unit</p>
              </div>
              <Truck size={28} className={
                amb.status === 'AVAILABLE' ? 'text-green-600' :
                amb.status === 'EN_ROUTE' ? 'text-blue-600' : 'text-gray-400'
              }/>
            </div>
            
            <div className="mt-4 flex items-center gap-2 text-gray-700">
              <MapPin size={16} /> <span className="text-sm">{amb.location}</span>
            </div>
            
            <div className="mt-4">
               <span className={`px-3 py-1 text-xs font-bold rounded-full ${
                  amb.status === 'AVAILABLE' ? 'bg-green-200 text-green-900' :
                  amb.status === 'EN_ROUTE' ? 'bg-blue-200 text-blue-900' : 'bg-gray-200 text-gray-900'
               }`}>
                 {amb.status}
               </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
""")

# Update Dashboard Sidebar
path = "frontend/src/layouts/DashboardLayout.tsx"
with open(path, "r") as f:
    content = f.read()

if "Billing & Invoicing" not in content:
    content = content.replace(
        "import { Activity, Calendar, Users, FileText, Settings, LogOut, Menu, X, Bed, Crosshair, Home, Package } from 'lucide-react';",
        "import { Activity, Calendar, Users, FileText, Settings, LogOut, Menu, X, Bed, Crosshair, Home, Package, CreditCard, Truck } from 'lucide-react';"
    )
    content = content.replace(
        "{ label: 'Pharmacy', icon: <Package size={20} />, path: '/pharmacy' },",
        "{ label: 'Pharmacy', icon: <Package size={20} />, path: '/pharmacy' },\n    { label: 'Billing & Invoicing', icon: <CreditCard size={20} />, path: '/billing' },\n    { label: 'Ambulance Dispatch', icon: <Truck size={20} />, path: '/ambulance' },"
    )
    with open(path, "w") as f:
        f.write(content)

# Update App.tsx Routing
path = "frontend/src/App.tsx"
with open(path, "r") as f:
    content = f.read()

imports = """
import { BillingDashboard } from './pages/billing/BillingDashboard';
import { AmbulanceDispatch } from './pages/ambulance/AmbulanceDispatch';
"""
content = content.replace("import { PharmacyInventory } from './pages/pharmacy/PharmacyInventory';", "import { PharmacyInventory } from './pages/pharmacy/PharmacyInventory';\n" + imports)

routes = """
        <Route path="/billing" element={<BillingDashboard />} />
        <Route path="/ambulance" element={<AmbulanceDispatch />} />
"""
content = content.replace('</Route>', routes + '\n      </Route>')

with open(path, "w") as f:
    f.write(content)

print("Enterprise UIs generated successfully.")
