"""
Author: Stephen Hutt
Course: 1351
Content: Drawing with color example
"""
import dudraw


print("Lab2 Example")
#Create our canvas
dudraw.set_canvas_size(400,400)
dudraw.set_x_scale(0,400)
dudraw.set_y_scale(0,400)
#Set the Pen Color
dudraw.set_pen_color_rgb(0,255,0)
#Draw the circle
dudraw.filled_circle(200, 200, 100)
dudraw.set_pen_color_rgb(255,0,0)
dudraw.filled_circle(200, 200, 50)
dudraw.show(100000)