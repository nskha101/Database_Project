
from flask import Flask, redirect, url_for, request,render_template
import psycopg2
from app import *


app = Flask(__name__)

@app.route("/")
def home():
   return render_template("login.html")


@app.route('/admin',methods=["POST"])
def admin():
   return render_template('admin.html')



@app.route('/host/<name>',methods=['POST'])
def host_name(name):
   return render_template('host.html',name=name)
@app.route('/guest/<name>',methods=["POST"])
def guest_name(name):
   return render_template('guest.html', name=name)



@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':

      user = request.form['un']
      password = request.form['pw']
      option = request.form['options']

      if user.__eq__('admin') and password.__eq__('ad123'):
         return redirect(url_for('admin'))
      elif user.__eq__("guest") and password.__eq__('guest123') :
         return redirect(url_for("guest_name", name=user))
      elif user.__eq__("host") and password.__eq__('host123'):
         return redirect(url_for("host_name"),name=user)
   else:
      user = request.args.get('un')
      password = request.args.get('pw')
      option = request.form['options']

      if user.__eq__('admin') and password.__eq__('ad123'):
         return redirect(url_for('admin'))
      elif user.__eq__("guest") and password.__eq__('guest123') and option.__eq__("guest"):
         return redirect(url_for("guest_name", name=user))
      elif user.__eq__("host") and password.__eq__('host123'):
         return redirect(url_for("host_name"),name=user)

# app.open_connection()

if __name__ == "__main__":
   app.run(debug=True)