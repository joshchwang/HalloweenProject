def setup():
    global bg, wizard, wizard0,wizard3,weaponvalue
    size(1100, 520)
    bg = loadImage("background.jpg")
    wizard0 = loadImage("wizard 0.gif")
    wizard3 = loadImage("wizard 3.gif")
    ghost1 = loadImage("Ghost 1.gif")
wizardx = -50
weaponvalue = 0 
weapx = 0
def keyTyped():
    if key=='d':
        global wizardx
        wizardx+=10
    elif key=='a':
        global wizardx
        wizardx-=10   
ghostx = 1300
def draw():
    global ghostx,ghost0
    background(0)
    image(bg,0,0,1100,520)
    
    if (wizardx+weapx+240)>=ghostx:
        weaponvalue=0
        weapx=0
        ghostx=1300
    else:
        ghost0 = loadImage("Ghost 0.gif")
        image(ghost0,ghostx,300,300,300)
        ghostx-=20
            
    if mousePressed==True:
        image(wizard0,wizardx,300,300,300)   
        weaponvalue=1
    else:
        image(wizard3,wizardx,300,300,300)
    if weaponvalue==1:
        global weaponvalue,weapx,projectile
        projectile = loadImage("projectile.gif")
        image(projectile,wizardx+weapx+240,400,50,50)
        weapx+=10
        
    
