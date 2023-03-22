from flask import Flask, render_template, redirect, request, session, jsonify
from datetime import datetime

# # Instantiate Flask object named app
app = Flask(__name__)

# # Configure sessions
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"]="/Volumes/mac/python/flask_session"


@app.route("/")
def index():
     return render_template ( "index.html")



# Only needed if Flask run is not used to execute the server
if __name__ == "__main__":
   app.run( host='0.0.0.0', port=8080)
