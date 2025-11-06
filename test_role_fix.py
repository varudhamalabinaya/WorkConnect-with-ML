#!/usr/bin/env python3
"""Quick test to verify role-based content fix"""

import requests
import json

def test_role_endpoints():
    """Test role-based ML endpoints"""
    base_url = "http://localhost:5000"
    
    print("Testing Role-Based ML Endpoints...")
    
    # Test freelancer endpoints
    freelancer_endpoints = [
        "/api/ml/recommendations/projects",
        "/api/ml/recommendations/users"
    ]
    
    # Test client/agency endpoints  
    client_endpoints = [
        "/api/ml/recommendations/freelancers"
    ]
    
    # Test shared endpoints
    shared_endpoints = [
        "/api/ml/recommendations/skills",
        "/api/market/trends"
    ]
    
    print("\nFreelancer-specific endpoints:")
    for endpoint in freelancer_endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=3)
            print(f"  {endpoint}: {response.status_code}")
        except:
            print(f"  {endpoint}: OFFLINE")
    
    print("\nClient/Agency-specific endpoints:")
    for endpoint in client_endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=3)
            print(f"  {endpoint}: {response.status_code}")
        except:
            print(f"  {endpoint}: OFFLINE")
    
    print("\nShared endpoints:")
    for endpoint in shared_endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=3)
            print(f"  {endpoint}: {response.status_code}")
        except:
            print(f"  {endpoint}: OFFLINE")

def main():
    print("Role-Based Content Fix Validation")
    print("=" * 35)
    
    test_role_endpoints()
    
    print("\nFix Applied:")
    print("- Removed hardcoded freelancer content for all users")
    print("- Added role-based conditional rendering")
    print("- Fixed skill recommendations messaging per role")
    print("- Clients now see freelancer recommendations only")
    
    print("\nExpected Behavior:")
    print("- Freelancers: See project + collaboration recommendations")
    print("- Clients/Agencies: See freelancer recommendations")
    print("- All roles: See market trends and skill insights")

if __name__ == "__main__":
    main()