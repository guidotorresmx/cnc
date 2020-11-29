# app.py (1/3)

from flask import Flask, render_template
from flask import request

# initialize instance of WSGI application
# act as a central registry for the view functions, URL rules, template configs
app = Flask(__name__)

## include db name in URI; _HOST entry overwrites all others
app.config['MONGODB_HOST'] = 'mongodb://localhost:27017/sivji-sandbox'
app.debug = True

# initalize app with database
#app = Flask(__name__)


@app.route("/", methods = ["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template(
            'base.html',
            val1=str(10),
            val2=str(20),
            val3=str(40)
            )
    print(request.method)
    print(request.form)
    return render_template(
        'base.html',
        val1=str(request.form["slider1"]),
        val2=str(request.form["slider2"]),
        val3=str(request.form["slider3"])
        )


if __name__ == "__main__":
    app.run()
