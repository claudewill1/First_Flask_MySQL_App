from flask import Flask, render_template, request, redirect, session
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html",all_friends = friends)

@app.route("/create_friend",methods=["POST"])
def create_friend():
    # first we make a data dictionary from our request.form coming from out template
    # the keys in data need to liine up exactly with the variables in our query string
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "occ": request.form["occ"]
    }
    # we pass the data dictionary into the save method from the friend class
    Friend.save(data)
    # Don't forget to redirect after saving to the database
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)