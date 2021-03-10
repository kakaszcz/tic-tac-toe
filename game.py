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

    draw_rect(board_model[0][0]["x"], board_model[0][0]["y"], 60, 80)
    draw_rect(board_model[0][1]["x"], board_model[0][1]["y"], 60, 80)
    draw_rect(board_model[0][2]["x"], board_model[0][2]["y"], 60, 80)

    draw_rect(board_model[1][0]["x"], board_model[1][0]["y"], 60, 80)
    draw_rect(board_model[1][1]["x"], board_model[1][1]["y"], 60, 80)
    draw_rect(board_model[1][2]["x"], board_model[1][2]["y"], 60, 80)

    draw_rect(board_model[2][0]["x"], board_model[2][0]["y"], 60, 80)
    draw_rect(board_model[2][1]["x"], board_model[2][1]["y"], 60, 80)
    draw_rect(board_model[2][2]["x"], board_model[2][2]["y"], 60, 80)

app = App(1024, 768)
app.background(255, 255, 255)
app.fill(255, 255, 0)
draw_board()
# app.ellipse(300, 200, 50, 50)  # draw a circle: center_x, center_y, size_x, size_y
# draw_rect(30, 30, 60, 80)
app.redraw()

# app.exit() # close the window
