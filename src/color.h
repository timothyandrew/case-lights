#ifndef COLOR_H
#define COLOR_H

#include "FastLED.h"

int nextHue(int color);

void flush();

void clearAll();

void setColorSpectrumStartingAt(CHSV color);

void setColor(CHSV color);

void addLeds();

#endif
