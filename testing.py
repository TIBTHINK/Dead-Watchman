from colorama import Fore, Style, Back
from os import system as cmd
from time import sleep
import src.menu as menu
import src.core as core
import src.core.var as var
import os
import sys
import colorama

from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()