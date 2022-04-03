from flask import Flask,render_template,redirect,request,url_for,session

app = Flask(__name__)
post = [1,2,3,4,4]
var=0
# sess = session()
app.secret_key = "super secret key"

@app.route("/",methods=["POST","GET"])
def login():
    if(request.method=="POST"):
        USERfname = request.form["fname"]
        USERlname = request.form["lname"]
        session["fname"] = USERfname
        session["lname"] = USERlname
        # return render_template("onpostrender.html",fname=USERfname,lname=USERlname)
        return redirect(url_for("user"))
    else:
        print("hi there 2")
        if "fname" in session:
            return redirect(url_for("user"))
        else:
            print("hi there 3")
            return render_template("home.html",title="home")




        # return render_template("home.html",title="home",var=var)

@app.route("/user",methods=["GET","POST"])
def user():
    print("in user")
    if(request.method == "POST" and session["page"]=="login"):
        print("i am here")
        return redirect(url_for("logout"))
    if(request.method == "POST" and session["page"]=="logout"):
        return redirect(url_for("logout"))
    if "fname" in session:
        if(session["fname"]=="keval"):
            print("pleasee enjoy")
            session["page"]= "login"
            return render_template("prizepic.html")

        else:
            print("sorry keval you cant have this")
            session["page"] = "logout"
            return render_template("nonlogonpage.html")
    else:
        return redirect(url_for("login"))

    # return render_template("base.html",title="base",myname="kevalkishan")
    # return
@app.route("/logout")
def logout():
    session.pop("fname",None)
    print("hi there1")
    return redirect(url_for("login"))
if(__name__=="__main__"):

    app.run()
