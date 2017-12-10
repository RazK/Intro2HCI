/*
* Ultrasonic Sensor HC-SR04 and Arduino Tutorial
*
* Crated by Dejan Nedelkovski,
* www.HowToMechatronics.com
*
*/
// defines pins numbers
const int trigPin = 9;
const int echoPin = 10;

const float SPEED_OF_SOUND = 0.034;

const int MAX_DISTANCE = 400;

const int SAMPLE_TIME = 50;

// defines variables
long duration;
int distance;
int t = 0;

void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600); // Starts the serial communication

}

void loop() {
  if (t < SAMPLE_TIME){
    // Clears the trigPin
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
  
    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    
    // Reads the echoPin, returns the sound wave travel time in microseconds
    duration = pulseIn(echoPin, HIGH);
  
    duration -= 10;
    
    // Calculating the distance
    distance= duration*SPEED_OF_SOUND/2;
    // Prints the distance on the Serial Monitor
    if (distance < MAX_DISTANCE){
      Serial.print("Distance: ");
      Serial.println(distance);
  
    }
  }
  t ++;
}
