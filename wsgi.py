from flask import Flask, request
application = Flask(__name__)

@application.route("/")
def hello():
    return "X-Forwarded-For header value: " + request.environ['HTTP_X_FORWARDED_FOR']

if __name__ == "__main__":
    application.run()
