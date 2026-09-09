import React from 'react';
import { Activity, Shield, Users, ArrowRight, HeartPulse, Stethoscope, Clock } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export const LandingPage = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-slate-50 font-sans selection:bg-blue-200">
      {/* Navigation */}
      <nav className="flex items-center justify-between px-8 py-6 max-w-7xl mx-auto">
        <div className="flex items-center gap-2">
          <Activity className="text-blue-600 w-8 h-8" />
          <span className="text-2xl font-black text-slate-900 tracking-tight">HealthSphere</span>
        </div>
        <div className="hidden md:flex items-center gap-8 text-sm font-semibold text-slate-600">
          <a href="#features" className="hover:text-blue-600 transition-colors">Features</a>
          <a href="#solutions" className="hover:text-blue-600 transition-colors">Solutions</a>
          <a href="#about" className="hover:text-blue-600 transition-colors">About</a>
        </div>
        <div className="flex items-center gap-4">
          <button 
            onClick={() => navigate('/login')}
            className="text-sm font-bold text-blue-600 hover:text-blue-700 px-4 py-2"
          >
            Sign In
          </button>
          <button 
            onClick={() => navigate('/dashboard')}
            className="text-sm font-bold bg-blue-600 text-white px-6 py-2.5 rounded-full hover:bg-blue-700 transition-all shadow-lg shadow-blue-200"
          >
            Enter Dashboard
          </button>
        </div>
      </nav>

      {/* Hero Section */}
      <header className="relative pt-20 pb-32 overflow-hidden">
        <div className="max-w-7xl mx-auto px-8 relative z-10 text-center">
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-blue-50 text-blue-600 text-sm font-bold mb-8 border border-blue-100">
            <span className="flex h-2 w-2 rounded-full bg-blue-600 animate-pulse"></span>
            Enterprise Medical OS 2.0 is Live
          </div>
          <h1 className="text-6xl md:text-7xl font-black text-slate-900 tracking-tight leading-tight mb-8 max-w-4xl mx-auto">
            The intelligent operating system for <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500">modern hospitals.</span>
          </h1>
          <p className="text-xl text-slate-600 mb-12 max-w-2xl mx-auto leading-relaxed">
            Unify your clinical workflows, AI risk predictions, pharmacy inventory, and telemedicine into one ridiculously fast platform.
          </p>
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <button 
              onClick={() => navigate('/dashboard')}
              className="flex items-center gap-2 bg-slate-900 text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-slate-800 transition-all shadow-xl hover:shadow-2xl hover:-translate-y-1"
            >
              Launch Platform <ArrowRight className="w-5 h-5" />
            </button>
            <button className="flex items-center gap-2 bg-white text-slate-900 border-2 border-slate-200 px-8 py-4 rounded-full font-bold text-lg hover:border-slate-300 transition-all">
              Book a Demo
            </button>
          </div>
        </div>
      </header>

      {/* Features Grid */}
      <section id="features" className="py-24 bg-white">
        <div className="max-w-7xl mx-auto px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-black text-slate-900 mb-4">Everything you need to run a hospital.</h2>
            <p className="text-lg text-slate-500">Built for doctors, administrators, and patients.</p>
          </div>
          
          <div className="grid md:grid-cols-3 gap-8">
            <div className="p-8 rounded-3xl bg-slate-50 border border-slate-100 hover:shadow-xl transition-all group">
              <div className="w-14 h-14 bg-blue-100 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                <HeartPulse className="text-blue-600 w-7 h-7" />
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">AI Risk Engine</h3>
              <p className="text-slate-600 leading-relaxed">Predict patient readmission risks and operational anomalies using our integrated Scikit-learn random forest models.</p>
            </div>
            
            <div className="p-8 rounded-3xl bg-slate-50 border border-slate-100 hover:shadow-xl transition-all group">
              <div className="w-14 h-14 bg-emerald-100 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                <Stethoscope className="text-emerald-600 w-7 h-7" />
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">Complete EMR</h3>
              <p className="text-slate-600 leading-relaxed">A lightning-fast clinical timeline for tracking prescriptions, lab results, and physician notes securely.</p>
            </div>
            
            <div className="p-8 rounded-3xl bg-slate-50 border border-slate-100 hover:shadow-xl transition-all group">
              <div className="w-14 h-14 bg-purple-100 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                <Clock className="text-purple-600 w-7 h-7" />
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">Real-time Telemedicine</h3>
              <p className="text-slate-600 leading-relaxed">Conduct remote video consultations with integrated WebSockets and live clinical chat environments.</p>
            </div>
          </div>
        </div>
      </section>
      
      {/* Footer */}
      <footer className="bg-slate-900 py-12 text-center text-slate-400">
        <div className="flex items-center justify-center gap-2 mb-4">
          <Activity className="text-blue-500 w-6 h-6" />
          <span className="text-xl font-black text-white tracking-tight">HealthSphere</span>
        </div>
        <p>© 2026 HealthSphere Enterprise Inc. All rights reserved.</p>
      </footer>
    </div>
  );
};
