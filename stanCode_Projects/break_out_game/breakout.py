"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics(brick_cols=10, brick_rows=10)

    # Add animation loop here!
    x = graphics.get_dx()
    y = graphics.get_dy()
    live = NUM_LIVES
    while True:
        # to pause till the mouseclick
        pause(FRAME_RATE)
        graphics.set_speed()
        if graphics.break_all_brick():
            graphics.rest_ball()
            break
        if graphics.click is True:
            pause(FRAME_RATE)
            # the condition of game over
            if live == 0 or graphics.break_all_brick():
                # rest the ball to the initial place
                graphics.rest_ball()
                break
            graphics.ball.move(x, y)
            # the ball move to the downside of the window
            if graphics.ball.y >= graphics.window.height - graphics.ball.height:
                live -= 1
                graphics.rest_ball()
                graphics.click = False
                y = - y
            # to check whether the ball hit the break or paddle
            if graphics.check():
                y = - y
                # to avoid the brick stick on the paddle
                graphics.ball.move(x, y)
            # when the ball hit the wall, the ball will change x direction
            if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
                x = -x
            # when the ball hit the wall, the ball will change y direction
            if graphics.ball.y <= 0 or graphics.ball.y >= graphics.window.height - graphics.ball.height:
                y = -y


if __name__ == '__main__':
    main()
