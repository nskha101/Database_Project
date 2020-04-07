
from flask import Flask, redirect, url_for, request,render_template
import psycopg2
from scripts import *  


app = Flask(__name__)
h_info ={}


@app.route("/")
def home():
   return render_template("login.html")

 
@app.route('/process_query',methods =['POST'])
def process_query():
   q = request.form['sql_command']
   return str(query(q))

@app.route('/admin')
def admin():

   return render_template('admin.html')

@app.route('/host/<name>')
def host_name(name):
   return render_template('host.html',name=name)


@app.route('/view_bnbs')
def view_bnbs():

   return 
   # return a table of bnbids/

# advanture list, exterpeice list, stay list
@app.route('/view_profile' , methods=['POST'])
def view_profile():
   global h_info 
   if (h_info == {} or len(h_info)== 1) and len(request.form)!=1:
      h_info = request.form
   elif h_info  != request.form:
      h_info = request.form
   try:
      return render_template('profile.html',info=h_info)
   except Exception as e:
      return "please update your profile first"

@app.route('/update_info')
def update_info():
   return render_template("host_info.html")

@app.route('/update_bnb',methods=['POST'])
def update_bnb():
   return render_template('host_upload.html')

@app.route('/host_upload',methods=['POST'])
def host_upload():
   name = request.form['property_name']
   email = request.form['email']
   location = request.form['location']
   duration = request.form['duration']
   maxsize = request.form['maxsize']
   language = request.form['language']
   description = request.form['description']
   rentaltype = request.form['type']
   rules = request.form['rules']
   cost = request.form['cost']
   availability = request.form['available']
   contact = request.form['host']
   uploadlisting(name, email, location, duration, maxsize, language, description, rentaltype, rules, cost, availability, contact)
   return render_template('host.html')

@app.route('/guest/<name>')
def guest_name(name):
   return render_template('guest.html', name=name)

@app.route('/occupancy_rate',methods=['POST'])
def occupancy_rate():
   bid = str(request.form['bnbid'])
   return occupancyrate(bid)

@app.route('/employee/<name>')
def employee_name(name):
   return render_template('employee.html',name=name)

# contact jeff

@app.route('/search_result' , methods=['POST','GET'])
def search_result():
    
   search_param = request.form['search_box']
   search_type = request.form['search_by']
   res = searchbnb(search_type,search_param)
   return render_template('search_result.html',my_list=res)

@app.route('/login',methods = ['POST','GET'])
def login():

   error=''
   try:

      if request.method == 'POST':
         user = request.form['un']
         password = request.form['pw']
         option = request.form['options']
         if user.__eq__('admin') and password.__eq__('ad123') and option == 'admin':
            return redirect(url_for('admin'))
         elif user.__eq__("guest") and password.__eq__('guest123') and option == 'guest' :
            return redirect(url_for("guest_name", name=user))
         elif user.__eq__("host") and password.__eq__('host123') and option == 'host':
            return redirect(url_for("host_name",name=user))
         elif user.__eq__("employee") and password.__eq__('em123') and option == 'employee' :
            return redirect(url_for("employee_name", name=user))   
         else:
            error='Invalid username or password, please try again!'
      return render_template('login.html',error=error)

   except Exception as ex:
      return render_template('login.html',error=error)



if __name__ == "__main__":
   app.run(debug=True)
   