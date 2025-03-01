from flask import Flask
from routes import bp as routes_bp

app = Flask(__name__, template_folder= "pages")
app.config["SECRET_KEY"] = "random string"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

#Registra rotas no app por blueprint
app.register_blueprint(routes_bp)

#Debug Mode
if __name__ == '__main__':
    app.run(debug=True, port=5000) 