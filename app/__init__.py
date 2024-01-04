from flask import Flask
from app.routes import home, dashboard
from app.db import init_db
from app.utils import filters

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

    app.jinja_env.filters['format_url'] = filters.format_url
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural

    init_db(app)

    return app

# Run the app if this script is executed
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)