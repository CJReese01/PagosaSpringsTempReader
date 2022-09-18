#include <WiFi.h>
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
#define OLED_RESET     4 // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Network information
char* ssid = "Guest";
const char* password = "";

// ThingSpeak settings
char server[] = "api.thingspeak.com";
String writeAPIKey = "5NKOO71X52Q4ALCQ";

#include <OneWire.h> 
#include <DallasTemperature.h>
#define ONE_WIRE_BUS 33

OneWire oneWire(ONE_WIRE_BUS); 
DallasTemperature sensors(&oneWire);
float tc;
float tf;

int ina = 14;
int inb = 27;
int but = 26;
int butstate;
float inaLS;
float count;
float inaa;
float bclick;
float h_exit;
float menu_layer;
float L;
float M;
float K;
float Kp;
float T;
int N;
int edit;
float pass_length;
int charIndex;
float px1;
float py1;
float tot;
float i;
float j; 
int v1;
int back;
float start_scan;

char varP;
String pass_save;
String wifi_ID;
float SID;
//---
const unsigned long eventInterval = 120000;   //120,000 = 2 min 
unsigned long send_time = 0;
int ts = 1;

//------------------------------
void setup(){
  Serial.begin(9600);
  //connectWiFi();
  pinMode(ina, INPUT);
  pinMode(inb, INPUT);
  pinMode(but, INPUT);
  bclick = 0;
  h_exit = 0;
  menu_layer = 0;
  L = 15;
  M = 31;
  N = 0;
  K = -1;
  edit = 0;
  charIndex = 0;
  px1 = -2;
  py1 = 7;
  tot = 0;
  i = 0;
  j = 0;
  v1 = 1;
  back = 0;
  start_scan = 1;
  ts = 1;
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);// Address 0x3C for 128x64
  }
//------------------------------
void loop(){

  unsigned long currentTime = millis();
  
  if (back == 1){
    h_exit = 1;
    back = 0;
    bclick = 0;
  }

  if (h_exit == 0){      // temp
    bclick = 0;
    rotate();
    temp_check();
    disp_temp();
    menu_layer = 0;

    if(ts == 1){
      send_time = currentTime;
      ts = 0;
      Serial.println("timer start");
    }
    if((currentTime - send_time) > eventInterval){
      Serial.println("sending data");
      httpRequest(tc, tf);
      ts = 1;
    }
  }
  
  if (h_exit > 0){       // no longer disp temp
    if (h_exit == 1){
      bclick = 0;
      menu1();
      menu_layer = 1;
      rotate();
      if (count != 0){
        scroll_m1();
      }
        
      if (bclick == 1){
        if (L == 15){       // network selection
          edit = 0;
          bclick = 0;
          start_scan = 1;
          K = -1;
          N = 0;
          network_select();
        }
        if (L == 23){       // password edit
          bclick = 0;
          L = 15;
          edit = 0;
          pass_change();
        }
        if (L == 31){       // clear password
          edit = 0;
          bclick = 0;
          M = 31;
          delay(500);
          pass_clear();
        }
        if (L == 39){       // wifi connection test
          bclick = 0;
          L = 15;
          edit = 0;
          delay(100);
          wifi_test();
        }
        if (L == 47){       // back
          menu_layer = 0;
          h_exit = 0;
          bclick = 0;
          L = 15;
          delay(100);
        }
        
      }
    }   
  }

/*  
    if (WiFi.status() != WL_CONNECTED) { 
      connectWiFi();
      }
    httpRequest(tc, tf);
*/
    
  }
//------------------------------
void connectWiFi(){

  //while (WiFi.status() != WL_CONNECT_FAILED){
  
    //WiFi.begin(ssid, password);
    //delay(1000);
    
    WiFi.begin(wifi_ID.c_str(), pass_save.c_str());
    delay(1000);
    
  //  } 
     
  //Serial.println("Connected");      // Display a notification that the connection is successful. 
  //delay(2000);
  }
