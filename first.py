from flask import *
app=Flask(__name__)


@app.route("/")
def one():
    return "welcome home"


@app.route("/x")
def two():
    return "hello world  !!!"



@app.route("/xx/<name>")
def three(name):
    return "name is %s"%name


@app.route("/yy/<int:age>")
def four(age):
    return "age is %d"%age


@app.route("/zz/<int:age><name>")
def five(name,age):
    # return "age is %d"%age+"name is %s"%name
    return f"name is{name} age is{age}"

@app.route("/m/<name>/<int:age>/<course>/<float:salary>")
def six(name,age,course,salary):
  
    return f"name is{name} age is{age} courseis{course} salary is {salary}"





@app.route("/ones")
def ones():
    return "welcome to one"

@app.route("/second")
def second():
    return redirect(url_for("ones"))


#task

@app.route("/admin")
def  admin():
    return "welcome admin"

@app.route("/student")
def student():
    return "welcome student"

@app.route("/teacher")
def teacher():
    return "welcome teacher"

@app.route("/user/<name>")
def user(name):
    return redirect(url_for(name))
    



@app.route("/postdata",methods=['POST'])
def new():
    u=request.form['username']
    p=request.form['password']
    return "username is %s" %u +"password is %s"%p
    
# get method case

@app.route("/postdata1",methods=['GET'])
def new1():
    u=request.args('username')
    p=request.args('password')
    return f"username is {u},password is {p}"
    

# to pass html page
@app.route("/first")
def first():
    return render_template("first.html")


# to pass values html page
@app.route("/sec")
def sec():
    a="flask"
    b=[10,20,30,40,50]
    c=""
    return render_template("first.html",data=a,value=b,view=c)

# multiplication table
@app.route("/mul/<int:num>")
def mul(num):
    a=num
    return render_template("mul.html",data=a)


@app.route("/tem")
def tem():
    return render_template("new.html")

#form pasing case
@app.route("/form")
def form():
    return render_template("form.html")
    

@app.route("/view",methods=['POST'])
def view():
    f=request.form['fname']
    l=request.form['lname']
    a=request.form['age']
    e=request.form['email']
    p=request.form['phone']
    return render_template("view.html",fname=f,lname=l,age=a,email=e,phone=p)


#file passing case

@app.route("/file")
def file():
    return render_template("file.html")


@app.route("/viewfile",methods=['POST'])
def viewfile():
    if request.method=="POST":
        f=request.files['file']
        f.save(f.filename)
        return "file successfuly saved"









if __name__=="__main__":
    app.run(debug=True)