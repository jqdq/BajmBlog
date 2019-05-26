from flask import Flask, render_template, g
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
baza.close()

#Utworzenie serwera
aplikacja = Flask(__name__)
start = clock()

@aplikacja.route('/')
def strona_glowna():
    if not 'db' in g:
        g.db = polaczenie()
    kursor = g.db.cursor()
    zwrot = pobierz(kursor, start)
    db = g.pop('db', None)
    if db is not None:
        db.close()
    return render_template('main_site.html', zmienne=zwrot)
