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
