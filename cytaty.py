import quicksqlite

def poczatek_pracy():
    ####
    # Tworzy bazę danych 
    ####
    baza = quicksqlite.Connection()
    baza.create_table('cytaty', ['nrop','utwor','cytat'], ["INTEGER","TEXT","TEXT"])

# def scrapuj():
    ####
    # Scrapuje teksty utworów
    ####

# def pobierz():
    ####
    # Zwraca listę cytatów
    ####