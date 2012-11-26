#include <Servo.h> 

Servo myservo;

void setup() 
{ 
  myservo.attach(9); 
  myservo.writeMicroseconds(1200); 
} 

int main(){
  
  int pos = 1200;
  int s = 0;

  while (pos < 1800)
  {
    myservo.writeMicroseconds(pos);              
    delay(5);
    pos = pos + 1;
  }
} 

