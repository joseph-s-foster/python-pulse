from flask import Flask
from app.routes import home, dashboard

def create_app(test_config=None):
    # set up app config
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )

    # Register blueprints
    app.register_blueprint(home)
    app.register_blueprint(dashboard)

    return app

# Run the app if this script is executed
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
