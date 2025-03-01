from flask import Flask

#Local Imports
from routes import bp as routes_bp

app = Flask(__name__, template_folder= "pages")
app.config["SECRET_KEY"] = "random string"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

#Register routes Blueprint
app.register_blueprint(routes_bp)

#Starts server in debug mode
if __name__ == '__main__':
    app.run(debug=True, port=5000) 