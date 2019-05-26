from random import shuffle
import requests
from bs4 import BeautifulSoup
from time import clock
import sqlite3

def polaczenie():
        baza = sqlite3.connect('dane.db')
        return baza

def usuwajzle(zwrot, listazlych):
        ####
        # Usuwa niepożądane znaki/zwroty
        ####
        for i in listazlych:
                zwrot = zwrot.replace(i, '')
        return zwrot

def usuwajpuste(lista):
        ####
        # Usuwa puste linie
        ####
        nowa=[]
        for i in lista:
                if not i=='':
                        nowa.append(i)
        return nowa

def dodaj(kursor, tresc):
        if len(tresc[0])<=400 and len(tresc[0])>5:
                kursor.execute('INSERT INTO cytaty (tresc, utwor) VALUES (?,?)', tresc)

def scrapuj(baza):
        ####
        # Scrapuje teksty utworów i dodaje je do bazy
        ####
        # wyszukiwanie linków ze stronki #
        strona = requests.get('https://teksciory.interia.pl/bajm,a,1796.html')
        drzewunio=BeautifulSoup(strona.content, 'lxml')
        listazaznaczen= drzewunio.findAll('div', class_='artistContent marginRight20')[1].findAll('a',class_='title')
        listalinkow=dict()
        for i in listazaznaczen:
                # pobieranie tekstów #
                listalinkow[i.string]='https://teksciory.interia.pl'+i['href']
        print("Zakończono zbieranie linków")
        for i in listalinkow:
                # upload linii #
                print("Pobieranie tekstu",i)
                stronka=requests.get(listalinkow[i])
                obszar = BeautifulSoup(stronka.content,'lxml').find('div',class_='txt border')
                tekst=usuwajzle(str(obszar), ['div class="txt border">','</div','<','>','\n','\r'])
                linijki=usuwajpuste(tekst.split('br/'))
                for j in linijki:
                        dodaj(baza, (j, i))

def pobierz(kursor,start):
        ####
        # Zwraca listę cytatów
        ####
        kiedy = int((clock() - start)//60)
        ilosc = str(min((kiedy, kursor.execute('SELECT COUNT(*) FROM losowo').fetchone()[0])))
        wynik = kursor.execute('SELECT * FROM losowo LIMIT (?)', [ilosc])
        return wynik.fetchall()
