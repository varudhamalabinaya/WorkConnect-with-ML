#!/usr/bin/env python3
"""
Test script for AI Career Growth Advisor endpoints
Run this to verify the AI Advisor functionality
"""

import requests
import json
from datetime import datetime

# Configuration
BACKEND_URL = "http://localhost:5000"
AI_ADVISOR_URL = f"{BACKEND_URL}/api/ai"

# Test user credentials (update with your test user)
TEST_USER_EMAIL = "freelancer@test.com"
TEST_USER_PASSWORD = "password123"

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def print_success(message):
    print(f"{Colors.GREEN}✓ {message}{Colors.END}")

def print_error(message):
    print(f"{Colors.RED}✗ {message}{Colors.END}")

def print_info(message):
    print(f"{Colors.BLUE}ℹ {message}{Colors.END}")

def print_warning(message):
    print(f"{Colors.YELLOW}⚠ {message}{Colors.END}")

def get_auth_token():
    """Login and get JWT token"""
    print_info("Attempting to get authentication token...")
    try:
        response = requests.post(
            f"{BACKEND_URL}/api/auth/login",
            json={
                "email": TEST_USER_EMAIL,
                "password": TEST_USER_PASSWORD
            }
        )
        
        if response.status_code == 200:
            data = response.json()
            token = data.get('access_token')
            print_success(f"Authentication successful")
            return token
        else:
            print_error(f"Login failed: {response.status_code}")
            print(f"Response: {response.text}")
            return None
    except Exception as e:
        print_error(f"Error during login: {str(e)}")
        return None

def test_health_check():
    """Test AI Advisor health endpoint"""
    print("\n" + "="*60)
    print("TEST 1: Health Check")
    print("="*60)
    
    try:
        response = requests.get(f"{AI_ADVISOR_URL}/health")
        if response.status_code == 200:
            print_success("Health check passed")
            print(f"Response: {json.dumps(response.json(), indent=2)}")
            return True
        else:
            print_error(f"Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def test_update_trends():
    """Test updating skill trends"""
    print("\n" + "="*60)
    print("TEST 2: Update Skill Trends")
    print("="*60)
    
    try:
        response = requests.post(f"{AI_ADVISOR_URL}/update-trends")
        if response.status_code == 200:
            print_success("Trends updated successfully")
            print(f"Response: {json.dumps(response.json(), indent=2)}")
            return True
        else:
            print_error(f"Update trends failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def test_trending_skills(token):
    """Test getting trending skills"""
    print("\n" + "="*60)
    print("TEST 3: Get Trending Skills")
    print("="*60)
    
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(f"{AI_ADVISOR_URL}/trending-skills?limit=5", headers=headers)
        if response.status_code == 200:
            print_success("Trending skills retrieved")
            data = response.json()
            skills = data.get('trending_skills', [])
            print(f"Found {len(skills)} trending skills:")
            for skill in skills:
                print(f"  - {skill.get('name')}: Demand {skill.get('demand_score', 0):.1f}%, Avg Rate: ${skill.get('average_rate', 0):.2f}")
            return True
        else:
            print_error(f"Get trending skills failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def test_market_analysis(token):
    """Test market analysis endpoint"""
    print("\n" + "="*60)
    print("TEST 4: Market Analysis")
    print("="*60)
    
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(f"{AI_ADVISOR_URL}/market-analysis", headers=headers)
        if response.status_code == 200:
            print_success("Market analysis retrieved")
            data = response.json()
            print(f"Total Skills: {data.get('total_skills', 0)}")
            print(f"Total Projects: {data.get('total_projects', 0)}")
            print(f"Average Project Budget: ${data.get('average_budget', 0):.2f}")
            print(f"Response: {json.dumps(data, indent=2)}")
            return True
        else:
            print_error(f"Market analysis failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def test_dashboard_summary(token):
    """Test dashboard summary endpoint"""
    print("\n" + "="*60)
    print("TEST 5: Dashboard Summary")
    print("="*60)
    
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(f"{AI_ADVISOR_URL}/dashboard-summary", headers=headers)
        if response.status_code == 200:
            print_success("Dashboard summary retrieved")
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
            return True
        else:
            print_error(f"Dashboard summary failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def test_recommendations(token):
    """Test getting recommendations"""
    print("\n" + "="*60)
    print("TEST 6: Get User Recommendations")
    print("="*60)
    
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(f"{AI_ADVISOR_URL}/recommendations", headers=headers)
        if response.status_code == 200:
            print_success("Recommendations retrieved")
            data = response.json()
            recommendations = data.get('recommendations', [])
            print(f"Found {len(recommendations)} recommendations:")
            for rec in recommendations[:3]:  # Show first 3
                print(f"\n  Type: {rec.get('type')}")
                print(f"  Title: {rec.get('title')}")
                print(f"  Confidence: {rec.get('confidence', 0):.2f}")
                print(f"  Description: {rec.get('description', 'N/A')[:100]}...")
            return True
        else:
            print_error(f"Get recommendations failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def test_career_insight(token):
    """Test getting career insight"""
    print("\n" + "="*60)
    print("TEST 7: Get Career Insight")
    print("="*60)
    
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(f"{AI_ADVISOR_URL}/career-insight", headers=headers)
        if response.status_code == 200:
            print_success("Career insight retrieved")
            data = response.json()
            print(f"Market Position: {data.get('current_market_position', 'N/A')}")
            print(f"Current Rate: ${data.get('current_rate', 0):.2f}")
            print(f"Potential Rate: ${data.get('potential_rate', 0):.2f}")
            print(f"Missing Skills: {', '.join(data.get('missing_trending_skills', []))}")
            return True
        else:
            print_error(f"Get career insight failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def run_all_tests():
    """Run all tests"""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*10 + "AI CAREER ADVISOR - ENDPOINT TESTING" + " "*12 + "║")
    print("╚" + "="*58 + "╝")
    
    print(f"\n🔧 Backend URL: {BACKEND_URL}")
    print(f"📅 Test Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    results = []
    
    # Test 1: Health check (no auth needed)
    results.append(("Health Check", test_health_check()))
    
    # Test 2: Update trends (no auth needed)
    results.append(("Update Trends", test_update_trends()))
    
    # Get auth token for remaining tests
    print_info("Getting authentication token...")
    token = get_auth_token()
    
    if not token:
        print_error("Cannot proceed without authentication token")
        print_warning("Make sure your test user credentials are correct:")
        print_warning(f"  Email: {TEST_USER_EMAIL}")
        print_warning(f"  Password: {TEST_USER_PASSWORD}")
        return
    
    # Tests requiring authentication
    results.append(("Trending Skills", test_trending_skills(token)))
    results.append(("Market Analysis", test_market_analysis(token)))
    results.append(("Dashboard Summary", test_dashboard_summary(token)))
    results.append(("Get Recommendations", test_recommendations(token)))
    results.append(("Career Insight", test_career_insight(token)))
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        color = Colors.GREEN if result else Colors.RED
        print(f"{color}{status}{Colors.END} - {test_name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print_success("All tests passed! AI Advisor is working correctly.")
    else:
        print_warning(f"{total - passed} test(s) failed. Check the output above for details.")

if __name__ == "__main__":
    run_all_tests()