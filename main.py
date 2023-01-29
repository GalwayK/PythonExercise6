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


@application.route("/api/v3/<station>/<year>")
def get_yearly_data(station, year):
    filename = f"data/data_small/TG_STAID{station.zfill(6)}.txt"
    df = pandas.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    yearly_data = df[df["    DATE"].str.startswith(str(year))]
    return yearly_data.to_dict(orient="records")


@application.route("/api/v2/<station>")
def get_station_data(station):
    filename = f"data/data_small/TG_STAID{station.zfill(6)}.txt"
    station_data = pandas.read_csv(filename, skiprows=20, parse_dates=["    DATE"]).to_dict(orient="records")
    return station_data


@application.route("/api/v1/<station>/<date>")
def get_weather_data(station, date):
    filename= f"data/data_small/TG_STAID{str(station).zfill(6)}.txt"

    df = pandas.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10

    station_dict = {"station": station_file,
                    "date": date,
                    "temperature": f"{temperature}"
                    }

    return station_dict


if __name__ == "__main__":
    application.run(debug=True, port=8080)
