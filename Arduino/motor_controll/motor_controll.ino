#include <Servo.h> 

int motorpin = 10;


void setup() 
{ 
  pinMode(motorpin, OUTPUT);
} 

int s = 0;

void loop()
{
  while (s < 1)
  {
    delay(1000);
    analogWrite(motorpin, );
    s = s + 1;
    delay(20);
  }
}
