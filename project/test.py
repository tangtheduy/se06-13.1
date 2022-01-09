from flask import Flask, render_template
app = Flask(__name__,template_folder='template',static_folder='static',)

@app.route("/")
def demo():
    return render_template('demo.html')

@app.route('/submit',methods=['POST','GET'])
def predict():
    return render_template('demo.html')


if __name__=="__main__":
    app.run(debug=True)