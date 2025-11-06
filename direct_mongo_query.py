#!/usr/bin/env python
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / 'backend' / '.env'
load_dotenv(env_path)

MONGO_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/workconnect')
DB_NAME = os.getenv('MONGODB_DB_NAME', 'workconnect')

print(f"Connecting to MongoDB...")
print(f"URI: {MONGO_URI[:50]}...")
print(f"DB: {DB_NAME}\n")

try:
    from pymongo import MongoClient
    
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    
    print("✓ Connected to MongoDB\n")
    
    print("=== Searching for 'harshika' ===")
    harshika_users = list(db.users.find(
        {'first_name': {'$regex': 'harshika', '$options': 'i'}},
        {'first_name': 1, 'last_name': 1, 'email': 1, 'role': 1, '_id': 1}
    ))
    
    if harshika_users:
        print(f"Found {len(harshika_users)} user(s):\n")
        for user in harshika_users:
            user_id = user['_id']
            print(f"Name: {user['first_name']} {user['last_name']}")
            print(f"Email: {user['email']}")
            print(f"Role: {user['role']}")
            print(f"ID: {user_id}\n")
            
            insights = db.careerinsuights.count_documents({'user': user_id})
            recommendations = db.skillrecommendation.count_documents({'user': user_id})
            
            print(f"Career Insights: {insights}")
            print(f"Skill Recommendations: {recommendations}")
            print()
    else:
        print("No users found with 'harshika'\n")
        print("Total users in DB:", db.users.count_documents({}))
        print("\nFirst 5 users:")
        for user in db.users.find({}, {'first_name': 1, 'last_name': 1, 'role': 1}).limit(5):
            print(f"  - {user['first_name']} {user['last_name']} ({user['role']})")

except Exception as e:
    import traceback
    print(f"Error: {e}")
    traceback.print_exc()
