#include <Stepper.h>
int dirPin =2;
int stepPin = 3;
const int stepsPerRevolution = 200;
int trigPin = 11;
int echoPin =12;
long duration, cm;
int DCMotorin1=9;
int DCMotorin2=10;
int enNema = 8;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(1);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(DCMotorin1, OUTPUT);
  pinMode(DCMotorin2, OUTPUT);
  pinMode(dirPin,OUTPUT);
  pinMode(stepPin,OUTPUT);
  Stepper myStepper(stepsPerRevolution, dirPin,stepPin);
  pinMode(enNema, OUTPUT);
 
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
void open_kicker(){
  digitalWrite(DCMotorin1,LOW);
  digitalWrite(DCMotorin2,HIGH);
  delay(100);
  digitalWrite(DCMotorin1,LOW);
  digitalWrite(DCMotorin2,LOW);
  
}

void close_kicker(){
  digitalWrite(DCMotorin1,HIGH);
  digitalWrite(DCMotorin2,LOW);
  delay(80);
  digitalWrite(DCMotorin1,HIGH);
  digitalWrite(DCMotorin2,HIGH);
  
}
 
void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  cm = (duration/2)/29.1;
  
  if(cm<=5){
    int x = 1;
    Serial.println(x);
    Serial.flush();
  }
  else{
    return;
  }
  while(!Serial.available()){}

  int y=0;
  while(Serial.available()){
    y=Serial.readString().toInt();
  }
    
    if(y==2){ //Type 1
      //move linear actuator to bin 1
      //kick the object
    delay(1000);
    open_kicker();
    delay(1000);
    close_kicker();

    int z=5;
    Serial.println(z);
    Serial.flush();
  }
  else if(y==3){ //Type 2
      //move linear actuator to bin 2
      //kick the object
    step_rev(16);
    delay(1000);
    open_kicker();
    delay(1000);
        close_kicker();
    back_step_rev(16);
    delay(1000);
    int z=5;
    Serial.println(z);
    Serial.flush();
  }
  else if(y==4){ //Type 3
      //move linear actuator to bin 3
      //kick the object
    step_rev(32);
    delay(1000);
    open_kicker();
    delay(1000);
  close_kicker();
    back_step_rev(32);
    delay(1000);
    int z=5;
    Serial.println(z);
    Serial.flush();
  }
  }
