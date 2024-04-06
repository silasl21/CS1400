# Silas Loosli
# CS1400 - MWF 9:30
cx = 500
cy = 720 / 2
lintx = cx - 100
inty = cy - 30
rintx = cx + 100
suncenterx = 925
suncentery = 40
import drawly
drawly.set_speed(9)
def yellow():
    drawly.set_color("gold1")
#defining variables
def black():
    drawly.set_color("black")
gold = "gold1"
def sun():
    drawly.set_color(gold)
    drawly.circle(925, 40, 100)
def stickcolor():
    drawly.set_color("sienna")
tophat = '''drawly.set_color("orange")
drawly.rectangle(cx-25, 112, 50, 40)
black()
drawly.rectangle(cx-50, 150, 100, 10)
drawly.rectangle(cx-25, 112, 50, 40, 5)'''
body = '''
black()
drawly.circle(cx, 200, 50, 5)
drawly.circle(cx,330,100, 5)
drawly.circle(cx,550,150, 5)
drawly.set_color("white")
drawly.circle(cx, 200, 45)
drawly.circle(cx,330,95)
drawly.circle(cx,550,145)
'''
buttons = '''
drawly.set_color("blue")
drawly.circle(cx, 300, 7)
drawly.circle(cx, 325, 7)
drawly.set_color("azure4")
drawly.circle(cx, 350, 7)
drawly.circle(cx, 375, 7)
drawly.set_color("aquamarine")
drawly.circle(cx, 400, 7)
drawly.circle(cx, 425, 7)
drawly.set_color("cyan3")
drawly.circle(cx, 450, 7)
drawly.circle(cx, 475, 7)
drawly.circle(cx, 500, 7)
'''
fill = '''
drawly.set_color("turquoise")
drawly.circle(cx, cy, 1000)
'''
redraw = '''
exec(fill)
exec(body)
exec(buttons)
'''
face = '''
black()
drawly.circle(cx - 15, 195, 5)
drawly.circle(cx + 15, 195, 5)
drawly.line(cx - 25, 205, cx + 25, 210, 5)
'''
facelook = '''
black()
drawly.circle(cx - 5, 200, 5)
drawly.circle(cx + 25, 200, 5)
drawly.circle(cx+10, 220, 10, 3)
'''
floorhat='''drawly.set_color("orange")
drawly.rectangle(900, 680, 40, 50)
black()
drawly.rectangle(900, 675, 10, 100)
drawly.rectangle(900, 680, 40, 50, 5)'''
larmpos1 = '''stickcolor()
drawly.line(lintx, inty, lintx-75, inty, 12)
drawly.line(lintx-75, inty, lintx-120, inty+25, 10)'''
rarmpos1 = '''
stickcolor()
drawly.line(rintx, inty, rintx+100, inty+100, 15)
drawly.line(rintx+100, inty+100, rintx+150, inty+150, 12)
drawly.line(rintx+150, inty+150, rintx+175, inty+165, 5)
drawly.line(rintx+150, inty+150, rintx+175, inty+180, 5)
drawly.line(rintx+150, inty+150, rintx+165, inty+190, 5)'''
rarmpos2 = '''
stickcolor()
drawly.line(rintx, inty, rintx+30, inty-90, 15)
drawly.line(rintx+30, inty-90, rintx-40, inty-180, 12)
drawly.line(rintx-40, inty-180, rintx-65, inty-210, 5)
drawly.line(rintx-40, inty-180, rintx-60, inty-190, 5)
drawly.line(rintx-40, inty-180, rintx-45, inty-220, 5)'''
def redraw_mad_sun():
    sun()
    black()
    drawly.circle(925, 55, 9, 5)
    drawly.circle(875, 55, 9, 5)
    drawly.rectangle(suncenterx - 20, suncentery, 30, 5, 0, 30)
    drawly.rectangle(suncenterx - 60, suncentery, 30, 5, 0, 140)
    drawly.arc(suncenterx - 65, suncentery + 30, 75, 25, 0, 120, 6)
def scene1():
    exec(redraw)
    exec(larmpos1)
    exec(rarmpos2)
    exec(tophat)
    exec(face)
    redraw_mad_sun()
def scene2():
    exec(redraw)
    exec(rarmpos2)
    exec(tophat)
    black()
    drawly.circle(cx - 5, 180, 5)
    drawly.circle(cx + 25, 180, 5)
    drawly.circle(cx + 10, 200, 10, 3)
    redraw_mad_sun()
def scene3():
    exec(redraw)
    exec(rarmpos2)
    exec(tophat)
    black()
    drawly.circle(cx - 5, 200, 5)
    drawly.circle(cx + 25, 200, 5)
    drawly.arc(cx-30, 210, 50, 50, 30,90, 6)
    drawly.rectangle(cx-20, 185, 30, 5, 0, 140)
    drawly.rectangle(cx +5, 185, 30, 5, 0, 40)
    redraw_mad_sun()
def scene4():
    exec(redraw)
    exec(rarmpos2)
    exec(tophat)
    black()
    drawly.circle(cx - 5, 180, 5)
    drawly.circle(cx + 25, 180, 5)
    drawly.arc(cx-30, 190, 50, 50, 30,90, 6)
    drawly.rectangle(cx-20, 165, 30, 5, 0, 140)
    drawly.rectangle(cx +5, 165, 30, 5, 0, 40)
    redraw_mad_sun()
