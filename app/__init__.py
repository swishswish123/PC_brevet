from flask import Flask
from app.config import ProdConfig

def create_app(config_class = ProdConfig):

    app = Flask(__name__, template_folder='../templates')
    # app.config.form_object(config_class)
    from app.routes import bp_main
    app.register_blueprint(bp_main)

    return app