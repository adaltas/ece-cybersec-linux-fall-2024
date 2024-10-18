#!/usr/bin/env python3

import duckdb
import sys

# Extract the arguments
datafile='passwd.db'

# Connect to a SQLite database (or create it if it doesn't exist)
conn = duckdb.connect(datafile)
cursor = conn.cursor()

# Create a sample users table
cursor.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
cursor.execute('''INSERT INTO users (id, username, password) VALUES (1, 'admin', 'password123')''')
conn.commit()
