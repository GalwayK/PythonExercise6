from flask import Flask, render_template

application = Flask("Test Website")


@application.route("/home/")
def get_home():
    return render_template("tutorial.html")


@application.route("/about/")
def get_about():
    return render_template("about.html")


application.run(debug=True)
