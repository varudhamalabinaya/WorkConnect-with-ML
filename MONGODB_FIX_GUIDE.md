# MongoDB Connection Fix Guide

## Current Issue
❌ **Authentication Failed**: `bad auth : authentication failed`

## Quick Fix Steps

### Step 1: Fix MongoDB Atlas Credentials

1. **Login to MongoDB Atlas**: https://cloud.mongodb.com/
2. **Go to your cluster** → **Database Access**
3. **Find user**: `varuabi005_db_user`
4. **Click "Edit"** → **Edit Password**
5. **Generate new password** or set a simple one like: `Password123!`
6. **Copy the connection string** with the new password

### Step 2: Update .env File

Replace the MONGODB_URI in your `.env` file:

```env
MONGODB_URI="mongodb+srv://varuabi005_db_user:NEW_PASSWORD_HERE@workconnect.tb2qc4j.mongodb.net/workconnect?retryWrites=true&w=majority&appName=workconnect"
```

### Step 3: Test Connection

```bash
cd backend
python fix_and_test.py
```

### Step 4: Create Test User and Posts

Once connection works:
```bash
cd backend
python fix_and_test.py
```

## Alternative: Use Correct Connection String Format

Try this format in your `.env`:
```env
MONGODB_URI="mongodb+srv://varuabi005_db_user:PASSWORD@workconnect.tb2qc4j.mongodb.net/?retryWrites=true&w=majority&appName=workconnect"
MONGODB_DB_NAME="workconnect"
```

## Test Credentials After Fix

**Login to your app with:**
- Email: `test@workconnect.com`
- Password: `password123`

## If Still Failing

1. **Check IP Whitelist**: Add `0.0.0.0/0` for development
2. **Verify Cluster Status**: Ensure cluster is running (not paused)
3. **Try Different User**: Create a new database user with simpler credentials