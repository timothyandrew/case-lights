#include <Arduino.h>
#include "styles.h"

int lastInstruction = 'rgb';

void ack() {
  Serial.write(2);
}

void execInstruction(int code, bool firstRun) {
  switch(code) {
  case 10:
    pulse(firstRun);
    break;
  case 11:
    rgb(firstRun);
    break;
  case 12:
    white();
    break;
  case 30:
    // Pause; do nothing
    break;
  }
}

void checkForInstructions() {
  if (Serial.available() > 0) {
    int incomingByte  = Serial.read();
    execInstruction(incomingByte, true);
    lastInstruction = incomingByte;
    ack();
  } else {
    execInstruction(lastInstruction, false);
  }
}
