from flask import Flask, render_template, Response, request, redirect, url_for
import rating
app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def rate_school():
    user_input = request.form["schoolSearch"]
    print(user_input)

    ratings = rating.rateSchool(user_input)

    return render_template("index.html", schools=ratings)
