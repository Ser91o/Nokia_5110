import time
import wiringpi
import spidev
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

# Initialize SPI for MCP3008
spi_adc = spidev.SpiDev()
spi_adc.open(0, 0)
spi_adc.max_speed_hz = 1350000

# Initialize WiringPi and LCD
wiringpi.wiringPiSetup()
wiringpi.pinMode(PINS['CS'], 1)
lcd = LCD(PINS)


# Function to read MCP3008 ADC value
def read_adc(channel):
    adc = spi_adc.xfer2([1, (8 + channel) << 4, 0])
    return ((adc[1] & 3) << 8) + adc[2]


try:
    ActivateLCD(PINS['CS'])
    lcd.clear()
    lcd.set_backlight(1)

    while True:
        # Read the potentiometer value from channel 0 (0-1023)
        adc_value = read_adc(0)

        # Adjust backlight brightness based on ADC value
        brightness = int(adc_value / 1023 * 255)  # Convert to range 0-255
        lcd.set_backlight(brightness)

        # Display the potentiometer value on the LCD
        lcd.clear()
        lcd.put_string(f"Pot Value:\n{adc_value}")
        lcd.refresh()

        time.sleep(0.1)  # Small delay

except KeyboardInterrupt:
    lcd.clear()
    lcd.refresh()
    lcd.set_backlight(0)
    DeactivateLCD(PINS['CS'])
