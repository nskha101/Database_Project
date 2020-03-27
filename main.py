from flask import Flask, redirect, url_for, request,render_template
import psycopg2
app = Flask(__name__)

@app.route("/")
def home():
   return render_template("login.html")


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['un']
      password = request.form['pw']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('un')
      password = request.args.get('pw')
      
      return redirect(url_for('success',name = user))

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


# @app.route('/admin')
# def admin():
#    return

if __name__ == "__main__":
   app.run(debug=True)

