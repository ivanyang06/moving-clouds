x = 2
y = 0.4
newx = 200
newy = 200
def setup():
    size(600,600)
    
def draw():
    global x
    global y
    global newx
    global newy
    
    #movement
    if newx == 520 or newx == 80:
        x *= -1
    if newy > 204 or newy < 196:
        y *= -1
    newx += x
    newy += y
    
    noStroke()
    clear()
    background(170,210,255)
    
    #sun
    fill(255,255,0)
    ellipse(80,80,60,60)
    
    #cloud
    fill(255,255,255)
    ellipse(newx+15, newy, 100, 40)
    ellipse(newx-15, newy, 100, 40)
    ellipse(newx+15, newy-20, 60, 25)
    ellipse(newx-15, newy-20, 60, 25)
    
    #ground
    fill(50,200,50)
    ellipse(300,500,700,50)
    rect(0,500,600,100)
    
    #house
    fill(255,255,50)
    rect(270,460,60,60)
    fill(255,50,50)
    triangle(260,460,300,420,340,460)
