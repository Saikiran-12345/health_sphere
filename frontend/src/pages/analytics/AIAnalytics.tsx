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
