from flask import Flask, request
application = Flask(__name__)

@application.route("/")
def hello():
    print(request.headers)

if __name__ == "__main__":
    application.run()
