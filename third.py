from flask import *
app=Flask(__name__)
app.secret_key='ab'



#flash
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/register",methods=['POST'])
def register():
    print("here")
    flash("you have registered succesfully!","success")
    print("there")
    return redirect(url_for('index'))

















if __name__=="__main__":
    app.run(debug=True)