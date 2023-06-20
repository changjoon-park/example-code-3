from flask import Flask

def create_app() -> Flask:
    # Initialize the core application
    app = Flask(__name__)

    # Register Blueprints
    from .views import main_view
    app.register_blueprint(main_view.bp)

    return app
