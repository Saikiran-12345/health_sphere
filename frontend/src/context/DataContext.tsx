import React, { createContext, useContext, useState, useEffect } from 'react';

export interface Doctor {
  id: string;
  name: string;
  spec: string;
  dept: string;
  phone: string;
  email: string;
  status: string;
  patientsCount: number;
}

export interface Patient {
  id: string;
  name: string;
  age: number;
  gender: string;
  phone: string;
  blood: string;
  condition: string;
  doctor: string;
  admitted: string;
  status: string;
}

export interface Appointment {
  id: string;
  patient: string;
  doctor: string;
  dept: string;
  date: string;
  time: string;
  status: string;
}

interface DataContextType {
  doctors: Doctor[];
  patients: Patient[];
  appointments: Appointment[];
  addDoctor: (doc: Doctor) => void;
  addPatient: (pat: Patient) => void;
  addAppointment: (apt: Appointment) => void;
}

const initialDoctors: Doctor[] = [
  { id: 'DOC-101', name: 'Dr. Saikiran Reddy', spec: 'Cardiology', dept: 'Cardiology', phone: '+91 98765 11111', email: 'saikiran@healthsphere.com', status: 'Active', patientsCount: 142 },
  { id: 'DOC-102', name: 'Dr. Priya Nair', spec: 'Neurology', dept: 'Neurology', phone: '+91 98765 22222', email: 'priya@healthsphere.com', status: 'Active', patientsCount: 98 },
  { id: 'DOC-103', name: 'Dr. Neha Gupta', spec: 'Gynecology & Obstetrics', dept: 'Maternity', phone: '+91 98765 33333', email: 'neha@healthsphere.com', status: 'Active', patientsCount: 115 },
  { id: 'DOC-104', name: 'Dr. Amit Shah', spec: 'General Medicine & Dialysis', dept: 'General', phone: '+91 98765 44444', email: 'amit@healthsphere.com', status: 'Active', patientsCount: 160 },
  { id: 'DOC-105', name: 'Dr. Vikramaditya Rao', spec: 'Orthopedics & Surgery', dept: 'Surgery', phone: '+91 98765 55555', email: 'vikram@healthsphere.com', status: 'On Leave', patientsCount: 74 },
];

const initialPatients: Patient[] = [
  { id: 'P-1001', name: 'Arun Kumar', age: 45, gender: 'Male', phone: '+91 98765 43210', blood: 'O+', condition: 'Hypertension', doctor: 'Dr. Saikiran Reddy', admitted: '2024-01-15', status: 'admitted' },
  { id: 'P-1002', name: 'Priya Sharma', age: 32, gender: 'Female', phone: '+91 87654 32109', blood: 'A+', condition: 'Pregnancy (32 weeks)', doctor: 'Dr. Neha Gupta', admitted: '2024-01-18', status: 'admitted' },
  { id: 'P-1003', name: 'Raj Patel', age: 58, gender: 'Male', phone: '+91 76543 21098', blood: 'B+', condition: 'Type 2 Diabetes', doctor: 'Dr. Amit Shah', admitted: '-', status: 'outpatient' },
  { id: 'P-1004', name: 'Meera Reddy', age: 28, gender: 'Female', phone: '+91 65432 10987', blood: 'AB+', condition: 'Appendicitis', doctor: 'Dr. Saikiran Reddy', admitted: '2024-01-20', status: 'discharged' },
  { id: 'P-1005', name: 'Vikram Singh', age: 67, gender: 'Male', phone: '+91 54321 09876', blood: 'O-', condition: 'Coronary Artery Disease', doctor: 'Dr. Priya Nair', admitted: '2024-01-12', status: 'critical' },
  { id: 'P-1006', name: 'Sunita Rao', age: 41, gender: 'Female', phone: '+91 43210 98765', blood: 'A-', condition: 'Migraine', doctor: 'Dr. Neha Gupta', admitted: '-', status: 'outpatient' },
  { id: 'P-1007', name: 'Deepak Mishra', age: 53, gender: 'Male', phone: '+91 32109 87654', blood: 'B-', condition: 'Chronic Kidney Disease', doctor: 'Dr. Amit Shah', admitted: '2024-01-19', status: 'admitted' },
  { id: 'P-1008', name: 'Latha Krishnan', age: 36, gender: 'Female', phone: '+91 21098 76543', blood: 'AB-', condition: 'Thyroid Disorder', doctor: 'Dr. Priya Nair', admitted: '-', status: 'outpatient' },
];

const initialAppointments: Appointment[] = [
  { id: 'APT-301', patient: 'Anita Desai', doctor: 'Dr. Saikiran Reddy', dept: 'Cardiology', date: '2024-01-22', time: '9:00 AM', status: 'confirmed' },
  { id: 'APT-302', patient: 'Rahul Verma', doctor: 'Dr. Priya Nair', dept: 'Neurology', date: '2024-01-22', time: '9:30 AM', status: 'confirmed' },
  { id: 'APT-303', patient: 'Kiran Joshi', doctor: 'Dr. Saikiran Reddy', dept: 'Cardiology', date: '2024-01-22', time: '10:00 AM', status: 'in_progress' },
  { id: 'APT-304', patient: 'Sunita Rao', doctor: 'Dr. Amit Shah', dept: 'General', date: '2024-01-22', time: '10:30 AM', status: 'scheduled' },
  { id: 'APT-305', patient: 'Deepak Mishra', doctor: 'Dr. Neha Gupta', dept: 'Oncology', date: '2024-01-22', time: '11:00 AM', status: 'scheduled' },
  { id: 'APT-306', patient: 'Latha Krishnan', doctor: 'Dr. Priya Nair', dept: 'Neurology', date: '2024-01-22', time: '11:30 AM', status: 'completed' },
  { id: 'APT-307', patient: 'Pooja Thakur', doctor: 'Dr. Saikiran Reddy', dept: 'Cardiology', date: '2024-01-22', time: '2:00 PM', status: 'cancelled' },
];

const DataContext = createContext<DataContextType>({
  doctors: [],
  patients: [],
  appointments: [],
  addDoctor: () => {},
  addPatient: () => {},
  addAppointment: () => {},
});

export const useHospitalData = () => useContext(DataContext);

export const DataProvider = ({ children }: { children: React.ReactNode }) => {
  const [doctors, setDoctors] = useState<Doctor[]>(() => {
    const s = localStorage.getItem('hs_doctors');
    return s ? JSON.parse(s) : initialDoctors;
  });

  const [patients, setPatients] = useState<Patient[]>(() => {
    const s = localStorage.getItem('hs_patients');
    return s ? JSON.parse(s) : initialPatients;
  });

  const [appointments, setAppointments] = useState<Appointment[]>(() => {
    const s = localStorage.getItem('hs_appointments');
    return s ? JSON.parse(s) : initialAppointments;
  });

  useEffect(() => { localStorage.setItem('hs_doctors', JSON.stringify(doctors)); }, [doctors]);
  useEffect(() => { localStorage.setItem('hs_patients', JSON.stringify(patients)); }, [patients]);
  useEffect(() => { localStorage.setItem('hs_appointments', JSON.stringify(appointments)); }, [appointments]);

  const addDoctor = (doc: Doctor) => setDoctors(prev => [doc, ...prev]);
  const addPatient = (pat: Patient) => setPatients(prev => [pat, ...prev]);
  const addAppointment = (apt: Appointment) => setAppointments(prev => [apt, ...prev]);

  return (
    <DataContext.Provider value={{ doctors, patients, appointments, addDoctor, addPatient, addAppointment }}>
      {children}
    </DataContext.Provider>
  );
};
