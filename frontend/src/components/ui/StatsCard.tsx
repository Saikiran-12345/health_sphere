import React from 'react';
import { Card } from './Card';

interface StatsCardProps {
  title: string;
  value: string | number;
  icon: React.ReactNode;
  trend?: string;
  trendUp?: boolean;
}

export const StatsCard: React.FC<StatsCardProps> = ({ title, value, icon, trend, trendUp }) => (
  <Card className="flex items-center justify-between">
    <div>
      <p className="text-gray-500 text-sm font-medium uppercase tracking-wide">{title}</p>
      <h3 className="mt-2 text-3xl font-bold text-gray-900">{value}</h3>
      {trend && (
        <p className={`mt-2 text-sm font-medium ${trendUp ? 'text-green-600' : 'text-red-600'}`}>
          {trendUp ? '↑' : '↓'} {trend}
        </p>
      )}
    </div>
    <div className="p-4 bg-blue-50 text-blue-600 rounded-full">
      {icon}
    </div>
  </Card>
);
