# Silas Loosli
# CS1400 - MWF 9:30
import drawly
import time
class Person:
    pass
hero = Person()
villain = Person()

print("Welcome to the superhero simulator!")
# Superhero stats
print("For the superhero, please enter...")
hero.name = input("A name: ")
hero.radius = int(input("Body size (diameter): ")) / 2
hero.location_x = int(input("X-location: "))
hero.location_y = int(input("Y-location: "))
hero.arm_length = int(input("Arm length: "))

# loop until the leg length is longer than the arm length
hero.leg_length = int(input("Leg length: "))
while hero.arm_length >= hero.leg_length:
    print("Superheros don't have shorter legs than arms, silly!")
    hero.leg_length = int(input("New leg length: "))

# loop until the leg length is longer than the arm length
hero.sword_length = int(input("Sword length: "))
while hero.leg_length >= hero.sword_length + hero.arm_length:
    print("A superhero's sword stroke should reach further than their legs will, silly!")
    hero.leg_length = int(input("New sword length: "))

# loop until the voice attack is longer than the arm + sword length
hero.voice_attack = int(input("Voice power distance: "))
while hero.voice_attack <= hero.arm_length + hero.sword_length:
    print("Now that is a weak voice, no superhero's voice reaches less far than their sword, silly")
    hero.voice_attack = int(input("New voice power distance: "))

print()
# Ask if the user is ready to fight
print(f"Welcome to the scene, {hero.name}! Are you ready for the fight of your life?")
ready = input("(Y/N): ")
if ready == "Y":
    print("Lets get it!")
else:
    num_loops = 1
    while num_loops <= 3:
        time.sleep(0.25)
        print(".")
        num_loops += 1
    print("Well looks like we're up for an interesting fight then.")
# Start defining the villain
print()
print("Now for the villain, please enter:")
villain.name = input("Name: ")
villain.radius = int(input("Body size (diameter): ")) / 2
villain.location_x = int(input("X-location: "))
villain.location_y = int(input("Y-location: "))
print()
print(f"Welcome to your judgement day, {villain.name}")
print()

# Prompt input to get the villain and hero to fight
print("Please keep in mind this situation is highly theoretical, don't try this at home")
input(f"Hit enter to help {hero.name} fight {villain.name}")
drawly.start(f"{hero.name} vs. {villain.name}")

# Draw the hero and villain
drawly.set_color("black")
drawly.circle(hero.location_x, hero.location_y, hero.radius)
drawly.set_color("red")
drawly.circle(villain.location_x, villain.location_y, villain.radius)
drawly.draw()
time.sleep(1)

# Draw the attack circles around the hero with respective colors
drawly.set_color("wheat")
drawly.circle(hero.location_x, hero.location_y, hero.radius + hero.arm_length, 3)
drawly.set_color("blue")
drawly.circle(hero.location_x, hero.location_y, hero.radius + hero.leg_length, 3)
drawly.set_color("grey")
drawly.circle(hero.location_x, hero.location_y, hero.radius + hero.arm_length + hero.sword_length, 3)
drawly.set_color("yellow")
drawly.circle(hero.location_x, hero.location_y, hero.voice_attack, 3)
drawly.draw()

# define a total distance between the hero and villain
total_distance = ((villain.location_x - hero.location_x) ** 2 + (villain.location_y - hero.location_y) ** 2) ** 0.5

# Make the total distance the distance between each body instead of the distance between the centers of the bodies
body_distance = total_distance - hero.radius - villain.radius

# Print various messages for each type of attack
# If the villain is connected with the hero, hero dies in a spatter of blood expanding over the whole screen
if body_distance < 0:
    print(f"Looks like you got a little too close for comfort, {hero.name}. Time's up :(")
    time.sleep(2)
    num_loops_2 = 1
    blood_radius = hero.radius - 40
    drawly.set_color("red")
    drawly.set_speed(10)
    while num_loops_2 < 50:
        drawly.circle(hero.location_x, hero.location_y, blood_radius)
        drawly.draw()
        blood_radius += 20
        num_loops_2 += 1
# If the villain is within the punch radius 
elif body_distance <= hero.arm_length:
    print(f"Punch 'em good and hard, {hero.name}")
# Within the kick radius
elif body_distance <= hero.leg_length:
    print(f"You done been kicked good and hard, {villain.name}")
# Within the sword distance
elif body_distance <= hero.sword_length + hero.arm_length:
    print(f"Now {villain.name} can join the headless games!")
# Within the voice distance
elif body_distance <= hero.voice_attack:
    print(f"Now that {villain.name} is stunned with your voice attack, go finish them off!")
# Out of range of all of these attacks
else:
    print(f"Wow, {villain.name} is a real coward. Go get 'em, {hero.name}!")
drawly.done()