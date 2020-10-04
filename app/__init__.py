from app.config import ProdConfig, DevConfig
from flask import Flask


def create_app(config_classname):

    app = Flask(__name__, template_folder='../templates')
    # app.config.form_object(config_class)
    app.config.from_object(config_classname)
    from app.routes import bp_main
    app.register_blueprint(bp_main)

    return app
