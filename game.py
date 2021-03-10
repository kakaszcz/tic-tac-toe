from processing_py import *
BOARD_X = 50
BOARD_Y = 50
SCALE = 2


def hello_world():
    print("Hello from a function")


def draw_rect(x, y, width, height):
    app.rect(x*SCALE, y*SCALE, width*SCALE, height*SCALE)


def draw_board():
    board_model = [
        [{"x": 30, "y": 30}, {"x": 90, "y": 30}, {"x": 150, "y": 30}],
        [{"x": 30, "y": 110}, {"x": 90, "y": 110}, {"x": 150, "y": 110}],
        [{"x": 30, "y": 190}, {"x": 90, "y": 190}, {"x": 150, "y": 190}]
    ]
    for row in range(0, 3):
        for col in range(0, 3):
            draw_rect(board_model[row][col]["x"], board_model[row][col]["y"], 60, 80)


app = App(1024, 768)
app.background(255, 255, 255)
app.fill(255, 255, 0)
draw_board()
# app.ellipse(300, 200, 50, 50)  # draw a circle: center_x, center_y, size_x, size_y
# draw_rect(30, 30, 60, 80)
app.redraw()

# app.exit() # close the window
