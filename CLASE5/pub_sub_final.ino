#include <WiFi.h>
#include <PubSubClient.h>

WiFiClient espClient;
PubSubClient client(espClient);
unsigned long int t = 0;
char msg[30];
void setup() {
  setup_wifi();
  client.setServer("192.168.1.14", 1883);
  client.setCallback(callback);
}
void callback(const char* topic, byte* payload, unsigned int length){
  payload[length] = '\0';
  String val = String((char*)payload);
  Serial.println(val);
}
void reconnect(){
  if(client.connect("ESP32")){
    Serial.println("Enlace MQTT OK");
    client.subscribe("canaly");
  }
}

void loop() {
  if(!client.connected())
    {
        reconnect();
    }
  client.loop();
  if(millis()-t>10000)
    {
      int pot1 = 14;
      int pot2 = 20;
      snprintf(msg,30,"%d,%d",pot1,pot2);
      client.publish("canalx",msg);
      t = millis();
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
