import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { LoginScreen } from './src/screens/LoginScreen';
import { PatientDashboardScreen } from './src/screens/PatientDashboardScreen';
import { AppointmentsScreen } from './src/screens/AppointmentsScreen';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen name="Login" component={LoginScreen} options={{ headerShown: false }} />
        <Stack.Screen name="PatientDashboard" component={PatientDashboardScreen} options={{ title: 'HealthSphere' }} />
        <Stack.Screen name="Appointments" component={AppointmentsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
