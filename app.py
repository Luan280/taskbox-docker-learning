from flask import Flask
import os

app = Flask(__name__)

TASKBOX_MESSAGE = os.getenv("TASKBOX_MESSAGE", "TaskBox funcionando!")


@app.route("/")
def index():
    return TASKBOX_MESSAGE
