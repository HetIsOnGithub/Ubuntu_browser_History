import sqlite3
import os
import shutil

# Specify the path to the Chrome history database file
history_db = os.path.expanduser('~') + '/.config/google-chrome/Default/History'

# Rest of the code...


# Create a temporary copy of the Chrome history database
temp_file = 'temp_history'
shutil.copyfile(history_db, temp_file)

# Connect to the temporary database file
conn = sqlite3.connect(temp_file)
cursor = conn.cursor()

# Query the browser history from the 'urls' table
cursor.execute("SELECT url FROM urls")
rows = cursor.fetchall()

# Save the browser history to a text file
with open('browser_history.txt', 'w') as file:
    for row in rows:
        file.write(row[0] + '\n')

# Close the database connection and remove the temporary file
cursor.close()
conn.close()
os.remove(temp_file)
