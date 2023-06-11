from flask import Flask, render_template, redirect, request, session, jsonify
from datetime import datetime

# # Instantiate Flask object named app
app = Flask(__name__)

# # Configure sessions
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"]="/Volumes/mac/python/flask_session"


@app.route("/<template>.html")
def index(template):
   # raise Exception("Sorry, not allowed to hit index.html")
   print(template)
   return render_template (template+".html")

@app.route("/<folder>/<template>.html")
def html_template(template,folder):
   # raise Exception("Sorry, not allowed to hit index.html")
   print(template,folder)
   return render_template ( folder + "/"+ template+".html")



# Only needed if Flask run is not used to execute the server
if __name__ == "__main__":
   app.run( host='0.0.0.0', port=8080)
