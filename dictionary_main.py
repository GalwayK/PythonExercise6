import pandas
from flask import Flask, render_template

application = Flask(__name__)

df = pandas.read_csv("data/dictionary.csv")


@application.route("/dict_about")
def get_dictionary_about_page():
    return render_template("dictionary_documentation.html")


@application.route("/dict/<word>")
def get_dictionary_word(word):
    definition = df.loc[df["word"] == word]["definition"].squeeze()
    word_dict = {"word": word,
                 "definition": definition}
    return word_dict


application.run(debug=True, port=8081)

