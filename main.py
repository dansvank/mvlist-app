from flask import Flask, render_template, jsonify
from database import loadMovies, showMovie

app = Flask(__name__)


#----------API ENDPOINTS---------
@app.route("/movie/")
def listMovies():
  return jsonify(loadMovies())


@app.route("/movie/<id>")
def getMovie(id):
  m = showMovie(id)
  return render_template("movie.html", movie=m)


#----------HTML ROUTES--------
@app.route("/")
def home():
  return render_template("home.html", movies=loadMovies())


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
