""" Demo showing how to scale and shift an image.
    File Name: scaled__shifted_house_parameter.py
    Author: COMP 1351 instructor
    Date:
    Course: COMP 1351
    Assignment: Notes on shifting and scaling
    Collaborators: None
    Internet Source: None
"""
import dudraw

def draw_house(x_shift: float, y_shift: float, 
               x_scale: float, y_scale: float) -> None:
    """ Draw a house. The size is x_scale by y_scale, 
        with (x_shift, y_shift) as the lower left corner.
        It fills a square:
        [x_shift, x_shift+x_scale]x[y_shift, y_shift + y_scale]
        parameters:
            x_shift: left corner of image (type: float)
            y_shift: bottom corner of image (type: float)
            x_scale: width of the image (type: float)
            y_scale: height edge of the shifted image (type: float)
        return: None
    """
    # draw green main body of the house
    dudraw.set_pen_color_rgb(20, 150, 100)
    # scale the x-positions and sizes by x_scale and the
    # y-positions and sizes by y_scale. Shift positions
    # by the appropriate shift values
    dudraw.filled_rectangle(
        x_shift + x_scale * 0.5, y_shift + y_scale * 0.3, 
        x_scale * 0.5, y_scale * 0.3)
    # draw brown roof
    dudraw.set_pen_color_rgb(100, 25, 10)
    # the filled_triangle function takes three points
    # as parameters, all of which have to be scaled and shifted
    dudraw.filled_triangle(
        x_shift + x_scale * 0, y_shift + y_scale * 0.6, 
        x_shift + x_scale * 1, y_shift + y_scale * 0.6, 
        x_shift + x_scale * 0.5, y_shift + y_scale * 1)
    # draw red door
    dudraw.set_pen_color_rgb(150, 0, 0)
    # scale all x and y values, shift all positions
    dudraw.filled_rectangle(
        x_shift + x_scale * 0.5, y_shift + y_scale * 0.15, 
        x_scale * 0.1, y_scale * 0.15)


def main():
    # On a 400x400 pixel canvas, with a scale from [0,1] and [0,1]
    dudraw.set_canvas_size(400, 400)
    dudraw.set_x_scale(0, 1)
    dudraw.set_y_scale(0, 1)
    # clear the background
    dudraw.clear(dudraw.LIGHT_GRAY)
    # draw several houses with various shifts and scaling
    draw_house(0.05, 0.05, 0.45, 0.45)
    draw_house(0.05, 0.75, 0.4, 0.1)
    draw_house(0.75, 0.55, 0.1, 0.4)
    draw_house(0.75, 0.25, 0.1, 0.1)
    # Display indefinitely
    dudraw.show(float('inf'))

# Run the program:
if __name__ == '__main__':
    main()
