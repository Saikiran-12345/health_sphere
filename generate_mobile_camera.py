import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Update Mobile Dependencies for Camera and Image Picker
path_pkg = "mobile/package.json"
with open(path_pkg, "r") as f:
    pkg_content = f.read()

if "expo-camera" not in pkg_content:
    pkg_content = pkg_content.replace(
        '"axios": "^1.6.8"',
        '"axios": "^1.6.8",\n    "expo-camera": "~14.1.1",\n    "expo-image-picker": "~14.7.1"'
    )
    with open(path_pkg, "w") as f:
        f.write(pkg_content)

# 2. Build Camera Upload Screen
create_file('mobile/src/screens/DocumentUploadScreen.tsx', """
import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Image, Alert } from 'react-native';
import { Camera } from 'expo-camera';
import * as ImagePicker from 'expo-image-picker';

export const DocumentUploadScreen = ({ navigation }: any) => {
  const [hasPermission, setHasPermission] = useState<boolean | null>(null);
  const [imageUri, setImageUri] = useState<string | null>(null);
  const [isUploading, setIsUploading] = useState(false);

  useEffect(() => {
    (async () => {
      const { status } = await Camera.requestCameraPermissionsAsync();
      setHasPermission(status === 'granted');
    })();
  }, []);

  const pickImage = async () => {
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      aspect: [4, 3],
      quality: 1,
    });

    if (!result.canceled) {
      setImageUri(result.assets[0].uri);
    }
  };

  const handleUpload = () => {
    setIsUploading(true);
    // Simulate AWS S3 Multipart Upload
    setTimeout(() => {
      setIsUploading(false);
      Alert.alert("Success", "Document uploaded securely to HealthSphere S3 Vault.");
      setImageUri(null);
      navigation.goBack();
    }, 2000);
  };

  if (hasPermission === null) {
    return <View style={styles.container}><Text>Requesting camera permission...</Text></View>;
  }
  if (hasPermission === false) {
    return <View style={styles.container}><Text>No access to camera</Text></View>;
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Secure Document Upload</Text>
      <Text style={styles.subtitle}>Upload prescriptions, IDs, or lab results directly to your secure vault.</Text>
      
      {imageUri ? (
        <View style={styles.previewContainer}>
          <Image source={{ uri: imageUri }} style={styles.preview} />
          <TouchableOpacity style={styles.uploadButton} onPress={handleUpload} disabled={isUploading}>
            <Text style={styles.buttonText}>{isUploading ? "Encrypting & Uploading..." : "Upload to Vault"}</Text>
          </TouchableOpacity>
          <TouchableOpacity style={[styles.uploadButton, {backgroundColor: '#ef4444'}]} onPress={() => setImageUri(null)}>
            <Text style={styles.buttonText}>Retake Photo</Text>
          </TouchableOpacity>
        </View>
      ) : (
        <View style={styles.actionsContainer}>
          <TouchableOpacity style={styles.cameraButton} onPress={pickImage}>
            <Text style={styles.buttonText}>📸 Choose from Library</Text>
          </TouchableOpacity>
        </View>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: '#f9fafb' },
  title: { fontSize: 24, fontWeight: 'bold', color: '#111827', marginBottom: 10 },
  subtitle: { fontSize: 14, color: '#6b7280', marginBottom: 30 },
  actionsContainer: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  cameraButton: { backgroundColor: '#2563eb', padding: 20, borderRadius: 10, width: '100%', alignItems: 'center' },
  buttonText: { color: 'white', fontWeight: 'bold', fontSize: 16 },
  previewContainer: { flex: 1, alignItems: 'center' },
  preview: { width: '100%', height: 300, borderRadius: 10, marginBottom: 20 },
  uploadButton: { backgroundColor: '#10b981', padding: 15, borderRadius: 10, width: '100%', alignItems: 'center', marginBottom: 10 }
});
""")

# 3. Update Mobile App Navigation to include Upload Screen
path_app = "mobile/App.tsx"
with open(path_app, "r") as f:
    app_content = f.read()

if "DocumentUploadScreen" not in app_content:
    app_content = app_content.replace(
        "import { AppointmentsScreen } from './src/screens/AppointmentsScreen';",
        "import { AppointmentsScreen } from './src/screens/AppointmentsScreen';\nimport { DocumentUploadScreen } from './src/screens/DocumentUploadScreen';"
    )
    app_content = app_content.replace(
        '<Stack.Screen name="Appointments" component={AppointmentsScreen} />',
        '<Stack.Screen name="Appointments" component={AppointmentsScreen} />\n        <Stack.Screen name="DocumentUpload" component={DocumentUploadScreen} options={{ title: "Upload Vault" }} />'
    )
    with open(path_app, "w") as f:
        f.write(app_content)

# 4. Update Dashboard to Navigate to Upload
path_dash = "mobile/src/screens/PatientDashboardScreen.tsx"
with open(path_dash, "r") as f:
    dash_content = f.read()

if "DocumentUpload" not in dash_content:
    dash_content = dash_content.replace(
        "<TouchableOpacity style={styles.card}>",
        "<TouchableOpacity style={styles.card} onPress={() => navigation.navigate('DocumentUpload')}>",
        1 # Only replace the first generic card
    )
    dash_content = dash_content.replace("💊 Medications", "📁 Upload Docs")
    with open(path_dash, "w") as f:
        f.write(dash_content)

print("Mobile camera and upload flow generated.")
