from flask import Flask,render_template, request
from stories import story
app = Flask(__name__)

@app.route("/")
def hello_world():
    prompts = story.prompts
    return render_template("form.html", prompts=prompts)

@app.route("/story")
def create_story():
    text = story.generate(request.args)
    return render_template("story.html", text = text)
    
if __name__ == '__main__':  
   app.run()