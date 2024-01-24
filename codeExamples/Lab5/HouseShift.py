""" Demo showing how to shift an image.
    The draw_house() function takes two parameters
    for the x-shift and y-shift values
    File Name: shifted_house_parameters.py
    Author: COMP 1351 instructor
    Date:
    Course: COMP 1351
    Assignment: Notes on shifting and scaling
    Collaborators: None
    Internet Source: None
"""
import dudraw

def draw_house(x_shift: float, y_shift: float) -> None:
    """ Draw a house. The size is 1 by 1, but it is shifted
        horizontally by x_shift and vertically by y_shift. Thus
        it fills a [x_shift, x_shift+1]x[y_shift, y_shift+1] square
        parameters:
            x_shift: left edge of the shifted image (type: float)
            y_shift: bottom edge of the shifted image (type: float)
        return: None
    """
    # draw green main body of the house
    dudraw.set_pen_color_rgb(20, 150, 100)
    # shift the (x, y) location of rectangle, 
    # leave the width and height as-is
    dudraw.filled_rectangle(x_shift + 0.5, y_shift + 0.3, 0.5, 0.3)
    # draw brown roof
    dudraw.set_pen_color_rgb(100, 25, 10)
    # the filled_triangle function takes three points as parameters,
    # all of which have to be shifted
    dudraw.filled_triangle(x_shift + 0, y_shift + 0.6, 
        x_shift + 1, y_shift + 0.6, x_shift + 0.5, y_shift + 1)
    # draw red door
    dudraw.set_pen_color_rgb(150, 0, 0)
    # shift the (x, y) location of rectangle
    # leave the width and height as-is
    dudraw.filled_rectangle(x_shift + 0.5, y_shift + 0.15, 0.1, 0.15)


def main():
    # On a 400x400 pixel canvas, with a scale from [0,5] and [0,5]
    dudraw.set_canvas_size(400, 400)
    dudraw.set_x_scale(0, 5)
    dudraw.set_y_scale(0, 5)
    # clear the background
    dudraw.clear(dudraw.LIGHT_GRAY)
    # draw four houses at various locations
    draw_house(2, 3)
    draw_house(1, 1)
    draw_house(4, 4)
    draw_house(3, 2)
    # Display indefinitely
    dudraw.show(float('inf'))

# Run the program:
if __name__ == '__main__':
    main()
