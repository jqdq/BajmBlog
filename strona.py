from flask import Flask, render_template, g, url_for
from cytaty import polaczenie, dodaj, pobierz, scrapuj
from time import clock
import sqlite3

start = clock()

# generowanie bazy
baza = polaczenie()
baza.execute('DROP TABLE IF EXISTS cytaty')
baza.execute('DROP TABLE IF EXISTS losowo')
kursor = baza.cursor()
kursor.execute('CREATE TABLE cytaty (tresc text, utwor text)')
print('Baza utworzona')

# importowanie danych
scrapuj(kursor)
kursor.execute('CREATE TABLE losowo AS SELECT * FROM cytaty ORDER BY RANDOM()')
print('Dane zaimportowane')

baza.commit()
baza.close()

#Utworzenie serwera
aplikacja = Flask(__name__)

@aplikacja.route('/')
def strona_glowna():
    if not 'db' in g:
        g.db = polaczenie()
    kursor = g.db.cursor()
    zwrot = pobierz(kursor, start)
    db = g.pop('db', None)
    if db is not None:
        db.close()
    return render_template('main_site.html', zmienna=zwrot)