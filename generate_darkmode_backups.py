import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Frontend: Theme Provider (Dark Mode)
create_file('frontend/src/theme/ThemeProvider.tsx', """
import React, { createContext, useContext, useEffect, useState } from 'react';

type Theme = 'dark' | 'light' | 'system';

type ThemeProviderProps = {
  children: React.ReactNode;
  defaultTheme?: Theme;
  storageKey?: string;
};

type ThemeProviderState = {
  theme: Theme;
  setTheme: (theme: Theme) => void;
};

const initialState: ThemeProviderState = {
  theme: 'system',
  setTheme: () => null,
};

const ThemeProviderContext = createContext<ThemeProviderState>(initialState);

export function ThemeProvider({
  children,
  defaultTheme = 'system',
  storageKey = 'healthsphere-ui-theme',
  ...props
}: ThemeProviderProps) {
  const [theme, setTheme] = useState<Theme>(
    () => (localStorage.getItem(storageKey) as Theme) || defaultTheme
  );

  useEffect(() => {
    const root = window.document.documentElement;
    root.classList.remove('light', 'dark');

    if (theme === 'system') {
      const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
      root.classList.add(systemTheme);
      return;
    }
    root.classList.add(theme);
  }, [theme]);

  const value = {
    theme,
    setTheme: (theme: Theme) => {
      localStorage.setItem(storageKey, theme);
      setTheme(theme);
    },
  };

  return (
    <ThemeProviderContext.Provider {...props} value={value}>
      {children}
    </ThemeProviderContext.Provider>
  );
}

export const useTheme = () => {
  const context = useContext(ThemeProviderContext);
  if (context === undefined) throw new Error('useTheme must be used within a ThemeProvider');
  return context;
};
""")

# 2. Update App.tsx to include ThemeProvider
path_app = "frontend/src/App.tsx"
with open(path_app, "r") as f:
    app_content = f.read()

if "ThemeProvider" not in app_content:
    app_content = app_content.replace(
        "import { AuthProvider } from './auth/AuthProvider';",
        "import { AuthProvider } from './auth/AuthProvider';\nimport { ThemeProvider } from './theme/ThemeProvider';"
    )
    app_content = app_content.replace(
        "<AuthProvider>",
        "<ThemeProvider defaultTheme=\"light\" storageKey=\"healthsphere-theme\">\n    <AuthProvider>"
    )
    app_content = app_content.replace(
        "</AuthProvider>",
        "</AuthProvider>\n    </ThemeProvider>"
    )
    with open(path_app, "w") as f:
        f.write(app_content)

# 3. Update Dashboard to include Theme Toggle
path_dash = "frontend/src/layouts/DashboardLayout.tsx"
with open(path_dash, "r") as f:
    dash_content = f.read()

if "useTheme" not in dash_content:
    dash_content = dash_content.replace(
        "import { useAuth } from '../auth/AuthProvider';",
        "import { useAuth } from '../auth/AuthProvider';\nimport { useTheme } from '../theme/ThemeProvider';\nimport { Moon, Sun } from 'lucide-react';"
    )
    dash_content = dash_content.replace(
        "const { user, logout } = useAuth();",
        "const { user, logout } = useAuth();\n  const { theme, setTheme } = useTheme();"
    )
    # Inject Theme Toggle Button near the Bell icon
    toggle_html = """
            <button 
              onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
              className="text-slate-400 hover:text-slate-600 dark:hover:text-slate-300 transition-colors"
            >
              {theme === 'dark' ? <Sun size={20} /> : <Moon size={20} />}
            </button>
    """
    dash_content = dash_content.replace(
        "<button className=\"relative text-slate-400 hover:text-slate-600 transition-colors\">",
        toggle_html + "\n            <button className=\"relative text-slate-400 hover:text-slate-600 transition-colors\">"
    )
    with open(path_dash, "w") as f:
        f.write(dash_content)

# 4. Backend: Automated Database Backups Script
create_file('backend/scripts/backup_db.py', """
import os
import subprocess
from datetime import datetime
import boto3
from botocore.exceptions import NoCredentialsError

# Configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "healthsphere")
DB_USER = os.getenv("DB_USER", "postgres")
S3_BUCKET = os.getenv("S3_BACKUP_BUCKET", "healthsphere-db-backups")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

def backup_postgres():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f"healthsphere_backup_{timestamp}.sql"
    
    print(f"Starting database backup to {backup_file}...")
    
    try:
        # Run pg_dump
        subprocess.run(
            ['pg_dump', '-h', DB_HOST, '-U', DB_USER, '-F', 'c', '-b', '-v', '-f', backup_file, DB_NAME],
            check=True,
            env=dict(os.environ, PGPASSWORD=os.getenv("DB_PASSWORD", "postgres"))
        )
        print("Backup created successfully.")
        return backup_file
    except subprocess.CalledProcessError as e:
        print(f"Error during backup: {e}")
        return None

def upload_to_s3(file_name):
    s3 = boto3.client('s3', region_name=AWS_REGION)
    try:
        print(f"Uploading {file_name} to S3 bucket {S3_BUCKET}...")
        s3.upload_file(file_name, S3_BUCKET, file_name)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available for AWS S3")
        return False

if __name__ == "__main__":
    file = backup_postgres()
    if file:
        success = upload_to_s3(file)
        if success:
            os.remove(file) # Clean up local file after S3 upload
            print("Backup process completely finished.")
""")

print("Dark mode and backup systems generated.")
