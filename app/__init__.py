from flask import Flask
from app.config import DevConfig

# initialize app
app = Flask(__name__,instance_relative_config = True)

# set up config
app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

from app import views







# def create_app(config_name):
    
#     app = Flask(__name__)
    
#     app.config.from_object(config_options[config_name])
#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)
    
    
#     from .request import configure_request
#     configure_request(app)
    
#     return app