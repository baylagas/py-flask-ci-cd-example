from flask import Flask
from routes.main_routes import MainRoutes

app = Flask(__name__)
MainRoutes.configure_routes(app)

if __name__ == "__main__":
    app.run()