def scene7():
    exec(redraw)
    exec(tophat)
    exec(rarmpos2)
    l_elbow_x = lintx + 55
    l_elbow_y = inty + 40
    l_palm_x = lintx + 60
    l_palm_y = inty - 85
    l_fingers_x = l_palm_x + 20
    l_fingers_y = l_palm_y - 40
    gun_x = l_fingers_x - 20
    gun_y = l_fingers_y + 20
    black()
    drawly.rectangle(gun_x, gun_y, 30, 10, 0, gun_rotation)
    drawly.rectangle(gun_x + 20, gun_y + 7, 5, 25, 0, gun_rotation)
    drawly.rectangle(gun_x + 15, gun_y + 7, 10, 10, 3, gun_rotation)
    stickcolor()
    drawly.line(lintx, inty, l_elbow_x, l_elbow_y, 17)
    drawly.line(l_elbow_x, l_elbow_y, l_palm_x, l_palm_y, 12)
    drawly.line(l_palm_x, l_palm_y, l_fingers_x, l_fingers_y + 15, 5)
    drawly.line(l_palm_x, l_palm_y, l_fingers_x + 15, l_fingers_y + 35, 5)
    drawly.line(l_palm_x, l_palm_y, l_fingers_x + 5, l_fingers_y + 45, 5)
    sun()
    surprised_sun()



drawly.start("THIS IS A SNOWMAN", (1000, 720), "turquoise")
exec(body)
#begin drawing entire snowman
black()
drawly.circle(cx - 15, 195, 5)
drawly.circle(cx + 15, 195, 5)
drawly.draw()

drawly.line(cx - 25, 205, cx + 25, 210, 5)
drawly.draw()
drawly.set_color("blue")
drawly.circle(cx, 300, 7)
drawly.circle(cx, 325, 7)
drawly.draw()
drawly.set_color("azure4")
drawly.circle(cx, 350, 7)
drawly.circle(cx, 375, 7)
drawly.draw()
drawly.set_color("aquamarine")
drawly.circle(cx, 400, 7)
drawly.circle(cx, 425, 7)
drawly.draw()
drawly.set_color("cyan3")
drawly.circle(cx, 450, 7)
drawly.circle(cx, 475, 7)
drawly.circle(cx, 500, 7)
drawly.draw()
stickcolor()
drawly.line(lintx, inty, lintx-75, inty-25, 12)
drawly.line(rintx, inty, rintx+75, inty-25, 12)
drawly.line(lintx-75, inty-25, lintx-100, inty-75, 10)
drawly.line(rintx+75, inty-25, rintx+100, inty-75, 10)
drawly.draw()
exec(redraw)
exec(face)
stickcolor()
drawly.line(lintx, inty, lintx-75, inty, 12)
drawly.line(rintx, inty, rintx+75, inty, 12)
drawly.line(lintx-75, inty, lintx-120, inty+25, 10)
drawly.line(rintx+75, inty, rintx+120, inty+25, 10)
drawly.draw()
exec(redraw)

#hat appears and snowman looks at it

exec(facelook)

exec(larmpos1)
drawly.line(rintx, inty, rintx+100, inty+100, 12)
black()
drawly.rectangle(900, 700, 10, 20)
drawly.draw()
exec(redraw)
exec(facelook)
exec(larmpos1)

#snowman arm reaches out

drawly.line(rintx, inty, rintx+100, inty+100, 15)
exec(floorhat)
stickcolor()
drawly.line(rintx+100, inty+100, rintx+150, inty+150, 12)
drawly.draw()
drawly.line(rintx+150, inty+150, rintx+170, inty+160, 5)
drawly.line(rintx+150, inty+150, rintx+170, inty+175, 5)
drawly.line(rintx+150, inty+150, rintx+160, inty+185, 5)
drawly.draw()
exec(redraw)
exec(facelook)
exec(floorhat)
exec(larmpos1)
exec(rarmpos1)
drawly.draw()

#Hat turns into ball

exec(redraw)
exec(facelook)
exec(larmpos1)
exec(rarmpos1)
drawly.set_color("orange")
drawly.circle(900, 680, 15)
black()
drawly.circle(900, 680, 15, 7)
drawly.draw()
exec(redraw)
exec(facelook)
exec(larmpos1)
exec(rarmpos1)
drawly.set_color("orange")
drawly.circle(825, 575, 10)
black()
drawly.circle(825, 575, 10, 5)
drawly.draw()
exec(redraw)
exec(facelook)
exec(larmpos1)
drawly.set_color("orange")
drawly.circle(775, 500, 10)
black()
drawly.circle(775, 500, 10, 5)
#Snowman catches ball hat
exec(rarmpos1)
drawly.draw()
exec(redraw)
exec(facelook)
exec(larmpos1)
drawly.set_color("orange")
drawly.circle(775, 500, 10)
black()
drawly.circle(775, 500, 10, 5)
stickcolor()
drawly.line(rintx, inty, rintx+50, inty+75, 15)
drawly.line(rintx+50, inty+75, rintx+150, inty+150, 12)
drawly.line(rintx+150, inty+150, rintx+175, inty+165, 5)
drawly.line(rintx+150, inty+150, rintx+175, inty+180, 5)
drawly.line(rintx+150, inty+150, rintx+165, inty+190, 5)
drawly.draw()

