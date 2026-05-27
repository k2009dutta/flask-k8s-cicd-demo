from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print ("This is version 2 of the application!")
    return "GitHub Actions & Kubernetes Rolling Deployment Successful"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
