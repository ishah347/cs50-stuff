from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Establish a list and intital value for user's total stock value
    stocks = []
    total = 0

    rows1 = db.execute("SELECT cash FROM users WHERE id = :userid", userid=session["user_id"])
    rows = db.execute("SELECT * FROM portfolio WHERE id = :userid", userid=session["user_id"])
    # If user has not yet made transactions, simply display his cash amount and total value
    if not rows:
        stock = {"cash": usd(rows1[0]["cash"]), "total": usd(rows1[0]["cash"])}
        stocks.append(stock)

    # if user has made transaction:
    else:
        # Iterate over each row in portfolio
        for i in rows:
            for j in rows:
                # Look up symbol of stock in that row of the portfolio
                quote = lookup(j["symbol"])

                # Repeatedly add the current price of the amount of stocks bought in each row together
                total = total + quote["price"] * j["shares"]

            # Look up symbol of stock in that row of the portfolio
            quoted = lookup(i["symbol"])

            # Create a dict made up of the values pertinent to your index table and append it to your list
            stock = {"name": i["stock"], "shares": i["shares"], "price": usd(quoted["price"]), "value": usd(
                i["shares"] * quoted["price"]), "cash": usd(rows1[0]["cash"]), "total": usd(total + rows1[0]["cash"])}
            stocks.append(stock)

    # Return list to index.html
    return render_template("index.html", stocks=stocks)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Look up symbol user submitted
        quote = lookup(request.form.get("symbol"))

        # Ensure stock symbol is valid
        if not quote:
            return apology("stock symbol is not valid", 400)

        # Ensure amount of shares bought is a positive integer value
        try:
            sharenumber = int(request.form.get("shares"))
        except ValueError:
            return apology("number of shares is not valid", 400)
        if sharenumber < 1:
            return apology("number of shares is not valid", 400)

        # If user can afford purchase, update his portfolio and the amount of cash he has left
        rows = db.execute("SELECT cash FROM users WHERE id = :userid", userid=session["user_id"])

        if rows[0]["cash"] > quote["price"] * sharenumber:
            db.execute("UPDATE users SET cash = cash - :totalprice WHERE id = :userid",
                       userid=session["user_id"], totalprice=quote["price"] * sharenumber)

            # Log transaction into user's history
            db.execute("INSERT INTO history ('bought or sold', id, 'number of shares', 'price of stock', 'stock symbol') VALUES('BOUGHT', :userid, :sharenumber, :price, :symbol)",
                       userid=session["user_id"], sharenumber=sharenumber, price=quote["price"], symbol=quote["symbol"])

            # If user doesn't already have the particular stock just bought, log transaction into user's portfolio
            rows1 = db.execute("SELECT * FROM portfolio WHERE id = :userid AND symbol = :symbol",
                               userid=session["user_id"], symbol=quote["symbol"])
            if not rows1:
                db.execute("INSERT INTO portfolio ('id', 'stock', 'shares', 'symbol') VALUES(:userid, :name, :sharenumber, :symbol)",
                           userid=session["user_id"], name=quote["name"], sharenumber=sharenumber, symbol=quote["symbol"])

            # If user does have the stock already, update his count of shares for that stock in his portfolio
            else:
                db.execute("UPDATE portfolio SET shares = shares + :share WHERE id = :userid AND symbol = :symbol",
                           share=sharenumber, userid=session["user_id"], symbol=quote["symbol"])

        # If user can't afford purchase, return apology
        else:
            return apology("cannot afford purchase", 400)

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Establish a blank list to later append to
    stocks = []

    # Access user's history
    rows = db.execute("SELECT * FROM history WHERE id = :userid", userid=session["user_id"])

    # Iterate over each row in history
    for i in rows:
        # Create a dict comprising of the elements pertinent to your history table and append it to your list
        stock = {"bs": i["bought or sold"], "symbol": i["stock symbol"], "shares": i["number of shares"], "price": usd(
            i["price of stock"]), "date": i["time of transaction"]}
        stocks.append(stock)

    # Return list to history.html to be displayed
    return render_template("history.html", stocks=stocks)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Look up symbol user submitted
        quote = lookup(request.form.get("symbol"))

        # Ensure stock symbol is valid
        if not quote:
            return apology("Stock symbol is not valid", 400)

        # Display name, price, and symbol of stock
        else:
            quote["price"] = usd(quote["price"])
            return render_template("quoted.html", quoted=quote)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must confirm password", 400)

        # Check if password and the password confirmation are the same
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords don't match", 400)

        # Hash and encrypt password
        hash = generate_password_hash(request.form.get("password"))

        # Add username to database
        result = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)", username=request.form.get("username"),
                            hash=hash)

        # Check if username already exists
        if not result:
            return apology("Username already exists", 400)

        # Log in user automatically
        session["user_id"] = result

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/changepassword", methods=["GET", "POST"])
def changepassword():
    """Changes user's password"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure old password was submitted
        if not request.form.get("old password"):
            return apology("must provide old password", 400)

        # Ensure new password was submitted
        elif not request.form.get("new password"):
            return apology("must provide new password", 400)

        # Ensure new password confirmation was submitted
        elif not request.form.get("confirm new password"):
            return apology("must confirm new password", 400)

        # Check if new password and the new password confirmation are the same
        elif request.form.get("new password") != request.form.get("confirm new password"):
            return apology("New passwords don't match", 400)

        # Check if old password given matches the current password
        rows = db.execute("SELECT hash FROM users WHERE id = :userid", userid=session["user_id"])
        if not check_password_hash(rows[0]["hash"], request.form.get("old password")):
            return apology("False old password given", 400)

        # Add new password to database
        newhash = generate_password_hash(request.form.get("new password"))
        db.execute("UPDATE users SET hash = :newhash WHERE id = :userid",
                   newhash=newhash, userid=session["user_id"])

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("changepassword.html")


@app.route("/sell")
@login_required
def sell1():
    """Set up html for selling shares of stock"""
    # Establish a blank list to later append to
    symbols = []

    # Access user's portfolio
    rows = db.execute("SELECT * FROM portfolio WHERE id = :userid", userid=session["user_id"])

    # Iterate over each row in the portfolio
    for i in rows:
        # Create a dict comprised of the symbol of the stock the user wishes to sell and append it to the list
        symbol = {"symbol": i["symbol"]}
        symbols.append(symbol)

    # Return list to sell.html to be printed
    return render_template("sell.html", symbols=symbols)


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell2():
    """Sell shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure stock symbol was chosen
        if request.form.get("symbol") is None:
            return apology("stock symbol was not chosen", 400)

        # Look up symbol selected by user
        quote = lookup(request.form.get("symbol"))

        # Ensure user has shares of that stock symbol
        rows = db.execute("SELECT shares FROM portfolio WHERE id = :userid AND symbol = :symbol",
                          userid=session["user_id"], symbol=quote["symbol"])
        if not rows:
            return apology("No shares of chosen stock found", 400)

        # Ensure amount of shares sold is a positive integer value
        try:
            sharenumber = int(request.form.get("shares"))
        except ValueError:
            return apology("number of shares is not valid", 400)
        if sharenumber < 1:
            return apology("number of shares is not valid", 400)

        # Ensure amount of shares sold is not greater than the amount of shares the user has for that stock
        if sharenumber > int(rows[0]["shares"]):
            return apology("Not enough shares of chosen stock found", 400)

        # Update user's portfolio and cash amount to take the sale into account
        db.execute("UPDATE portfolio SET shares = shares - :share WHERE id = :userid AND symbol = :symbol",
                   share=sharenumber, userid=session["user_id"], symbol=quote["symbol"])
        db.execute("UPDATE users SET cash = cash + :totalprice WHERE id = :userid",
                   userid=session["user_id"], totalprice=quote["price"] * sharenumber)

        # Log transaction into user's history
        db.execute("INSERT INTO history ('bought or sold', id, 'number of shares', 'price of stock', 'stock symbol') VALUES('SOLD', :userid, :sharenumber, :price, :symbol)",
                   userid=session["user_id"], sharenumber=sharenumber, price=quote["price"], symbol=quote["symbol"])

        # Remove stock from portfolio if user now has no shares of it left
        rows1 = db.execute("SELECT shares FROM portfolio WHERE id = :userid AND symbol = :symbol",
                           userid=session["user_id"], symbol=quote["symbol"])
        if rows1[0]["shares"] == 0:
            db.execute("DELETE FROM portfolio WHERE symbol = :symbol", symbol=quote["symbol"])

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("sell.html")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
