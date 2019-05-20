import quicksqlite
from random import shuffle

def poczatek_pracy():
    ####
    # Tworzy bazę danych 
    ####
    baza = quicksqlite.Connection()
    baza.create_table('main', ['nr','utwor','cytat'], ["INTEGER","TEXT","TEXT"])
    print('Baza utworzona')
    return baza
'''
def scrapuj(baza):
    ####
    # Scrapuje teksty utworów i dodaje je do bazy
    ####
    zbior=[]
    nr+=1
    baza.insert('main', [nr, utwor, cytat])
    zbior.append(nr)
    
    shuffle(zbior)



def pobierz():
    ####
    # Zwraca listę cytatów
    ####
'''