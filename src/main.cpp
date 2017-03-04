#include "FastLED.h"

#define DATA_PIN    5        // change to your data pin
#define COLOR_ORDER GRB      // if colors are mismatched; change this
#define NUM_LEDS    30       // change to the number of LEDs in your strip
#define LED_TYPE    WS2812B

CRGB leds[NUM_LEDS];

void setup() {
  FastLED.addLeds<LED_TYPE, DATA_PIN, COLOR_ORDER>(leds, NUM_LEDS);
}

int nextColor(int color) {
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

void setColorSpectrumStartingAt(int color, int saturation, int value) {
  for(int i=0; i<NUM_LEDS; i++) {
    leds[i] = CHSV(color,saturation,value);
    color = nextColor(color);
  }

  flush();
}

void loop() {
  int startColor = 0;
  int saturation = 120;
  int value = 255;

  while(startColor < 255) {
    setColorSpectrumStartingAt(startColor, saturation, value);
    startColor = nextColor(startColor);
    delay(80);
  }
}
