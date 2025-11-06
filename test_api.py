#!/usr/bin/env python3
"""
Simple API test script to verify all endpoints are working
"""
import requests
import json

BASE_URL = "http://localhost:5000/api"

def test_login(email="alice.johnson@example.com", password="password123"):
    """Test login with sample user"""
    login_data = {
        "email": email,
        "password": password
    }
    
    response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    print(f"Login Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        user = data['user']
        print(f"Login successful for: {user['first_name']} {user['last_name']} ({user['role']})")
        return data['access_token'], user['role']
    else:
        print(f"Login failed: {response.json()}")
        return None, None

def test_role_permissions(token, user_role):
    """Test role-based permissions for project operations"""
    headers = {"Authorization": f"Bearer {token}"}
    
    print(f"=== Testing Role-Based Permissions for {user_role.upper()} ===")
    
    # Test project creation
    project_data = {
        "title": f"Test Project by {user_role}",
        "description": "This is a test project to verify role-based permissions"
    }
    
    response = requests.post(f"{BASE_URL}/projects", json=project_data, headers=headers)
    print(f"Project Creation: {response.status_code}")
    
    if response.status_code == 201:
        print("  ✓ Project created successfully")
        project_id = response.json()['project']['id']
        
        # Test project update
        update_data = {"title": "Updated Test Project"}
        update_response = requests.put(f"{BASE_URL}/projects/{project_id}", json=update_data, headers=headers)
        print(f"Project Update: {update_response.status_code}")
        
        # Test project deletion
        delete_response = requests.delete(f"{BASE_URL}/projects/{project_id}", headers=headers)
        print(f"Project Deletion: {delete_response.status_code}")
        
    elif response.status_code == 403:
        error_msg = response.json().get('message', 'Access denied')
        print(f"  ✓ Access properly restricted: {error_msg}")
    else:
        print(f"  ✗ Unexpected response: {response.json()}")
    
    print()

def test_endpoints(token):
    """Test various endpoints with authentication"""
    headers = {"Authorization": f"Bearer {token}"}
    
    endpoints = [
        ("GET", "/users/profile", "User Profile"),
        ("GET", "/skills", "Skills List"),
        ("GET", "/users/skills", "User Skills"),
        ("GET", "/teams", "Teams"),
        ("GET", "/projects", "Projects"),
        ("GET", "/messages", "Messages"),
        ("GET", "/ai-matching", "AI Matching"),
        ("GET", "/teams/invitations", "Team Invitations"),
    ]
    
    for method, endpoint, description in endpoints:
        try:
            if method == "GET":
                response = requests.get(f"{BASE_URL}{endpoint}", headers=headers)
            
            print(f"{description}: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, dict):
                    for key, value in data.items():
                        if isinstance(value, list):
                            print(f"  - {key}: {len(value)} items")
                        else:
                            print(f"  - {key}: {type(value).__name__}")
                print()
            else:
                print(f"  Error: {response.json()}")
                print()
                
        except Exception as e:
            print(f"  Exception: {str(e)}")
            print()

def main():
    print("=== WorkConnect API Test ===")
    print()
    
    # Test different user roles
    test_users = [
        ("alice.johnson@example.com", "password123"),  # Should be client or agency
        # Add more test users with different roles if available
    ]
    
    for email, password in test_users:
        print(f"Testing user: {email}")
        token, role = test_login(email, password)
        print()
        
        if token and role:
            print("=== Testing Authenticated Endpoints ===")
            test_endpoints(token)
            
            # Test role-based permissions
            test_role_permissions(token, role)
        else:
            print("Cannot test authenticated endpoints without valid token")
        
        print("=" * 50)
        print()

if __name__ == "__main__":
    main()