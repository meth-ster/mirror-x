# Test the Jinja2 fix
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app

# Test the index route
with app.test_client() as client:
    # Test login first
    client.post('/login', data={
        'username': 'testuser',
        'password': 'password123'
    }, follow_redirects=True)
    
    # Test index route
    response = client.get('/')
    print(f"Index status: {response.status_code}")
    print(f"Response data length: {len(response.data)}")
    
    if response.status_code == 200:
        print("SUCCESS: Index route works!")
    else:
        print("FAILED: Index route still has errors")
        print(response.data.decode())
