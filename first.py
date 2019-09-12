from flask import Flask,render_template,url_for,request
from form import RegistrationForm,LoginForm
import requests
app=Flask(__name__)
app.config['SECRET_KEY']='af4c76322516d4273b7624476bf410ef'


@app.route("/")
def index():
	return render_template("bootstrap.html")




@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register',form=form)




@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form=form)


@app.route("/search")
def search1():
    form = LoginForm()
    return render_template('search.html')    




@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=d6da3f12fde1216d906420bd83085fc8')
    json_object = r.json()

    #return json_object
    temp_k = float(json_object['main']['temp'])
    temp_f = (temp_k - 273.15) * 1.8 + 32
    return render_template('weatherzip1.html',temp=temp_f)    



if ( __name__ =="__main__" ):
	app.run(debug=True)	