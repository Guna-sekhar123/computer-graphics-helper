from flask import render_template
from application import app

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/drawingalgorithm')
def drawing_algorithm():
    return render_template('Drawingalgo.html')


@app.route('/tranformationalgorithm2d')
def trans_2d():
    return render_template('Transformation2d.html')


@app.route('/transformationalgorithm3d')
def trans_3d():
    return render_template('Transformation3d.html')
