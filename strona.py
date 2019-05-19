from flask import Flask
from cytaty import poczatek_pracy, scrapuj

app = Flask(__name__)

@app.route('/')
def x():
    return 'elo'
