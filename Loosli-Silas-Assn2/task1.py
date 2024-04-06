# Silas Loosli
# CS1400 - MWF 9:30
import drawly
drawly.set_speed(9)


#Get user's Name
user_name = input("Enter your name: ")
drawly.start(user_name + "'s Faceinator", (1000,1000), "azure2")
print("Hello, " + user_name + ", welcome to the Faceinator! Just a few questions to get us started:")
print("Every time you are asked for a number, remember that the scene is 1000 by 1000 pixels")
print("By the way, here's a website to see what colors you can choose: https://www.pygame.org/docs/ref/color_list.html")

#find skin color and face shape from user
skin_color = input("Please enter a skin color for your face: ")
face_shape = input("Press 1 for a rounded face, 2 for a more oblong face: ")
face_radius = int(input("Enter the radius you would like the face to be: "))

#start getting locations for face
print("Now we will get the location for the face")
print()
face_center_x = int(input("Enter where you would like the face to be in the x direction (center is 500): "))
face_center_y = int(input("Enter where you would like the face to be in the y direction (center is also 500): "))

if face_shape == "1":
    drawly.set_color(skin_color)
    drawly.circle(face_center_x, face_center_y, face_radius-5)
    drawly.set_color("black")
    drawly.circle(face_center_x, face_center_y, face_radius, 5)
if face_shape == "2":
    drawly.set_color(skin_color)
    drawly.ellipse(face_center_x - (face_radius), face_center_y - ((face_radius * 2 + 50)/2), face_radius * 2, face_radius * 2 + 50)
    drawly.set_color("black")
    drawly.ellipse(face_center_x - (face_radius), face_center_y - ((face_radius * 2 + 50)/2), face_radius * 2, face_radius * 2 + 50, 5)
drawly.draw()

print()
print("Now for the eyes: ")
input("(Press Enter)")
#get eye color
print()
eye_color = input("Enter the eye color: ")
drawly.set_color(eye_color)

#ask if the user wants to place eyes symetrically or precisely
eye_input = input("Press 1 to set precise eye coordinates, press 2 for symmetrical eye placement: ")

#If they want it precise
if eye_input == "1":
    eye_width = int(input("Enter how wide you want the eyes to be: "))
    left_eye_position_x = int(input("Enter the x distance from the center of the face for the left eye: "))
    left_eye_position_y = int(input("Enter the y distance from the center of the face for the left eye: "))
    right_eye_position_x = int(input("Enter the x distance from the center of the face for the right eye: "))
    right_eye_position_y = int(input("Enter the y distance from the center of the face for the right eye: "))
    #draw the eyes
    drawly.circle(face_center_x - left_eye_position_x, face_center_y - left_eye_position_y, eye_width / 2)
    drawly.circle(face_center_x + right_eye_position_x, face_center_y - right_eye_position_y, eye_width / 2)

#If they want to be symetric
if eye_input == "2":
    eye_width = int(input("Enter a diameter for the eyes: "))
    eye_spacing_x = int(input("Enter how far apart the eyes should be: "))
    eye_spacing_y = int(input("Enter how far up you want the eyes from the center of the face: "))
    #draw the eyes
    drawly.circle(face_center_x - eye_spacing_x, face_center_y - eye_spacing_y, eye_width / 2)
    drawly.circle(face_center_x + eye_spacing_x, face_center_y - eye_spacing_y, eye_width / 2)

drawly.draw()
#Now we start on the mouth
print()
print("Now for the mouth:")
input("(Press Enter)")
print()

#get the mouth shape from the user
mouth_shape = input("Press 1 for a smiley face, 2 for a frowny face, and 3 for a meh face: ")
mouth_color = input("Enter the color for the mouth: ")
mouth_start_x = int(input("Enter how far left you want the left side of the mouth from the center of the face: "))
mouth_start_y = int(input("Enter how far down you want the mouth to be from the center of the face: "))
mouth_width = int(input("Enter how wide you would like your mouth to be: "))

#draw whichever mouth they wanted
#happy face

drawly.set_color(mouth_color)
if mouth_shape == "1":
    mouth_height = int(input("Enter how tall you would like your smile to be: "))
    drawly.arc(face_center_x - mouth_start_x,face_center_y + mouth_start_y,mouth_width,mouth_height, 200, 340, 12)

#Frowny face:
if mouth_shape == "2":
    mouth_height = int(input("Enter how tall you would like your frown to be: "))
    drawly.arc(face_center_x - mouth_start_x,face_center_y + mouth_start_y,mouth_width,mouth_height, 10, 170, 12)

#meh face
if mouth_shape == "3":
    mouth_draw_x = face_center_x - mouth_start_x
    while 1 == 1:
        drawly.line(mouth_draw_x, face_center_y + mouth_start_y, mouth_draw_x + 20, face_center_y + mouth_start_y, 12,)
        drawly.drawly
        drawly.draw()
        mouth_draw_x = mouth_draw_x + 20
        if mouth_draw_x  >= face_center_x + mouth_width - 140:
            break


drawly.draw()

#Place name 25 units above the head
drawly.set_color("skyblue4")

if face_shape == "1":
    drawly.text(50, face_center_y - face_radius - 100, user_name + "'s face", 75)
if face_shape == "2":
    drawly.text(50, face_center_y - face_radius - 100, user_name + "'s face", 75)
drawly.draw()

print("Here's your completed face, " + user_name + "!")
drawly.done()