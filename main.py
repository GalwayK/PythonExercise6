from flask import Flask, render_template
import pandas
import numpy

application = Flask(__name__)

station_list = []
station_file = pandas.read_csv("data/data_small/stations.txt", skiprows=17)
station_file = station_file[["STANAME                                 ", "STAID"]]

@application.route("/")
def get_home():
    return render_template("home.html", data=station_file)


@application.route("/about/")
def get_about():
    return render_template("about.html")


@application.route("/api/v1/<station>/<date>")
def get_weather_data(station, date):
    station_file = f"data/data_small/TG_STAID{str(station).zfill(6)}.txt"

    df = pandas.read_csv(station_file, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10

    station_dict = {"station": station_file,
                    "date": date,
                    "temperature": f"{temperature}"
                    }

    return station_dict


if __name__ == "__main__":
    application.run(debug=True, port=8080)
