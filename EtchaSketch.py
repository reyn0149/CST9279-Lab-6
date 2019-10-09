from gfxhat import lcd,  fonts
from PIL import Image, ImageFont, ImageDraw
from click import getchar

xCoordinate = 64
yCoordinate = 32
userInput = 0

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 12)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()

displayText("Etch a Sketch",lcd,2,2)
while userInput != "q":
    userInput = getchar()
    if userInput == "s":
        clearScreen(lcd)
        displayText("Etch a Sketch",lcd,2,2)
        lcd.show()
    if userInput =="\x1b[C":
        xCoordinate = xCoordinate+1
        if xCoordinate > 127:
            xCoordinate = 0
        lcd.set_pixel(xCoordinate,yCoordinate,1)
        lcd.show()
    if userInput == "\x1b[D":
        xCoordinate = xCoordinate-1
        if xCoordinate < 0:
            xCoordinate = 127
        lcd.set_pixel(xCoordinate,yCoordinate,1)
        lcd.show()
    if userInput == "\x1b[A":
        yCoordinate = yCoordinate-1
        if yCoordinate < 0:
            yCoordinate = 63
        lcd.set_pixel(xCoordinate,yCoordinate,1)
        lcd.show()
    if userInput == "\x1b[B":
        yCoordinate = yCoordinate+1
        if yCoordinate > 63:
            yCoordinate = 0
        lcd.set_pixel(xCoordinate,yCoordinate,1)
        lcd.show()
    
