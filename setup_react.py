import os
import subprocess
import sys
import platform

def create_directory(path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")
    else:
        print(f"Directory already exists: {path}")

def create_file(path, content):
    """Create file with specified content"""
    with open(path, 'w') as f:
        f.write(content)
    print(f"Created file: {path}")

def main():
    """Set up React frontend structure"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    frontend_dir = os.path.join(base_dir, "frontend")
    
    # Create frontend directory structure
    create_directory(frontend_dir)
    create_directory(os.path.join(frontend_dir, "public"))
    create_directory(os.path.join(frontend_dir, "src"))
    create_directory(os.path.join(frontend_dir, "src", "components"))
    create_directory(os.path.join(frontend_dir, "src", "pages"))
    
    # Create package.json
    package_json = """{
  "name": "ai-fitness-health-analyzer",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@emotion/react": "^11.11.1",
    "@emotion/styled": "^11.11.0",
    "@mui/icons-material": "^5.14.3",
    "@mui/material": "^5.14.5",
    "@testing-library/jest-dom": "^5.17.0",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "axios": "^1.4.0",
    "chart.js": "^4.3.3",
    "date-fns": "^2.30.0",
    "react": "^18.2.0",
    "react-chartjs-2": "^5.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.15.0",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "proxy": "http://localhost:5000"
}
"""
    create_file(os.path.join(frontend_dir, "package.json"), package_json)
    
    # Create public/index.html
    index_html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="AI Fitness Health Analyzer - Analyze your fitness data with AI"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
    />
    <title>AI Fitness Health Analyzer</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>
"""
    create_file(os.path.join(frontend_dir, "public", "index.html"), index_html)
    
    # Create manifest.json
    manifest_json = """{
  "short_name": "Fitness AI",
  "name": "AI Fitness Health Analyzer",
  "icons": [
    {
      "src": "favicon.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}
"""
    create_file(os.path.join(frontend_dir, "public", "manifest.json"), manifest_json)
    
    # Create src/index.js
    index_js = """import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
"""
    create_file(os.path.join(frontend_dir, "src", "index.js"), index_js)
    
    # Create src/index.css
    index_css = """body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}
"""
    create_file(os.path.join(frontend_dir, "src", "index.css"), index_css)
    
    # Create src/reportWebVitals.js
    report_web_vitals = """const reportWebVitals = (onPerfEntry) => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry);
      getFID(onPerfEntry);
      getFCP(onPerfEntry);
      getLCP(onPerfEntry);
      getTTFB(onPerfEntry);
    });
  }
};

export default reportWebVitals;
"""
    create_file(os.path.join(frontend_dir, "src", "reportWebVitals.js"), report_web_vitals)
    
    print("\nReact directory structure setup complete!")
    print("Next steps:")
    print("1. Create React components (App.js, Header.js, etc.)")
    print("2. Install dependencies with 'npm install' in the frontend directory")
    print("3. Run 'npm start' to start the development server or 'npm run build' to build for production")

if __name__ == "__main__":
    main()
