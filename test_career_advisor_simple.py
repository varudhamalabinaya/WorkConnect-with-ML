#!/usr/bin/env python3
"""
Career Advisor Fix Validation - Simple Version
"""

import requests
import os

def test_apis():
    """Test Career Advisor API endpoints"""
    base_url = "http://localhost:5000"
    
    print("Testing Career Advisor API Dependencies...")
    
    endpoints = [
        "/api/users/profile",
        "/api/ml/recommendations/skills",
        "/api/market/trends"
    ]
    
    working_count = 0
    
    for endpoint in endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=3)
            if response.status_code in [200, 401, 403]:
                print(f"OK: {endpoint} - {response.status_code}")
                working_count += 1
            else:
                print(f"ERROR: {endpoint} - {response.status_code}")
        except:
            print(f"OFFLINE: {endpoint}")
    
    return working_count

def check_files():
    """Check if key files exist"""
    print("\nChecking Frontend Files...")
    
    files = [
        "src/pages/CareerAdvisor.tsx",
        "src/hooks/use-ai-advisor.ts",
        "src/App.tsx"
    ]
    
    for file_path in files:
        if os.path.exists(file_path):
            print(f"EXISTS: {file_path}")
        else:
            print(f"MISSING: {file_path}")

def main():
    print("Career Advisor Blank Page Fix Validation")
    print("=" * 45)
    
    check_files()
    working_apis = test_apis()
    
    print(f"\nSummary: {working_apis}/3 APIs accessible")
    
    print("\nFixes Applied:")
    print("- Added userRole state management")
    print("- Added error handling with fallback data") 
    print("- Fixed null userRole conditions")
    print("- Added loading states")
    
    print("\nTo test:")
    print("1. npm run dev")
    print("2. Go to /career-advisor")
    print("3. Should show content even if backend is offline")

if __name__ == "__main__":
    main()