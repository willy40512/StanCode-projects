"""
File: draw line
Name: Willie Li
-------------------------
The file shows the function of
drawing the line. For the first
time clicking, a circle will be
created for marking. For the second
time clicking, a line will be drew
from the center of circle to the place of
second time clicking
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# the constant controls the size of the circle
SIZE = 30

# Global Variable
w = GWindow()
circle = GOval(SIZE, SIZE)
click = True


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(circle_line)


def circle_line(event):
    global click
    # odd time click
    if click is True:
        # mark the first clicking place with circle
        w.add(circle, event.x-SIZE/2, event.y - SIZE/2)
        # making next click to the part of drawing line
        click = False
    # even time click
    else:
        # draw the line from the circle to the second clicking place
        line = GLine(circle.x+SIZE/2, circle.y+SIZE/2, event.x, event.y)
        w.add(line)
        # remove the circle marked on the window
        w.remove(circle)
        # go back to the first time click
        click = True


if __name__ == "__main__":
    main()
