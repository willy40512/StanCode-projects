"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
The file will build the graphic of breakout game, and create the method of the object
to make sure the game will be activated.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.

click = False


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.pof = paddle_offset
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (window_width-self.paddle.width)/2, window_height-self.pof)

        # Center a filled ball in the graphical window.
        self.ball = GOval(2 * ball_radius, 2 * ball_radius)
        self.ball.filled = True
        self.window.add(self.ball, self.window.width/2-self.ball.width/2, self.window.height/2)
        self.initial_x = self.window.width/2-self.ball.width/2
        self.initial_y = self.window.height/2
        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0
        self.set_speed()
        self.get_dx()
        self.get_dy()

        # Initialize our mouse listeners.
        self.click = False
        onmousemoved(self.paddle_follow)
        onmouseclicked(self.start)

        # Draw bricks.
        self.br = brick_rows
        self.bc = brick_cols
        self.sp = brick_spacing
        self.of = brick_offset
        self.set_brick()
        # self.check()
        # self.rest_ball()
        self.total = self.br * self.bc
        # self.break_all_brick()

    def start(self, m):
        # make a button for mouseclick to let user start the game
        if self.ball.x == self.initial_x and self.ball.y == self.initial_y:
            self.click = True

    def break_all_brick(self):
        # to check the amount of brick
        if self.total == 0:
            return True

    def rest_ball(self):
        self.window.add(self.ball, self.window.width/2-self.ball.width/2, self.window.height/2)

    def check(self):
        maybe_wall = self.window.get_object_at(self.ball.x, self.ball.y)
        maybe_wall1 = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        maybe_wall2 = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        maybe_wall3 = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.width)

        if maybe_wall is None:
            if maybe_wall2 is None:
                if maybe_wall3 is None:
                    if maybe_wall1 is None:
                        return False
                    else:
                        if maybe_wall1 is self.paddle:
                            return True
                        else:
                            # the object is brick
                            self.window.remove(maybe_wall1)
                            self.total -= 1
                            return True
                else:
                    if maybe_wall3 is self.paddle:
                        return True
                    else:
                        # the object is brick
                        self.window.remove(maybe_wall3)
                        self.total -= 1
                        return True
            else:
                if maybe_wall2 is self.paddle:
                    return False
                else:
                    # the object is brick
                    self.window.remove(maybe_wall2)
                    self.total -= 1
                    return True
        else:
            if maybe_wall is self.paddle:
                return False
            else:
                # the object is brick
                self.window.remove(maybe_wall)
                self.total -= 1
                return True

    def get_dy(self):
        return self.__dy

    def get_dx(self):
        return self.__dx

    def set_speed(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = - self.__dx
        if random.random() > 0.5:
            self.__dy = -self.__dy

    def paddle_follow(self, event):
        if self.paddle.width/2 <= event.x <= self.window.width-self.paddle.width/2:
            self.window.add(self.paddle, event.x-self.paddle.width/2, self.window.height-PADDLE_OFFSET)

    def set_brick(self):
        for i in range(self.br):
            for k in range(self.bc):
                # produce the brick
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                brick.filled = True
                # change the color of brick at different row
                if 2 > i >= 0:
                    brick.fill_color = 'red'
                elif 4 > i >= 2:
                    brick.fill_color = 'orange'
                elif 6 > i >= 4:
                    brick.fill_color = 'yellow'
                elif 8 > i >= 6:
                    brick.fill_color = 'green'
                elif 10 > i >= 8:
                    brick.fill_color = 'blue'
                self.window.add(brick, k * (brick.width + self.sp), self.of + i * (brick.height + self.sp))
