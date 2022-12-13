from flask import Flask, render_template
from utils import *

app = Flask(__name__, template_folder='templates')


@app.route('/')
def all_candidates():
    candidates = []
    for i in get_all():
        candidates.append(i["name"])
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<id>')
def candidate(id):
    candidate = get_by_id(int(id))
    return render_template('card.html', name=candidate["name"], position=candidate["position"],
                           picture=candidate['picture'], skills=candidate["skills"])


@app.route("/search/<name>")
def search_by_name(name):
    candidates: list[dict] = get_by_name(name)
    return render_template('search.html', candidates=candidates, amount=len(candidates))

@app.route("/skill/<skill>")
def search_by_skill(skill):
    candidates: list[dict] = get_by_skill(skill)
    return render_template('skill.html', candidates=candidates, skill=skill, amount=len(candidates))

app.run()
