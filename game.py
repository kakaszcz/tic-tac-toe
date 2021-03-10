from processing_py import *
BOARD_X = 50
BOARD_Y = 50
SCALE = 2
RECT_WIDTH = 60
RECT_HEIGHT = 80

board_model = [
    [{"x": 30, "y": 30}, {"x": 90, "y": 30}, {"x": 150, "y": 30}],
    [{"x": 30, "y": 110}, {"x": 90, "y": 110}, {"x": 150, "y": 110}],
    [{"x": 30, "y": 190}, {"x": 90, "y": 190}, {"x": 150, "y": 190}]
]


def hello_world():
    print("Hello from a function")


def draw_rect(x, y, width, height):
    app.rect(x*SCALE, y*SCALE, width*SCALE, height*SCALE)


def draw_board():
    app.fill(169, 136, 179)
    for row in range(0, 3):
        for col in range(0, 3):
            draw_rect(board_model[row][col]["x"], board_model[row][col]["y"], RECT_WIDTH, RECT_HEIGHT)


def draw_circle(row, col):
    app.fill(152, 140, 156)
    x = board_model[row][col]["x"] * SCALE + (RECT_WIDTH/2) * SCALE
    y = board_model[row][col]["y"] * SCALE + (RECT_HEIGHT/2) * SCALE
    app.ellipse(x, y, 50, 50)  # draw a circle: center_x, center_y, size_x, size_y


app = App(1024, 768)
app.background(255, 255, 255)
draw_board()
draw_circle(0, 2)
app.redraw()

# app.exit() # close the window
