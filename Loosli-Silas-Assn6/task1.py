# Silas Loosli
# CS1400 - MWF 9:30
import drawly
from random import randint
import time


class Game:
    pass


game = Game()

game.SCREEN_WIDTH = 720
game.SCREEN_HEIGHT = 720
game.SCORE_GOAL = 10
game.POINT_LIST = [5, 4, 3, 2, 1]
game.score = 0
game.answer = False
game.bar_height = 0
game.score_change = 0
drawly.set_speed(100)


def redraw():
    drawly.set_color("wheat")
    drawly.circle(360, 360, 10000)
    drawly.set_color("black")
    drawly.text(100, 100, f"Score: {game.score}", 40)
    drawly.rectangle(500, 125, 100, 250, 5)
    drawly.rectangle(500, 370, 100, 250, 5)
    drawly.set_color("white")
    drawly.rectangle(505, 130, 90, 240)
    drawly.rectangle(505, 375, 90, 240)


def animate():
    for i in range(24):
        if game.bar_height >= 240 + game.score_change or game.bar_height <= -245 + game.score_change:
            break
        # if the answer is correct
        if game.answer:
            redraw()
            if game.bar_height >= 0:
                drawly.set_color("green")
                drawly.rectangle(505, 370 - game.bar_height, 90, game.bar_height)
            else:
                drawly.set_color("red")
                drawly.rectangle(505, 375, 90, abs(game.bar_height))
            drawly.draw()
            game.bar_height += game.score_change

        # if the answer is incorrect
        else:
            redraw()
            if game.bar_height >= 0:
                drawly.set_color("green")
                drawly.rectangle(505, 370 - game.bar_height, 90, game.bar_height)
            else:
                drawly.set_color("red")
                drawly.rectangle(505, 375, 90, abs(game.bar_height))
            game.bar_height -= game.score_change
            drawly.draw()


def question():
    # create a math problem
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    sum = num1 + num2
    user_answer = int(input(f"{num1} + {num2} = "))
    # set answer to true or false
    game.answer = sum == user_answer


def points(time_elapsed):
    if time_elapsed <= 1:
        game.score_change = game.POINT_LIST[0]
    elif time_elapsed <= 2:
        game.score_change = game.POINT_LIST[1]
    elif time_elapsed <= 3:
        game.score_change = game.POINT_LIST[2]
    elif time_elapsed <= 4:
        game.score_change = game.POINT_LIST[3]
    else:
        game.score_change = game.POINT_LIST[4]


def score():
    if game.answer:
        game.score += game.score_change
        print("good job you got it right!")
    else:
        game.score -= game.score_change
        print("not so good, try again!")
    if game.score >= 10:
        game.score = 10
    elif game.score <= -10:
        game.score = -10


def main():
    # set variables for the score and ask the question
    start_time = time.time()
    question()
    # get the time and determine how many points they get
    elapsed_time = time.time() - start_time
    points(elapsed_time)
    score()
    animate()


print("Welcome to the addition game! You will get a bunch of addition problems to answer and based on how fast you"
      " answer them correctly or incorrectly, you will get positive or negative points.")
input("Press enter to start! ")
drawly.start("An Unassuming Thermometer", (game.SCREEN_WIDTH, game.SCREEN_HEIGHT), "wheat")
redraw()
drawly.draw()

while -game.SCORE_GOAL < game.score < game.SCORE_GOAL:
    main()
drawly.set_color("black")
if game.answer:
    drawly.text(150, 550,"Good Job! You won!", 40)
else:
    drawly.text(150, 550,"Bad Luck! You lost!", 40)
drawly.draw()
