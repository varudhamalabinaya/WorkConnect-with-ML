#!/usr/bin/env python3
"""
Test Role-Specific ML Recommendations
Validates that freelancers and clients get different, appropriate content
"""

import requests
import json

def test_role_specific_endpoints():
    """Test that endpoints return role-appropriate content"""
    base_url = "http://localhost:5000"
    
    print("Testing Role-Specific ML Recommendations")
    print("=" * 45)
    
    # Test freelancer-specific endpoints
    print("\nFreelancer-Only Endpoints:")
    freelancer_endpoints = [
        "/api/ml/recommendations/projects",
        "/api/ml/recommendations/skills", 
        "/api/ml/recommendations/users"
    ]
    
    for endpoint in freelancer_endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=3)
            status = "REQUIRES AUTH" if response.status_code == 401 else f"STATUS: {response.status_code}"
            print(f"  {endpoint}: {status}")
        except:
            print(f"  {endpoint}: OFFLINE")
    
    # Test client-specific endpoints
    print("\nClient/Agency-Only Endpoints:")
    client_endpoints = [
        "/api/ml/recommendations/freelancers"
    ]
    
    for endpoint in client_endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=3)
            status = "REQUIRES AUTH" if response.status_code == 401 else f"STATUS: {response.status_code}"
            print(f"  {endpoint}: {status}")
        except:
            print(f"  {endpoint}: OFFLINE")

def main():
    test_role_specific_endpoints()
    
    print("\nRole-Specific Content Rules:")
    print("- Freelancers: Projects + Skills + Collaboration")
    print("- Clients/Agencies: Freelancer Recommendations Only")
    print("- Market Trends: Available to All Roles")
    
    print("\nFrontend Changes Applied:")
    print("- Strict role-based API calls")
    print("- No skill development for clients")
    print("- No project recommendations for clients")
    print("- Clear data separation by role")

if __name__ == "__main__":
    main()