from flask import Flask, request
from caesar import rotate_character

app = Flask(__name__)
app.config["DEBUG"] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action = "/" method = "POST">
        <input type = "text" name = "rot" value = "0">
        <textarea name = "text">{0}</textarea>
        <input type = "submit" value = "Submit">
        </form>


    </body>
</html>
"""

@app.route("/")
def index():
    new_string ="" 
    return form.format(new_string)

@app.route("/", methods = ["POST"])
def encrypt():
    text = str(request.form["text"])
    rot = int(request.form["rot"])
    rotated_string = rotated_string(text,rot)
    result = "<h1>" + rotated_string + "</h1>"
    return form.format(rotated_string)



if __name__=="__main__":
    app.run()

