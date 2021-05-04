from flask import Flask, render_template, send_from_directory, jsonify, send_file
import csv

app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')
# @app.route('/index.html')
# def index():
#     return render_template('index.html', the_title='Health in Yorkshire & Humber')

'''
@app.route('/data')
def get_csv():
    print('here')
    p = 't2dcomorbids_lineage.csv'
    f = open(p, 'r')
    return list(csv.DictReader(f))
'''

@app.route('/data/t2dcomorbids_lineage.csv', methods = ['GET','POST'])
def get_csv():
    return 'Hi!'

@app.route('/templates/upset.html')
def upsetTool():
    return render_template('upset.html', the_title='UpSet')

@app.route('/templates/paral.html')
def parallelTool():
    return render_template('paral.html', the_title='Parallel Sets')

@app.route('/templates/rad.html')
def radialTool():
    return render_template('rad.html', the_title='Radial Sets')


@app.route('/templates/test.html')
def dataTest():
    return render_template('test.html', the_title='Parallel Sets')

@app.route('/templates/test_paral.html')
def testParallelTool():
    return render_template('test_paral.html', the_title='Parallel Sets')

@app.route('/templates/schemaExp.html')
def dataSchema():
    return render_template('schemaExp.html', the_title='Data Schema')


if __name__ == '__main__':
    app.run(debug=True)
