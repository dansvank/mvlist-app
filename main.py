from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, india',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, india',
    'salary': 'Rs. 15,00,000',
}, {
    'id': 3,
    'title': 'Middle Ager',
    'location': 'San Jose, Costa Rica',
    'salary': 'CRC. 1,000,000',
}]


@app.route("/")
def home():
  return render_template("home.html", jobs=JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
