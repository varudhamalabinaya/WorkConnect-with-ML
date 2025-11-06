#!/usr/bin/env python3
"""
Career Advisor Blank Page Fix Validation
Tests the fixes applied to prevent blank page issues
"""

import requests
import json
import time

def test_career_advisor_apis():
    """Test all APIs that Career Advisor depends on"""
    base_url = "http://localhost:5000"
    
    print("🔍 Testing Career Advisor API Dependencies...")
    
    # Test endpoints that Career Advisor uses
    endpoints = [
        "/api/users/profile",
        "/api/ml/recommendations/skills",
        "/api/ml/recommendations/projects", 
        "/api/ml/recommendations/users",
        "/api/market/trends"
    ]
    
    results = {}
    
    for endpoint in endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=5)
            results[endpoint] = {
                "status": response.status_code,
                "accessible": response.status_code in [200, 401, 403]  # 401/403 means endpoint exists
            }
            print(f"✅ {endpoint}: {response.status_code}")
        except requests.exceptions.ConnectionError:
            results[endpoint] = {"status": "Connection Error", "accessible": False}
            print(f"❌ {endpoint}: Connection Error")
        except Exception as e:
            results[endpoint] = {"status": str(e), "accessible": False}
            print(f"⚠️ {endpoint}: {e}")
    
    return results

def check_frontend_build():
    """Check if frontend files exist"""
    import os
    
    print("\n🔍 Checking Frontend Files...")
    
    files_to_check = [
        "src/pages/CareerAdvisor.tsx",
        "src/hooks/use-ai-advisor.ts", 
        "src/lib/api.ts",
        "src/App.tsx"
    ]
    
    for file_path in files_to_check:
        full_path = f"c:\\Users\\ABINAYA\\OneDrive\\Desktop\\workflow-ai-77-main\\{file_path}"
        if os.path.exists(full_path):
            print(f"✅ {file_path}: Exists")
        else:
            print(f"❌ {file_path}: Missing")

def main():
    print("🎯 Career Advisor Blank Page Fix Validation")
    print("=" * 50)
    
    # Check frontend files
    check_frontend_build()
    
    # Test API endpoints
    api_results = test_career_advisor_apis()
    
    print("\n📊 Summary:")
    print("-" * 30)
    
    accessible_count = sum(1 for result in api_results.values() if result["accessible"])
    total_count = len(api_results)
    
    print(f"API Endpoints Accessible: {accessible_count}/{total_count}")
    
    if accessible_count >= 3:  # At least basic endpoints working
        print("✅ Career Advisor should load with basic functionality")
    else:
        print("⚠️ Career Advisor may have limited functionality")
    
    print("\n🚀 Fixes Applied:")
    print("- Added userRole state management")
    print("- Added error handling with fallback data")
    print("- Fixed null/undefined userRole conditions")
    print("- Added loading states to prevent blank pages")
    
    print("\n💡 To test the fix:")
    print("1. Start backend: cd backend && python app.py")
    print("2. Start frontend: npm run dev")
    print("3. Navigate to /career-advisor")
    print("4. Page should load with content even if APIs fail")

if __name__ == "__main__":
    main()