#snowman brings ball hat to head

exec(redraw)
exec(facelook)
exec(larmpos1)

drawly.set_color("orange")
drawly.circle(rintx+145, inty+10, 10)
black()
drawly.circle(rintx+145, inty+10, 10, 5)

stickcolor()
drawly.line(rintx, inty, rintx+75, inty+40, 15)
drawly.line(rintx+75, inty+40, rintx+125, inty+20, 12)
drawly.line(rintx+125, inty+20, rintx+145, inty+5, 5)
drawly.line(rintx+125, inty+20, rintx+155, inty+15, 5)
drawly.line(rintx+125, inty+20, rintx+150, inty+30, 5)
drawly.draw()

exec(redraw)
exec(facelook)
exec(larmpos1)

drawly.set_color("orange")
drawly.circle(rintx+125, inty-40, 10)
black()
drawly.circle(rintx+125, inty-40, 10, 5)

stickcolor()
drawly.line(rintx, inty, rintx+80, inty+15, 15)
drawly.line(rintx+80, inty+15, rintx+120, inty-20, 12)
drawly.line(rintx+120, inty-20, rintx+110, inty-40, 5)
drawly.line(rintx+120, inty-20, rintx+135, inty-50, 5)
drawly.line(rintx+120, inty-20, rintx+140, inty-30, 5)
drawly.draw()

exec(redraw)
exec(facelook)
exec(larmpos1)

drawly.set_color("orange")
drawly.circle(rintx+20, inty-130, 10)
black()
drawly.circle(rintx+20, inty-130, 10, 5)

stickcolor()
drawly.line(rintx, inty, rintx+50, inty-40, 15)
drawly.line(rintx+50, inty-40, rintx+30, inty-110, 12)
drawly.line(rintx+30, inty-110, rintx+10, inty-125, 5)
drawly.line(rintx+30, inty-110, rintx+20, inty-140, 5)
drawly.line(rintx+30, inty-110, rintx+30, inty-130, 5)
drawly.draw()

exec(redraw)
exec(facelook)
exec(larmpos1)

drawly.set_color("orange")
drawly.circle(rintx-60, inty-190, 10)
black()
drawly.circle(rintx-60, inty-190, 10, 5)


exec(rarmpos2)
drawly.draw()

#turn ball into hat

exec(redraw)
exec(facelook)
exec(larmpos1)


drawly.set_color("orange")
drawly.circle(rintx-75, inty-180, 20)
black()
drawly.circle(rintx-75, inty-180, 20, 9)
exec(rarmpos2)

drawly.draw()

exec(redraw)
exec(facelook)
exec(larmpos1)
exec(rarmpos2)


exec(tophat)
drawly.draw()
exec(redraw)
exec(larmpos1)
exec(rarmpos2)
exec(tophat)
exec(face)
drawly.draw()

#create a sun

drawly.set_color("gold1")
drawly.circle(1000, 0, 40)
drawly.draw()
drawly.circle(975, 20, 50)
drawly.draw()
drawly.circle(950, 30, 75)
drawly.draw()
drawly.circle(suncenterx, suncentery, 100)
drawly.draw()



#sun starts opening eyes

black()
drawly.rectangle(935, 45,10,5 )
drawly.rectangle(885, 45, 10, 5)
drawly.draw()


sun()
black()
drawly.rectangle(935, 45,20,10 )
drawly.rectangle(885, 45,20,10 )
drawly.draw()

sun()
black()
drawly.circle(935, 45, 10, 9)
drawly.circle(885, 45, 10, 9)
drawly.draw()

sun()
black()
drawly.circle(935, 45, 10, 7)
drawly.circle(885, 45, 10, 7)
drawly.draw()

sun()
black()
drawly.circle(935, 45, 10, 3)
drawly.circle(885, 45, 10, 3)
drawly.draw()

#sun sees the snowman


#sun gets mad
sun()
black()
drawly.circle(925, 55, 9, 5)
drawly.circle(875, 55, 9, 5)
drawly.rectangle(suncenterx-20, suncentery, 30, 5,0,30)
drawly.rectangle(suncenterx-60, suncentery, 30, 5,0,140)
drawly.draw()

sun()
black()
drawly.circle(925, 55, 9, 5)
drawly.circle(875, 55, 9, 5)
drawly.rectangle(suncenterx-20, suncentery, 30, 5,0,30)
drawly.rectangle(suncenterx-60, suncentery, 30, 5,0,140)
drawly.arc(suncenterx-65,suncentery+30, 75, 25, 0, 120, 6)
drawly.draw()

#sun starts shooting rays at the snowman

scene1()
yellow()
drawly.rectangle(840, 90, 10, 10, 0, 30)
drawly.draw()

scene1()
yellow()
drawly.rectangle(830, 92, 30, 15, 0, 30)
drawly.draw()

