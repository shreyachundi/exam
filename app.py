from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('register.html')
@app.route('/register',methods=['POST'])
def register():
    name=request.form["name"]
    email=request.form["email"]
    id=request.form["id"]
    year=request.form["year"]
    return render_template('success.html',name=name,email=email,id=id,year=year)
if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5003)