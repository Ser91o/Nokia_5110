import time
import wiringpi
from class_LCD import LCD, ActivateLCD, DeactivateLCD

# Define the pins
PINS = {
    'RST': 17,
    'CS': 13,  # Chip Select (CE)
    'DC': 9,  # Data/Command
    'DIN': 11,  # SPI MOSI
    'SCLK': 14,  # SPI Clock
    'LED': 6,  # Backlight
}
BUTTON_PIN = 4  # GPIO pin for the button

# Initialize WiringPi and LCD
wiringpi.wiringPiSetup()
wiringpi.pinMode(PINS['CS'], 1)
wiringpi.pinMode(BUTTON_PIN, wiringpi.INPUT)
wiringpi.pullUpDnControl(BUTTON_PIN, wiringpi.PUD_DOWN)  # Pull-down for button

lcd = LCD(PINS)

try:
    ActivateLCD(PINS['CS'])
    lcd.clear()
    lcd.set_backlight(1)

    message_1 = "Hello!"
    message_2 = "Goodbye!"
    current_message = message_1

    while True:
        button_state = wiringpi.digitalRead(BUTTON_PIN)

        if button_state == wiringpi.HIGH:
            # Toggle between the two messages
            if current_message == message_1:
                current_message = message_2
            else:
                current_message = message_1

            # Display the message
            lcd.clear()
            lcd.put_string(current_message)
            lcd.refresh()

            time.sleep(0.5)  # Debounce delay

except KeyboardInterrupt:
    lcd.clear()
    lcd.refresh()
    lcd.set_backlight(0)
    DeactivateLCD(PINS['CS'])
