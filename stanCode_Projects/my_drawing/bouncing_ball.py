"""
File: bouncing ball
Name:Willie Li
-------------------------
This file shows the ball bouncing
at a setting place, and the process
won't be interupted by mouse clicking
before the ball exceeded the window.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
window = GWindow(800, 500, title='bouncing_ball.py')

click = True
Time = 3
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    ball.filled = True
    # the primary ball before clicking
    window.add(ball)
    onmouseclicked(bouncing)


def bouncing(m):
    global START_X, START_Y, VX, GRAVITY, DELAY, click,Time
    if Time > 0:
        # remove the ball at START_X and START_Y
        window.remove(ball)
        while click is True: # The ball will not be influenced by click as moving
            # creating the ball at the next moving place
            ball2 = GOval(SIZE, SIZE, x=START_X + VX, y=START_Y + GRAVITY)
            ball2.filled = True
            window.add(ball2)
            # the primary down speed
            gravity = 0
            while True: # the process of moving
                click = False
                gravity = gravity + GRAVITY
                ball2.move(VX, gravity)
                if ball2.y >= window.height:
                    gravity = -gravity
                    gravity = gravity * REDUCE
                    ball2.move(VX, gravity)
                pause(DELAY)
                if ball2.x > window.width:
                    break
            # back to the primary place
            window.add(ball)
            # count the time
            Time -= 1
        click = True


if __name__ == "__main__":
    main()
