
# ESP - Rozproszony system czujnikow
#
Układ oparty na podzespołach:
1. nodemcu v3
2. sensor BMP280
Działa stabilnie z ArduinoIDE 1.8.9
#
## HOW TO
Obsługa płytek w tym wykonaniu jest banalnie prosta. Każda płytka ma swój indeks. W tym przypadku BMP1 oraz BMP2. Każda płytka nadaje na dwóch kanałach: "temp" oraz "pres" będącymi odpowiednio wartością temperatury oraz ciśnienia Aby dodać kolejne urządzenie należy swtorzyć mu jego indywidualny indeks oraz na jego podstawie stowrzyć temat do publikowania: BMP1/pres oraz BMP1/temp.

## Troubleshooting

1. __Bład połączenia__ - przeanalizuj czy masz właściwe dane sieci oraz dobrze podany adres brokera MQTT
2. __Brak publikacji__ - możliwe, że tematy na ESP oraz Brokerze MQTT nie są sobie równe. 
3. __Niepodłączony czujnik__ - sprawdz połaczenie czujnika, program sam przeprowadza diagnostykę co 5 sekund. W folderze schematy znajdziesz informacje odnośnie sposobu podłączenia. 
4. __Bład kompilacji__ - sprawdz czy Twój wypadkowałeś biblioteki oraz czy Twój program spełnia wymogi z poniższego punktu:
# 
## Biblioteki
Wszystkie potrzebne biblioteki są zawarte w plikach, które się tu znajdują.
Program działa na czystym, wgranym Arduino IDE, bez dogrywanych bibliotek, 
zmian w katalogach Arduino IDE ( w tym wrzucanie bibliotek ręcznie).

__UWAGA__ należy dodać poniższe linki:
Plik> Preferencje> Dodatkowe adresy URL>:
https://dl.espressif.com/dl/package_esp32_index.json
https://arduino.esp8266.com/stable/package_esp8266com_index.json
#


