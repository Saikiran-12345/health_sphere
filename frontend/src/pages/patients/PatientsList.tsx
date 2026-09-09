import React, { useState, useEffect } from 'react';
import { Search, Plus, Filter, MoreVertical, Edit, Trash, FileText } from 'lucide-react';
import axios from 'axios';

interface Patient {
  id: string;
  first_name: string;
  last_name: string;
  date_of_birth: string;
  gender: string;
  blood_group: string;
  phone_number: string;
}

export const PatientsList: React.FC = () => {
  const [patients, setPatients] = useState<Patient[]>([]);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    // In a real app, fetch from /api/patients
    setPatients([
      { id: '1', first_name: 'John', last_name: 'Doe', date_of_birth: '1980-05-15', gender: 'Male', blood_group: 'O+', phone_number: '+1234567890' },
      { id: '2', first_name: 'Jane', last_name: 'Smith', date_of_birth: '1992-11-22', gender: 'Female', blood_group: 'A-', phone_number: '+0987654321' },
      { id: '3', first_name: 'Alice', last_name: 'Johnson', date_of_birth: '1975-03-08', gender: 'Female', blood_group: 'B+', phone_number: '+1122334455' },
    ]);
  }, []);

  return (
    <div className="bg-white rounded-lg shadow h-full flex flex-col">
      <div className="p-6 border-b border-gray-200 flex justify-between items-center">
        <h2 className="text-2xl font-bold text-gray-800">Patient Directory</h2>
        <button className="flex items-center gap-2 bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
          <Plus size={18} /> New Patient
        </button>
      </div>
      
      <div className="p-4 border-b border-gray-200 bg-gray-50 flex gap-4">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={18} />
          <input 
            type="text" 
            placeholder="Search patients by name, ID, or phone..." 
            className="w-full pl-10 pr-4 py-2 border rounded-md focus:ring-2 focus:ring-blue-500"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>
        <button className="flex items-center gap-2 px-4 py-2 border rounded-md bg-white hover:bg-gray-50">
          <Filter size={18} /> Filters
        </button>
      </div>

      <div className="flex-1 overflow-auto">
        <table className="w-full text-left border-collapse">
          <thead>
            <tr className="bg-gray-50 text-gray-600 text-sm uppercase tracking-wider">
              <th className="p-4 font-semibold border-b">Name</th>
              <th className="p-4 font-semibold border-b">ID</th>
              <th className="p-4 font-semibold border-b">DOB</th>
              <th className="p-4 font-semibold border-b">Gender</th>
              <th className="p-4 font-semibold border-b">Blood Group</th>
              <th className="p-4 font-semibold border-b">Contact</th>
              <th className="p-4 font-semibold border-b text-right">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {patients.map((patient) => (
              <tr key={patient.id} className="hover:bg-gray-50 transition-colors">
                <td className="p-4 font-medium text-gray-900">{patient.first_name} {patient.last_name}</td>
                <td className="p-4 text-gray-500 text-sm">PAT-{patient.id.padStart(5, '0')}</td>
                <td className="p-4 text-gray-600">{patient.date_of_birth}</td>
                <td className="p-4 text-gray-600">{patient.gender}</td>
                <td className="p-4">
                  <span className="px-2 py-1 bg-red-100 text-red-800 rounded-full text-xs font-bold">{patient.blood_group}</span>
                </td>
                <td className="p-4 text-gray-600">{patient.phone_number}</td>
                <td className="p-4 flex justify-end gap-3 text-gray-400">
                  <button className="hover:text-blue-600" title="View Records"><FileText size={18} /></button>
                  <button className="hover:text-green-600" title="Edit"><Edit size={18} /></button>
                  <button className="hover:text-red-600" title="Delete"><Trash size={18} /></button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
