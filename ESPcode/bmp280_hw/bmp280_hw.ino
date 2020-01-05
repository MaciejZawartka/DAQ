/***************************************************
Nalezy sciagnac biblioteke:
  Adafriut MQTT Library by Adafriut ver. 1.0.3
Nalezy dodac biblioteke:
  Plik>Preferencje>Dodatkowe biblioteki:
    https://dl.espressif.com/dl/package_esp32_index.json    -> biblioteka uzywana dla dzialania programu na NODEMCU v3
    https://arduino.esp8266.com/stable/package_esp8266com_index.json  -> biblioteka dla komunikacji MQTT



MORE INFO:

AUTHORS:    Kamil Walczyk
            Maciej Zawartka
DESC:       Program na plytke HW-628 v1.1  (NODEMCU v3)
            Wspoldziala z czujnikiem BMP280. Odczyt temperatury oraz cisnienia. 
            PODLACZENIE
            NODE MCU -> BMP280
            D1       -> SCL
            D2       -> SDA
            GND      -> GND
            3v3      -> VCC, SDD, CSB
****************************************************/
//Deklaracja bibliotek
#include <Wire.h>
#include <SPI.h>
#include <ESP8266WiFi.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>
#include <Adafruit_MQTT.h>
#include "libs\Adafruit_MQTT_Client.h"

//******* SEKTOR CZUJNIKA ================
float temp, pres;
int poczekaj= 5000; 
Adafruit_BMP280 bme; // I2C

#define ID_URZ "b1";  //definicja id urzadzenia

/************************* WiFi Access Point *********************************/

#define WLAN_SSID       "UPC2501659" // enter your WiFi SSID
#define WLAN_PASS       "wy2fHfsvJkyp" // this is your WiFi password

/************************* Dane do polaczenia z Brokerem MQTT *********************************/

#define MQTT_SERVER      "192.168.0.200" // Adress IP Brokera MQTT
#define MQTT_SERVERPORT  1883            // Port do wyslanie
#define MQTT_USERNAME    ""              // W przypadku uzywania autoryzacji
#define MQTT_KEY         ""              // W przypadku uzywania autoryzacji

/************ Global State  ******************/

//Tworzenie klasy clienta dla NodeMCU do polaczenia z serwerem
WiFiClient client;

//Tworzenie polaczenia klasy clienta MQTT przez podanie polaczenia WiFi i Brokera MQTT oraz danych logowania
Adafruit_MQTT_Client mqtt(&client, MQTT_SERVER, MQTT_SERVERPORT, MQTT_USERNAME, MQTT_KEY);

/****************************** data stream publish/subscribe ***************************************/

Adafruit_MQTT_Publish temp_stream = Adafruit_MQTT_Publish(&mqtt, MQTT_USERNAME "b1/temp");
Adafruit_MQTT_Publish pres_stream = Adafruit_MQTT_Publish(&mqtt, MQTT_USERNAME "b1/pres");  
/*************************** Kod ************************************/

void MQTT_connect();

void setup() {
  Serial.begin(115200);
  delay(10);
  Serial.println(F("BMP280 test"));
  //Sprawdzenie czy jest podłączony czujnik 
  if (!bme.begin()) {  
    Serial.println("Sprawdz polaczenie czujnika!");
    while (1);
  }
  // Laczenie do AP WiFi
  Serial.println(); Serial.println();
  Serial.print("Connecting to ");
  Serial.println(WLAN_SSID);

  WiFi.begin(WLAN_SSID, WLAN_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();

  Serial.println("WiFi polaczone");
  Serial.println("Adres IP: "); Serial.println(WiFi.localIP());


  
}



//********** WLASCIWY PROGRAM **********************
uint32_t x=0;

void loop() {
  // Sprawdzanie polaczenia z serwerem i ponowne polaczanie gdy wymagane  
  MQTT_connect();

  // ODCZYT WARTOSCI
  float temp=bme.readTemperature();
  float pres=bme.readPressure()/100;
  // WYPISANIE NA KONSOLI  
  Serial.print("Temperatura : ");
  Serial.println(temp,DEC);
  Serial.print("Cisnienie : ");
  Serial.println(pres,DEC);
  //PUBLIKOWANIE
  temp_stream.publish(temp);
  delay(100);
  pres_stream.publish(pres);
  //POCZEKAJ
  delay(poczekaj);
  

}




//====== KONTROLA POLACZENIA ========
// Funkcja do laczenia sie ( i odnawiania polaczenia) z Brokerem MQTT
void MQTT_connect() {
  int8_t ret;

  // Wprawdz czy polaczone
  if (mqtt.connected()) {
    return;
  }

  Serial.print("Laczenie z MQTT... ");

  uint8_t retries = 3;
  while ((ret = mqtt.connect()) != 0) { // 0 oznacza polaczenie udane
       Serial.println(mqtt.connectErrorString(ret));
       Serial.println("Ponawianie proby za 5 sek...");
       mqtt.disconnect();
       delay(5000);  
       retries--;
       if (retries == 0) {
         // uspij
         while (1);
       }
  }
  Serial.println("MQTT Polaczone!");
}
