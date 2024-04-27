from flask import Flask, render_template, request
from chatgpt import get_response

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return render_template("index.html")

# Define route for home page
@app.route("/get", methods=["GET", "POST"])
def gpt_response():
    user_request = request.args.get('msg')
    return str(get_response(user_request))

if __name__ == "__main__":
    app.run()