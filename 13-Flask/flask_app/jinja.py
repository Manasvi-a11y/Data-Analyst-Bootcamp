from flask import Flask,render_template,request,redirect,url_for

'''
It creates an instance of the Flask class,
which will be your WSGI (web Server Gateway Interface) application
'''
##WSGI APPLICATION
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html>H1>Welcome to the flask course</H1<html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit',methods=['GET','POST'])
def form():
     if request.method=='POST':
       name=request.method['name']
       return f'Hello{name}!'
     return render_template('form.html')

##Variable Rule
@app.route('/success/<int:score>')
def success(score):
   res=""
   if score>=50:
       res="Passed"
   else:
       res="Failed"

       return render_template('result.html',results=res)


##Variable Rule
@app.route('/successres/<int:score>')
def successres(score):
   res=""
   if score>=50:
       res="Passed"
   else:
       res="Failed"

       result_data={'score': score,"res":res}

       return render_template('result.html',results=result_data)


@app.route('/fail/<int:score>')
def fail(score):
   

 return render_template('result.html',results=score)
   
@app.route('/submit', methods=['POST','GET'])
def submit(): 
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
        return redirect(url_for('successres',score=total_score))


if __name__== "__main__":
    app.run(debug=True)