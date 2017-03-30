#include <Arduino.h>
#include "color.h"
#include "comm.h"

bool firstRun = true;

void setup() {
  Serial.begin(9600);
  Serial.write(1);
  addLeds();
}

void loop() {
  if(firstRun) {
    clearAll();
    firstRun = false;
  }

  checkForInstructions();
}
