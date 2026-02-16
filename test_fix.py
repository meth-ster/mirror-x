# Test the database fix
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import get_user_by_id, init_database

# Initialize database
init_database()

# Test getting user by ID
user = get_user_by_id(1)
print(f"User test result: {user}")

# Test with non-existent ID
user_none = get_user_by_id(999)
print(f"Non-existent user result: {user_none}")
