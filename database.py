import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('inventory.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create table for inventory items
cursor.execute('''
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()