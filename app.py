from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Render!"

# no need for `if __name__ == '__main__'` when using gunicorn
