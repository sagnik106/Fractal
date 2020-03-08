from flask import Flask, render_template, request, redirect
from ML.vision import Vision
import ML.sympton as s

#v=Vision()
app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
    print(request.method)
    if request.method == 'POST':
        m=[request.form['firstsymptom'],request.form['secondsymptom'],request.form['thirdsymptom'],request.form['foursymptom']]
        m=[i for i in m if i!='']
        l=s.look_up(m)
        print(m)
        return render_template('index.html',tasks=l)
    else:
        return render_template('index.html',tasks=[" "])


@app.route('/fire',methods=['POST','GET'])
def cam():
    if request.method == 'POST':
        pass
    else:
        return render_template('fire.html')

@app.route('/symp',methods=['POST','GET'])
def symp():
    if request.method== 'POST':
        pass
    else:
        return render_template('symptoms.html')

if __name__=="__main__":
    app.run(debug=True)