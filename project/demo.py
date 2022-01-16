from flask import Flask, render_template, request,redirect,url_for
from PIL import Image
import animegan2 as a
import os

UPLOAD_FOLDER = 'static//upload/'
OUTPUT_FOLDER = 'static/output/'
app = Flask(__name__,template_folder='template',static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER 


@app.route("/")
def demo():    
    return render_template('demo.html')

@app.route("/",methods=['POST'])
def run():
    if request.method == "POST":
        if 'myFile' not in request.files:
            return 'there is no file1 in form!'
        file = request.files['myFile']
        filename = file.filename
        path_ip = os.path.join(app.config['UPLOAD_FOLDER'], filename)        
        file.save(path_ip) 
        output = a.run(path_ip)
        path_op = os.path.join(app.config['OUTPUT_FOLDER'], filename)
        output.save(path_op)         
        return render_template('demo.html',filename=filename)
    else:
        return redirect(request.url)

@app.route("/root/<filename>") 
def root(filename):
    return redirect(url_for('static',filename='upload/'+filename),code=301)
   
@app.route("/show/<filename>") 
def show(filename):
    return redirect(url_for('static',filename='output/'+filename),code=301)

if __name__=="__main__":
    app.run()