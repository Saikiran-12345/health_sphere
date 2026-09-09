import React, { useState } from 'react';
import { Search, FileText, Activity, Pill, FlaskConical } from 'lucide-react';

export const MedicalRecords: React.FC = () => {
  const [records] = useState([
    { id: '1', date: '2026-09-08', type: 'CLINICAL_NOTE', title: 'General Checkup', doctor: 'Dr. Sarah Smith', excerpt: 'Patient presents with mild fever and fatigue...' },
    { id: '2', date: '2026-09-08', type: 'PRESCRIPTION', title: 'Amoxicillin 500mg', doctor: 'Dr. Sarah Smith', excerpt: 'Take twice daily for 7 days after meals.' },
    { id: '3', date: '2026-09-01', type: 'LAB_RESULT', title: 'Complete Blood Count', doctor: 'Dr. Michael Chen', excerpt: 'All parameters within normal limits. Hemoglobin 14.2 g/dL.' },
  ]);

  const getIcon = (type: string) => {
    switch (type) {
      case 'CLINICAL_NOTE': return <FileText className="text-blue-500" />;
      case 'PRESCRIPTION': return <Pill className="text-green-500" />;
      case 'LAB_RESULT': return <FlaskConical className="text-purple-500" />;
      default: return <Activity className="text-gray-500" />;
    }
  };

  return (
    <div className="h-full flex flex-col bg-white rounded-lg shadow-sm">
      <div className="p-6 border-b border-gray-200">
        <h2 className="text-2xl font-bold text-gray-800">Electronic Medical Records (EMR)</h2>
        <p className="text-gray-500 mt-1">Search and manage clinical documentation</p>
      </div>
      
      <div className="p-6 flex-1 bg-gray-50 overflow-auto">
        <div className="max-w-4xl mx-auto relative space-y-8 before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-slate-300 before:to-transparent">
          {records.map((record, idx) => (
            <div key={record.id} className={`relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active`}>
              <div className="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-white shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10">
                {getIcon(record.type)}
              </div>
              <div className="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white p-4 rounded-lg border border-gray-200 shadow-sm">
                <div className="flex items-center justify-between mb-2">
                  <span className="font-bold text-slate-900">{record.title}</span>
                  <time className="text-sm font-medium text-slate-500">{record.date}</time>
                </div>
                <div className="text-sm text-slate-500 mb-2">{record.doctor}</div>
                <p className="text-slate-600">{record.excerpt}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
