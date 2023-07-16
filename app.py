from flask import Flask , render_template
#flask is the module Flask is the class
app = Flask(__name__)


#decoraor
@app.route("/")
def hello():

  return render_template("./home.html")


print(__name__)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
