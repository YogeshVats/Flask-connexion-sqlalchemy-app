# app.py this is the main application

from flask import render_template, abort # Remove: import Flask

import config
from models import Person


app = config.connex_app
app.add_api(config.basedir / "swagger_third.yml")


@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home_third.html", people=people)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)      # Flask’s development server defaults to host 127.0.0.1 
                                                        # and port 5000