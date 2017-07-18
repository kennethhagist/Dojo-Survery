from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    print request.form
    return render_template("result.html", user = request.form)

app.run(debug=True)
