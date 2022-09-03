from flask import Flask, request, make_response, redirect, abort

app = Flask(__name__)


@app.route("/")
def index():
    abort(404)
    return redirect("https://google.com/search?q=1+1")
    response = make_response("<h1>This is the response</h1>")
    response.set_cookie('answer', '42')
    return response


@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, {}</h1>".format(name)


if __name__ == "__main__":
    app.run(debug=True)