scene1()
yellow()
drawly.rectangle(825, 92, 40, 15, 0, 30)
drawly.draw()

scene1()
yellow()
drawly.rectangle(800, 105, 40, 15, 0, 30)
drawly.draw()

scene1()
yellow()
drawly.rectangle(775, 120, 40, 15, 0, 30)
drawly.draw()

scene1()
yellow()
drawly.rectangle(750, 135, 40, 15, 0, 30)
drawly.draw()

scene1()
yellow()
drawly.rectangle(725, 150, 40, 15, 0, 30)
drawly.draw()

scene1()
yellow()
drawly.rectangle(700, 165, 40, 15, 0, 30)
drawly.draw()

scene1()
yellow()
drawly.rectangle(675, 180, 40, 15, 0, 30)
drawly.draw()

scene1()
yellow()
drawly.rectangle(650, 195, 40, 15, 0, 30)
drawly.draw()

scene1()
yellow()
drawly.rectangle(625, 210, 40, 15, 0, 30)
drawly.draw()

scene1()
yellow()
drawly.rectangle(600, 225, 40, 15, 0, 30)
drawly.draw()

scene1()
yellow()
drawly.rectangle(575, 240, 40, 15, 0, 30)
drawly.draw()

scene1()
yellow()
drawly.rectangle(550, 255, 40, 15, 0, 30)
drawly.draw()

scene2()
yellow()
drawly.circle(540, 280, 30)
exec(larmpos1)
drawly.draw()

scene2()
yellow()
drawly.circle(540, 280, 20)
exec(larmpos1)
drawly.draw()

scene2()
yellow()
drawly.circle(540, 280, 10, 7)
exec(larmpos1)
drawly.draw()

scene3()
exec(larmpos1)
drawly.draw()
#gun appears


scene3()
exec(larmpos1)
black()
drawly.rectangle(200, 700, 10, 30, 0, 20)
yellow()
drawly.rectangle(840, 90, 10, 10, 0, 30)
drawly.draw()

scene3()
exec(larmpos1)
black()
drawly.rectangle(200, 700, 10, 30, 0, 20)
drawly.rectangle(200, 700, 5, 40, 0)
yellow()
drawly.rectangle(830, 92, 30, 15, 0, 30)
drawly.draw()


scene4()
exec(larmpos1)
black()
drawly.rectangle(210, 640, 30, 10, 0, 0)
drawly.rectangle(210, 640, 5, 25, 0)
drawly.rectangle(215, 647, 10, 10, 3)
yellow()
drawly.rectangle(825, 92, 40, 15, 0, 30)
drawly.draw()


scene4()
exec(larmpos1)
black()
drawly.rectangle(216, 620, 30, 10, 0, 0)
drawly.rectangle(216, 620, 5, 25, 0)
drawly.rectangle(221, 627, 10, 10, 3)
yellow()
drawly.rectangle(800, 105, 40, 15, 0, 30)
drawly.draw()

#starts reaching out for gun

scene4()
stickcolor()
drawly.line(lintx, inty, lintx-75, inty+20, 12)
drawly.line(lintx-75, inty+20, lintx-120, inty+60, 10)
drawly.line(lintx-120, inty+60, lintx-130, inty+65, 5)
drawly.line(lintx-120, inty+60, lintx-120, inty+70, 5)
drawly.line(lintx-120, inty+60, lintx-115, inty+80, 5)
black()
drawly.rectangle(217, 600, 30, 10, 0, 0)
drawly.rectangle(217, 600, 5, 25, 0)
drawly.rectangle(222, 607, 10, 10, 3)
yellow()
drawly.rectangle(775, 120, 40, 15, 0, 30)
drawly.draw()

scene4()
stickcolor()
drawly.line(lintx, inty, lintx-65, inty+40, 12)
drawly.line(lintx-65, inty+40, lintx-115, inty+80, 10)
drawly.line(lintx-115, inty+80, lintx-145, inty+70, 5)
drawly.line(lintx-115, inty+80, lintx-145, inty+90, 5)
drawly.line(lintx-115, inty+80, lintx-115, inty+100, 5)
black()
drawly.rectangle(218, 580, 30, 10, 0, 0)
drawly.rectangle(218, 580, 5, 25, 0)
drawly.rectangle(223, 587, 10, 10, 3)
yellow()
drawly.rectangle(750, 135, 40, 15, 0, 30)
drawly.draw()

scene4()
stickcolor()
drawly.line(lintx, inty, lintx-75, inty+60, 12)
drawly.line(lintx-75, inty+60, lintx-120, inty+100, 10)
drawly.line(lintx-120, inty+100, lintx-150, inty+90, 5)
drawly.line(lintx-120, inty+100, lintx-150, inty+110, 5)
drawly.line(lintx-120, inty+100, lintx-120, inty+120, 5)
black()
drawly.rectangle(219, 560, 30, 10, 0, 0)
drawly.rectangle(219, 560, 5, 25, 0)
drawly.rectangle(224, 567, 10, 10, 3)
yellow()
drawly.rectangle(725, 150, 40, 15, 0, 30)
drawly.draw()

