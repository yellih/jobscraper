from flask import Flask, render_template, request

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="user")

@app.route("/hello")
def hello():
    return 'hello you!'

@app.route("/search")
def search():
    # print(request.args)
    keyword = request.args.get("keyword")
    return render_template("search.html", keyword=keyword )

app.run("0.0.0.0")