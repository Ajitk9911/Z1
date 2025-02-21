Image Resizer & Publisher App 📸
Overview
This is a web application that allows users to upload an image, automatically resize it into multiple predefined sizes, and publish it on X (formerly Twitter).

Features
✅ Upload an image (PNG, JPG, JPEG)
✅ Resize image into 300x250, 728x90, 160x600, 300x600
✅ Publish resized images to X (Twitter)
✅ Secure authentication using Twitter API
✅ Works on Desktop & Mobile

Tech Stack
Frontend: Streamlit
Backend: FastAPI
Image Processing: Pillow
Twitter API: Tweepy
Deployment: Streamlit Sharing, Render
Installation & Setup
Step 1: Clone the Repository

git clone https://github.com/yourusername/image-resizer-app.git
cd image-resizer-app

Step 2: Setup Backend (FastAPI)

cd backend
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
uvicorn main:app --reload

Backend Running at: http://127.0.0.1:8000
Test API Docs: http://127.0.0.1:8000/docs


Step 3: Setup Frontend (Streamlit)


cd ../frontend
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
streamlit run app.py


Frontend Running at: http://localhost:8501

Usage
Upload an image in the frontend UI.
The backend resizes the image into predefined dimensions.
Optionally, post images to X (Twitter) after authentication.
Twitter API Integration
To enable Twitter posting:

Get Twitter API keys from developer.twitter.com.
Add your API keys in backend/twitter_api.py:

Run backend and authenticate users before posting.

Deployment
Backend: Deploy on Render/Vercel
Frontend: Deploy on Streamlit Sharing
