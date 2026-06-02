
#include<Arduino.h>

int in1 = 2;
int in2 = 3;
int in3 = 4;
int in4 = 5;

int command = 0;


void setup()
{
  Serial.begin(9600);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);

}

void stopALL()
{
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}

void moveForward()
{
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
}

void movebackward()
{
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
}

void moveLeft()
{
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);

}

void moveRight()
{
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);

}

void loop()
{
  if(Serial.available())
  {
    String Char = Serial.readStringUntil('\n');

    if(Char == "F")
    {
      command = 1;
    }

    else if(Char == "B")
    {
      command = 2;
    }

    else if(Char == "R")
    {
      command = 3;
    }

    else if(Char == "L")
    {
      command = 4;
    }

    else if(Char == "S")
    {
      command = 5;
    }


  }
  

   if(command == 1)
   {
     moveForward();
   }

   else if(command == 2)
   {
     movebackward();
   }

   else if(command == 3)
   {
     moveRight();
   }

   else if(command == 4)
   {
     moveLeft();
   }

   else if(command == 5)
   {
    stopALL();
   }






}