import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')

# Get a cursor object
c = conn.cursor()

# Create a table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# Insert a record into the table
c.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))

# Read records from the table
c.execute("SELECT * FROM users")
print(c.fetchall())

# Update a record in the table
c.execute("UPDATE users SET email = ? WHERE name = ?", ("alice.new@example.com", "Alice"))

# Read records from the table
c.execute("SELECT * FROM users")
print(c.fetchall())

# Delete a record from the table
c.execute("DELETE FROM users WHERE name = ?", ("Alice",))

# Read records from the table
c.execute("SELECT * FROM users")
print(c.fetchall())

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()