# WorkConnect MongoDB Setup Guide

## Current Status ✅

Your WorkConnect application is **successfully connected** to MongoDB! Here's what we've verified:

- ✅ Backend Flask application starts correctly
- ✅ MongoDB connection is established
- ✅ API endpoints are responding
- ✅ Database operations work (read/write/delete)

## MongoDB Connection Details

**Database:** `workconnect`  
**Connection URI:** `mongodb+srv://varuabi005_db_user:varuabi005_db_user@workconnect.tb2qc4j.mongodb.net/?retryWrites=true&w=majority&appName=workconnect`

## Commands to Start Your Application

### 1. Start Backend Server

```bash
# Navigate to project directory
cd c:\Users\ABINAYA\OneDrive\Desktop\WorkConnect_Proj\workflow-ai-77-main

# Start backend (Option 1 - using batch file)
start_backend_server.bat

# OR Start backend (Option 2 - manual)
cd backend
python app.py
```

The backend will be available at:
- **Main API:** http://localhost:5000
- **Health Check:** http://localhost:5000/health
- **API Endpoints:** http://localhost:5000/api/

### 2. Start Frontend

```bash
# In a new terminal, navigate to project root
cd c:\Users\ABINAYA\OneDrive\Desktop\WorkConnect_Proj\workflow-ai-77-main

# Install dependencies (if not done already)
npm install

# Start frontend development server
npm run dev
```

The frontend will be available at: http://localhost:5173

## Test MongoDB Connection

To verify your MongoDB connection anytime:

```bash
cd backend
python simple_test.py
```

## Create Sample Data

### Create Sample Posts for Feed

```bash
cd backend
python create_sample_feed_posts.py
```

### Create Sample Users (if needed)

```bash
cd backend
python seed_data/generate_users.py
```

## Troubleshooting

### If MongoDB Connection Fails

1. **Check Internet Connection:** Ensure you can access the internet
2. **Verify Credentials:** Make sure the username/password in `.env` is correct
3. **IP Whitelist:** In MongoDB Atlas, ensure your IP is whitelisted (or use 0.0.0.0/0 for development)
4. **Cluster Status:** Check if your MongoDB Atlas cluster is running

### If Backend Won't Start

1. **Check Python Version:** Ensure Python 3.8+ is installed
2. **Install Dependencies:** Run `pip install -r requirements.txt` in the backend folder
3. **Check Port:** Ensure port 5000 is not being used by another application

### If Frontend Won't Start

1. **Check Node.js:** Ensure Node.js 16+ is installed
2. **Install Dependencies:** Run `npm install` in the project root
3. **Check Port:** Ensure port 5173 is available

## Environment Variables

Your `.env` file in the backend folder contains:

```env
MONGODB_URI="mongodb+srv://varuabi005_db_user:varuabi005_db_user@workconnect.tb2qc4j.mongodb.net/?retryWrites=true&w=majority&appName=workconnect"
MONGODB_DB_NAME="workconnect"
JWT_SECRET_KEY="workconnect-jwt-secret-key-2024"
SECRET_KEY="workconnect-secret-key-2024"
```

## API Endpoints

Once your backend is running, you can access these endpoints:

- `GET /health` - Health check
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/users/profile` - Get user profile (requires auth)
- `GET /api/projects` - Get projects
- `GET /api/posts` - Get feed posts
- `POST /api/posts` - Create new post (requires auth)

## Next Steps

1. **Start both servers** (backend and frontend)
2. **Create sample posts** using the provided script
3. **Test the application** by registering a new user
4. **Explore the features** like creating posts, projects, and messaging

Your WorkConnect application is ready to use! 🎉