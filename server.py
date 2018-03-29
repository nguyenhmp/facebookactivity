from flask import Flask, render_template, session, redirect, request, flash
from mysqlconnection import MySQLConnector 
app = Flask(__name__)
app.secret_key = "my secret key"
mysql = MySQLConnector(app, "facebook1pymarch20186pm")

# print mysql.query_db("SELECT * FROM users")[0]["pw"]
@app.route("/")
def index():
    if "logged_id" in session:
        return redirect("/dashboard")
    return render_template("index.html")

@app.route("/users", methods=["POST"])
def users():
    form_data = request.form
    action = form_data["action"]
    if action == "register":
        errors = []
        first_name = form_data["first_name"]
        last_name = form_data["last_name"]
        username = form_data["username"]
        pw = form_data["pw"]
        
        if len(first_name) == 0:
            errors.append("first name cannot be blank")
        if len(first_name) >  256:
            errors.append("first name is to long(less than 256)")
        if len(last_name) == 0:
            errors.append("last name cannot be blank")
        if len(username) == 0:
            errors.append("username cannot be blank")
        if len(pw) == 0:
            errors.append("password cannot be blank")

        if len(errors) == 0:
            query = "INSERT INTO `users` (`first_name`, `last_name`, `username`, `pw`, `created_at`, `updated_at`) VALUES (:slot_one, :slot_two, :slot_three, :slot_four, now(), now());"
            data = {
                "slot_one":first_name,
                "slot_two":last_name,
                "slot_three":username,
                "slot_four":pw,
            }
            mysql.query_db(query, data)
            flash("successful registration!")
            return redirect("/")
        else:
            for message in errors:
                flash(message)
            return redirect("/")
    elif action == "login":
        #TODO
        #validate data
        #if data is valid, check if username exist
            #if username exist, check if password match
                #if both match, store id in session
        pass

        #redirect and display errors
    #do we need data to display the view

app.run(debug=True)