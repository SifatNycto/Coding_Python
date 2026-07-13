# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "hello, world"




# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")





# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/")
# def index():
#     name = request.args["name"]
#     return render_template("index.html", placeholder=name)







# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/")
# def index():
#     if "name" in request.args:
#         name = request.args["name"]
#     else:
#         name = "yo world"
#     return render_template("index.html", placeholder=name)




# from flask import Flask, render_template, request

# app = Flask(__name__)


# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/greet", methods=["POST"])
# def greet():
#     return render_template("greet.html", name=request.form.get("name", "worldyy"))










from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("greet.html", name=request.form.get("name"))
    else:
        return render_template("index.html")