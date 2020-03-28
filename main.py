
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

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['un']
      password = request.form['pw']
      if user.__eq__('admin') and password.__eq__('ad123'):
         return redirect(url_for('admin'))
   else:
      user = request.args.get('un')
      password = request.args.get('pw')
      
      return redirect(url_for('success',name = user))

open_connection()

if __name__ == "__main__":
   app.run(debug=True)