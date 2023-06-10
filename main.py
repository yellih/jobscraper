from flask import Flask, render_template, request, redirect
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="user")

db = {}

@app.route("/search")
def search():
    # print(request.args)
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:   
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = indeed + wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword is not db:
        redirect(f"/search?keyword={keyword}")
app.run("0.0.0.0")