import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Set up the PiTFT display
cs_pin = digitalio.DigitalInOut(board.D5)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

BAUDRATE = 64000000

# Set up SPI
spi = board.SPI()

# Create the ST7789 display
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)


# Set up landscape orientation
height = disp.width
width = disp.height
rotation = 90

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Create a blank black screen
image = Image.new("RGB", (width, height), "black")
draw = ImageDraw.Draw(image)

# Set up font
# Fonts
# Set up font
font = ImageFont.truetype(
    "/usr/share/fonts/truetype/piboto/Piboto-Regular.ttf",
    19
)

# Write text on the screen
def show_status(text):
    # Dark navy background
    draw.rectangle(
        (0, 0, width, height),
        fill=(0, 0, 100)
    )

    # Measure the status text
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]

    # Center status text
    x = (width - text_width) // 2 - bbox[0]
    y = 40 - bbox[1]

    # Light blue text
    draw.text(
        (x, y),
        text,
        font=font,
        fill=(130, 200, 255)
    )

    # Static dots underneath
    draw.text(
        (width // 2, 85),
        "•  •  •",
        font=font,
        fill=(130, 200, 255),
        anchor="mm"
    )

    disp.image(image, rotation)

def show_caption(text):
    # Clear the screen
    draw.rectangle(
        (0, 0, width, height),
        fill=(0, 0, 100)
    )

    # Break the caption into lines that fit the screen
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + (" " if current_line else "") + word

        bbox = draw.textbbox((0, 0), test_line, font=font)
        test_width = bbox[2] - bbox[0]

        if test_width <= width - 20:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    # Draw each line centered
    line_height = 28
    total_height = len(lines) * line_height
    y = (height - total_height) // 2

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]

        x = (width - text_width) // 2

        draw.text(
            (x, y),
            line,
            font=font,
            fill=(170, 220, 255)
        )

        y += line_height

    # Update the PiTFT
    disp.image(image, rotation)