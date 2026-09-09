
import React, {useState, useEffect} from 'react';
import { Search, Plus, Edit, Trash2 } from 'lucide-react';

export const Waste_managementDashboard = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setTimeout(() => {
      setData([]);
      setLoading(false);
    }, 1000);
  }, []);

  return (
    <div className="p-8 w-full h-full">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-slate-800">Waste_management Management System</h1>
      </div>
      <div className="mt-8 bg-white p-6 rounded-xl shadow-sm border border-slate-200">
        <h2 className="text-xl font-bold mb-4">Detailed Edit Form</h2>
        <div className="grid grid-cols-3 gap-4">
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 1</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 2</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 3</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 4</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 5</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 6</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 7</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 8</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 9</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 10</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 11</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 12</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 13</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 14</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 15</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 16</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 17</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 18</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 19</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 20</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 21</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 22</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 23</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 24</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 25</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 26</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 27</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 28</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 29</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 30</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 31</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 32</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 33</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 34</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 35</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 36</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 37</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 38</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 39</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 40</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 41</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 42</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 43</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 44</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 45</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 46</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 47</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 48</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 49</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>
          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field 50</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>

        </div>
      </div>
    </div>
  );
};
