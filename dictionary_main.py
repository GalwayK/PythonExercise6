from flask import Flask, render_template

application = Flask(__name__)


@application.route("/dict_about")
def get_dictionary_about_page():
    return render_template("dictionary_documentation.html")


@application.route("/dict/<word>")
def get_dictionary_word(word):
    word_dict = {"word": word,
                 "definition": word.upper()}
    return word_dict


application.run(debug=True, port=8081)

