import sqlite3

connection = sqlite3.connect("nyc_boroughs.db")
cursor = connection.cursor()

# Create table to hold boroughs, location info, and population
cursor.execute("DROP TABLE IF EXISTS NYC_Boroughs")
cursor.execute("CREATE TABLE NYC_Boroughs (Borough text, County text, Latitude text, Longitude text, Population int)")

# Define data for NYC_Boroughs table
nyc_boroughs = [
    ("Manhattan", "New York", "40.783333", "-73.966667", 0),
    ("Brooklyn", "Kings", "40.692778", "-73.990278", 0),
    ("Queens", "Queens", "40.75", "-73.866667", 0),
    ("The Bronx", "Bronx", "40.837222", "-73.886111", 0),
    ("Staten Island", "Richmond", "40.571944", "-74.146944", 0)
]

# Insert borough data into NYC_Boroughs table
cursor.executemany("INSERT INTO NYC_Boroughs VALUES (?, ?, ?, ?, ?)", nyc_boroughs)
connection.commit()

# Print all table rows
for row in cursor.execute("SELECT * FROM NYC_Boroughs"):
    print(row)

print("***************************************************")

# Print specific rows
print("NYC boroughs in a county that starts with Q:")
cursor.execute("SELECT * FROM NYC_Boroughs WHERE County LIKE 'Q%'")
nyc_search = cursor.fetchall()
print(nyc_search)

# Create new table to hold 2020 census total population for each borough
cursor.execute("DROP TABLE IF EXISTS Borough_Populations")
cursor.execute("CREATE TABLE Borough_Populations (Borough text, Population int)")

# Define population data
populations = [
    ("Manhattan", 1694251),
    ("Brooklyn", 2736074),
    ("Queens", 2405464),
    ("The Bronx", 1472654),
    ("Staten Island", 495747)
]

# Insert population data into Borough_Populations table
cursor.executemany("INSERT INTO Borough_Populations VALUES (?, ?)", populations)
connection.commit()

print("***************************************************")

# Print database rows
for row in cursor.execute("SELECT * FROM Borough_Populations"):
    print(row)

print("***************************************************")

# Print specific rows
print("Populations Greater Than 2 Million:")
cursor.execute("SELECT * FROM Borough_Populations WHERE Population > 2000000")
population_search = cursor.fetchall()
print(population_search)

print("***************************************************")

# Manipulate database data to replace 0 populatino value in NYC_Boroughs table with population data from Borough_Populations table
print("Adjusted:")
adjusted_data = [
    row[:-1] + (pop[1],) # Add the value in the last row of nyc_boroughs to the value at index 1 of the population table...
    for row in nyc_boroughs
    for pop in populations
    if row[0] == pop[0] # ... if the borough name at the 0 index of nyc_boroughs matches the 0 index in the population table
]
for row in adjusted_data:
    print(row)

# Update the NYC_Boroughs table with the adjusted data
cursor.execute("DELETE FROM NYC_Boroughs")
cursor.executemany("INSERT INTO NYC_Boroughs VALUES (?, ?, ?, ?, ?)", adjusted_data)
connection.commit()

print("***************************************************")

# Print adjusted database rows
for row in cursor.execute("SELECT * FROM NYC_Boroughs"):
    print(row)

connection.commit()
connection.close()