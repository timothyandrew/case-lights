#include "FastLED.h"
#include "color.h"

int color;
int saturation;
int value;

void rgb(bool firstRun) {
  if(firstRun) {
    color = 0;
    saturation = 255;
    value = 255;
  }

  setColorSpectrumStartingAt(CHSV(color, saturation, value));
  color = nextHue(color);
  delay(80);
}

void pulse(bool firstRun) {
  if(firstRun) {
    color = 0;
    saturation = 255;
    value = 255;
  }

  setColor(CHSV(color, saturation, value));
  color++;
  delay(80);
}

void white() {
  color = 140;
  saturation = 100;
  value = 200;

  setColor(CHSV(color, saturation, value));
}

void clear() {
  setColor(CHSV(0,0,0));
}
