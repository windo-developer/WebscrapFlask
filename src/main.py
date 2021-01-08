from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("Scrapper Server")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    search = request.args.get('search')
    if search:
        search = search.lower()
        fromDb = db.get(search)
        if fromDb:
            jobs = fromDb
        else:
            jobs = get_jobs(search)
            db[search] = jobs
    else:
        return redirect("/")

    return render_template("report.html", searchingBy=search, resultsNumber=len(jobs), jobs=jobs)


app.run()
