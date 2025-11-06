# WorkConnect Setup Guide

## Quick Start

### 1. Backend Setup
```bash
cd backend
pip install -r requirements.txt
python start.py
```

### 2. Frontend Setup
```bash
npm install
npm run dev
```

## Backend API Endpoints

- Health Check: `GET /health`
- Posts: `GET/POST /api/posts`
- User Profile: `GET /api/users/profile`
- Authentication: `POST /api/auth/login`, `POST /api/auth/register`

## Environment Variables

### Backend (.env in backend folder)
- `MONGODB_URI`: MongoDB connection string
- `JWT_SECRET_KEY`: JWT signing key
- `SECRET_KEY`: Flask secret key

### Frontend (.env in root folder)
- `VITE_API_URL`: Backend API URL (default: http://localhost:5000)

## Troubleshooting

### "Failed to fetch" errors:
1. Ensure backend server is running on port 5000
2. Check MongoDB connection
3. Verify CORS settings

### Posts not displaying:
1. Check authentication token in localStorage
2. Verify API endpoints are accessible
3. Check browser console for errors

### Database connection issues:
1. Verify MongoDB URI in backend/.env
2. Check network connectivity to MongoDB Atlas
3. Ensure database credentials are correct