scene4()
stickcolor()
drawly.line(lintx, inty, lintx-75, inty+60, 12)
drawly.line(lintx-75, inty+60, lintx-115, inty+115, 10)
drawly.line(lintx-115, inty+115, lintx-145, inty+105, 5)
drawly.line(lintx-115, inty+115, lintx-145, inty+125, 5)
drawly.line(lintx-115, inty+115, lintx-115, inty+135, 5)
black()
drawly.rectangle(220, 540, 30, 10, 0, 0)
drawly.rectangle(220, 540, 5, 25, 0)
drawly.rectangle(225, 547, 10, 10, 3)
yellow()
drawly.rectangle(700, 165, 40, 15, 0, 30)
drawly.draw()

scene4()
stickcolor()
drawly.line(lintx, inty, lintx-75, inty+60, 12)
drawly.line(lintx-75, inty+60, lintx-115, inty+115, 10)
drawly.line(lintx-115, inty+115, lintx-145, inty+105, 5)
drawly.line(lintx-115, inty+115, lintx-145, inty+125, 5)
drawly.line(lintx-115, inty+115, lintx-115, inty+135, 5)
black()
drawly.rectangle(225, 510, 30, 10, 0, 0)
drawly.rectangle(225, 510, 5, 25, 0)
drawly.rectangle(230, 517, 10, 10, 3)
yellow()
drawly.rectangle(675, 180, 40, 15, 0, 30)
drawly.draw()

scene4()
stickcolor()
drawly.line(lintx, inty, lintx-75, inty+60, 12)
drawly.line(lintx-75, inty+60, lintx-115, inty+115, 10)
drawly.line(lintx-115, inty+115, lintx-145, inty+105, 5)
drawly.line(lintx-115, inty+115, lintx-145, inty+125, 5)
drawly.line(lintx-115, inty+115, lintx-115, inty+135, 5)
black()
drawly.rectangle(240, 480, 30, 10, 0, 0)
drawly.rectangle(240, 480, 5, 25, 0)
drawly.rectangle(245, 487, 10, 10, 3)
yellow()
drawly.rectangle(650, 195, 40, 15, 0, 30)
drawly.draw()

scene4()
black()
drawly.rectangle(lintx-120, inty+100, 30, 10, 0, 0)
drawly.rectangle(lintx-120, inty+100, 5, 25, 0)
drawly.rectangle(lintx-120+5, inty+100+7, 10, 10, 3)
stickcolor()
drawly.line(lintx, inty, lintx-75, inty+60, 12)
drawly.line(lintx-75, inty+60, lintx-100, inty+100, 10)
drawly.line(lintx-105, inty+105, lintx-110, inty+90, 5)
drawly.line(lintx-105, inty+105, lintx-125, inty+125, 5)
drawly.line(lintx-105, inty+105, lintx-115, inty+135, 5)
yellow()
drawly.rectangle(625, 210, 40, 15, 0, 30)
drawly.draw()

#creating variables to make my life a whole lot easier

l_elbow_x = lintx-65
l_elbow_y = inty+75
l_palm_x = lintx-10
l_palm_y = inty+100
l_fingers_x = lintx
l_fingers_y = inty + 75
gun_x = l_fingers_x - 10
gun_y = l_fingers_y + 10
gun_rotation = 0

#continuing to move arm towards

scene4()
black()
drawly.rectangle(gun_x, gun_y, 30, 10, 0, gun_rotation)
drawly.rectangle(gun_x, gun_y, 5, 25, gun_rotation)
drawly.rectangle(gun_x+5, gun_y+7, 10, 10, 3, gun_rotation)
stickcolor()
drawly.line(lintx, inty, l_elbow_x, l_elbow_y, 12)
drawly.line(l_elbow_x, l_elbow_y, l_palm_x, l_palm_y, 10)
drawly.line(l_palm_x, l_palm_y, l_fingers_x, l_fingers_y, 5)
drawly.line(l_palm_x, l_palm_y, l_fingers_x + 15, l_fingers_y + 35, 5)
drawly.line(l_palm_x, l_palm_y, l_fingers_x + 5, l_fingers_y + 45, 5)
yellow()
drawly.rectangle(600, 225, 40, 15, 0, 30)
drawly.draw()


l_elbow_x = lintx-50
l_elbow_y = inty+50
l_palm_x = lintx+20
l_palm_y = inty+50
l_fingers_x = lintx + 30
l_fingers_y = inty + 10
gun_x = l_fingers_x - 10
gun_y = l_fingers_y + 25
gun_rotation = 0

scene4()
black()
drawly.rectangle(gun_x, gun_y, 30, 10, 0, gun_rotation)
drawly.rectangle(gun_x, gun_y, 5, 25, gun_rotation)
drawly.rectangle(gun_x+5, gun_y+7, 10, 10, 3, gun_rotation)
stickcolor()
drawly.line(lintx, inty, l_elbow_x, l_elbow_y, 12)
drawly.line(l_elbow_x, l_elbow_y, l_palm_x, l_palm_y, 10)
drawly.line(l_palm_x, l_palm_y, l_fingers_x, l_fingers_y+15, 5)
drawly.line(l_palm_x, l_palm_y, l_fingers_x + 15, l_fingers_y + 35, 5)
drawly.line(l_palm_x, l_palm_y, l_fingers_x + 5, l_fingers_y + 45, 5)
yellow()
drawly.rectangle(575, 240, 40, 15, 0, 30)
drawly.draw()

