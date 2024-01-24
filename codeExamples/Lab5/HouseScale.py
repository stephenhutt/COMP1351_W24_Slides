""" Demo showing how to scale an image.
    File Name: scaled_house_parameter.py
    Author: COMP 1351 instructor
    Date:
    Course: COMP 1351
    Assignment: Notes on shifting and scaling
    Collaborators: None
    Internet Source: None
"""
import dudraw

def draw_house(x_scale: float, y_scale: float) -> None:
    """ Draw a house. The size is x_scale by y_scale, 
        with (0, 0) as the lower left corner.
        [0, x_scale]x[0, y_scale] square
        parameters:
            x_scale: width of the scaled image (type: float)
            y_scale: height of the scaled image (type: float)
        return: None
    """
    # draw green main body of the house
    dudraw.set_pen_color_rgb(20, 150, 100)
    # scale the x-positions and sizes by x_scale and the
    # y-positions and sizes by y_scale.
    dudraw.filled_rectangle(x_scale * 0.5, y_scale * 0.3, 
        x_scale * 0.5, y_scale * 0.3)
    # draw brown roof
    dudraw.set_pen_color_rgb(100, 25, 10)
    # the filled_triangle function takes three points as parameters,
    # all of which have to be scaled
    dudraw.filled_triangle(x_scale * 0, y_scale * 0.6, x_scale * 1, 
        y_scale * 0.6, x_scale * 0.5, y_scale * 1)
    # draw red door
    dudraw.set_pen_color_rgb(150, 0, 0)
    # scale all x and y values
    dudraw.filled_rectangle(x_scale * 0.5, y_scale * 0.15, 
        x_scale * 0.1, y_scale * 0.15)


def main():
    # On a 400x400 pixel canvas, with a scale from [0,5] and [0,5]
    dudraw.set_canvas_size(400, 400)
    dudraw.set_x_scale(0, 5)
    dudraw.set_y_scale(0, 5)
    # clear the background
    dudraw.clear(dudraw.LIGHT_GRAY)
    # draw a 2x5 unit house with lower left corner at (0, 0)
    draw_house(2, 5)
    # Display indefinitely
    dudraw.show(float('inf'))

# Run the program:
if __name__ == '__main__':
    main()
