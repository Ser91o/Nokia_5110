# Nokia 5110 LCD with Orange Pi using WiringPi and SPI
This project demonstrates how to interface a Nokia 5110 LCD display with an Orange Pi using the WiringPi library and SPI communication. The included code makes use of a custom LCD class to simplify operations like displaying text, controlling the backlight, and updating the screen. 
The project also shows how to control the LCD using a button and potentiometer.

## Overview
The Nokia 5110 LCD is a simple, monochrome display with an 84x48 pixel resolution. Originally used in Nokia mobile phones, this display is perfect for displaying text, basic graphics, and sensor data in small embedded projects. It communicates via SPI, making it fast and easy to use with microcontrollers or single-board computers like the Orange Pi.
This project takes advantage of the WiringPi library to control the GPIO pins and SPI bus, ensuring seamless communication between the Orange Pi and the LCD.

## Features
Text Display: Display custom messages on the Nokia 5110 LCD screen using the put_string() method.

Backlight Control: Use a potentiometer to adjust the backlight brightness of the LCD.

Button Interaction: Toggle between different text messages using a button.

SPI Communication: The project uses SPI for efficient communication between the Orange Pi and the Nokia 5110 LCD.

## Components
Orange Pi (any variant with GPIO/SPI support)

Nokia 5110 LCD Display

Potentiometer (for backlight control)

Push Button (for toggling text)

MCP3008 ADC (for reading analog values from the potentiometer)

Resistors, jumper wires, and a breadboard


## API Overview
### LCD Class API
The LCD class in this project provides an abstraction layer for controlling the Nokia 5110 LCD. This class wraps common functionalities such as writing text, drawing shapes, setting pixels, controlling the backlight, and refreshing the screen. Here's an overview of the key methods:

put_string(text, x, y): Displays a string of text on the LCD starting from the position (x, y).

Example: lcd.put_string("Hello World", 0, 0)

put_char(char, x, y): Displays a single character at the position (x, y).

clear(): Clears the screen by wiping off all pixels, useful when refreshing the display with new content.

refresh(): Updates the LCD with the contents of the buffer. Any modifications to the screen content (text, graphics) are reflected on the display when this method is called.

set_backlight(value): Controls the brightness of the LCD backlight. The value can range from 0 (off) to 255 (maximum brightness).

set_pixel(x, y, color): Sets an individual pixel at the coordinates (x, y) to either black (on) or white (off).

draw_line(x1, y1, x2, y2): Draws a line between the points (x1, y1) and (x2, y2) on the LCD.

draw_circle(x, y, radius): Draws a circle with a specified radius at the center (x, y).

These methods simplify communication with the LCD display and allow easy integration with other sensors, buttons, or user interfaces in your project.

ActivateLCD(CS_PIN) and DeactivateLCD(CS_PIN)
These two helper functions are used to control the Chip Select (CS) pin of the SPI interface. The LCD shares the SPI bus with other devices (such as the MCP3008 for the potentiometer), so it needs to be activated before sending data and deactivated afterward.

ActivateLCD(CS_PIN): Pulls the CS pin low to enable communication with the LCD.

DeactivateLCD(CS_PIN): Pulls the CS pin high to disable communication with the LCD, allowing other SPI devices to use the bus.

These functions are essential for managing SPI communication between multiple peripherals on the same bus.
