import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet, ScrollView } from 'react-native';

export const PatientDashboardScreen = ({ navigation }: any) => {
  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.welcome}>Welcome back, John!</Text>
        <Text style={styles.subtitle}>Patient ID: PAT-00123</Text>
      </View>
      
      <View style={styles.grid}>
        <TouchableOpacity style={styles.card} onPress={() => navigation.navigate('Appointments')}>
          <Text style={styles.cardTitle}>📅 Appointments</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.card} onPress={() => navigation.navigate('DocumentUpload')}>
          <Text style={styles.cardTitle}>💊 Medications</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.card}>
          <Text style={styles.cardTitle}>🔬 Lab Results</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.card}>
          <Text style={styles.cardTitle}>📹 Telemedicine</Text>
        </TouchableOpacity>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f3f4f6' },
  header: { padding: 20, backgroundColor: '#2563eb' },
  welcome: { fontSize: 24, fontWeight: 'bold', color: 'white' },
  subtitle: { color: '#bfdbfe', marginTop: 5 },
  grid: { padding: 15, flexDirection: 'row', flexWrap: 'wrap', justifyContent: 'space-between' },
  card: { backgroundColor: 'white', width: '48%', padding: 20, borderRadius: 10, marginBottom: 15, shadowColor: '#000', shadowOpacity: 0.1, shadowRadius: 5, elevation: 3 },
  cardTitle: { fontSize: 16, fontWeight: '600', color: '#1f2937' }
});
