from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.sighting import Sighting
from flask_app.models.user import User
from flask_bcrypt import Bcrypt


@app.route('/make')
def report():
    x = session['user']
    y = session['name']
    return render_template('sightings.html', x = x , name = y )


############################################################################

@app.route('/add_site', methods = ['POST'])
def add():
    data = {
        'location' : request.form['location'],
        'what' : request.form['what'],
        'date' : request.form['date'],
        'number': request.form['number'],
        'User_id': request.form['User_id'],
        'reported': request.form['reported']
    }
    if not Sighting.validate(request.form):
        return redirect('/make')
    Sighting.create(data)
    num = session['user']
    return redirect(f'/dashboard/{num}')


    ############################################################################

@app.route('/del/<int:num>')
def get_rid(num):
    data = {'id' : num}
    Sighting.delete(data)
    x = session['user']
    return redirect(f'/dashboard/{x}')


@app.route('/edit/<int:num>')
def update(num):
    data = {'id' : num}
    edit = Sighting.retrieve_by(data)

    return render_template('update.html' , name =  session['name'], update = edit, x = session['user'], y = num)

######################################################################################


@app.route('/update_rec', methods =['POST'])
def edit():
        data = {
        'location' : request.form['location'],
        'what' : request.form['what'],
        'date' : request.form['date'],
        'number': request.form['number'],
        'reported': request.form['reported'],
        'id': request.form['id']
    }
        if not Sighting.validate(request.form):
            x = session['user']
            return redirect(f"/update/{request.form['id']}")
        Sighting.up(data)
        x = session['user']
        return redirect(f'dashboard/{x}')
##############################################################################

@app.route('/see/<int:num>')
def see(num):
    data = {'id': num}
    y = Sighting.retrieve_by(data)
    name = session['name']
    x = session['user']

    return render_template("site.html", it = y, name = name, x = x)
