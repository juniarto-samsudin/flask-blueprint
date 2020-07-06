from flask import Blueprint, render_template

first = Blueprint("firstBlueprint", __name__, static_folder="static", template_folder="template")

@first.route("/home")
@first.route("/")
def home():
    return render_template("home.html")

@first.route('/test')
def test():
    return "<h1>test</h1>"