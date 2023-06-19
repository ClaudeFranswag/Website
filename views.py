from flask import Blueprint, render_template, redirect, url_for, request, flash

views = Blueprint(__name__, "views")

@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/caca")
def caca():
    return render_template("garbage.html")

@views.route("/click")
def click():
    return render_template("click.html")

@views.route("/trap")
def trap():
    return redirect(url_for("views.caca"))

@views.route("/java")
def java():
    return render_template("java.html",salut = "salut ça va ?")

@views.route("/bruh")
def bruh():
    return render_template("bruh.html")

@views.route("/message", methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        rep = request.form.get('num_or_email')
        rep_num = request.form.get("numéro")
        rep_email = request.form.get("e-mail")
        if rep_num != None:    
            print(rep_num)
        if rep_email != None:    
            print(rep_email)
        if rep != 'num' and rep != 'email' and rep_num == None and rep_email == None:
            print("error")
            return render_template("message.html")
        if rep == "num":
            return render_template("message_num.html")
        elif rep == "email":
            return render_template("message_email.html")
    return render_template("message.html")

