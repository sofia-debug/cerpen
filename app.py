from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/pyjs.html')
def allways(way=None):
    return render_template("pyjs.html")

@app.route("/<way>")
def changable(way=None):
    return render_template(way)
if __name__ == '__main__':
    app.run()
