from flask import *
import mysql.connector 
mydb = mysql.connector.connect(host="localhost",username="root",password="1234",database="civilproject")
cur = mydb.cursor()
app =Flask(__name__)
app.config["SECRET_KEY"] = "1234"
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/recovery")
def recovery():
    cur.execute("select * from recoveryboiler")
    recs = cur.fetchall()
    grades = []
    for i in recs:
        grades.append([i[0],i[1],i[3]])
    return render_template("recovery.html",grades = grades)
@app.route("/<grade>/<op>")
def jfi(grade,op):
    spacing = None
    if(op == "min"):
        cur.execute(f"select rod_min from recoveryboiler where grade = '{grade}'")
        spacing = cur.fetchall()[0][0]
    else:
        cur.execute(f"select rod_max from recoveryboiler where grade = '{grade}'")
        spacing = cur.fetchall()[0][0]
    return render_template("rodthickness.html",spacing=str(spacing))
@app.route("/power")
def power():
    return "<h1>Power</h1>"
app.run(debug=True,host="0.0.0.0")