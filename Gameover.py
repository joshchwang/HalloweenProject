def setup():
    size(1300, 500)

rectx = 1250
circley = 450

def draw():
    global rectx
    global circley
    background(5)
    ellipse(50,circley, 100,100)
    rect(rectx, 450, 50, 50, 10) 
    rectx-=10    
    
    #attempt at collision   
    if rectx-50<=50 and circley<=450:
        rectx = 100
        circley = 450
        textAlign(CENTER , CENTER) 
        textSize(200)
        text("Game over",  650, 250)
        
