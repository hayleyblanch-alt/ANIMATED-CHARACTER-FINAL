waving = False
waveStart = 0
rainbow = False

def setup ():
    size (700, 700)


def draw ():
    global waving
    background (225)
    
    # Leaves
    fill(0, 200, 90)
    stroke(0)
    
    # Left leaf
    pushMatrix()
    translate(350, 600)

    if waving:
        rotate(radians(155 + sin(frameCount * 0.15) * 12))
    else:
        rotate(radians(-155))

    fill(0, 200, 90)
    stroke(0)
    ellipse(65, 0, 130, 40)
    popMatrix()
    
    # Right leaf
    pushMatrix()
    translate(350, 600)

    if waving:
        rotate(radians(25 - sin(frameCount * 0.15) * 12))
    else:
        rotate(radians(-25))

    fill(0, 200, 90)
    stroke(0)
    ellipse(65, 0, 130, 40)
    popMatrix()
         
    # Stem
    fill(0, 190, 90)
    rect(325, 410, 50, 300)


    # Middle Top
    if rainbow:
        fill(255, 50, 50)  # Red
    else:
        fill(250, 90, 200)  # Pink
    ellipse(350, 230, 90, 160)
    
    # Top Right petal
    pushMatrix()
    translate(390, 170)
    rotate(radians(45))
    if rainbow:
        fill(255, 150, 0)   # Orange
    else:
        fill(250, 90, 200)  # Pink
    ellipse(100, 100, 90, 280)
    popMatrix()
    
    
    # Middle Right
    if rainbow:
        fill(255, 230, 0)   # Yellow
    else:
        fill(250, 90, 200)  # Pink
    ellipse(470, 350, 200, 80)
    
    # Bottom Right petal
    pushMatrix()
    translate(170, 170)
    rotate(radians(-45))
    if rainbow:
        fill(50, 210, 80)   # Green
    else:
        fill(250, 90, 200)  # Pink
    ellipse(10, 380, 85, 180)
    popMatrix()
    
    # Middle Bottom
    if rainbow:
        fill(50, 150, 255)   # Blue
    else:
        fill(250, 90, 200)  # Pink   
    ellipse(350, 470, 90, 160)
    
    # Bottom Left petal
    pushMatrix()
    translate(275, 270)
    rotate(radians(45))
    if rainbow:
        fill(0, 210, 260 )   # Aqua
    else:
        fill(250, 90, 200)  # Pink  
    ellipse(100, 100, 90, 230)
    popMatrix()
    
    # Middle Left
    if rainbow:
        fill(160, 80, 255)   # Purple
    else:
        fill(250, 90, 200)  # Pink  
    ellipse(230, 350, 200, 80)
    
    # Top left petal
    pushMatrix()
    translate(275, 270)
    rotate(radians(-45))
    
    if rainbow:
        fill(260, 120, 900)   # Magenta
    else:
        fill(250, 90, 200)  # Pink 
    ellipse(0, 0, 80, 200)
    popMatrix()

    # Middle
    fill (240, 170, 20) 
    ellipse(350, 350, 120, 120)
    
    # Blinking eyes

    if frameCount % 120 < 10:

        # Eyes closed
        stroke(0)
        strokeWeight(3)
        line(318, 345, 342, 345)
        line(358, 345, 382, 345)

    else:
        # Eyes open
        fill(255)
        stroke(0)
        strokeWeight(1)
        ellipse(330, 340, 25, 40)
        ellipse(370, 340, 25, 40)

        # Pupils follow mouse
        pupilX = map(mouseX, 0, width, -5, 5)
        pupilY = map(mouseY, 0, height, -5, 5)

        fill(0)
        ellipse(330 + pupilX, 345 + pupilY, 15, 21)
        ellipse(370 + pupilX, 345 + pupilY, 15, 21)
    
    # Smile
    noFill()
    stroke(5)
    strokeWeight(2)
    arc(350, 375, 40, 30, 0, PI)
    
    # Stop waving after 90 frames
    if waving and frameCount - waveStart > 90:
        waving = False
        
def mousePressed():
    global waving, waveStart

    if dist(mouseX, mouseY, 350, 350) < 60:
        waving = True
        waveStart = frameCount
        
def keyPressed():
    global rainbow

    if key == ' ':
        rainbow = not rainbow
