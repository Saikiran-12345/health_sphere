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
