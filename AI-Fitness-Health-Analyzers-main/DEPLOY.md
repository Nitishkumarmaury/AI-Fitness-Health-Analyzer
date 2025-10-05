# 🚀 Deployment Guide

## Quick Deploy to GitHub

Run this command to push everything to GitHub:

```bash
deploy_github.bat
```

## Free Deployment Options

### 1. 🎯 Streamlit Cloud (Recommended - Easiest)

**Steps:**
1. Push to GitHub using `deploy_github.bat`
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select your repository: `AI-Fitness-Health-Analyzers`
5. Set main file path: `app.py`
6. Add your secrets:
   ```
   GEMINI_API_KEY = "your_actual_api_key_here"
   ```
7. Deploy!

**Live URL:** `https://ai-fitness-analyzer.streamlit.app`

### 2. 🚂 Railway (Full Stack)

**Steps:**
1. Go to [railway.app](https://railway.app)
2. Connect GitHub and select your repo
3. Add environment variable:
   - `GEMINI_API_KEY`: your_api_key_here
4. Deploy automatically

**Live URL:** `https://ai-fitness-analyzer.up.railway.app`

### 3. ⚡ Vercel (Serverless)

**Steps:**
1. Go to [vercel.com](https://vercel.com)
2. Import project from GitHub
3. Add environment variable:
   - `GEMINI_API_KEY`: your_api_key_here
4. Deploy

**Live URL:** `https://ai-fitness-analyzer.vercel.app`

### 4. 🌐 Netlify (Frontend + Functions)

**Steps:**
1. Go to [netlify.com](https://netlify.com)
2. Connect GitHub repo
3. Build command: `cd frontend && npm run build`
4. Publish directory: `frontend/build`
5. Add environment variable: `GEMINI_API_KEY`

### 5. ☁️ Google Cloud Platform

**Steps:**
1. Install Google Cloud CLI
2. Run: `gcloud app deploy app.yaml`
3. Edit `app.yaml` with your API key

## Environment Variables Needed

For all platforms, you need:
```
GEMINI_API_KEY=your_actual_google_gemini_api_key
```

## Troubleshooting

### Build Fails
- Check if all dependencies are in `requirements.txt`
- Verify Node.js version (use Node 18+)
- Check frontend build: `cd frontend && npm run build`

### API Key Issues
- Make sure API key is valid
- Check environment variable name matches exactly
- For Streamlit: use secrets.toml format

### Memory Issues
- Use Streamlit version for lighter deployment
- Railway and Vercel have generous free tiers
- Consider reducing image processing complexity

## Post-Deployment

1. Test all functionality
2. Add custom domain (if needed)
3. Set up monitoring
4. Update README with live demo links
