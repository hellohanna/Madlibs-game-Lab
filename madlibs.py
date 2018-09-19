"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")

@app.route('/game')
def show_madlib_form():
    """Gets user's response to 'would you like to play a game?'."""
    answer = request.args.get("answer")
    if answer == "False":
       return render_template("goodbye.html") 
    else:
        return render_template("game.html")

@app.route('/result')
def game_result():
        """Generate result using data from game.html"""

        p = request.args.get("person")
        c = request.args.get("color")
        a = request.args.get("adjective")
        n = request.args.get("noun")
      
        b = request.args.get("night")
        s = request.args.get("sky")
        u = request.args.get("underwater")
        return render_template("result.html", person = p, noun = n, adjective = a, 
        color = c, night = b, sky = s, underwater = u)


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
