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
