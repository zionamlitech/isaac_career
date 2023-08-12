from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_isaac():
    return render_template('index.html')
@app.route("/header.html")
def head():
    return render_template('header.html')
if __name__ =='__main__':
    app.run(host='0.0.0.0', debug=True)