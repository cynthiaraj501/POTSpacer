// Temperature sensor
#include <Adafruit_AHTX0.h>

Adafruit_AHTX0 aht;


// Pulse sensor
#define USE_ARDUINO_INTERRUPTS true    // Set-up low-level interrupts for most acurate BPM math.
#include <PulseSensorPlayground.h>     // Includes the PulseSensorPlayground Library.   

//  Variables
const int PulseWire = 0;       // PulseSensor PURPLE WIRE connected to ANALOG PIN 0
const int LED13 = 13;          // The on-board Arduino LED, close to PIN 13.
int Threshold = 550;           // Determine which Signal to "count as a beat" and which to ignore.
                               // Use the "Gettting Started Project" to fine-tune Threshold Value beyond default setting.
                               // Otherwise leave the default "550" value. 
                               
PulseSensorPlayground pulseSensor;



// General
double sum_temp = 0;
double sum_bpm = 0;
unsigned long initTime;


char userInput;



void setup() {
  // Vibration motor
  pinMode(4, OUTPUT);
  
  
  // General
  initTime = millis();
  
  // Temperature sensor
  Serial.begin(115200);
  //Serial.println("Adafruit AHT10/AHT20 demo!");

  if (! aht.begin()) {
    Serial.println("AHT20 NOT WORKING!");
    while (1) delay(10);
  }

  // Pulse sensor
  // Serial.begin(9600);          // For Serial Monitor

  // Configure the PulseSensor object, by assigning our variables to it. 
  pulseSensor.analogInput(PulseWire);   
  pulseSensor.blinkOnPulse(LED13);       //auto-magically blink Arduino's LED with heartbeat.
  pulseSensor.setThreshold(Threshold);   

  // Double-check the "pulseSensor" object was created and "began" seeing a signal. 
   if (pulseSensor.begin()) {
    //Serial.println("We created a pulseSensor Object !");  //This prints one time at Arduino power-up,  or on Arduino reset.  
  }
}



void loop() {
  // Temperature sensor
  sensors_event_t humidity, temp;
  aht.getEvent(&humidity, &temp);// populate temp and humidity objects with fresh data


  //Serial.print("Temperature: "); Serial.print(temp.temperature); Serial.println(" degrees C");
  //Serial.print("Humidity: "); Serial.print(humidity.relative_humidity); Serial.println("% rH");

  // Pulse sensor
  int myBPM = pulseSensor.getBeatsPerMinute();  // Calls function on our pulseSensor object that returns BPM as an "int".
                                               // "myBPM" hold this BPM value now. 

  //if (pulseSensor.sawStartOfBeat()) {            // Constantly test to see if "a beat happened". 
    //Serial.println("♥  A HeartBeat Happened ! "); // If test is "true", print a message "a heartbeat happened".

  /*
  Serial.print("BPM: ");                        // Print phrase "BPM: " 
  Serial.println(myBPM);                        // Print the value inside of myBPM. 
  //}
  */

  if (Serial.available() > 0) {
    userInput = Serial.read();
      if (userInput == 's') {
        Serial.print(temp.temperature);
        Serial.print(",");
        Serial.println(myBPM); 
        delay(1000);
      }
  }


  if (myBPM >= 100) {
    digitalWrite(4, HIGH);
    delay(1000);
    digitalWrite(4, LOW);
    delay(1000);
  }

  if (temp.temperature >= 38) {
    digitalWrite(4, HIGH);
    delay(1000);
    digitalWrite(4, LOW);
    delay(1000);
  }

}
