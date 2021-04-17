import dotenv
from flask import Flask

# Load .env config
dotenv.load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello world</h1>"

if __name__ == "__main__":
    app.run()