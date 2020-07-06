from flask import Flask, url_for
from admin.firstBlueprint import first

app = Flask(__name__)
app.register_blueprint(first, url_prefix="/admin")


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