//------------------------------
void httpRequest(float field1Data, int field2Data) {

  WiFiClient client;  
  if (!client.connect(server, 80)){
      
    Serial.println("Connection failed");
    client.stop();
    return;     
  }
    
  else{   // Create data string to send to ThingSpeak.
    String data = "field1=" + String(field1Data) + "&field2=" + String(field2Data); //shows how to include additional field data in http post
        
    if (client.connect(server, 80)) {    // POST data to ThingSpeak.
          
      client.println("POST /update HTTP/1.1");
      client.println("Host: api.thingspeak.com");
      client.println("Connection: close");
      client.println("User-Agent: ESP32WiFi/1.1");
      client.println("X-THINGSPEAKAPIKEY: "+writeAPIKey);
      client.println("Content-Type: application/x-www-form-urlencoded");
      client.print("Content-Length: ");
      client.print(data.length());
      client.print("\n\n");
      client.print(data);
      Serial.println("sent");
      delay(250);
      }
    }
  client.stop();
  }
//------------------------------
void temp_check(){
  sensors.requestTemperatures();                // Send the command to get temperature readings 
  tc = sensors.getTempCByIndex(0);
  tf = tc * 9 / 5 + 32;
}
//------------------------------
void rotate(){
  inaa = digitalRead(ina);
  if (inaa != inaLS){
    if (digitalRead(inb) != inaa){
      count = count-.4;
      if (round(count) < count){
        count = round(count);
        }
      }
      
    else {count = count+.4;
      if (round(count) > count){
        count = round(count);
        }
      }
    }
  inaLS = inaa;
  
  butstate = digitalRead(but);
  if (butstate != 1){
    count = 0;
    bclick = 1;
    h_exit = h_exit + 1;
//    Serial.println(butstate);
    delay(250);
    }

}
//---------------------------------------- temp
void disp_temp(){
  display.clearDisplay();
  display.setTextSize(2);             // Normal 1:1 pixel scale
  display.setTextColor(SSD1306_WHITE);        // Draw white text
  display.setCursor(0,0);             // Start at top-left corner
  display.print(tf);
  display.print(" "); 
  display.cp437(true);
  display.write(248);
  display.print("F");
  display.display();
}
//---------------------------------------- options
void menu1(){
  display.clearDisplay();
  display.setTextSize(1.5);             // Normal 1:1 pixel scale
  display.setTextColor(SSD1306_WHITE);        // Draw white text
  display.setCursor(0,0);             // Start at top-left corner
  display.println("Current connection:");
  display.print("  "); 
  display.println(wifi_ID);
  display.drawLine(0,15 , 127,15, WHITE);
  display.println("Acess Point");
  display.println("Password");
  display.println(" Clear password");
  display.println("Connection test");
  display.println("Return");
  display.drawRect(-1,L-1 , 92,11, WHITE);    //L = 15 ini 
  display.display();
}
//---------------------------------------- password clear
void menu2(){
  display.clearDisplay();
  display.setTextSize(1.5);             // Normal 1:1 pixel scale
  display.setTextColor(SSD1306_WHITE);        // Draw white text
  display.setCursor(0,0);             // Start at top-left corner
  display.println("Do you want to clear the current password?");
  display.drawLine(0,16 , 127,16, WHITE);
  display.setCursor(37,30);
  display.println("NO    YES");
  display.drawRect(M,28 , 21,11, WHITE);    //M =  35 ini 
  display.display();
}
//----------------------------------------
void scroll_m1(){
  if(menu_layer == 1){
    if(count == 1){
      count = 0;
      L = L + 8;
    }
    
    if(count == -1){
      count = 0;
      L = L - 8;
    }
    
    if(L > 48){
      L = 47;
    }
    
    if(L < 12){
      L = 15;
    }
  }
}
//----------------------------------------
void scroll_m2(){
  if(count == 1){
    count = 0;
    M = M + 40;
  }
    
  if(count == -1){
    count = 0;
    M = M - 40;
  }
    
  if(M > 73){
    M = 71;
  }
    
  if(M < 30){
    M = 31;
  }
}
//----------------------------------------
void scroll_m3(){
  if(count == 1){
    count = 0;
    K = K + 8;
  }
  
  if(count == -1){
    count = 0;
    K = K - 8;
  }
  
  if(K > 57){
    K = 55;
  }
  
  if(K < -2){
    K = -1;
  }
}
//----------------------------------------
void pass_change(){
  
  while (edit == 0){
  //int charL = 26 + 26 + 10 + 10 + 20; //letters (upper), letters (lower), numbers, number_sym, extra (NO, '";:`~)
  String sym = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[]{}|\/,<>.?";
  int charL = sym.length();

  bclick = 0;
  if (v1 == 0){
    rotate();
  }
  v1 = 0;
  
  if (count == 1) {              //cycle to next char at position
    charIndex = charIndex + 1;
    count = 0;
    tot = 1;
    if (charIndex > (charL - 1)){
      charIndex = 0;
    }
  }
   
  else if (count == -1) {        //cycle tp previous char at position
    charIndex = charIndex - 1;
    count = 0;
    tot = -1;
    if (charIndex < 0){
      charIndex = charL - 1;
    }
  }
   
  else if (bclick == 1) {        // select button pressed increase position or exit
    delay(500);
    butstate = digitalRead(but);
    if (butstate != 1){
      back = 1;
      edit = 1;
      h_exit = 1;
      bclick = 0;
      menu_layer = 1;
      L = 15;
      count = 0;
      display.clearDisplay();
      display.setTextSize(1);          // Normal 1:1 pixel scale
      display.setTextColor(WHITE);     // Draw white text
      display.setCursor(20,16);          // Start at top-left corner
      display.print("Password Saved");
      display.display();
      delay(1500);
      
      edit = 1;
      h_exit = 1;
      bclick = 0;
      menu_layer = 1;
      L = 15;
      count = 0;
      back = 1;
      break;
    }

    varP = sym[charIndex];
    varP = char(varP);
    pass_save = String(pass_save + varP);

    Serial.println(varP);
    Serial.println(pass_save);
    bclick = 0;
 
  }
    
//20 x 5
  if (tot == 1){         // forward
    if ((charIndex % 21 == 0)){
      py1 = 7 + (charIndex/20)*8;
      px1 = -2;
      i = 1;
    }
    if(i != 1){
      px1 = px1 + 6;
      i = 0;
    }
    tot = 0;
    i = 0;
  }

  if (tot == -1){         // backward
    if ((charIndex != 0) && ((charIndex-20) % 21 == 0)){
      py1 = 39 - (-1*((charIndex-20)/21)+4)*8;
      px1 = 118;
      j = 1;
    }
    if(j != 1){
      px1 = px1 - 6;
      j = 0;
    }
    if (charIndex == 86){
      py1 = 39;
      px1 = 10;
      j = 0;
    }
    tot = 0;
    j = 0;
  }

  display.clearDisplay();
  display.setTextSize(1);          // Normal 1:1 pixel scale
  display.setTextColor(WHITE);     // Draw white text
  display.drawLine(0,7 , 127,7, WHITE);
  display.setCursor(0,9);          // Start at top-left corner
  display.cp437(true);             // Use full 256 char 'Code Page 437' font
  display.print(sym);
  display.drawRect(px1,py1 , 9,11, WHITE);
  display.setCursor(0,0);
  display.print(pass_save);
  display.display();
  }
  h_exit == 1;
}
//----------------------------------------
void pass_clear(){
  while (edit == 0){
    menu2();
    bclick = 0;
    rotate();
    scroll_m2();

    if (bclick == 1 && M == 31){
      edit = 1;
      h_exit = 1;
      bclick = 0;
      menu_layer = 1;
      L = 15;
      M = 31;
      count = 0;
      back == 1;
      menu1();
      delay(500);
      break;
    }

    if (bclick == 1 && M == 71){
      pass_save = String();
      display.clearDisplay();
      display.setTextSize(1);          // Normal 1:1 pixel scale
      display.setTextColor(WHITE);     // Draw white text
      display.setCursor(16,16);          // Start at top-left corner
      display.print("Password Cleared");
      display.display();
      delay(1750);
      
      h_exit = 1;
      bclick = 0;
      menu_layer = 1;
      L = 15;
      M = 31;
      count = 0;
      back == 1;
      menu1();
      break;
    }
    
  }
}
//----------------------------------------
void network_select(){
  display.clearDisplay();
  display.display();
  delay(100);
  bclick = 0;
  start_scan = 1;
  edit = 0;
  
  
  while (edit == 0){
    rotate();
    scroll_m3();
    
    if (start_scan == 1){
      int n = WiFi.scanNetworks();
      while (edit == 0){
        if (n == 0) {
          display.clearDisplay();
          display.setTextSize(1);          // Normal 1:1 pixel scale
          display.setTextColor(WHITE);     // Draw white text
          display.setCursor(0,0);          // Start at top-left corner
          display.println("No networks found!");
        }
        else {
          for (int i = 0; i < 7; ++i) {
            // Print SSID and RSSI for each network found
            if (edit == 0){
              display.setTextSize(1);          // Normal 1:1 pixel scale
              display.setTextColor(WHITE);     // Draw white text
              display.setCursor(0,N);          // Start at top-left corner
              display.fillRect(0,N, 127, 6, BLACK);
              display.display();
              display.print(WiFi.SSID(i));
              display.display();
              N = N + 8;
              if (N > 64){
                edit = 1;
                K = -1;
                Kp = K;
              }
            }
          //delay(250);
          }
        }
        start_scan = 0;
      }
      edit = 0;
    }

    //Serial.println(K);
    display.drawRect(-1,K, 126,9, WHITE);
    display.display();
    if (K != Kp){
      display.drawRect(-1,Kp, 126,9, BLACK);
      display.display();
    }
    Kp = K;
    if (bclick == 1){
      bclick = 0;
      SID = ((K+1)/8);
      wifi_ID = WiFi.SSID(SID);
      
      delay(500);
      butstate = digitalRead(but);
      if (butstate != 1){
        back = 1;
        edit = 1;
        h_exit = 1;
        bclick = 0;
        menu_layer = 1;
        L = 15;
        count = 0;
        display.clearDisplay();
        display.setTextSize(1);          // Normal 1:1 pixel scale
        display.setTextColor(WHITE);     // Draw white text
        display.setCursor(10,16);          // Start at top-left corner
        display.print("Acess point Saved");
        display.display();
        delay(1500);
        break;
      }
      
      //Serial.println(K);
      //Serial.println(SID);
      //Serial.println(wifi_ID);
      delay(1000);
    }
  }
}
//----------------------------------------
void wifi_test(){
  edit = 0;
  T = 1;

  display.clearDisplay();
  display.setTextSize(1);          // Normal 1:1 pixel scale
  display.setTextColor(WHITE);     // Draw white text
  display.setCursor(10,16);          // Start at top-left corner
  display.print("Testing connection");
  display.display();
  
  while (edit == 0){
    connectWiFi();
    //Serial.println(WiFi.status());
    delay(5000);
  
    WiFiClient client;  
    while (!client.connect(server, 80)){
      client.stop();
      T = T + 1;
      Serial.println("Server connection failed");
      delay(1000);
      
      if (T == 5){
        display.clearDisplay();
        display.setTextSize(1);          // Normal 1:1 pixel scale
        display.setTextColor(WHITE);     // Draw white text
        display.setCursor(6,16);        
        display.print("Could not connect to");
        display.setCursor(6,24);
        display.print(" the network/server");
        display.display();
        delay(3000);
        back = 1;
        break; 
      }
    }

    if (T != 5){
      display.clearDisplay();
      display.setTextSize(1);          // Normal 1:1 pixel scale
      display.setTextColor(WHITE);     // Draw white text
      display.setCursor(15,16);        
      display.print("Connected to the");
      display.setCursor(21,24);
      display.print("network/server");
      display.display();
      delay(3000);
    }
    edit = 1;
    back = 1;
  }
}
