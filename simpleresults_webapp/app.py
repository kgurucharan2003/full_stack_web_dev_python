from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/results/<int:score>')
def results(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    exp={'score':score,'res':res}
    return render_template('result.html', result=exp)

### Result checker HTML page
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science + maths + c + data_science) / 4
    return redirect(url_for('results', score=total_score))

if __name__ == '__main__':
    app.run(debug=True)
