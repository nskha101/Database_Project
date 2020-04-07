import psycopg2
import random
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db

config = config()
connection = psycopg2.connect(**config)

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
        return fetched
   except (Exception) as error:
       return error
   

   cursor.close()
   

def uploadlisting(name, email, location, duration, maxsize, language, description, rentaltype, rules, cost, availability, contact):
    #test query, note the type values. uploadlisting("testbnb", "test@test.com", "ottawa", 365, 2, "english", "fun place", "no pets", "300", True, "jeff")

    try:
        cursor = connection.cursor()
        connection.cursor().execute("SET SCHEMA '{}'".format('airbnb'))
        bnbid=random.randint(1,10000)
        print(bnbid)
        cursor.execute("INSERT INTO bnb (bnbid, email, name, location, duration, maxsize, Language, description, rentaltype, rules, cost, availability, contact) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (bnbid, email, name, location, duration, maxsize, [language], description, rentaltype, rules, cost, availability, contact))
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

def addhost(email, firstname, lastname, middlename, language, gender, govid, phonenum, address, emergencycontact, dob, staylist, adventurelist, experiencelist):
    try:   
        cursor = connection.cursor()
        connection.cursor().execute("SET SCHEMA '{}'".format('airbnb'))
        cursor.execute("INSERT INTO person (email, firstname, lastname, middlename, language, gender, govid, phonenum, address, emergencycontact, dob) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (email, firstname, lastname, middlename, [language], gender, govid, phonenum, address, emergencycontact, dob) )
        cursor.execute("INSERT INTO host (email, staylist, adventurelist, experiencelist) VALUES (%s, %s, %s, %s)", (email,[staylist],[adventurelist],[experiencelist]))
        connection.commit()
        cursor.close()
        
       # anotherone(email, staylist, adventurelist, experiencelist)
    except (Exception) as error :
        print("exception - " , error)

def edithost(email, firstname, lastname, middlename, language, gender, govid, phonenum, address, emergencycontact, dob, staylist, adventurelist, experiencelist):
    try:
        cursor = connection.cursor()
        connection.cursor().execute("SET SCHEMA '{}'".format('airbnb'))
        cursor.execute("DELETE FROM host WHERE email = '{}'".format(email))
        cursor.execute("DELETE FROM person WHERE email = '{}'".format(email))
        cursor.execute("INSERT INTO person (email, firstname, lastname, middlename, language, gender, govid, phonenum, address, emergencycontact, dob) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (email, firstname, lastname, middlename, [language], gender, govid, phonenum, address, emergencycontact, dob) )
        cursor.execute("INSERT INTO host (email, staylist, adventurelist, experiencelist) VALUES (%s, %s, %s, %s)", (email,[staylist],[adventurelist],[experiencelist]))
        connection.commit()
        cursor.close()

    except (Exception) as error :
        print("exception - " , error)

def searchbnb(searchtype, searchparam):
    try:
        cursor = connection.cursor()
        connection.cursor().execute("SET SCHEMA '{}'".format('airbnb'))
        cursor.execute("SELECT * FROM BNB WHERE {} = '{}'".format(searchtype, searchparam))
        availability = cursor.fetchall()
        return availability
    except (Exception) as error :
        print("exception - " , error)

if __name__ == "__main__":
        #edithost("hosttest@test.com", "testchange", "test", "middle", "english", "Male", "123456", "1231231234", "doe doe doe st.", "123456789", "1920-01-01", "962", "1234", "1234")
        print(searchbnb("location", "markham"))