l_elbow_x = lintx
l_elbow_y = inty+75
l_palm_x = lintx+75
l_palm_y = inty
l_fingers_x = lintx + 100
l_fingers_y = inty - 40
gun_x = l_fingers_x - 10
gun_y = l_fingers_y + 25
gun_rotation = 0

scene4()
black()
drawly.rectangle(gun_x, gun_y, 30, 10, 0, gun_rotation)
drawly.rectangle(gun_x, gun_y, 5, 25, gun_rotation)
drawly.rectangle(gun_x+5, gun_y+7, 10, 10, 3, gun_rotation)
stickcolor()
drawly.line(lintx, inty, l_elbow_x, l_elbow_y, 17)
drawly.line(l_elbow_x, l_elbow_y, l_palm_x, l_palm_y, 12)
drawly.line(l_palm_x, l_palm_y, l_fingers_x, l_fingers_y+15, 5)
drawly.line(l_palm_x, l_palm_y, l_fingers_x + 15, l_fingers_y + 35, 5)
drawly.line(l_palm_x, l_palm_y, l_fingers_x + 5, l_fingers_y + 45, 5)
yellow()
drawly.rectangle(550, 255, 40, 15, 0, 30)
drawly.draw()


l_elbow_x = lintx + 15
l_elbow_y = inty + 35
l_palm_x = lintx + 90
l_palm_y = inty - 10
l_fingers_x = lintx + 110
l_fingers_y = inty - 40
gun_x = l_fingers_x - 10
gun_y = l_fingers_y + 25
gun_rotation = 0

scene4()
black()
drawly.rectangle(gun_x, gun_y, 30, 10, 0, gun_rotation)
drawly.rectangle(gun_x, gun_y, 5, 25, gun_rotation)
drawly.rectangle(gun_x+5, gun_y+7, 10, 10, 3, gun_rotation)
stickcolor()
drawly.line(lintx, inty, l_elbow_x, l_elbow_y, 17)
drawly.line(l_elbow_x, l_elbow_y, l_palm_x, l_palm_y, 12)
drawly.line(l_palm_x, l_palm_y, l_fingers_x, l_fingers_y+15, 5)
drawly.line(l_palm_x, l_palm_y, l_fingers_x + 15, l_fingers_y + 35, 5)
drawly.line(l_palm_x, l_palm_y, l_fingers_x + 5, l_fingers_y + 45, 5)
yellow()
drawly.circle(540, 280, 30)
drawly.draw()


l_elbow_x = lintx + 15
l_elbow_y = inty + 35
l_palm_x = lintx + 90
l_palm_y = inty - 10
l_fingers_x = lintx + 110
l_fingers_y = inty - 40
gun_x = l_fingers_x - 10
gun_y = l_fingers_y + 10
gun_rotation = 30

scene4()
yellow()
drawly.circle(540, 280, 20)
black()
drawly.rectangle(gun_x, gun_y, 30, 10, 0, gun_rotation)
drawly.rectangle(gun_x+5, gun_y+7, 5, 25, 0, gun_rotation)
drawly.rectangle(gun_x+5, gun_y+7, 10, 10, 3, gun_rotation)
stickcolor()
drawly.line(lintx, inty, l_elbow_x, l_elbow_y, 17)
drawly.line(l_elbow_x, l_elbow_y, l_palm_x, l_palm_y, 12)
drawly.line(l_palm_x, l_palm_y, l_fingers_x, l_fingers_y+15, 5)
drawly.line(l_palm_x, l_palm_y, l_fingers_x + 15, l_fingers_y + 35, 5)
drawly.line(l_palm_x, l_palm_y, l_fingers_x + 5, l_fingers_y + 45, 5)
drawly.draw()


l_elbow_x = lintx + 85
l_elbow_y = inty - 5
l_palm_x = lintx + 160
l_palm_y = inty - 70
l_fingers_x = l_palm_x + 20
l_fingers_y = l_palm_y - 40
gun_x = l_fingers_x - 10
gun_y = l_fingers_y + 10
gun_rotation = 30

scene4()
yellow()
drawly.circle(540, 280, 10, 7)
black()
drawly.rectangle(gun_x, gun_y, 30, 10, 0, gun_rotation)
drawly.rectangle(gun_x+5, gun_y+7, 5, 25, 0, gun_rotation)
drawly.rectangle(gun_x+5, gun_y+7, 10, 10, 3, gun_rotation)
stickcolor()
drawly.line(lintx, inty, l_elbow_x, l_elbow_y, 17)
drawly.line(l_elbow_x, l_elbow_y, l_palm_x, l_palm_y, 12)
drawly.line(l_palm_x, l_palm_y, l_fingers_x, l_fingers_y+15, 5)
drawly.line(l_palm_x, l_palm_y, l_fingers_x + 15, l_fingers_y + 35, 5)
drawly.line(l_palm_x, l_palm_y, l_fingers_x + 5, l_fingers_y + 45, 5)
drawly.draw()



