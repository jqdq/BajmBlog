from flask import Flask
from flask import templating
from cytaty import poczatek_pracy
from time import clock

baza = poczatek_pracy()
start = clock()

aplikacja = Flask(__name__)

@aplikacja.route('/')
def strona_glowna():
    return 'test'
