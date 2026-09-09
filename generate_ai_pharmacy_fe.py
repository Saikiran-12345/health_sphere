import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. AI Analytics Dashboard
create_file('frontend/src/pages/analytics/AIAnalytics.tsx', """
import React, { useState } from 'react';
import { Activity, AlertTriangle, ShieldCheck, BrainCircuit, HeartPulse } from 'lucide-react';
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, BarChart, Bar } from 'recharts';

const dummyRiskData = [
  { ageGroup: '18-30', lowRisk: 80, highRisk: 5 },
  { ageGroup: '31-45', lowRisk: 75, highRisk: 15 },
  { ageGroup: '46-60', lowRisk: 50, highRisk: 35 },
  { ageGroup: '61-75', lowRisk: 30, highRisk: 60 },
  { ageGroup: '75+', lowRisk: 10, highRisk: 85 },
];

const dummyAnomalyData = [
  { time: '08:00', load: 45, threshold: 80 },
  { time: '10:00', load: 78, threshold: 80 },
  { time: '12:00', load: 120, threshold: 80 }, // Anomaly Spike
  { time: '14:00', load: 85, threshold: 80 },
  { time: '16:00', load: 60, threshold: 80 },
];

export const AIAnalytics: React.FC = () => {
  const [patientVitals, setPatientVitals] = useState({ age: 68, systolic_bp: 145, bmi: 31 });
  const [riskScore, setRiskScore] = useState<number | null>(82);

  const simulatePrediction = () => {
    setRiskScore(null);
    setTimeout(() => setRiskScore(Math.floor(Math.random() * 40) + 60), 800); // Simulate API call to ML model
  };

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-gray-800 flex items-center gap-2">
          <BrainCircuit className="text-purple-600" size={28}/> AI Risk & Analytics Engine
        </h2>
      </div>

      {/* Top Models View */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        
        {/* Real-time Patient Predictor */}
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <h3 className="text-lg font-bold text-gray-800 border-b pb-2 mb-4 flex items-center gap-2">
            <HeartPulse className="text-red-500"/> Real-Time Patient Risk Predictor (Random Forest)
          </h3>
          <div className="space-y-4">
            <div className="grid grid-cols-3 gap-4">
              <div>
                <label className="block text-xs font-medium text-gray-500 uppercase">Age</label>
                <input type="number" value={patientVitals.age} onChange={e => setPatientVitals({...patientVitals, age: +e.target.value})} className="mt-1 w-full p-2 border rounded bg-gray-50" />
              </div>
              <div>
                <label className="block text-xs font-medium text-gray-500 uppercase">Systolic BP</label>
                <input type="number" value={patientVitals.systolic_bp} onChange={e => setPatientVitals({...patientVitals, systolic_bp: +e.target.value})} className="mt-1 w-full p-2 border rounded bg-gray-50" />
              </div>
              <div>
                <label className="block text-xs font-medium text-gray-500 uppercase">BMI</label>
                <input type="number" value={patientVitals.bmi} onChange={e => setPatientVitals({...patientVitals, bmi: +e.target.value})} className="mt-1 w-full p-2 border rounded bg-gray-50" />
              </div>
            </div>
            
            <button onClick={simulatePrediction} className="w-full py-2 bg-purple-600 hover:bg-purple-700 text-white rounded font-medium transition-colors">
              Run Inference
            </button>
            
            {riskScore !== null && (
              <div className={`mt-4 p-4 rounded-lg flex items-center gap-4 ${riskScore > 75 ? 'bg-red-50 border border-red-200' : 'bg-green-50 border border-green-200'}`}>
                {riskScore > 75 ? <AlertTriangle size={32} className="text-red-600"/> : <ShieldCheck size={32} className="text-green-600"/>}
                <div>
                  <h4 className={`text-xl font-bold ${riskScore > 75 ? 'text-red-800' : 'text-green-800'}`}>
                    {riskScore}% Readmission Risk
                  </h4>
                  <p className="text-sm text-gray-600 mt-1">Based on historical data and current vitals.</p>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Operational Anomaly Chart */}
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <h3 className="text-lg font-bold text-gray-800 border-b pb-2 mb-4 flex items-center gap-2">
            <Activity className="text-orange-500"/> Operational Load Anomalies (Isolation Forest)
          </h3>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={dummyAnomalyData}>
                <CartesianGrid strokeDasharray="3 3" vertical={false}/>
                <XAxis dataKey="time" />
                <YAxis />
                <Tooltip />
                <Line type="monotone" dataKey="threshold" stroke="#ef4444" strokeWidth={2} strokeDasharray="5 5" dot={false} name="Safety Threshold"/>
                <Line type="monotone" dataKey="load" stroke="#f97316" strokeWidth={3} name="Hospital Load"/>
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
        
      </div>
      
      {/* Risk Distribution Chart */}
      <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
         <h3 className="text-lg font-bold text-gray-800 mb-4">Demographic Risk Distribution</h3>
         <div className="h-72">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={dummyRiskData}>
                <CartesianGrid strokeDasharray="3 3" vertical={false}/>
                <XAxis dataKey="ageGroup" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="lowRisk" stackId="a" fill="#22c55e" name="Low Risk" />
                <Bar dataKey="highRisk" stackId="a" fill="#ef4444" name="High Risk" />
              </BarChart>
            </ResponsiveContainer>
         </div>
      </div>
      
    </div>
  );
};
""")

