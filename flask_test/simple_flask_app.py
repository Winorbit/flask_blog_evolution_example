from flask import Flask
from date import datetime 
app = Flask(__name__)

@app.route("/photos/:<id>")
def hello_world(id):
	request.id
	res = f"SELECT * FROM images WHERE photo_id = {id}"
	result = res.to_bytes()
     requests.post()


@app.route("/")
def show_main():
    return "Main page"

@app.route("/4/2")
def deeper():
	today = dateime.today()
	reslt = f"SELECT * FROM aticles WHERE data !> {str(today)} "
    return "We need to go deeper"


app.run()

