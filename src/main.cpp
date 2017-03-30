#include "FastLED.h"

#define DATA_PIN    5        // change to your data pin
#define COLOR_ORDER GRB      // if colors are mismatched; change this
#define NUM_LEDS    30       // change to the number of LEDs in your strip
#define LED_TYPE    WS2812B

CRGB leds[NUM_LEDS];

void setup() {
  Serial.begin(9600);
  FastLED.addLeds<LED_TYPE, DATA_PIN, COLOR_ORDER>(leds, NUM_LEDS);
}

int nextHue(int color) {
  return (color + (255/NUM_LEDS)) % 255;
}

void flush() {
  FastLED.show();
}

void clearAll() {
  for(int i=0; i<NUM_LEDS; i++) {
    leds[i] = CHSV(0,0,0);
  }

  flush();
}

void setColorSpectrumStartingAt(CHSV color) {
  for(int i=0; i<NUM_LEDS; i++) {
    leds[i] = color;
    color = CHSV(nextHue(color.hue), color.sat, color.val);
  }

  flush();
}

void setColor(CHSV color) {
  for(int i=0; i<NUM_LEDS; i++) {
    leds[i] = color;
  }

  flush();
}

void loop() {
  Serial.print("Hello world!");
  delay(10);
}
