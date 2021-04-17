import dotenv
from flask import Flask

# Load .env config
dotenv.load_dotenv()

app = Flask(__name__)

from caesar import routes