l_elbow_x = lintx + 120
l_elbow_y = inty - 20
l_palm_x = lintx + 220
l_palm_y = inty - 100
l_fingers_x = l_palm_x + 20
l_fingers_y = l_palm_y - 40
gun_x = l_fingers_x - 10
gun_y = l_fingers_y + 10
gun_rotation = 40

def scene5():
    scene4()
    black()
    drawly.rectangle(gun_x, gun_y, 30, 10, 0, gun_rotation)
    drawly.rectangle(gun_x+5, gun_y+7, 5, 25, 0, gun_rotation)
    drawly.rectangle(gun_x+5, gun_y+7, 10, 10, 3, gun_rotation)
    stickcolor()
    drawly.line(lintx, inty, l_elbow_x, l_elbow_y, 17)
    drawly.line(l_elbow_x, l_elbow_y, l_palm_x, l_palm_y, 12)
    drawly.line(l_palm_x, l_palm_y, l_fingers_x, l_fingers_y+15, 5)
    drawly.line(l_palm_x, l_palm_y, l_fingers_x + 15, l_fingers_y + 35, 5)
    drawly.line(l_palm_x, l_palm_y, l_fingers_x + 5, l_fingers_y + 45, 5)
scene5()
drawly.draw()
scene5()
drawly.draw()
#Snowman fires at the sun

gun_rotation = 60
scene5()
black()
drawly.circle(gun_x + 35, gun_y - 15, 5)
drawly.draw()

gun_rotation = 40
scene5()
black()
drawly.circle(gun_x + 55, gun_y - 25, 5)
drawly.draw()
#speed up bullet

scene5()
black()
drawly.circle(gun_x + 75, gun_y - 35, 5)
drawly.draw()

scene5()
black()
drawly.circle(gun_x + 95, gun_y - 45, 5)
drawly.draw()

scene5()
black()
drawly.circle(gun_x + 115, gun_y - 55, 5)
drawly.draw()

scene5()
black()
drawly.circle(gun_x + 135, gun_y - 65, 5)
drawly.draw()


scene5()
black()
drawly.circle(gun_x + 155, gun_y - 75, 5)
drawly.draw()

scene5()
black()
drawly.circle(gun_x + 175, gun_y - 85, 5)
drawly.draw()

scene5()
black()
drawly.circle(gun_x + 195, gun_y - 95, 5)
drawly.draw()

scene5()
black()
drawly.circle(gun_x + 215, gun_y - 105, 5)
drawly.draw()

scene5()
black()
drawly.circle(gun_x + 215, gun_y - 105, 5)
drawly.draw()

#sun gets hit by bullet
def surprised_sun():
    sun()
    black()
    drawly.circle(925, 55, 9, 5)
    drawly.circle(875, 55, 9, 5)
    drawly.rectangle(suncenterx - 20, suncentery, 30, 5, 0, 140)
    drawly.rectangle(suncenterx - 60, suncentery, 30, 5, 0, 30)
    drawly.circle(suncenterx-20, suncentery + 50, 10, 5)


scene5()
surprised_sun()
black()
drawly.circle(gun_x + 225, gun_y - 110, 7, 5)
drawly.draw()

scene5()
surprised_sun()
drawly.draw()
scene5()
surprised_sun()
drawly.draw()

gold = "goldenrod1"
scene5()
surprised_sun()
drawly.draw()

gold = "goldenrod2"
scene5()
surprised_sun()
drawly.draw()

gold = "goldenrod3"
scene5()
surprised_sun()
drawly.draw()
gold = "goldenrod4"

scene5()
surprised_sun()
drawly.draw()
gold = "ivory4"
scene5()
surprised_sun()
drawly.draw()


def scene6():
    scene4()
    black()
    drawly.rectangle(gun_x, gun_y, 30, 10, 0, gun_rotation)
    drawly.rectangle(gun_x + 20, gun_y + 7, 5, 25, 0, gun_rotation)
    drawly.rectangle(gun_x + 15, gun_y + 7, 10, 10, 3, gun_rotation)
    stickcolor()
    drawly.line(lintx, inty, l_elbow_x, l_elbow_y, 17)
    drawly.line(l_elbow_x, l_elbow_y, l_palm_x, l_palm_y, 12)
    drawly.line(l_palm_x, l_palm_y, l_fingers_x, l_fingers_y + 15, 5)
    drawly.line(l_palm_x, l_palm_y, l_fingers_x + 15, l_fingers_y + 35, 5)
    drawly.line(l_palm_x, l_palm_y, l_fingers_x + 5, l_fingers_y + 45, 5)
    sun()
    surprised_sun()

#snowman brings gun to face

l_elbow_x = lintx + 100
l_elbow_y = inty
l_palm_x = lintx + 160
l_palm_y = inty - 80
l_fingers_x = l_palm_x + 20
l_fingers_y = l_palm_y - 40
gun_x = l_fingers_x - 20
gun_y = l_fingers_y + 20
gun_rotation = 90
scene6()
drawly.draw()

