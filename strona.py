from flask import Flask
from flask import render_template
from cytaty import poczatek_pracy
from time import clock

#generowanie bazy i zegara
baza = poczatek_pracy()
start = clock()

aplikacja = Flask(__name__)

@aplikacja.route('/')
def strona_glowna():
    return render_template('test.html') # zamiast test.html trzeba potem wstawić 
