from processing_py import *

app = App(1024, 768)
app.background(255, 255, 255)
app.fill(255, 255, 0)
app.ellipse(300, 200, 50, 50) # draw a circle: center_x, center_y, size_x, size_y

app.redraw()

#app.exit() # close the window