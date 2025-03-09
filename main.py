from flask import Flask, render_template,request,session,url_for,redirect,flash
import sqlite3 as sql
import os
from os.path import join, dirname, realpath
from flask_sqlalchemy import SQLAlchemy

UPLOADS_PATH = join(dirname(realpath(__file__)), 'static\\images')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/register")
def registration():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/flight")
def fly():
    return render_template("flightbooking.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/destination")
def dest():
    return render_template("destination.html")

@app.route("/package")
def pack():
    return render_template("package.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/404")
def issue():
    return render_template("404.html")

@app.route("/contact1")
def con():
    return render_template("contact1.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/confirm")
def confir():
    return render_template("confirm.html")

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/booking")
def booking():
    return render_template("booking.html")

@app.route("/forgotten")
def forgotten():
    return render_template("forgotten.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

@app.route("/darma")
def darma():
    return render_template("dramastala.html")

@app.route("/mysore")
def mysore():
    return render_template("mysure.html")

@app.route("/tamil")
def tamil():
    return render_template("tamilnadu.html")

@app.route("/bengaluru")
def bengaluru():
    return render_template("bengaluru.html")

@app.route("/goa")
def goa():
    return render_template("goa.html")

@app.route("/tha")
def tha():
    return render_template("thailand.html")

@app.route("/male")
def male():
    return render_template("malaysia.html")

@app.route("/andra")
def andra():
    return render_template("andrapradesh.html")

@app.route("/feed")
def feed():
    return render_template("feedback.html")

@app.route("/indo")
def indoo():
    return render_template("indonisia.html")

@app.route("/aust")
def aust():
    return render_template("austrila.html")

@app.route("/regAction", methods = ["GET","POST"])
def regAction():
    msg=None
    if(request.method=="POST"):
        if (request.form["username"]!="" and  request.form["email"]!=""and request.form["password"]!=""and request.form["phone"]!=""):
            username = request.form["username"]
            
            email = request.form["email"]
            password = request.form["password"]
            phone = request.form["phone"]
                       
            with sql.connect("base1.db") as con:
                c=con.cursor()
                c.execute("INSERT INTO  register1(username,email,password,phone) VALUES('"+username+"','"+email+"','"+password+"','"+phone+"')")
                msg = "Register Details submitted successfully"

                con.commit()
        else:
            msg="Something went wrong"
        flash("DETAILS SAVED SUCCESSFULLY")
        return render_template("login.html", msg=msg)
           
@app.route("/loginAction",methods=['GET','POST'])
def loginAction():
    msg=None
    if (request.method == "POST"):
        email= request.form['email']
      
        password = request.form['password']
        
        with sql.connect("base1.db") as con:
            c=con.cursor()
            c.execute("SELECT email,password  FROM register1 WHERE email = '"+email+"' and password ='"+password+"'")
            r=c.fetchall()
            for i in r:
                if(email==i[0] and password==i[1]):
                    session["logedin"]=True
                    session["email"]=email
                    flash("LOGIN SUCCESSFULL")
                    return redirect("/index")         
                else:
                    msg= "please enter valid username and password"
                    flash("LOGIN UNSUCCESSFULL")
            return render_template("error.html",msg=msg) 
        

@app.route("/order", methods = ["GET","POST"])
def book():
    msg=None
    if(request.method=="POST"):
        if (request.form["yourname"]!="" and request.form["youremail"]!=""and request.form["date"]!=""and request.form["message"]!=""):
            yourname = request.form["yourname"]
            youremail = request.form["youremail"]
            date = request.form["date"]
            message = request.form["message"]
                       
            with sql.connect("base1.db") as con:
                c=con.cursor()
                c.execute("INSERT INTO  book(yourname,youremail,date,message) VALUES('"+yourname+"','"+youremail+"','"+date+"','"+message+"')")
                msg = "Register Details submitted successfully"

                con.commit()
        else:
            msg="Something went wrong"
        flash("DETAILS SAVED SUCCESSFULLY")
        return render_template("confirm.html", msg=msg)
    

@app.route("/flightbooking", methods = ["GET","POST"])
def bookings():
    msg=None
    if(request.method=="POST"):
        if (request.form["ffrom"]!="" and request.form["fto"]!=""and request.form["dep"]!=""and request.form["freturn"]!=""and request.form["round"]!=""and request.form["oneway"]!=""):
            ffrom = request.form["ffrom"]
            fto = request.form["fto"]
            dep = request.form["dep"]
            freturn = request.form["freturn"]
            round = request.form["round"]
            oneway = request.form["oneway"]
                       
            with sql.connect("base1.db") as con:
                c=con.cursor()
                c.execute("INSERT INTO  flightbooking(ffrom,fto,dep,freturn,round,oneway) VALUES('"+ffrom+"','"+fto+"','"+dep+"','"+freturn+"','"+round+"','"+oneway+"')")
                msg = "Register Details submitted successfully"

                con.commit()
        else:
            msg="Something went wrong"
        flash("DETAILS SAVED SUCCESSFULLY")
        return render_template("confirm.html", msg=msg)


@app.route("/feedback", methods = ["GET","POST"])
def feedbacking():
    msg=None
    if(request.method=="POST"):
        if (request.form["feedname"]!="" and request.form["feedemail"]!=""and request.form["subject"]!=""and request.form["feedmessage"]!=""):
            feedname = request.form["feedname"]
            feedemail = request.form["feedemail"]
            subject = request.form["subject"]
            feedmessage = request.form["feedmessage"]
                       
            with sql.connect("base1.db") as con:
                c=con.cursor()
                c.execute("INSERT INTO  feedback(feedname,feedemail,subject,feedmessage) VALUES('"+feedname+"','"+feedemail+"','"+subject+"','"+feedmessage+"')")
                msg = "Register Details submitted successfully"

                con.commit()
        else:
            msg="Something went wrong"
        flash("DETAILS SAVED SUCCESSFULLY")
        return render_template("feedback.html", msg=msg)
    
@app.route("/feedback2", methods = ["GET","POST"])
def feedbacking2():
    msg=None
    if(request.method=="POST"):
        if (request.form["feedname"]!="" and request.form["feedemail"]!=""and request.form["subject"]!=""):
            feedname = request.form["feedname"]
            feedemail = request.form["feedemail"]
            subject = request.form["subject"]
            
                       
            with sql.connect("base1.db") as con:
                c=con.cursor()
                c.execute("INSERT INTO  feedback(feedname,feedemail,subject) VALUES('"+feedname+"','"+feedemail+"','"+subject+"')")
                msg = "Register Details submitted successfully"

                con.commit()
        else:
            msg="Something went wrong"
        flash("DETAILS SAVED SUCCESSFULLY")
        return render_template("feedback.html", msg=msg)

@app.route("/adminreh")
def admin_logiiin():
    return render_template("adminreh.html")

@app.route("/admin_login")
def admin_login():
    return render_template("adminlogin.html")

@app.route("/regActionnn", methods = ["GET","POST"])
def regActiooon():
    msg=None
    if(request.method=="POST"):
        if (request.form["username"]!="" and   request.form["password"]!=""):
            username = request.form["username"]
            password = request.form["password"]
            
            with sql.connect("base1.db") as con:
                c=con.cursor()
                c.execute("INSERT INTO  admin(username,password) VALUES('"+username+"','"+password+"')")
                msg = "Register Details submitted successfully"
                con.commit()
        else:
            msg="Something went wrong"
        flash("DETAILS SAVED SUCCESSFULLY")
        return render_template("adminlogin.html", msg=msg)
    
    
             
@app.route("/admin_login_action", methods=['POST'])
def admin_login_action():
    msg = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        with sql.connect("base1.db") as con:
            c = con.cursor()
            c.execute("SELECT username, password FROM admin WHERE username = ? AND password = ?", (username, password))
            admin = c.fetchone()
            if admin:
                session["admin_logged_in"] = True
                session["admin_username"] = username
                flash("Admin login successful")
                return redirect(url_for('admin_dashboard'))
            else:
                msg = "Invalid credentials"
                flash("Admin login unsuccessful")
    return render_template("adminlogin.html", msg=msg)

@app.route("/admin_dashboard")
def admin_dashboard():
    if "admin_logged_in" not in session:
        return redirect(url_for('adminlogin'))

    with sql.connect("base1.db") as con:
        c = con.cursor()
        c.execute("SELECT email FROM register1")
        users = c.fetchall()
    return render_template("admin_dashboard.html", users=users)

@app.route("/delete_user", methods=['POST'])
def delete_user():
    if "admin_logged_in" not in session:
        return redirect(url_for('adminlogin'))
    
    email = request.form['email']
    with sql.connect("base1.db") as con:
        c = con.cursor()
        c.execute("DELETE FROM register1 WHERE email = ?", (email,))
        con.commit()
        flash("User deleted successfully")
    return redirect(url_for('admin_dashboard'))

@app.route("/logout")
def logout():
    session.pop("admin_logged_in", None)
    session.pop("admin_username", None)
    flash("Logged out successfully")
    return redirect(url_for('admin_login'))










if __name__ == "__main__":
    app.run(debug=True)
