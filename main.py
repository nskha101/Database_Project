
from flask import Flask, redirect, url_for, request,render_template
import psycopg2
from app import *  


app = Flask(__name__)

@app.route("/")
def home():
   return render_template("login.html")

@app.route('/admin')
def admin():
   return render_template('admin.html')

@app.route('/host/<name>')
def host_name(name):
   return render_template('host.html',name=name)

@app.route('/update_info')
def update_info():
   return render_template('host_info.html')


@app.route('/guest/<name>')
def guest_name(name):
   return render_template('guest.html', name=name)


@app.route('/employee/<name>')
def employee_name(name):
   return render_template('employee.html',name=name)

@app.route('/result')
def result():
   if request.method.__eq__('POST'):
      result = request.form
      return render_template('search_result.html',result=result)

@app.route('/login',methods = ['POST','GET'])
def login():

   error=''
   try:

      if request.method == 'POST':
         user = request.form['un']
         password = request.form['pw']
         option = request.form['options']
         if user.__eq__('admin') and password.__eq__('ad123'):
            return redirect(url_for('admin'))
         elif user.__eq__("guest") and password.__eq__('guest123') and option == 'guest' :
            return redirect(url_for("guest_name", name=user))
         elif user.__eq__("host") and password.__eq__('host123') and option == 'host':
            return redirect(url_for("host_name",name=user))
         else:
            error='Invalid username or password, please try again!'
      return render_template('login.html',error=error)

   except Exception as ex:
      return render_template('login.html',error=error)



if __name__ == "__main__":
   app.run(debug=True)
   