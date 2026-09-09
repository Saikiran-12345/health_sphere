import React, { useState, createContext, useContext } from 'react';
import { CheckCircle, AlertTriangle, XCircle, X, Info } from 'lucide-react';

interface ToastItem {
  id: number;
  message: string;
  type: 'success' | 'error' | 'warning' | 'info';
}

interface ToastContextType {
  showToast: (message: string, type?: 'success' | 'error' | 'warning' | 'info') => void;
}

const ToastContext = createContext<ToastContextType>({ showToast: () => {} });
export const useToast = () => useContext(ToastContext);

const icons: any = { success: CheckCircle, error: XCircle, warning: AlertTriangle, info: Info };
const colors: any = {
  success: { bg: '#dcfce7', border: '#bbf7d0', color: '#16a34a' },
  error: { bg: '#fee2e2', border: '#fecaca', color: '#dc2626' },
  warning: { bg: '#fef3c7', border: '#fde68a', color: '#d97706' },
  info: { bg: '#e0f2fe', border: '#bae6fd', color: '#0284c7' },
};

export const ToastProvider = ({ children }: { children: React.ReactNode }) => {
  const [toasts, setToasts] = useState<ToastItem[]>([]);
  let counter = 0;

  const showToast = (message: string, type: 'success' | 'error' | 'warning' | 'info' = 'success') => {
    const id = Date.now() + (counter++);
    setToasts(prev => [...prev, { id, message, type }]);
    setTimeout(() => setToasts(prev => prev.filter(t => t.id !== id)), 4000);
  };

  const dismiss = (id: number) => setToasts(prev => prev.filter(t => t.id !== id));

  return (
    <ToastContext.Provider value={{ showToast }}>
      {children}
      <div style={{ position: 'fixed', top: 20, right: 20, zIndex: 9999, display: 'flex', flexDirection: 'column', gap: 8 }}>
        {toasts.map(toast => {
          const Icon = icons[toast.type];
          const c = colors[toast.type];
          return (
            <div key={toast.id} style={{
              display: 'flex', alignItems: 'center', gap: '0.75rem',
              padding: '0.85rem 1.25rem', borderRadius: 8,
              background: c.bg, border: '1px solid ' + c.border,
              boxShadow: '0 4px 12px rgba(0,0,0,0.1)',
              animation: 'slideIn 0.3s ease-out',
              minWidth: 300, maxWidth: 420
            }}>
              <Icon size={18} style={{ color: c.color, flexShrink: 0 }} />
              <span style={{ flex: 1, fontSize: '0.9rem', fontWeight: 500, color: '#1e293b' }}>{toast.message}</span>
              <button onClick={() => dismiss(toast.id)} style={{ background: 'none', border: 'none', cursor: 'pointer', color: '#94a3b8', padding: 2 }}><X size={16} /></button>
            </div>
          );
        })}
      </div>
    </ToastContext.Provider>
  );
};
