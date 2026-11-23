from flask import Flask
@app.route("/")
def home:
    return "sportstournament application"