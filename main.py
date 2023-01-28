from flask import Flask, render_template

application = Flask(__name__)


@application.route("/home/")
def get_home():
    return render_template("home.html")


@application.route("/about/")
def get_about():
    return render_template("about.html")


@application.route("/api/v1/<station>/<date>")
def get_weather_data(station, date):
    temperature = 12
    return {"station": station,
            "date": date,
            "temperature": f"{temperature}"}


if __name__ == "__main__":
    application.run(debug=True, port=8080)
