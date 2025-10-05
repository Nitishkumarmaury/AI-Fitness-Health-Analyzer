# Free Deployment Options for AI Fitness Health Analyzer

## 🚀 Quick Deploy Options

### 1. Railway (Recommended - Full Stack)
**Free tier**: 500 hours/month, $5 credit

1. **Push to GitHub** (use `push_to_github.bat`)
2. **Go to [Railway.app](https://railway.app)**
3. **Connect GitHub** and select your repository
4. **Add environment variable**: `GEMINI_API_KEY`
5. **Deploy automatically**

**One-click deploy:**
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/your-repo)

### 2. Render (Full Stack)
**Free tier**: 750 hours/month

1. **Push to GitHub**
2. **Go to [Render.com](https://render.com)**
3. **Create Web Service** from GitHub repo
4. **Build Command**: `pip install -r requirements.txt && cd frontend && npm install && npm run build`
5. **Start Command**: `gunicorn wsgi:app`
6. **Add environment variable**: `GEMINI_API_KEY`

### 3. Heroku (Full Stack)
**Free tier ended**, but still popular for learning

1. **Install Heroku CLI**
2. **Commands**:
   ```bash
   heroku create your-app-name
   heroku config:set GEMINI_API_KEY=your_key_here
   git push heroku main
   ```

### 4. Streamlit Cloud (Backend Only)
**Free tier**: Unlimited public apps

1. **Push to GitHub**
2. **Go to [share.streamlit.io](https://share.streamlit.io)**
3. **Connect repository**
4. **Main file**: `app.py`
5. **Add secrets**: `GEMINI_API_KEY = "your_key"`

### 5. Vercel (Full Stack with Serverless)
**Free tier**: 100GB bandwidth, 1000 serverless function invocations

1. **Push to GitHub**
2. **Go to [Vercel.com](https://vercel.com)**
3. **Import project**
4. **Add environment variable**: `GEMINI_API_KEY`
5. **Auto-deploy**

### 6. Netlify + Backend-as-a-Service
**Free tier**: 100GB bandwidth, 300 build minutes

**Frontend only** (use with external API):
1. **Build command**: `cd frontend && npm run build`
2. **Publish directory**: `frontend/build`

### 7. Google Cloud Platform (Free Tier)
**Free tier**: $300 credit + always free tier

**App Engine**:
```bash
gcloud app deploy app.yaml
```

**Cloud Run**:
```bash
gcloud run deploy --source .
```

## 🎯 Recommended Deployment Strategy

### For Beginners: Streamlit Cloud
- Easiest to deploy
- No configuration needed
- Perfect for demos

**Deploy command**:
```bash
python run_streamlit.py
```

### For Production: Railway
- Full-stack support
- Automatic deployments
- Good free tier
- PostgreSQL database included

### For Frontend-Heavy Apps: Vercel + Serverless
- Excellent React support
- Global CDN
- Serverless functions for API

## 📝 Pre-Deployment Checklist

- [ ] Push code to GitHub
- [ ] Add `.env` to `.gitignore` (already done)
- [ ] Set environment variables on platform
- [ ] Test build process locally
- [ ] Ensure frontend builds successfully
- [ ] Verify API endpoints work

## 🔧 Environment Variables Needed

For all platforms, add:
```
GEMINI_API_KEY=your_actual_api_key_here
```

## 🐛 Troubleshooting

### Common Issues:

1. **Build Fails**:
   ```bash
   # Local test
   cd frontend
   npm install
   npm run build
   ```

2. **Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Tesseract Issues**:
   - Railway/Render: Included in buildpack
   - Heroku: Add `heroku-buildpack-apt` buildpack

### Memory Issues:
If you hit memory limits, consider:
- Using Streamlit version (lighter)
- Reducing image processing complexity
- Using external image processing services

## 🌐 Live Demo URLs

After deployment, your app will be available at:
- Railway: `https://your-app-name.up.railway.app`
- Render: `https://your-app-name.onrender.com`
- Vercel: `https://your-app-name.vercel.app`
- Streamlit: `https://your-app-name.streamlit.app`
