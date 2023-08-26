# app.py this is the main application

from flask import render_template, abort # Remove: import Flask

import connexion


app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger_first.yml")


@app.route("/")
def home():
    return render_template("home_first.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)      # Flask’s development server defaults to host 127.0.0.1 
                                                        # and port 5000