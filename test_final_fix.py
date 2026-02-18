# Final test of all fixes
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app

# Test the entire app
with app.test_client() as client:
    print("Testing MIRROR-X app...")
    
    # Test login
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'password123'
    }, follow_redirects=True)
    
    print(f"Login status: {response.status_code}")
    
    if response.status_code == 200:
        print("✅ Login works")
        
        # Test index route
        response = client.get('/')
        print(f"Index status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Index route works")
            print("✅ Authentication fixed!")
        else:
            print("❌ Index route failed")
            print(response.data.decode())
    else:
        print("❌ Login failed")
        print(response.data.decode())
