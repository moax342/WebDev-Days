from flask import Flask
from random import choice
app = Flask(__name__)

number =choice([0,1,2,3,4,5,6,7,8,9])

@app.route("/")
def first_page():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzgwaHFzdDd2dGpleTdkaXlnOW5iMHJuaGs3MnNod2sy"
            "Y2lxeXdqNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jf9JkuUiFtOssW6evL/giphy.gif'>")

@app.route("/<int:guessedNumber>")
def chosen_number(num):
    if num == number:
        return ("<h1 style='color: green;'>Well done you got it write</h1>"
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDk2ZGY5NnowMWl1NDE0NnMwa2dheXZyMm81eXh1"
                "NWQ4czBoYWRwciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YRuFixSNWFVcXaxpmX/giphy.gif'>")
    elif num > number:
        return ("<h1 style='color: red;'>Too High chose another number please!</h1>"
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExend1bWR5ZHdpZzNwNDU1aGlyZXBwMmQ3b3ZwdG9"
                "vaGozYm56a21ldSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wHB67Zkr63UP7RWJsj/giphy.gif'>")
    else:
        return ("<h1 style='color: red;'>Too low chose another number please!</h1>"
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnZ0ZXRhMWJ4MzhpMm45YnhoMDhicXZyMnF2djd6"
                "M2F5OHdrZ3JuNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/s1MX7LfOn5nhTyb0dy/giphy.gif'>")

if __name__ == "__main__":
    app.run(debug=True)
