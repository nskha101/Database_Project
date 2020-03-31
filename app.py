import psycopg2
import random
def open_connection():
 try:
   connection = psycopg2.connect(user = "nskha101",
                                  password = "Nithrocksu25",
                                  host = "web0.eecs.uottawa.ca",
                                  port = "15432",
                                  database = "nskha101")

   cursor = connection.cursor()
   # Print PostgreSQL Connection properties
   print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
   cursor.execute("SELECT version();")
   record = cursor.fetchone()
   print("You are connected to - ", record,"\n")
 
 except (Exception, psycopg2.Error) as error:
        print ("Error while connecting to PostgreSQL", error)
#finally:
    #closing database connection.
   
def query(query):
   record = cursor.fetchone()
   print("You are connected to - ", record,"\n")
   cursour = conn.cursor()
   cursor.execute(query)
   conn.commit()
   fetched = cursor.fetchall()
   print(fetched)
   cursor.close()
   

def uploadlisting(name, email, location, duration, maxsize, language, description, rules, cost, availability, contact):
    try:
        cursor = conn.cursor()
        bnbid=random.randint(1,10000)+name
        cursor.execute("INSERT INTO bnb (bnbid, email, name, location, duration, maxsize, langugage, description, rules, cost, availability, contact) VALUES(%s, %s, %s)", (bnbid, email, name, location, duration, maxsize, language, description, rules, cost, availability, contact))
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error :
        print("exception, yo")

def availability(name):
    cursor = conn.cursor()
    query = "SELECT availablity, cost FROM bnb WHERE name = " + name
    cursor.execute(query)
    availability = cursor.fetchall()
    for row in availability:
        print("availability = ", row[0])
        print("cost = ", row[1], "/n")
    
def close():
   if(connection):
      connection.close()
      print("PostgreSQL connection is closed")