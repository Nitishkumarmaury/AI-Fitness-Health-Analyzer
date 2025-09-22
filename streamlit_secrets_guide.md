# 🔐 How to Add Secret Keys in Streamlit Cloud

## Method 1: Streamlit Cloud Dashboard (Recommended)

### Step 1: Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository: `AI-Fitness-Health-Analyzers`
5. Set main file path: `app.py`

### Step 2: Add Secrets
1. **Before deploying**, click "Advanced settings"
2. In the "Secrets" section, add your API key in TOML format:
   ```toml
   GEMINI_API_KEY = "your_actual_api_key_here"
   ```
3. Click "Deploy!"

### Step 3: Add Secrets to Existing App
If your app is already deployed:
1. Go to your app dashboard
2. Click the "⚙️ Settings" button (gear icon)
3. Go to "Secrets" tab
4. Add your secrets in TOML format:
   ```toml
   GEMINI_API_KEY = "AIzaSyCmCit_f6F6EBC6yEIeith1apjJ8AH3rWY"
   ```
5. Click "Save"

## Method 2: Local Development with .streamlit/secrets.toml

### Step 1: Create Secrets File
Create `.streamlit/secrets.toml` in your project root:
```toml
GEMINI_API_KEY = "your_api_key_here"
```

### Step 2: Access Secrets in Code
```python
import streamlit as st

# Access secrets
api_key = st.secrets["GEMINI_API_KEY"]
```

## Method 3: Environment Variables (Alternative)

### For Local Development:
```bash
# Windows
set GEMINI_API_KEY=your_api_key_here

# macOS/Linux
export GEMINI_API_KEY=your_api_key_here
```

### For Streamlit Cloud:
Use the dashboard method above - it's more secure.

## 🔄 Complete Deployment Process

### Quick Commands:
```bash
# 1. Push to GitHub
repush_to_github.bat

# 2. Test locally first
python run_streamlit.py
```

### Streamlit Cloud Setup:
1. **Repository**: https://github.com/Nitishkumarmaury/AI-Fitness-Health-Analyzers
2. **Main file**: `app.py`
3. **Python version**: 3.11
4. **Secrets format**:
   ```toml
   GEMINI_API_KEY = "AIzaSyCmCit_f6F6EBC6yEIeith1apjJ8AH3rWY"
   ```

## 🚨 Security Best Practices

### ✅ DO:
- Use Streamlit Cloud secrets dashboard
- Keep API keys in `.streamlit/secrets.toml` for local dev
- Add `.streamlit/secrets.toml` to `.gitignore`

### ❌ DON'T:
- Put real API keys in code
- Commit secrets to GitHub
- Share API keys in public

## 🎯 Quick Deploy Links

1. **Streamlit Cloud**: [share.streamlit.io](https://share.streamlit.io)
2. **Your Repo**: [GitHub Repository](https://github.com/Nitishkumarmaury/AI-Fitness-Health-Analyzers)
3. **Railway**: [railway.app](https://railway.app)
4. **Vercel**: [vercel.com](https://vercel.com)
