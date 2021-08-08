from flask import Flask, redirect, url_for, render_template, request 
import json
import pymongo
from pymongo import mongo_client
from pymongo import message


app = Flask(__name__)


#connecting to mongodb.

cluster = mongo_client.MongoClient("mongodb+srv://<username>:<pwd>@cluster0.ncyur.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["db"]

collection = db["users"]


@app.route("/")
def index():
    return render_template('index.html')



@app.route("/register", methods=["POST","GET"]) 
def home():
    if request.method == "POST":

        name = request.form["name"]
        district = request.form["district"]
        mail = request.form["email"]
        

        user_data = { "name": name , "d": district , "email": mail }

        check_user = collection.count_documents({"email": mail})

        print(check_user)

        if(check_user):
            print("user already registered")
            return render_template("register.html",message="You are already Registered :)")

        else:
            collection.insert_one(user_data)
            return render_template("success.html",message="Congrats You are Registered !")

        
    
    else:
        return render_template("register.html")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/unsubscribe", methods=["POST","GET"])
def unsubscribe():
    if request.method == "POST":
        mail = request.form["email"]
        check_user = collection.count_documents({"email": mail})

        if(check_user):
            collection.delete_one({"email": mail})
            return render_template("success.html",message="You are unsubscriped now !")

        else:
            return redirect(url_for("unsubscribe.html",message="You are not registered !"))
                
    return render_template("unsubscribe.html")


@app.route("/about")
def about():
    return render_template("about.html")



if(__name__=="__main__"):
    app.run(debug=True)