from flask import Flask, render_template, request, redirect
from ML.vision import Vision
import ML.sympton as s

#v=Vision()
app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    print(request.method)
    if request.method == 'POST':
        l=s.look_up([request.form['firstsymptom'],request.form['secondsymptom'],request.form['thirdsymptom'],request.form['foursymptom']])
        print(l)
        return redirect('/')
    else:
        return render_template('index.html')

@app.route('/camera',methods=['POST','GET'])
def cam():
    if request.method == 'POST':
        pass
    else:
        return render_template('camera.html')

@app.route('/symp',methods=['POST','GET'])
def symp():
    if request.method== 'POST':
        pass
    else:
        return render_template('symptoms.html')

if __name__=="__main__":
    app.run(debug=True)