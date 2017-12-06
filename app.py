from flask import Flask, render_template, request, redirect
from helper.realitycheck import reality_check

app = Flask('RC')
@app.route('/')
def index():
	return render_template('main.html')


app.run(debug=True)
