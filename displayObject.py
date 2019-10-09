def displayObject(obj,x,y):
    from gfxhat import lcd, fonts
    from PIL import Image, ImageFont, ImageDraw
    row =[]
    initialX = x
# Clearing Screen
    lcd.clear()
    lcd.show()
    
# Resetting y and/or x to 0 if the initial value is too high    
    if y > 63:
        y = 0
    if initialX > 127:
        initialX = 0

# Starting for loops to draw object
    for i in range(len(obj)):
        row =obj[i]
        y = y+1
        x = initialX
        # Resetting y if the value gets too high
        if y > 63:
            y = 0
        for i in range (len(row)):
            if row[i] == 1:
                lcd.set_pixel(x,y,1)
                lcd.show()
            x = x+1
            # Resetting x if the value gets too high
            if x > 127:
                x = 0+i
