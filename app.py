from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
	#aktuální datum
	date = datetime.now().strftime("%d. %m. %Y")

	name=request.args.get("name")
	surname=request.args.get("surname")
	return render_template("page.html", date=date, name=name, surname=surname)

@app.route("/pozdrav-post", methods=["POST", "GET"])
def pozdrav_post():
	#aktuální datum
	date = datetime.now().strftime("%d. %m. %Y")

	name=request.form.get("name")
	surname=request.form.get("surname")
	heslo=request.form.get("password")
	spravne_heslo = "tajneheslo"
	if heslo == spravne_heslo:
		zprava = "Správné heslo!"

	else:
		zprava = "Nesprávné heslo!"
	jmeno_zadane= True
	if not name:
		jemno_zadane = False
	if name and len(name) >= 50:
		jmeno_zadane = False
	else:
		name = name

	return render_template("pozdrav_post.html", date=date, name=name, surname=surname, zprava=zprava)


if __name__=="__main__":
	app.run(debug=True)