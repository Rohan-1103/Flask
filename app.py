from flask import Flask, render_template, request, redirect, url_for, jsonify

## Create a simple flask application
app = Flask(__name__)

### Flask App Routing
# @app.route("path", method=["GET(default)"/"POST"/"PUT"])
@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to Krish Naik hindi Channel"

@app.route("/index", methods=["GET"])
def index():
    return "<h2>Welcome to the Index page</h2>"

### Variable rule
@app.route("/success/<int:score>")
def success(score):
    return "The person has passed and the score is: " + str(score)

@app.route("/failure/<int:score>")
def failure(score):
    return "The person has failed and score is: " + str(score)

@app.route("/form", methods = ["GET", "POST"])
def form():
    if request.method=="GET":
        # form.html should be in templates folder
        return render_template('form.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
        
        average_marks = (maths + science + history) / 3
        
        # sending score to html form
        # return render_template('form.html', score = average_marks)
        res = ""
        if average_marks >= 50:
            res = "success"
        else:
            res = "failure"
        return redirect(url_for(res, score = average_marks))

# creating api
@app.route("/api", methods = ["POST"])
def calculate_sum():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    return jsonify(a_val + b_val)

if __name__=="__main__":
    app.run(debug = True)