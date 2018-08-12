from flask import Flask, render_template, redirect, request, flash
app = Flask(__name__)
app.secret_key='blahblah'

@app.route('/')
def dojosurvey():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    error = False
    if request.form['your_name'] == "":
        flash("Name cannot be blank")
        error = True
    if len(request.form['location']) < 1:
        flash("Location cannot be blank")
        error = True
    if len(request.form['favorite_language']) < 1:
        flash("Favorite Language cannot be blank")
        error = True
    if len(request.form['comment']) > 120:
        flash("comment must be less than 120 characters")
        error = True
    if error == False:
        flash('success!')
    else:
        print request.form
    return render_template('results.html')


app.run(debug=True)