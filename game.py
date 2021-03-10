from processing_py import *
BOARD_X = 50
BOARD_Y = 50
SCALE = 2


def hello_world():
    print("Hello from a function")


def draw_rect(x, y, width, height):
    app.rect(x*SCALE, y*SCALE, width*SCALE, height*SCALE)


app = App(1024, 768)
app.background(255, 255, 255)
app.fill(255, 255, 0)
app.ellipse(300, 200, 50, 50)  # draw a circle: center_x, center_y, size_x, size_y
draw_rect(30, 30, 60, 80)
app.redraw()

# app.exit() # close the window
