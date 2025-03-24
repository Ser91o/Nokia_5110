import time
import wiringpi
from class_LCD import LCD, ActivateLCD, DeactivateLCD

# Define the pins (adjust if necessary)
PINS = {
    'RST': 17,
    'CS': 13,  # Chip Select (CE)
    'DC': 9,  # Data/Command
    'DIN': 11,  # SPI MOSI
    'SCLK': 14,  # SPI Clock
    'LED': 6,  # Backlight
}

# Initialize WiringPi
wiringpi.wiringPiSetup()
wiringpi.pinMode(PINS['CS'], 1)  # Set CS pin as output

# Create an LCD instance
lcd = LCD(PINS)

try:
    ActivateLCD(PINS['CS'])

    # Clear the LCD and set the backlight on
    lcd.clear()
    lcd.set_backlight(1)

    # Display a string on the LCD
    lcd.put_string("Hello, Orange Pi!")
    lcd.refresh()  # Push buffer to display

    time.sleep(10)  # Keep the text on the screen for 10 seconds

except KeyboardInterrupt:
    # Clear the LCD and turn off the backlight on exit
    lcd.clear()
    lcd.refresh()
    lcd.set_backlight(0)
    DeactivateLCD(PINS['CS'])
