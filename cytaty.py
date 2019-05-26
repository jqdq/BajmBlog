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

def usuwajpuste(lista):
    nowa=[]
    for i in lista:
        if not i=='':
            nowa.append(i)
    return nowa

def scrapuj(baza):
    ####
    # Scrapuje teksty utworów i dodaje je do bazy
    ####
    
    # tu jest wyszukiwanie linków ze stronki pozdrawiam #
    stronka= requests.get('https://teksciory.interia.pl/bajm,a,1796.html')
    drzewunio=BeautifulSoup(strona.content, 'lxml')
    listazaznaczen= drzewunio.findAll('div', class_='artistContent marginRight20')[1].findAll('a',class_='title')
    listalinkow=dict()
    for i in listazaznaczen:
        listalinkow[i.string]='https://teksciory.interia.pl'+i['href']
        print("Zakończono zbieranie linków")
    

def pobierz():
    ####
    # Zwraca listę cytatów
    ####
    #witam tutaj mam zrobione juz pobieranko tekstow pozderki 
    licznik=0
    for i in listalinkow:
        print("Pobieranie tekstu",i)
        stronka=requests.get(listalinkow[i])
        tekst=str(BeautifulSoup(strona.content,'lxml').find('div',class='txt border'))
        tekst=tekst.replace('div class="txt border">','').replace('</div','').replace('\n','').replace('\r','')
        linijki=usuwajpuste(tekst.split('<br/>'))
        for j in linijki:
            liczcznik+=1


