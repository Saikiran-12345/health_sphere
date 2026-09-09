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
