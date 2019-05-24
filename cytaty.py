import quicksqlite
from random import shuffle
import requests
from bs4 import BeautifulSoup

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


def usuwajpuste(lista):
    nowa=[]
    for i in lista:
        if not i=='':
            nowa.append(i)
    return nowa

#tu jest wyszukiwanie linków ze stronki pozdrawiam

stronka= requests.get('https://teksciory.interia.pl/bajm,a,1796.html')
drzewunio=BeautifulSoup(strona.content, 'lxml')
listazaznaczen= drzewunio.findAll('div', class_='artistContent marginRight20')[1].findAll('a',class_='title')
listalinkow=dict()
for i in listazaznaczen:
    listalinkow[i.string]='https://teksciory.interia.pl'+i['href']
    print("Zakończono zbieranie linków")

