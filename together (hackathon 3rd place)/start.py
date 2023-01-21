from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    f = open("index.html","r")
    g=f.readlines()
    f.close()
    site="".join(map(str,g))
    return site


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)