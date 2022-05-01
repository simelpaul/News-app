from flask import Flask
from .config import DevConfig

app = Flask(__name__)

#configuration setup
app.config.frm_object(DevConfig)

from app import views