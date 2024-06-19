#include <WiFiNINA.h>

//wifi
char ssid[] = "Nextphp";
char pass[] = "88888888";
// char myServer[] = "192.168.0.193"; //OM2M的IP
char myServer[] = "python-img.vercel.app";
int status = WL_IDLE_STATUS;
WiFiServer server(80);


//ultrasonic sensor
const int trigPin = 9;
const int echoPin = 10;
float duration, distance;
String sensorID = "1";

void setup() {
  //ultrasonic sensor
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);

  //wifi
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to Network named: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid, pass);
    delay(1000);
  }
  server.begin();

  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);  
}

void getData(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = (duration*.0343)/2;
  Serial.print("Distance: ");
  Serial.println(distance);
  delay(100);
}

void sendData(){
  String jsonID = "{\"ID\":" + sensorID;
  String jsonData = ",\"Distance\":" + String(distance) + "}";
  String jsonStr = jsonID + jsonData; // 定義JSON字串

  WiFiClient client;
  Serial.println("\nStarting connection to server...");
  Serial.println(jsonStr);
  
  // if you get a connection, report back via serial:
  if (client.connectSSL(myServer, 443)) {
    Serial.println("Connected to server");

    // Make a HTTP request
    client.println("POST /api/sensorData HTTP/1.1");
    client.println("Host: " + String(myServer));
    client.println("Content-Type: application/json");
    client.print("Content-Length: ");
    client.println(jsonStr.length());
    client.println("Connection: close");
    client.println();
    client.println(jsonStr);

    // Wait for the server's response
    // while (client.connected()) {
    //   if (client.available()) {
    //     String line = client.readStringUntil('\n');
    //     // Serial.println(line);
    //   }
    // }
      client.stop();


  }
  else{
    Serial.println(client.connect(myServer, 80));
  }
  delay(500);
}

void loop() {
  getData();
  sendData();
}