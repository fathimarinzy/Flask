from flask import *
import sqlite3
app=Flask(__name__)
app.secret_key='abc'
from flask_mail import *

#cookie
@app.route("/setcookie")
def cookieset():
    r=make_response("cookie is set")
    r.set_cookie("flask","its a framework")
    return r


@app.route("/getcookie")

def cookieget():
    data=request.cookies.get('flask')
    return data


#session
@app.route("/setsession")
def sessionset():
    session['email']='abc@gmail.com'
    return make_response("session set")

@app.route("/getsession")
def getsession():
    r=session['email']
    return make_response(r)

@app.route("/delsession")
def delsession():
    session.pop('email')
    return make_response("session deleted")


# mail sending in flask
app.config['MAIL_SERVER']="smtp.gmail.com"
app.config["MAIL_PORT"]=465
app.config["MAIL_USERNAME"]='rinurinuzz01@gmail.com'
app.config['MAIL_PASSWORD']="egds nwix egyg nfxn"
app.config['MAIL_USE_SSL']=True


@app.route("/sendmail")
def mailsend():
    mail=Mail(app)
    msg=Message("flask",sender='rinurinuzz01@gmail.com',recipients=['akshaysuresh0504@gmail.com'])
    msg.body="this is a flask mail"
    mail.send(msg)
    return "mail sent"


# crud operations in flask
@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/get',methods=['POST'])
def getform():
    if request.method=="POST":
        f=request.form['fname']
        l=request.form['lname']
        a=request.form['age']
        e=request.form['email']
        con=sqlite3.connect("student.db")
        cursor1=con.cursor()
        cursor1.execute("insert into  student(firstname,lastname,age,email)values(?,?,?,?) ",(f,l,a,e))
        con.commit()
        return make_response("datas inserted successfully")


@app.route("/viewdata")
def viewdata():
    con=sqlite3.connect("student.db")
    con.row_factory=sqlite3.Row
    cursor1=con.cursor()
    cursor1.execute("select * from student")
    data=cursor1.fetchall()
  
    return render_template("viewstudent.html",view=data)


# to view without rowfactor method
# @app.route("/viewdata")
# def viewdata():
#     con=sqlite3.connect("student.db")
#     cursor1=con.cursor()
#     cursor1.execute("select * from student")
#     data=cursor1.fetchall()
#     for i in data:
#         # print(i)
#         # print(i[0])
#         print(i['firstname'])
#     return render_template("viewstudent.html",view=data)


#to delete
@app.route("/deletedata/<int:id>")
def deletedata(id):
    con=sqlite3.connect("student.db")
    cursor1=con.cursor()
    cursor1.execute(" delete from student where studid=%d"%id)
    con.commit()
    return make_response("datas deleted successfully")

@app.route("/editdata/<int:id>")
def editdata(id):
    con=sqlite3.connect("student.db")
    con.row_factory=sqlite3.Row
    cursor1=con.cursor()
    cursor1.execute("select * from student where studid=%d"%id)
    data=cursor1.fetchone()
    print(data)
    return render_template("editstudent.html",view=data)

#update
@app.route("/update/<int:id>",methods=["POST"])
def updatedata(id):
    if request.method=="POST":
        f=request.form['fname']
        l=request.form['lname']
        a=request.form['age']
        e=request.form['email']
        con=sqlite3.connect("student.db")
        cursor1=con.cursor()
        cursor1.execute("update student set firstname=?,lastname=?,age=?,email=? where studid=?",(f,l,a,e,id))
        con.commit()
        return make_response("updated successfully") 



















































if __name__=="__main__":
    app.run(debug=True)