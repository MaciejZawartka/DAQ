
# ESP - Rozproszony system czujnikow
#
Układ oparty na podzespołach:
1. nodemcu v3
2. sensor BMP280
#
## TO DO:
1. Zrobienie uniwersalnej biblioteki
2. Kalibracja
3. Weryfikacja
#
## Biblioteki
Wszystkie potrzebne biblioteki są zawarte w plikach, które się tu znajdują.
Program działa na czystym, wgranym Arduino IDE, bez dogrywanych bibliotek, 
zmian w katalogach Arduino IDE ( w tym wrzucanie bibliotek ręcznie).
#
## Info
Nie pokazują się komunikaty o wielu tych samych bibliotekach (czyste Ardu IDE)
#

## UWAGA
`queue.h` -> biblioteka u mnie pokazuje się że nie działa, wg problemów jakie spotkałem na forach,
jest to błąd że mam domyślną płytke na którą kompiluje - Arduino Uno a nie NODEMCU v3,
czekam na to aż strona http://arduino.esp8266.com/staging/package_esp8266com_index.json zacznie
działać, wtedy dokonam weryfikacji. 