# 2. Pharmacy Inventory UI
create_file('frontend/src/pages/pharmacy/PharmacyInventory.tsx', """
import React, { useState } from 'react';
import { Search, Plus, AlertCircle, Package } from 'lucide-react';

export const PharmacyInventory: React.FC = () => {
  const [medicines] = useState([
    { id: 'MED-001', name: 'Amoxicillin 500mg', generic: 'Amoxicillin', category: 'Antibiotic', stock: 450, reorder: 100, price: 12.50 },
    { id: 'MED-002', name: 'Lisinopril 10mg', generic: 'Lisinopril', category: 'Antihypertensive', stock: 85, reorder: 150, price: 8.00 },
    { id: 'MED-003', name: 'Metformin 850mg', generic: 'Metformin', category: 'Antidiabetic', stock: 1200, reorder: 500, price: 5.75 },
    { id: 'MED-004', name: 'Ibuprofen 400mg', generic: 'Ibuprofen', category: 'Analgesic', stock: 30, reorder: 200, price: 4.20 },
  ]);

  return (
    <div className="bg-white rounded-lg shadow h-full flex flex-col">
      <div className="p-6 border-b border-gray-200 flex justify-between items-center">
        <h2 className="text-2xl font-bold text-gray-800 flex items-center gap-2">
          <Package className="text-blue-600"/> Pharmacy & Inventory
        </h2>
        <button className="flex items-center gap-2 bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
          <Plus size={18} /> Add Stock
        </button>
      </div>
      
      <div className="p-4 border-b border-gray-200 bg-gray-50 flex gap-4">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={18} />
          <input type="text" placeholder="Search medicines by name, generic, or category..." className="w-full pl-10 pr-4 py-2 border rounded-md" />
        </div>
      </div>

      <div className="flex-1 overflow-auto">
        <table className="w-full text-left border-collapse">
          <thead>
            <tr className="bg-gray-50 text-gray-600 text-sm uppercase tracking-wider">
              <th className="p-4 font-semibold border-b">ID</th>
              <th className="p-4 font-semibold border-b">Medicine Name</th>
              <th className="p-4 font-semibold border-b">Category</th>
              <th className="p-4 font-semibold border-b">Unit Price</th>
              <th className="p-4 font-semibold border-b">Stock Level</th>
              <th className="p-4 font-semibold border-b text-right">Status</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {medicines.map((med) => {
              const isLowStock = med.stock <= med.reorder;
              return (
                <tr key={med.id} className="hover:bg-gray-50">
                  <td className="p-4 text-gray-500 font-medium">{med.id}</td>
                  <td className="p-4">
                    <div className="font-bold text-gray-900">{med.name}</div>
                    <div className="text-xs text-gray-500">Generic: {med.generic}</div>
                  </td>
                  <td className="p-4 text-gray-600">{med.category}</td>
                  <td className="p-4 text-gray-600">${med.price.toFixed(2)}</td>
                  <td className="p-4">
                    <span className={`font-bold ${isLowStock ? 'text-red-600' : 'text-gray-700'}`}>{med.stock}</span>
                    <span className="text-gray-400 text-sm ml-1">/ {med.reorder} min</span>
                  </td>
                  <td className="p-4 flex justify-end">
                    {isLowStock ? (
                      <span className="flex items-center gap-1 text-red-600 bg-red-50 px-3 py-1 rounded-full text-xs font-bold border border-red-200">
                        <AlertCircle size={14}/> LOW STOCK
                      </span>
                    ) : (
                      <span className="flex items-center gap-1 text-green-600 bg-green-50 px-3 py-1 rounded-full text-xs font-bold border border-green-200">
                        IN STOCK
                      </span>
                    )}
                  </td>
                </tr>
              )
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};
""")

# 3. Add Pharmacy to DashboardLayout sidebar
path = "frontend/src/layouts/DashboardLayout.tsx"
with open(path, "r") as f:
    content = f.read()

# Make sure we only add it once
if "Pharmacy" not in content:
    content = content.replace("import { Activity, Calendar, Users, FileText, Settings, LogOut, Menu, X, Bed, Crosshair, Home } from 'lucide-react';", 
                              "import { Activity, Calendar, Users, FileText, Settings, LogOut, Menu, X, Bed, Crosshair, Home, Package } from 'lucide-react';")
    content = content.replace("{ label: 'Admissions & Beds', icon: <Bed size={20} />, path: '/admissions' },", 
                              "{ label: 'Admissions & Beds', icon: <Bed size={20} />, path: '/admissions' },\n    { label: 'Pharmacy', icon: <Package size={20} />, path: '/pharmacy' },")
    with open(path, "w") as f:
        f.write(content)

# 4. Update App.tsx Routing
path = "frontend/src/App.tsx"
with open(path, "r") as f:
    content = f.read()

imports = """
import { AIAnalytics } from './pages/analytics/AIAnalytics';
import { PharmacyInventory } from './pages/pharmacy/PharmacyInventory';
"""
content = content.replace("import { BedManagement } from './pages/admissions/BedManagement';", "import { BedManagement } from './pages/admissions/BedManagement';\n" + imports)

content = content.replace('<Route path="/analytics" element={<div className="p-6">AI Analytics Module Coming Soon</div>} />', '<Route path="/analytics" element={<AIAnalytics />} />')

# Add pharmacy route
content = content.replace('</Route>', '  <Route path="/pharmacy" element={<PharmacyInventory />} />\n      </Route>')

with open(path, "w") as f:
    f.write(content)

print("AI and Pharmacy UI generated successfully.")
