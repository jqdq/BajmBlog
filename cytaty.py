import sqlite3
from random import shuffle
from time import clock

def polaczenie():
    baza = sqlite3.connect('dane.db')
    return baza

def dodaj(kursor, tresc):
    if len(tresc)<=400:
        kursor.execute('INSERT INTO cytaty (tresc, utwor) VALUES (?,?)', tresc)

'''
def scrapuj(baza):
    ####
    # Scrapuje teksty utworów i dodaje je do bazy
    ####
    dodaj(baza, (#cytat#,#utwór#))
'''

def pobierz(kursor,start):
    ####
    # Zwraca listę cytatów
    ####
    kiedy = int((clock() - start)//60)
    ilosc = min((kiedy, kursor.execute('SELECT COUNT(*) FROM losowo').fetchone()[0]))
    wynik = kursor.execute('SELECT * FROM losowo LIMIT (?)', str(ilosc))
    return wynik.fetchall()

    
