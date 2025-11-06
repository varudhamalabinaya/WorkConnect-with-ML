#!/usr/bin/env python
import sys
sys.stdout.write("Script started\n")
sys.stdout.flush()

try:
    from pymongo import MongoClient
    sys.stdout.write("PyMongo imported\n")
    sys.stdout.flush()
    
    MONGO_URI = "mongodb+srv://varuabi005_db_user:Abi_2005@workconnect.tb2qc4j.mongodb.net/?retryWrites=true&w=majority&appName=workconnect"
    sys.stdout.write("Connecting to MongoDB...\n")
    sys.stdout.flush()
    
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000, connectTimeoutMS=5000)
    sys.stdout.write("Client created\n")
    sys.stdout.flush()
    
    db = client['workconnect']
    sys.stdout.write("DB selected\n")
    sys.stdout.flush()
    
    # Try to ping
    db.command('ping')
    sys.stdout.write("✓ Connected successfully\n")
    sys.stdout.flush()
    
    # Count users
    user_count = db.users.count_documents({})
    sys.stdout.write(f"Total users: {user_count}\n")
    sys.stdout.flush()
    
except Exception as e:
    import traceback
    sys.stdout.write(f"Error: {e}\n")
    sys.stdout.flush()
    traceback.print_exc()
    sys.exit(1)
