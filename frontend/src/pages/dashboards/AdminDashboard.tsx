import React from 'react';
import { StatsCard } from '../../components/ui/StatsCard';
import { Users, Calendar, Activity, Bed } from 'lucide-react';
import { ResponsiveContainer, AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';

const dummyChartData = [
  { name: 'Mon', admissions: 12, appointments: 45 },
  { name: 'Tue', admissions: 19, appointments: 52 },
  { name: 'Wed', admissions: 15, appointments: 38 },
  { name: 'Thu', admissions: 22, appointments: 65 },
  { name: 'Fri', admissions: 18, appointments: 48 },
  { name: 'Sat', admissions: 8, appointments: 25 },
  { name: 'Sun', admissions: 5, appointments: 15 },
];

export const AdminDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-gray-800">Hospital Administration</h2>
      
      {/* Top Stats */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <StatsCard title="Total Patients" value="12,450" icon={<Users size={24} />} trend="12% from last month" trendUp={true} />
        <StatsCard title="Today's Appointments" value="142" icon={<Calendar size={24} />} trend="4% from yesterday" trendUp={true} />
        <StatsCard title="Current Admissions" value="89" icon={<Bed size={24} />} trend="2% from last week" trendUp={false} />
        <StatsCard title="AI Risk Alerts" value="7" icon={<Activity size={24} />} trend="High priority" trendUp={false} />
      </div>

      {/* Analytics Chart */}
      <div className="bg-white p-6 rounded-lg shadow">
        <h3 className="text-lg font-bold text-gray-800 mb-4">Weekly Operational Overview</h3>
        <div className="h-80">
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={dummyChartData}>
              <defs>
                <linearGradient id="colorAppts" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.8}/>
                  <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" vertical={false} />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Area type="monotone" dataKey="appointments" stroke="#3b82f6" fillOpacity={1} fill="url(#colorAppts)" />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
};
