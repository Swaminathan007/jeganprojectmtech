from flask import *
grades = {
    "M30":{250:150,300:200},
    "M35":{200:150,300:175},
    "M40":{200:150,300:200}
}
app =Flask(__name__)
app.config["SECRET_KEY"] = "1234"
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/recovery")
def recovery():
    minmax = []
    for i in grades:
        keys = list(grades[i].keys())
        print(keys)
        minmax.append([i,keys[0],keys[1]])
    return render_template("recovery.html",minmax=minmax)
@app.route("/<grade>/<op>")
def hetspacing(grade,op):
    spacing = None
    keys = list(grades[grade].keys())
    if(op == "min"):
        spacing = grades[grade][keys[0]]
    else:
         spacing = grades[grade][keys[1]]
    return render_template("rodthickness.html",spacing=str(spacing))
@app.route("/power")
def power():
    return "<h1>Power</h1>"
app.run(debug=True,host="0.0.0.0")