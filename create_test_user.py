# Create a test user to fix the deployment
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import init_database, create_user, get_user_by_id

# Initialize database
init_database()

# Create a test user
try:
    user_id = create_user('testuser', 'test@example.com', 'password123')
    print(f"Created test user with ID: {user_id}")
    
    # Test getting the user
    user = get_user_by_id(user_id)
    print(f"Retrieved user: {user}")
    
except Exception as e:
    print(f"Error creating test user: {e}")
    
    # Try to get existing user
    try:
        user = get_user_by_id(1)
        print(f"Existing user ID 1: {user}")
    except Exception as e2:
        print(f"Error getting existing user: {e2}")
