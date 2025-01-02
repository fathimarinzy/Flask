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
    u=request.args.get('username')
    p=request.args.get('password')
    return f"username is {u},password is {p}"
    














if __name__=="__main__":
    app.run(debug=True)