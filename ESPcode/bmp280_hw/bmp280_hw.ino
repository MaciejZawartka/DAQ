 /**********************************************
 Połączenie czujnika BMP280 do płytki HW 628 v1.1
 Odczyt danych z czujnka
 Polaczenie z siecią
 wysyłanie danych do clienta
**********************************************/

#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>
#include <ESP8266WiFi.h> 

#define BMP_SCK 13
#define BMP_MISO 12
#define BMP_MOSI 11 
#define BMP_CS 10

Adafruit_BMP280 bme; // I2C
float temp,pres,altit;
int ilosc_odczytow=0;

// ====================== dane do sieci wi fi 
String apiKey = "192.168.0.15";
const char* server1 = "80";

//=================================== dom    ==========
//const char* ssid = "TP-LINK_832C7D";
//const char* password = "90699443";

// ============== samsung =========
//const char* ssid = "Kamilwifi";
//const char* password = "11112222";

// ============== mackowe =========
const char* ssid = "UPC2501659";
const char* password = "wy2fHfsvJkyp";


// ===SOSNOWIEC===
//const char* ssid = "UPC52173CC";
//const char* password = "CsebYcwrm4zz";

WiFiClient client;
WiFiServer server(80);


//================= wspolczynniki kalibracyjne ============================
float korekt_temp,korekt_pres,korekt_wys=1;

//===============================================================================
//=============================================  SETUP  =========================
//===============================================================================
void setup() {
  
  Serial.begin(9600);
  Serial.println(F("BMP280 test"));

  //=============== sprawdzenie czy jest podłączony czujnik ================
  if (!bme.begin()) {  
    Serial.println("Sprawdz połączenie czujnika!");
    while (1);
  }
 // WiFi.begin(ssid, password);
  
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  
  //=============== progres w łaczeniu sie z siecia=============
  while (WiFi.status() != WL_CONNECTED) 
  {
    delay(500);
    Serial.print(".");
  }
  //============== polaczono z wi fi ==================
  Serial.println("");
  Serial.println(" Polaczono sie z siecia WiFi ");  
 //================== adres gdzie sa rzeczy ================
  Serial.print("Use this URL to connect: ");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/"); 
  server.begin();
}

//================================================================================================
//================================================================================================

void loop() {
 
  //================== serwer ================
    WiFiClient client = server.available();
    if (!client) {
      return;
    }
     
    // Wait until the client sends some data
    Serial.println("new client");
    int timewate = 0;
    while(!client.available()){
      delay(1);
      timewate = timewate +1;
      if(timewate>1800)
      {
        Serial.println(">>> Client Timeout !");
        client.stop();
        return;
      }
    }
  //===================== odswiezenie strony co odczyt - na komp - dziala/ telefon - nie dziala=====
   client.print("<meta http-equiv='refresh' content='1'>");
   client.println('\n');

  //================ zliczanie odczytow =================================
  
   ilosc_odczytow=ilosc_odczytow+1;
    client.print((String)"jest to odczyt numer: "+ilosc_odczytow);
   client.println('\n');
  //=============== odczyt temperatury =================================
    Serial.print("T=");
    temp=bme.readTemperature();
    Serial.print(temp);
    Serial.print(" *C");
    client.println((String)"temperatura: "+temp+" C");
    client.println('\n');
    
  //=============== odczyt cisnienia ===================================
    Serial.print(" P=");
    pres=bme.readPressure()/100;
    Serial.print(pres);
    Serial.print(" hPa");
    client.println((String)"cisnienie: "+pres+" hPa");
    client.println('\n');
    
  //=============== odczyt wysokosci na podst. cisnienia odniesienia ===
    Serial.print(" A= ");
    altit=bme.readAltitude(1013.25);
    Serial.print(altit); // this should be adjusted to your local forcase
    Serial.println(" m");
    client.println((String)"wysokosc: "+altit+" m");
    client.println('\n');
  
    //przerwa 5s  
    delay(1000);
}
