//int motor1pin1 = 2;
//int motor1pin2 = 3;
//int enA = 9;
int DCMotorin1=9;
int DCMotorin2=10;
int en = 8;

void setup(){
  pinMode(DCMotorin1, OUTPUT);
  pinMode(DCMotorin2, OUTPUT);
  pinMode(en,OUTPUT);
  Serial.begin(9600);
  digitalWrite(en,HIGH);
  open_kicker();

 
}
void loop(){
  
}
//  close_kicker();
//  delay(2000);
void open_kicker(){
  digitalWrite(DCMotorin1,LOW);
  digitalWrite(DCMotorin2,HIGH);
  delay(150);
  digitalWrite(DCMotorin1,LOW);
  digitalWrite(DCMotorin2,LOW);
  
}

void close_kicker(){
  digitalWrite(DCMotorin1,HIGH);
  digitalWrite(DCMotorin2,LOW);
  delay(100);
  digitalWrite(DCMotorin1,HIGH);
  digitalWrite(DCMotorin2,HIGH);
  
}
