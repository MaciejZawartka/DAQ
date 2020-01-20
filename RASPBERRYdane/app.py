#aplikacja


#import biblitotek
import paho.mqtt.client as mqtt #mqtt
import sqlite3 #SQL

dbname = 'dane.db'

#potwierdzenia nawiazania polaczenia
def on_connect(client, userdata, flags, rc):
    print("Polaczono z kodem "+str(rc))
    client.subscribe([("BMP1/temp",0), ("BMP1/pres",0), ("BMP2/temp",0), ("BMP2/pres",0)])
#odczyt wiadomosci
def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    temat=str(msg.topic)
    wiadomosc=str(msg.payload)
    id = temat[:4]
    meas = temat[-4:]
    val = float(wiadomosc)
    logDane(id, meas, val)
    print(id+' '+meas)
    print(val)
#    print(msg.topic+" "+str(msg.payload))

# zapis danych do bazy
def logDane (id, meas, val):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO "+id+" values(datetime('now'), (?), (?))", (meas, val))
    conn.commit()
    conn.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()
