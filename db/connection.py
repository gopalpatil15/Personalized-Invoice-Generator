import sys
import os
import mysql.connector

# Ensure Python always uses the project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Moves up one level to the root
sys.path.insert(0, PROJECT_ROOT)  # Insert at the beginning to give priority

# Debugging: Print sys.path
print("🔍 sys.path after modification:", sys.path)

# Import the database configuration
try:
    from config.config import DB_CONFIG
    print("✅ Config module found!")
except ModuleNotFoundError as e:
    print(f"❌ Import Error: {e}")
    sys.exit(1)

def get_connection():
    """Establishes and returns a connection to the database using configuration settings."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Database Connection Error: {err}")
        return None

# Test the connection
if __name__ == "__main__":
    conn = get_connection()
    if conn and conn.is_connected():
        print("✅ Database connected successfully!")
        conn.close()
    else:
        print("❌ Failed to connect to the database.")
