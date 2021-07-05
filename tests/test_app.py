from flask import Flask
from routes.main_routes import MainRoutes


def test_index():
    app = Flask(__name__, template_folder="../src/templates/")
    MainRoutes.configure_routes(app)
    with app.test_client() as client:
        result = client.get("/")
        assert "this is my main" in str(result.data)
