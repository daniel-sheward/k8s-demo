import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    unique_id = os.getenv("UNIQUE_ID")
    return f"Hello Kubernetes! from {unique_id}!\n"


app.run(host="0.0.0.0", port=80)
