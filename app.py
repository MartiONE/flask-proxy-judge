from flask import Flask, request
app = Flask(__name__)

a = ['HTTP_HOST', 'HTTP_CONNECTION','HTTP_UPGRADE_INSECURE_REQUESTS','HTTP_USER_AGENT', "HTTP_ACCEPT", 'REMOTE_ADDR', 'REMOTE_PORT', 'CLIENT_IP', 'REQUEST_METHOD', 'REQUEST_URI', 'REQUEST_TIME_FLOAT', 'REQUEST_TIME']


@app.route("/")
def judge():
    return "<pre>"+"\n".join(["{}= {}".format(i,j) for i,j in request.headers.environ.items() if i in a])+"</pre>"

@app.route("/json")
def json():
    return str({i:j for i,j in request.headers.environ.items() if i in a})

if __name__ == "__main__":
    app.run()