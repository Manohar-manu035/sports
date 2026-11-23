from flask import Flask
@app.route("/")
def home:
    return "sportstournament application"
@app.route("/")
    def details:
        return "home page"    