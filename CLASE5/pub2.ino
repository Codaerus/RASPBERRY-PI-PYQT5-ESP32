#include <WiFi.h>
#include <PubSubClient.h>

WiFiClient espClient;
PubSubClient client(espClient);
unsigned long int t = 0;
int i = 0;
int j = 0;
char msg[30];
void setup() {
  setup_wifi();
  client.setServer("192.168.1.16", 1883);
}
void reconnect(){
  if(client.connect("ESP32")){
    Serial.println("Enlace MQTT OK");
  }
}

void loop() {
  if(!client.connected())
    {
        reconnect();
    }
  if(millis()-t>5000)
    {
      snprintf(msg,30,"%d,%d",i,j);
      client.publish("canalx",msg);
      t = millis();
      i++;
      j+=2;
    }
}

void setup_wifi(){
  Serial.begin(9600);
  WiFi.begin("MOVISTAR_78A8","NS2ajtQJ7TtDt9m"); //DHCP
  while(WiFi.status() != WL_CONNECTED)
    {
      Serial.print(".");
      delay(300);
    }
  Serial.println(WiFi.localIP());
}
