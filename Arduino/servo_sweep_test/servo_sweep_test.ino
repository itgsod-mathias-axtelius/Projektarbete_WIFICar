#include <Servo.h> 

Servo myservo;

void setup() 
{ 
  myservo.attach(9);
  myservo.writeMicroseconds(1200); 
} 

int pos = 1200;
int s = 0;

int main(){
  while(s < 4)
  {
    for(pos = 1200; pos < 1800; pos += 1)  
    {                                  
      myservo.writeMicroseconds(pos);              
      delay(15);                       
    } 
    for(pos = 1800; pos>= 1200; pos-=1)    
    {                                
      myservo.writeMicroseconds(pos);              
      delay(15);                      
    }
    s = s + 1;
  } 
} 
