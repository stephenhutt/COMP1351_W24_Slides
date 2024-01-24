""" Demo showing how to shift an image.
    File Name: shifted_house.py
    Author: COMP 1351 instructor
    Date:
    Course: COMP 1351
    Assignment: Notes on shifting and scaling
    Collaborators: None
    Internet Source: None
"""
import dudraw

def draw_house() -> None:
    """ Draw a house. The size is 1x1, but it is shifted
        to the right 2 and up 3. Thus it fills a 
        [2, 3]x[3, 4] square
        parameters: None
        return: None
    """
    # draw green main body of the house
    dudraw.set_pen_color_rgb(20, 150, 100)
    # shift the (x, y) center, leave the width and height as-is
    dudraw.filled_rectangle(2 + 0.5, 3 + 0.3, 0.5, 0.3)
    # draw brown roof
    dudraw.set_pen_color_rgb(100, 25, 10)
    # the filled_triangle function takes three points as parameters,
    # all of which have to be shifted
    dudraw.filled_triangle(2 + 0, 3 + 0.6, 2 + 1, 
        3 + 0.6, 2 + 0.5, 3 + 1)
    # draw red door
    dudraw.set_pen_color_rgb(150, 0, 0)
    # shift the (x, y) center, leave the width and height as-is
    dudraw.filled_rectangle(2 + 0.5, 3 + 0.15, 0.1, 0.15)


def main():
    # On a 400x400 pixel canvas, with a scale from [0,5] and [0,5]
    dudraw.set_canvas_size(400, 400)
    dudraw.set_x_scale(0, 5)
    dudraw.set_y_scale(0, 5)
    # clear the background
    dudraw.clear(dudraw.LIGHT_GRAY)
    # draw a 1x1 unit house shifted to the point (2, 3)
    draw_house()
    # Display indefinitely
    dudraw.show(float('inf'))

# Run the program:
if __name__ == '__main__':
    main()
