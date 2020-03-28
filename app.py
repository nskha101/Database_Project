import psycopg2

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
    
   cursor.execute("SELECT * from bnb")
   print("Selecting rows from bnb table using cursor.fetchall")
   bnb = cursor.fetchall() 
   
   print("Print each row and it's columns values")
   for row in bnb:
     for item in row:
         print(row[item])
   close()

def close():
   if(connection):
      cursor.close()
      connection.close()
      print("PostgreSQL connection is closed")