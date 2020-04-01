import psycopg2
import random
connection = psycopg2.connect(user = "nskha101",
                                  password = "Nithrocksu25",
                                  host = "web0.eecs.uottawa.ca",
                                  port = "15432",
                                  database = "nskha101")
def open_connection():

 try:

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
   try: 
        cursor = connection.cursor()
        connection.cursor().execute("SET SCHEMA '{}'".format('airbnb'))
        cursor.execute(query)
        connection.commit()
        fetched = cursor.fetchall()
   except:
       pass 
   
   cursor.close()
   

def uploadlisting(name, email, location, duration, maxsize, language, description, rules, cost, availability, contact):
    #test query, note the type values. uploadlisting("testbnb", "test@test.com", "ottawa", 365, 2, "english", "fun place", "no pets", "300", True, "jeff")

    try:
        cursor = connection.cursor()
        connection.cursor().execute("SET SCHEMA '{}'".format('airbnb'))
        bnbid=random.randint(1,10000)
        print(bnbid)
        cursor.execute("INSERT INTO bnb (bnbid, email, name, location, duration, maxsize, Language, description, rules, cost, availability, contact) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (bnbid, email, name, location, duration, maxsize, [language], description, rules, cost, availability, contact))
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error :
        print("exception - " , error)

def availability(name):
    cursor = connection.cursor()
    connection.cursor().execute("SET SCHEMA '{}'".format('airbnb'))
    query = "SELECT availability, cost FROM bnb WHERE name = '{}'".format(name)
    cursor.execute(query)
    availability = cursor.fetchall()
    string = ""
    for row in availability:
       string += "availability = {}".format(row[0]) + " , " + "cost = {}".format( row[1])
    print(string) 
    return string

def occupancyrate(bnbid):
    cursor = connection.cursor()
    connection.cursor().execute("SET SCHEMA '{}'".format('airbnb'))
    query = "SELECT duration FROM bnb WHERE bnbid = '{}'".format(bnbid)
    cursor.execute(query)
    duration = cursor.fetchone()
    return "occupancy rate: {:.2f}%".format((duration[0]/365)*100)

def close():
   if(connection):
      connection.close()
      print("PostgreSQL connection is closed")

