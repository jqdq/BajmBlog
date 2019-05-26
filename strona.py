from flask import Flask
from flask import render_template
from cytaty import polaczenie, dodaj, pobierz
from time import clock
import sqlite3

#generowanie bazy
baza = polaczenie()
kursor = baza.cursor()
kursor.execute('CREATE TABLE cytaty (tresc text, utwor text)')
baza.commit()
print('Baza utworzona')

#importowanie danych (DANE PRZYKŁADOWE, TU WEJDZIE SCRAPER)
dodaj(kursor, ('pies','kot'))
dodaj(kursor, ('arka','gdynia'))
dodaj(kursor, ('lech','poznań'))
dodaj(kursor, ('litwa','ojczyzna'))
kursor.execute('CREATE TABLE losowo AS SELECT * FROM cytaty ORDER BY RANDOM()')
print('Dane zaimportowane')

#Utworzenie serwera
aplikacja = Flask(__name__)
start = clock()

@aplikacja.route('/')
def strona_glowna():
    return render_template('test.html', zmienne=pobierz(kursor, start)) # zamiast test.html trzeba potem wstawić 
