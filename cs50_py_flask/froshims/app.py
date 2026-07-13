# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/register", methods=["POST"])
# def register():
#     if not request.form.get("name") or not request.form.get("sport"):
#         return render_template("failure.html")
#     return render_template("success.html")









# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/register", methods=["POST"])
# def register():
#     if not request.form.get("name"):
#         return render_template("failure.html")
#     sport = request.form.get("sport")
#     if sport != "Basketball" and sport != "Soccer" and sport != "Ultimate Frisbee":
#         return render_template("failure.html")
#     return render_template("success.html")\










# from flask import Flask, render_template, request

# app = Flask(__name__)

# SPORTS = [
#     "Basketball",
#     "Soccer",
#     "Ultimate Frisbee"
# ]

# @app.route("/")
# def index():
#     return render_template("index.html", sports=SPORTS)


# @app.route("/register", methods=["POST"])
# def register():
#     if not request.form.get("name") or request.form.get("sport") not in SPORTS:
#         return render_template("failure.html")
    
#     return render_template("success.html")











# from flask import Flask, render_template, request

# app = Flask(__name__)

# SPORTS = [
#     "Basketball",
#     "Soccer",
#     "Ultimate Frisbee"
# ]

# @app.route("/")
# def index():
#     return render_template("index.html", sports=SPORTS)


# @app.route("/register", methods=["POST"])
# def register():
    
#     # Validate name
#     name = request.form.get("name")
#     if not name:
#         return render_template("error.html", message="Missing Name")
    
#     # Validate sport
#     sport = request.form.get("sport")
#     if not sport:
#         return render_template("error.html", message="Missing Sport!")
    
#     if sport not in SPORTS:
#         return render_template("error.html", message="Invalid Sport!")
    
#     # Confirmed
#     return render_template("success.html")












# from flask import Flask, render_template, request

# app = Flask(__name__)

# REGISTRANTS = {}

# SPORTS = [
#     "Basketball",
#     "Soccer",
#     "Ultimate Frisbee"
# ]

# @app.route("/")
# def index():
#     return render_template("index.html", sports=SPORTS)


# @app.route("/register", methods=["POST"])
# def register():
    
#     # Validate name
#     name = request.form.get("name")
#     if not name:
#         return render_template("error.html", message="Missing Name")
    
#     # Validate sport
#     sport = request.form.get("sport")
#     if not sport:
#         return render_template("error.html", message="Missing Sport!")
    
#     if sport not in SPORTS:
#         return render_template("error.html", message="Invalid Sport!")
    
    
#     # Remember student
#     REGISTRANTS[name] = sport
    
#     # Confirmed
#     return render_template("success.html")



# @app.route("/registrants")
# def registrants():
#     return render_template("registrants.html", registrants=REGISTRANTS)















# from flask import Flask, render_template, redirect, request

# app = Flask(__name__)

# REGISTRANTS = {}

# SPORTS = [
#     "Basketball",
#     "Soccer",
#     "Ultimate Frisbee"
# ]

# @app.route("/")
# def index():
#     return render_template("index.html", sports=SPORTS)


# @app.route("/register", methods=["POST"])
# def register():
    
#     # Validate name
#     name = request.form.get("name")
#     if not name:
#         return render_template("error.html", message="Missing Name")
    
#     # Validate sport
#     sport = request.form.get("sport")
#     if not sport:
#         return render_template("error.html", message="Missing Sport!")
    
#     if sport not in SPORTS:
#         return render_template("error.html", message="Invalid Sport!")
    
    
#     # Remember student
#     REGISTRANTS[name] = sport
    
#     # Confirmed
#     return redirect("/registrants")



# @app.route("/registrants")
# def registrants():
#     return render_template("registrants.html", registrants=REGISTRANTS)














from cs50 import SQL
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

db = SQL("sqlite:///froshims.db")

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    
    # Validate name
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing Name")
    
    # Validate sport
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing Sport!")
    
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid Sport!")
    
    
    # Remember student
    db.execute("INSERT into ")
    
    # Confirmed
    return redirect("/registrants")



@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)