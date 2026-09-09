import React from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';

export const AppointmentsScreen = () => {
  const appointments = [
    { id: '1', doc: 'Dr. Sarah Smith', date: 'Oct 12, 10:00 AM', status: 'Confirmed' },
    { id: '2', doc: 'Dr. Michael Chen', date: 'Oct 15, 02:30 PM', status: 'Scheduled' },
  ];

  return (
    <View style={styles.container}>
      <FlatList
        data={appointments}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <View style={styles.item}>
            <Text style={styles.doc}>{item.doc}</Text>
            <Text style={styles.date}>{item.date}</Text>
            <Text style={styles.status}>{item.status}</Text>
          </View>
        )}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, padding: 15, backgroundColor: '#f9fafb' },
  item: { backgroundColor: 'white', padding: 15, borderRadius: 8, marginBottom: 10, borderWidth: 1, borderColor: '#e5e7eb' },
  doc: { fontSize: 18, fontWeight: 'bold', color: '#111827' },
  date: { color: '#6b7280', marginVertical: 5 },
  status: { color: '#059669', fontWeight: '500' }
});
