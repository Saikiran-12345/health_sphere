import React, { useState } from 'react';
import { Save, Building, Globe, Shield, Bell } from 'lucide-react';

export const SettingsPage = () => {
  const [saved, setSaved] = useState(false);
  const handleSave = () => { setSaved(true); setTimeout(() => setSaved(false), 3000); };

  return (
    <div>
      <div className="page-header"><div className="page-title"><h2>System Settings</h2><p>Configure hospital preferences and security</p></div></div>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
        <div className="data-table-container">
          <div className="table-header"><h3 style={{ display: 'flex', alignItems: 'center', gap: 8 }}><Building size={18} /> Hospital Information</h3></div>
          <div style={{ padding: '1.5rem' }}>
            <div className="form-group"><label>Hospital Name</label><input className="form-control" defaultValue="HealthSphere General Hospital" /></div>
            <div className="form-group"><label>Registration No.</label><input className="form-control" defaultValue="HOSP-KA-2024-08741" /></div>
          </div>
        </div>
        <div className="data-table-container">
          <div className="table-header"><h3 style={{ display: 'flex', alignItems: 'center', gap: 8 }}><Globe size={18} /> Preferences</h3></div>
          <div style={{ padding: '1.5rem' }}>
            <div className="form-group"><label>Timezone</label><select className="form-control"><option>Asia/Kolkata (IST +5:30)</option><option>UTC</option></select></div>
          </div>
        </div>
      </div>
      <div style={{ marginTop: '1.5rem', display: 'flex', gap: '1rem', alignItems: 'center' }}>
        <button className="btn btn-primary" onClick={handleSave}><Save size={16} /> Save All Settings</button>
        {saved && <span style={{ color: '#16a34a', fontWeight: 600 }}>Settings saved successfully!</span>}
      </div>
    </div>
  );
};
