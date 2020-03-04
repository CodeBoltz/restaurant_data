import cgi
import sqlite3
import os 

form = cgi.FieldStorage()
v_neighborhood=[]
v_neighborhood.append(form.getvalue("neighborhood"))

# connect to the database file, and create a connection object
db_connection = sqlite3.connect('restaurants.db')

# create a database cursor object, which allows us to perform SQL on the database. 
db_cursor = db_connection.cursor()

# run a first query 
for i in v_neighborhood:
  db_cursor.execute("SELECT restaurants.name FROM restaurants  INNER JOIN neighborhoods ON restaurants.NEIGHBORHOOD_ID=neighborhoods.ID WHERE neighborhoods.NAME='%s'"%(i))


# store the result in a local variable. 
# this will be a list of tuples, where each tuple represents a row in the table
list_restaurants = db_cursor.fetchall()

print("list_restaurants contents:")
print(list_restaurants)

db_connection.close()

print(f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Restaurants in {v_neighborhood[0]}</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
 
  </head>  
  <body style="color:black; font-family:arial" >
  <h1>here are all the restaurants from {v_neighborhood[0]}:</h1>
  <ul>""")
    
for i in range (len(list_restaurants)):
  print(f"""<li>{list_restaurants[i]}</li>\n""")

  
print("""</ul>
  </body>
</html>""")