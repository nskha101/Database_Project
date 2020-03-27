# from flask import Flask
import psycopg2

# app = Flask(__name__)
# @app.route("/")
# def home():
#     return "Hello, Flask!"



try:
    connection = psycopg2.connect(user = "yren020",
                                  password = "",
                                  host = "web0.eecs.uottawa.ca",
                                  port = "15432",
                                  database = "yren020")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
