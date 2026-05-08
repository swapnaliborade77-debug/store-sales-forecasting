# test_connection.py
import sqlalchemy
import urllib.parse
import sys

print("--- Starting Connection Test ---")
try:
    # 1. Encode Password
    password = urllib.parse.quote_plus("Swapnali@2020")
    print("Step 1: Password encoded.")

    # 2. Setup Engine (Using pymysql now)
    engine = sqlalchemy.create_engine(f"mysql+pymysql://root:{password}@localhost/rossmann_sales_db")
    print("Step 2: Engine created.")

    # 3. Try Connection
    with engine.connect() as conn:
        print("Step 3: Handshake with MySQL successful.")
        result = conn.execute(sqlalchemy.text("SELECT 1"))
        print("✅ SUCCESS: Your Python script can talk to MySQL!")

except Exception as e:
    print(f"❌ CONNECTION FAILED")
    print(f"Error Details: {e}")