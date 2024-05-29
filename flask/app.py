from flask import Flask
# wsgi application
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome To My World "

@app.route('/members')
def members():
    return "Hello Members"


if __name__=='__main__':
    app.run(debug=True)