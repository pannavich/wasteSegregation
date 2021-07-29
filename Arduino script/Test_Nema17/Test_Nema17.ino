#include <Stepper.h>
int dirPin =2;
int stepPin = 3;
int enNema = 8;
const int stepsPerRevolution = 200;
void setup() {
  // put your setup code here, to run once:
  pinMode(dirPin,OUTPUT);
  pinMode(stepPin,OUTPUT);
  Stepper myStepper(stepsPerRevolution, dirPin,stepPin);
  back_step_rev(16);
  delay(2000);
   back_step_rev(16);
  delay(2000);
//   step_rev(16);
//  delay(2000);
//  step_rev(16);
//  delay(2000);
}
void back_step_rev(int rev){
  digitalWrite(enNema,LOW);
  delay(500);
   digitalWrite(dirPin, LOW);
   
    for(int i = 0; i < rev*stepsPerRevolution; i++)
  {
    // These four lines result in 1 step:
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(500);
  }
  digitalWrite(enNema,HIGH);
}
void step_rev(int rev){
  digitalWrite(enNema,LOW);
   delay(500);
   digitalWrite(dirPin, HIGH);
    for(int i = 0; i < rev*stepsPerRevolution; i++)
  {
    // These four lines result in 1 step:
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(500);
  }
  digitalWrite(enNema,HIGH);

}
void loop() {

}
