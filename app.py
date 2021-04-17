from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/form-validation/")
def validation():
    return render_template('form-validation.html')

@app.route("/form-search/")
def search():
    return render_template('form-search.html')

@app.route("/form-search_expt/")
def search_expt():
    return render_template('form-search_expt.html')

@app.route("/form-register/")
def register():
    return render_template('form-register.html')

@app.route("/form-mini/")
def mini():
    return render_template('form-mini.html')

@app.route("/form-login/")
def login():
    return render_template('form-login.html')

@app.route("/Admins-Form/")
def adminsForm():
    return render_template('Admins-Form.html')