import sqlite3
from random import shuffle
from time import clock

def polaczenie():
    baza = sqlite3.connect(':memory:')
    return baza

def dodaj(kursor, tresc):
    if len(tresc)<=400:
        kursor.execute('INSERT INTO cytaty (tresc, utwor) VALUES (?,?)', tresc)

'''
def scrapuj(baza):
    ####
    # Scrapuje teksty utworów i dodaje je do bazy
    ####
    zbior=[]
    nr+=1
    ('main', [nr, utwor, cytat])
    zbior.append(nr)
'''

def pobierz(kursor,start):
    ####
    # Zwraca listę cytatów
    ####
    kiedy = int((clock() - start)//60)
    ilosc = min((kiedy, kursor.execute('SELECT COUNT(*) FROM losowo').fetchone()[0]))
    wynik = kursor.execute('SELECT * FROM losowo LIMIT (?)', str(ilosc))
    return wynik.fetchall()

    
