import time
import sqlite3
import random


dbname='dane.db'
czestProb = 1 # sekundy


# pobranie wartosci czujnikow
def pobierzDane(lcz):   

    cisn=[0,0]
    temp=[0,0]
    for i in range(lcz):
        cisn[i] = random.randint(900, 1100)
        temp[i] = random.randint(19, 22)
        if cisn is not None and temp is not None:
            cisn[i] = round(cisn[i])
            temp[i] = round(temp[i], 1)
    return temp, cisn

# zapis danych do bazy
def logDane (temp, cisn, lcz):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    for i in range(lcz):
        curs.execute("INSERT INTO Czujnik"+str(i+1)+" values(datetime('now'), (?), (?))", (temp[i], cisn[i]))
    conn.commit()
    conn.close()
    
# wyswietlenie dasnych
def wyswietlDane(lcz):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    for i in range(lcz):
        print ("\nWartosc czujnika",(i+1),":\n")
        for row in curs.execute("SELECT * FROM Czujnik"+str(i+1)+" ORDER BY timestamp DESC LIMIT 1"):
            print (row)
    conn.close()
    
def liczbaCzujnikow():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    for lcz in curs.execute("SELECT liczba_czujnikow FROM Dane"):
        lcz = lcz[0]
    conn.close()
    return lcz
 
# main function
def main():
    while True:
        lcz = liczbaCzujnikow()
        temp, cisn = pobierzDane(lcz)
        logDane (temp, cisn, lcz)
        time.sleep(czestProb)
        wyswietlDane(lcz)

# ------------ Execute program 
main()