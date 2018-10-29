x = 2
y = 0.4
randx = 0
randy = 0
newx = 200
newy = 300
time_counter = 180
sky_color = [60,100,145]
cloud_color = [185,185,185]
sun_color = [255,255,0]
light_brightness = 0.6
moonwidth = 0
mooncounter = 0
def setup():
    size(600,600)
    
def draw():
    global randx
    global randy
    global x
    global y
    global newx
    global newy
    global time_counter
    global moonwidth
    global a
    global mooncounter
    
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
        if sun_color[2] == 0:
            sun_color[2] = 210
        else:
            sun_color[2] = 0
    if time_counter > 205 and sun_color[2] == 0:
        light_brightness = -0.5
    elif time_counter > 205 and sun_color[2] == 210:
        light_brightness = 0.5
    
    #movement
    if newx == 520 or newx == 80:
        x *= -1
    if newy > 304 or newy < 296:
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
    
    #sun/moon
    translate(width/2, 800)
    rotate(radians(time_counter))
    fill(*sun_color)
    ellipse(300, 600,60,60)
    
    if time_counter == 175 and sun_color[2] == 210:
        mooncounter += 1
    if mooncounter == 12:
        mooncounter = 0
    print(mooncounter)
    fill(*sun_color)
    ellipse(300, 600, 60, 60)
    fill(*sky_color)
    if mooncounter == 0: #new moon
        ellipse(300,600,60,60)
    if mooncounter == 1:
        rect(300,540,60,120)
        ellipse(300,600,40,60)
    if mooncounter == 2:
        rect(300,540,60,120)
        ellipse(300,600,20,60)
    if mooncounter == 3: #half moon
        rect(300,540,60,120)
        ellipse(0,0,0,0)
    if mooncounter == 4:
        rect(300,540,60,120)
        fill(*sun_color)
        ellipse(300,600,20,60)
    if mooncounter == 5:
        rect(300,540,60,120)
        fill(*sun_color)
        ellipse(300,600,40,60)
    if mooncounter == 6: # full moon
        fill(*sun_color)
        ellipse(300,600,60,60)
    if mooncounter == 7:
        rect(240,540,60,120)
        fill(*sun_color)
        ellipse(300,600,40,60)
    if mooncounter == 8:
        rect(240,540,60,120)
        fill(*sun_color)
        ellipse(300,600,20,60)
    if mooncounter == 9: #half moon
        rect(240,540,60,120)
        ellipse(0,0,0,0)
    if mooncounter == 10:
        rect(240,540,60,120)
        ellipse(300,600,20,60)
        rect(240,540,60,120)
    if mooncounter == 11:
        rect(240,540,60,120)
        ellipse(300,600,40,60)
    
    if sun_color[2] == 0:
        fill(*sun_color)
        ellipse(300, 600,60,60)
