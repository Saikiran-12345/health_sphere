import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Appointments UI
create_file('frontend/src/pages/appointments/AppointmentsList.tsx', """
import React, { useState } from 'react';
import { Calendar as CalendarIcon, Clock, User, Activity, CheckCircle, XCircle } from 'lucide-react';

export const AppointmentsList: React.FC = () => {
  const [appointments] = useState([
    { id: '1', patient: 'John Doe', doctor: 'Dr. Sarah Smith', date: '2026-09-09', time: '10:00 AM', type: 'Checkup', status: 'CONFIRMED' },
    { id: '2', patient: 'Jane Roe', doctor: 'Dr. Michael Chen', date: '2026-09-09', time: '11:30 AM', type: 'Consultation', status: 'CHECKED_IN' },
    { id: '3', patient: 'Sam Smith', doctor: 'Dr. Sarah Smith', date: '2026-09-09', time: '02:00 PM', type: 'Follow-up', status: 'SCHEDULED' },
  ]);

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'CONFIRMED': return 'bg-blue-100 text-blue-800';
      case 'CHECKED_IN': return 'bg-green-100 text-green-800';
      case 'SCHEDULED': return 'bg-gray-100 text-gray-800';
      case 'CANCELLED': return 'bg-red-100 text-red-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-gray-800">Appointments Schedule</h2>
        <button className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 shadow-sm flex items-center gap-2">
          <CalendarIcon size={18} /> Schedule New
        </button>
      </div>

      <div className="grid gap-4">
        {appointments.map(appt => (
          <div key={appt.id} className="bg-white p-6 rounded-lg shadow-sm border border-gray-100 flex items-center justify-between hover:shadow-md transition-shadow">
            <div className="flex items-center gap-6">
              <div className="p-3 bg-blue-50 text-blue-600 rounded-full">
                <Clock size={24} />
              </div>
              <div>
                <h3 className="text-lg font-bold text-gray-900">{appt.time}</h3>
                <p className="text-sm text-gray-500">{appt.date}</p>
              </div>
              <div className="h-10 w-px bg-gray-200"></div>
              <div>
                <div className="flex items-center gap-2 text-gray-800 font-medium">
                  <User size={16} className="text-gray-400"/> {appt.patient}
                </div>
                <div className="flex items-center gap-2 text-sm text-gray-500 mt-1">
                  <Activity size={16} /> {appt.doctor} • {appt.type}
                </div>
              </div>
            </div>
            
            <div className="flex items-center gap-4">
              <span className={`px-3 py-1 rounded-full text-xs font-bold tracking-wide ${getStatusColor(appt.status)}`}>
                {appt.status.replace('_', ' ')}
              </span>
              <div className="flex gap-2">
                <button className="p-2 text-gray-400 hover:text-green-600 hover:bg-green-50 rounded-full transition-colors" title="Check In">
                  <CheckCircle size={20} />
                </button>
                <button className="p-2 text-gray-400 hover:text-red-600 hover:bg-red-50 rounded-full transition-colors" title="Cancel">
                  <XCircle size={20} />
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
""")

# 2. Medical Records (EMR) UI
create_file('frontend/src/pages/records/MedicalRecords.tsx', """
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
""")

# 3. Admissions & Bed Management UI
create_file('frontend/src/pages/admissions/BedManagement.tsx', """
import React from 'react';
import { BedDouble, User } from 'lucide-react';

export const BedManagement: React.FC = () => {
  const wards = [
    {
      name: 'Intensive Care Unit (ICU)',
      beds: [
        { id: 'ICU-1', status: 'OCCUPIED', patient: 'Robert Fox' },
        { id: 'ICU-2', status: 'OCCUPIED', patient: 'Jane Smith' },
        { id: 'ICU-3', status: 'AVAILABLE', patient: null },
        { id: 'ICU-4', status: 'MAINTENANCE', patient: null },
      ]
    },
    {
      name: 'General Ward A',
      beds: [
        { id: 'GEN-1', status: 'AVAILABLE', patient: null },
        { id: 'GEN-2', status: 'AVAILABLE', patient: null },
        { id: 'GEN-3', status: 'OCCUPIED', patient: 'Alice Johnson' },
        { id: 'GEN-4', status: 'AVAILABLE', patient: null },
      ]
    }
  ];

  return (
    <div className="space-y-8">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-gray-800">Bed Management</h2>
        <div className="flex gap-4 text-sm font-medium text-gray-600">
          <div className="flex items-center gap-2"><span className="w-3 h-3 rounded-full bg-green-500"></span> Available</div>
          <div className="flex items-center gap-2"><span className="w-3 h-3 rounded-full bg-red-500"></span> Occupied</div>
          <div className="flex items-center gap-2"><span className="w-3 h-3 rounded-full bg-yellow-500"></span> Maintenance</div>
        </div>
      </div>

      {wards.map((ward, idx) => (
        <div key={idx} className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
          <h3 className="text-lg font-bold text-gray-800 mb-6 border-b pb-2">{ward.name}</h3>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
            {ward.beds.map(bed => (
              <div key={bed.id} className={`p-4 rounded-lg border-2 flex flex-col items-center text-center transition-all cursor-pointer hover:shadow-md
                ${bed.status === 'AVAILABLE' ? 'border-green-200 bg-green-50' : 
                  bed.status === 'OCCUPIED' ? 'border-red-200 bg-red-50' : 'border-yellow-200 bg-yellow-50'}`}
              >
                <BedDouble size={32} className={`mb-3 ${bed.status === 'AVAILABLE' ? 'text-green-600' : bed.status === 'OCCUPIED' ? 'text-red-600' : 'text-yellow-600'}`} />
                <span className="font-bold text-gray-900">{bed.id}</span>
                {bed.patient ? (
                  <div className="mt-2 flex items-center gap-1 text-sm font-medium text-gray-700 bg-white/50 px-2 py-1 rounded">
                    <User size={14}/> {bed.patient}
                  </div>
                ) : (
                  <div className="mt-2 text-sm font-medium text-gray-500 uppercase tracking-wider">{bed.status}</div>
                )}
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
};
""")

# Update App.tsx Routing
path = "frontend/src/App.tsx"
with open(path, "r") as f:
    content = f.read()

# Add imports
imports = """
import { AdminDashboard } from './pages/dashboards/AdminDashboard';
import { PatientsList } from './pages/patients/PatientsList';
import { AppointmentsList } from './pages/appointments/AppointmentsList';
import { MedicalRecords } from './pages/records/MedicalRecords';
import { BedManagement } from './pages/admissions/BedManagement';
"""
content = content.replace("import { AdminDashboard } from './pages/dashboards/AdminDashboard';\nimport { PatientsList } from './pages/patients/PatientsList';", imports)

# Replace routes
content = content.replace('<Route path="/appointments" element={<div className="p-6">Appointments Module Coming Soon</div>} />', '<Route path="/appointments" element={<AppointmentsList />} />')
content = content.replace('<Route path="/records" element={<div className="p-6">Medical Records Module Coming Soon</div>} />', '<Route path="/records" element={<MedicalRecords />} />')
content = content.replace('<Route path="/admissions" element={<div className="p-6">Admissions & Beds Module Coming Soon</div>} />', '<Route path="/admissions" element={<BedManagement />} />')

with open(path, "w") as f:
    f.write(content)

print("Clinical and Ops UI generated successfully.")
