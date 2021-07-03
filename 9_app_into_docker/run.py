from blog import views

if __name__ == "__main__":
	views.app.config['SECRET_KEY'] = "Your_secret_string"
	views.app.run(debug=True,host='0.0.0.0')