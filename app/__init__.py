from  flask import Flask

app = Flask(__name__)

from app.views import index 
from app.models import Contato
