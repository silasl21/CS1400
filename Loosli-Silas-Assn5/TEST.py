# Silas Loosli
# CS1400 - MWF 9:30
import drawly

class Game:
    pass


game = Game()

game.SCREEN_WIDTH = 720
game.SCREEN_HEIGHT = 720
game.SCORE_GOAL = 10
game.POINT_LIST = [5, 4, 3, 2, 1]
game.score = -1
game.answer = True
game.int_height = 10
game.int_y = 370
game.bar_height = 0
game.score_change = game.POINT_LIST[0]
drawly.set_speed(20)

drawly.start("An Unassuming Thermometer", (game.SCREEN_WIDTH, game.SCREEN_HEIGHT), "wheat")
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

for i in range(20):
    if game.answer:
        game.bar_height += 1
        print(game.bar_height)
        redraw()
        if game.bar_height >= 0:
            drawly.set_color("green")
            drawly.rectangle(505, 370 - game.bar_height, 90, game.bar_height)
        else:
            drawly.set_color("red")
            drawly.rectangle(505, 375, 90, abs(game.bar_height))
        drawly.draw()
drawly.done()
