from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolBarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "topsecret"

debug = DebugToolBarExtension(app)

@app.route("/")
def inputs():

    prompts = story.prompts
    return render_template("inputs.html", prompts=prompts)

@app.route("/story")
def make_story():
    text = story.generate(request.args)
    return render_template("story.html", text=text)t