x = 2
y = 0.4
newx = 200
newy = 200
time_counter = 180
sky_color = [20,60,105]
cloud_color = [125,125,125]
sun_color = [255,255,0]
light_brightness = 0.6
def setup():
    size(600,600)
    
def draw():
    global x
    global y
    global newx
    global newy
    global time_counter
    
    global sky_color
    global cloud_color
    global sun_color
    global light_brightness
    
    #time
    time_counter += 0.2
    if sky_color[2] + light_brightness <= 255 and sky_color[2] + light_brightness >= 0:
        sky_color[0]+=light_brightness
        sky_color[1]+=light_brightness
        sky_color[2]+=light_brightness
        cloud_color[0]+=light_brightness
        cloud_color[1]+=light_brightness
        cloud_color[2]+=light_brightness
    if time_counter >= 235:
        time_counter = 175
    if time_counter == 175:
        light_brightness *= -1
        if sun_color[2] == 0:
            sun_color[2] = 210
        else:
            sun_color[2] = 0
    
    #movement
    if newx == 520 or newx == 80:
        x *= -1
    if newy > 204 or newy < 196:
        y *= -1
    newx += x
    newy += y
    
    noStroke()
    clear()
    
    background(*sky_color)
    
    #cloud
    fill(*cloud_color)
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
    
    #sun
    translate(width/2, 800)
    rotate(radians(time_counter))
    fill(*sun_color)
    ellipse(300, 600,60,60)
