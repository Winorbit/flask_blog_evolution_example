from flask import Flask, request, make_response, render_template
from db import *
  
signup_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>

    <form action="" method="post">
        <p>
        <label for="email">Email</label>
        <input type="text" name="email">
    </p>
    <p>
        <label for="password">Password</label>
        <input type="password" name="password">
    </p>
    <p>
        <input type="submit">
    </p>
    </form>
    
</body>
</html>

"""


login_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>

    <form action="" method="post">
        <p>
        <label for="email">Email</label>
        <input type="text" name="email">
    </p>
    <p>
        <label for="password">Password</label>
        <input type="password" name="password">
    </p>
    <p>
        <input type="submit">
    </p>
    </form>
    
</body>
</html>

"""

cabinet_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Личный кабинет</title>
</head>
<body>
Кабинет!

    <form action="" method="post">
        <p>
        <label for="title">Title</label>
        <input type="text" name="title">
    </p>
    <p>
        <label for="post_text">Text</label>
        <input type="text" name="post_text">
    </p>
    <p>
        <input type="submit">
    </p>
    </form>
    
</body>
</html>

"""

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    simple_string = "Hello!"
    simple_dict = {"title": "I am title!"}
    posts = get_all_posts()
    return render_template('main.html', posts=posts)


@app.route("/signup", methods = ["get", "post"])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')  
        password = request.form.get('password')
        result = write_new_user(email, password)
        if result:
            return "Поздравляю, вы успешно зарегестрированы!"
    else:
        return signup_html

@app.route("/login", methods = ["get", "post"])
def login():
    if request.method == 'POST':
        email = request.form.get('email') 
        password = request.form.get('password')
        result = check_user_exist(email, password)
        if not result:
            return "Проверьте правильность введенных данных"
        else:
            res = make_response("Setting a cookie")
            res.set_cookie('email', email)
            res.set_cookie('password', password, max_age=600)
            return res
    else:
        print(request.cookies)
        return login_html

@app.route("/cabinet", methods = ["get", "post"])
def my_cabinet():
    if request.method == 'POST':
        title = request.form.get('title') 
        text = request.form.get('post_text')
        result = write_new_post(title, text)
        if result:
            return"Ваш пост успешно опубликован!"

        pass
    else:
        if request.cookies.get("email") and request.cookies.get("password"):
            return cabinet_html
        else:
            return "У вас пустые куки"
            
    

if __name__ == "__main__":
    app.run()
