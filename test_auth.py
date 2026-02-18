# Test authentication fix
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app

# Create a test client
with app.test_client() as client:
    # Test login
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'password123'
    }, follow_redirects=True)
    
    print(f"Login response status: {response.status_code}")
    
    # Test accessing protected route
    response = client.get('/')
    print(f"Index response status: {response.status_code}")
    print(f"Index response data: {response.data.decode()}")