l_elbow_x = lintx + 90
l_elbow_y = inty + 20
l_palm_x = lintx + 120
l_palm_y = inty - 75
l_fingers_x = l_palm_x + 20
l_fingers_y = l_palm_y - 40
gun_x = l_fingers_x - 20
gun_y = l_fingers_y + 20
scene6()
drawly.draw()

l_elbow_x = lintx + 70
l_elbow_y = inty + 30
l_palm_x = lintx + 90
l_palm_y = inty - 75
l_fingers_x = l_palm_x + 20
l_fingers_y = l_palm_y - 40
gun_x = l_fingers_x - 20
gun_y = l_fingers_y + 20
scene6()
drawly.draw()

l_elbow_x = lintx + 60
l_elbow_y = inty + 35
l_palm_x = lintx + 70
l_palm_y = inty - 78
l_fingers_x = l_palm_x + 20
l_fingers_y = l_palm_y - 40
gun_x = l_fingers_x - 20
gun_y = l_fingers_y + 20
scene6()
drawly.draw()

l_elbow_x = lintx + 55
l_elbow_y = inty + 40
l_palm_x = lintx + 60
l_palm_y = inty - 85
l_fingers_x = l_palm_x + 20
l_fingers_y = l_palm_y - 40
gun_x = l_fingers_x - 20
gun_y = l_fingers_y + 20
scene6()
drawly.draw()

#snowman blows away smoke
scene6()
drawly.set_color("azure4")
drawly.rectangle(gun_x + 10, gun_y - 20, 10, 15)
drawly.draw()


scene7()
black()
drawly.circle(cx + 10, 190, 5)
drawly.circle(cx - 20, 185, 5)
drawly.circle(cx-10, 210, 8, 3)
drawly.set_color("azure4")
drawly.rectangle(gun_x, gun_y - 20, 10, 15)
drawly.draw()

scene7()
black()
drawly.circle(cx + 5, 190, 5)
drawly.circle(cx - 25, 190, 5)
drawly.circle(cx-10, 210, 5, 3)
drawly.set_color("azure4")
drawly.rectangle(gun_x - 20, gun_y - 30, 15, 30)
drawly.draw()

scene7()
black()
drawly.circle(cx + 5, 190, 5)
drawly.circle(cx - 25, 190, 5)
drawly.circle(cx-10, 210, 5, 3)
drawly.set_color("azure4")
drawly.rectangle(gun_x - 40, gun_y - 40, 15, 50)
drawly.draw()

scene7()
black()
drawly.circle(cx + 5, 190, 5)
drawly.circle(cx - 25, 190, 5)
drawly.circle(cx-10, 210, 5, 3)
drawly.set_color("azure4")
drawly.rectangle(gun_x - 60, gun_y - 40, 30, 50)
drawly.draw()

#smoke gets bigger and reveals the snowman's name
scene7()
black()
drawly.circle(cx + 5, 190, 5)
drawly.circle(cx - 25, 190, 5)
drawly.circle(cx-10, 210, 5, 3)
drawly.set_color("azure4")
drawly.rectangle(gun_x - 120, gun_y - 50, 60, 60)
drawly.draw()
scene7()
black()
drawly.circle(cx + 5, 190, 5)
drawly.circle(cx - 25, 190, 5)
drawly.circle(cx-10, 210, 5, 3)
drawly.set_color("azure3")
drawly.rectangle(gun_x - 190, gun_y - 50, 100, 60)
drawly.draw()

scene7()
black()
drawly.circle(cx + 5, 190, 5)
drawly.circle(cx - 25, 190, 5)
drawly.circle(cx-10, 210, 5, 3)
drawly.set_color("azure2")
drawly.rectangle(gun_x - 230, gun_y - 50, 150, 60)
drawly.draw()

drawly.set_color("azure2")
drawly.rectangle(gun_x - 230, gun_y - 50, 150, 60)
drawly.draw()

drawly.text(gun_x - 200, gun_y - 50, "Terry", 50)
drawly.draw()

drawly.set_color("azure1")
drawly.rectangle(gun_x - 230, gun_y - 50, 150, 60)
drawly.set_color("turquoise")
drawly.rectangle(gun_x - 230, gun_y - 50, 150, 60)
drawly.set_color("azure3")
drawly.text(gun_x - 200, gun_y - 50, "Terry", 50)
drawly.draw()

scene7()
black()
drawly.circle(cx + 5, 190, 5)
drawly.circle(cx - 25, 190, 5)
drawly.circle(cx-10, 210, 5, 3)
drawly.set_color("azure3")
drawly.text(gun_x - 225, gun_y - 50, "T e r r y", 50)
drawly.draw()

scene7()
black()
drawly.circle(cx + 5, 190, 5)
drawly.circle(cx - 25, 190, 5)
drawly.circle(cx-10, 210, 5, 3)
drawly.set_color("azure4")
drawly.text(gun_x - 275, gun_y - 75, "T  e  r  r  y", 50)
drawly.draw()

scene7()
black()
drawly.circle(cx + 5, 190, 5)
drawly.circle(cx - 25, 190, 5)
drawly.circle(cx-10, 210, 5, 3)
drawly.set_color("azure4")
drawly.text(gun_x - 275, gun_y - 75, "T  e  r  r  y", 50)
drawly.draw()


drawly.done()
