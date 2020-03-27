from flask import Flask, redirect, url_for, request,render_template
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



# @app.route('/admin')
# def admin():
#    return 
if __name__ == '__main__':
   app.run(debug = True)


