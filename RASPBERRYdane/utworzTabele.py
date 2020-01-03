import sqlite3 as lite
import sys
con = lite.connect('dane.db')
typ_czujnikow = str(input("Podaj typ wykorzystywanych czujnikow: "))
liczba_czujnikow = int(input("Podaj liczbe wykorzystywanych czujnikow: "))

with con: 
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Dane")
    cur.execute("CREATE TABLE Dane(Typ_czujnikow STRING, Liczba_czujnikow NUMERIC)")

    for i in range(liczba_czujnikow):
        cur.execute("DROP TABLE IF EXISTS Czujnik"+ str(i+1))
        cur.execute("CREATE TABLE Czujnik"+ str(i+1) + "(timestamp DATETIME, temperatura NUMERIC, cisnienie NUMERIC)")
    
    cur.execute("INSERT INTO Dane(Typ_czujnikow, Liczba_czujnikow) VALUES ('"+typ_czujnikow+"', "+str(liczba_czujnikow)+")")

