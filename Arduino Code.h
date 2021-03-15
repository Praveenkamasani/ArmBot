//ARDUINO CODE

#define lmotorf 10
#define lmotorb 5
#define rmotorf 9
#define rmotorb 6
#include <Servo.h>
#define pumpf 12
#define pumpb 13
#define enable 8
Servo myservo;
int pos = 0,k;
char readvalue;
55void setup()
{
 pinMode(lmotorf,OUTPUT);
 pinMode(lmotorb,OUTPUT);
 pinMode(rmotorf,OUTPUT);
 pinMode(rmotorb,OUTPUT);
 pinMode(enable,OUTPUT);
 pinMode(4,INPUT);
 pinMode(2,INPUT);
 myservo.attach(3);
 pinMode(pumpf,OUTPUT);
 pinMode(pumpb,OUTPUT);
 digitalWrite(enable,HIGH);
 Serial.begin(9600);
}
void loop()
{
 int lsensor=digitalRead(4);
 int rsensor=digitalRead(2);
 if((lsensor==HIGH)&&(rsensor==HIGH))
56 {
 digitalWrite(lmotorf,HIGH);
 digitalWrite(rmotorf,HIGH);
 }
 if((lsensor==HIGH)&&(rsensor==LOW))
 {
 digitalWrite(lmotorf,LOW);
 digitalWrite(rmotorf,HIGH);
 }
 if((lsensor==LOW)&&(rsensor==HIGH))
 {
 digitalWrite(lmotorf,HIGH);
 digitalWrite(rmotorf,LOW);
 }
 if((lsensor==LOW)&&(rsensor==LOW))
 {
 digitalWrite(lmotorf,LOW);
 digitalWrite(rmotorf,LOW);
 delay(200);
 Serial.println("signal from arduino");
57 if (Serial.available())
 {
 readvalue = Serial.read();
 if(readvalue='1')
 {
 myservo.write(k);
 for (pos = k; pos <= 180; pos += 1)
 {
 myservo.write(pos);
 delay(100);
 }
 digitalWrite(pumpf,HIGH);
 digitalWrite(pumpb,LOW);
 delay(2000);
 digitalWrite(pumpf,LOW);
 digitalWrite(pumpb,LOW);
 for (pos = 180; pos >= k; pos -= 1)
 {
 myservo.write(pos);
 delay(100);
 }
58 do
 {
 digitalWrite(lmotorf,HIGH);
 digitalWrite(rmotorf,HIGH);
 digitalWrite(lmotorb,LOW);
 digitalWrite(rmotorb,LOW);
 }while((lsensor== LOW)&&(rsensor== LOW));
 }
 else
 {
do
 {
 delay(3000);
 digitalWrite(lmotorf,HIGH);
 digitalWrite(rmotorf,HIGH);
 digitalWrite(lmotorb,LOW);
 digitalWrite(rmotorb,LOW);
 }while((lsensor==LOW)&&(rsensor==LOW));
 }
 }}}
