"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
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
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


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
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'

        # set paddle's instance variable
        self.pad_width = paddle_width
        self.pad_height = paddle_height
        self.pad_offset = paddle_offset
        """
        go will be a variable set to 0 or 1
        go equal 1 means it's touch paddle already and go to bricks
        go equals 0 means it's touch bricks and can go back to paddle  
        """
        self.go = 0

        # set ball's instance variable
        self.radius = ball_radius

        # Center a filled ball in the graphical window.
        self.ball = GOval(2*self.radius, 2*self.radius)
        self.set_ball()                   # start set_ball method

        # set brick's instance variable
        self.bri_width = brick_width
        self.bri_height = brick_height
        self.bri_cols = brick_cols
        self.bri_rows = brick_rows
        self.bri_spacing = brick_spacing
        self.bri_offset = brick_offset
        self.brick = GRect(self.bri_width, self.bri_height)
        self.tot_brick = brick_rows * brick_cols
        self.move_brick = 0

        # Default initial velocity for the ball.
        self.__dx = 0                  # use to storage the x speed
        self.__dy = 0                  # use to storage the y speed
        self.dx = self.get_dx()        # get the x speed
        self.dy = self.get_dy()        # get the y speed

        # Initialize our mouse listeners.
        onmouseclicked(self.mouse_click)
        onmousemoved(self.paddle_move)

        # Draw bricks.
        self.set_brick()

        # set label for the text
        self.dead_label = GLabel('')
        self.cry_label = GLabel('')
        self.win_label = GLabel('')
        self.smile_label = GLabel('')

    def dead(self):
        """
        if the lives equal zero, it mean the player dead. so it will remove the ball and show you are dead
        """
        self.window.remove(self.ball)                                                              # remove the ball
        self.dead_label = GLabel('You are dead')                                                   # add label context
        self.dead_label.font = 'courier-40'                                                        # set text size and type
        self.cry_label = GLabel('(〒︿〒)')                                                         # add label context
        self.cry_label.font = 'courier-30'                                                         # set text size and type
        self.window.add(self.dead_label, x=self.window.width/2 - 195, y=self.window.height/2)      # add on windows of specific location
        self.window.add(self.cry_label, x=self.window.width/2 - 80, y=(self.window.height/2 + 80)) # add on windows of specific location

    def win(self):
        """
        if all the bricks are remove, it means you win the game
        """
        self.window.remove(self.ball)                                                               # remove the ball
        self.win_label = GLabel('Congratulation')                                                   # add label context
        self.win_label.font = 'courier-40'                                                          # set text size and type
        self.smile_label = GLabel('(ﾉ>ω<)ﾉ')                                                        # add label context
        self.smile_label.font = 'courier-30'                                                        # set text size and type
        self.window.add(self.win_label, x=self.window.width/2-250, y=self.window.height/2)          # add on windows of specific location
        self.window.add(self.smile_label, x=self.window.width/2-85, y=(self.window.height/2 + 80))  # add on windows of specific location

    def set_ball(self):
        """
        let a ball filled with color
        """
        self.ball.filled = True         # True to fill color
        self.ball.fill_color = 'navy'   # choose the color
        self.__dy = 0                   # speed of initial position of the ball
        self.__dx = 0                   # speed of initial position of the ball
        """
        put the ball on a specific location on window
        """
        self.window.add(self.ball, x=(self.window.width-self.radius)/2, y=(self.window.height-self.radius)/2)

    def detect_brick(self):
        """
        use four corner to detect if it touch a brick or not
        maybe_obj1 to maybe_obj4 is use to get if there is object or not
        """
        maybe_obj1 = self.window.get_object_at(self.ball.x, self.ball.y)
        maybe_obj2 = self.window.get_object_at(self.ball.x, self.ball.y + (2 * self.radius))
        maybe_obj3 = self.window.get_object_at(self.ball.x + (2 * self.radius), self.ball.y)
        maybe_obj4 = self.window.get_object_at(self.ball.x + (2 * self.radius), self.ball.y + (2 * self.radius))
        if maybe_obj1 is not self.paddle and maybe_obj1 is not None:  # if it has object and is not paddle - means brick
            self.window.remove(maybe_obj1)                            # remove the object
            self.__dy = -self.__dy                                    # change the direction
            self.go = 0                                               # ball can touch the paddle now
            self.move_brick += 1                                      # number of remove brick plus 1
        elif maybe_obj2 is not self.paddle and maybe_obj2 is not None:  # if it has object and is not paddle - means brick
            self.window.remove(maybe_obj2)                              # remove the object
            self.__dy = -self.__dy                                      # change the direction
            self.go = 0                                                 # ball can touch the paddle now
            self.move_brick += 1                                        # number of remove brick plus 1
        elif maybe_obj3 is not self.paddle and maybe_obj3 is not None:  # if it has object and is not paddle - means brick
            self.window.remove(maybe_obj3)                              # remove the object
            self.__dy = -self.__dy                                      # change the direction
            self.go = 0                                                 # ball can touch the paddle now
            self.move_brick += 1                                        # number of remove brick plus 1
        elif maybe_obj4 is not self.paddle and maybe_obj4 is not None:  # if it has object and is not paddle - means brick
            self.window.remove(maybe_obj4)                              # remove the object
            self.__dy = -self.__dy                                      # change the direction
            self.go = 0                                                 # ball can touch the paddle now
            self.move_brick += 1                                        # number of remove brick plus 1

    def detect_paddle(self):
        """
        use four corner to detect if it touch a paddle or not
        maybe_obj1 to maybe_obj4 is use to get if there is object or not
        """
        maybe_obj1 = self.window.get_object_at(self.ball.x, self.ball.y)
        maybe_obj2 = self.window.get_object_at(self.ball.x + (2 * self.radius), self.ball.y)
        maybe_obj3 = self.window.get_object_at(self.ball.x + (2 * self.radius), self.ball.y)
        maybe_obj4 = self.window.get_object_at(self.ball.x + (2 * self.radius), self.ball.y + (2 * self.radius))
        if self.go == 0:  # go is use to let the ball detect the paddle only one times
            if maybe_obj1 is self.paddle:    # if it is paddle
                self.__dy = -self.__dy       # change the direction
                self.go = 1                  # go equal 1 means it's touch and go to bricks
            elif maybe_obj2 is self.paddle:  # if it is paddle
                self.__dy = -self.__dy       # change the direction
                self.go = 1                  # go equal 1 means it's touch and go to bricks
            elif maybe_obj3 is self.paddle:  # if it is paddle
                self.__dy = -self.__dy       # change the direction
                self.go = 1                  # go equal 1 means it's touch and go to bricks
            elif maybe_obj4 is self.paddle:  # if it is paddle
                self.__dy = -self.__dy       # change the direction
                self.go = 1                  # go equal 1 means it's touch and go to bricks

    def mouse_click(self, event):
        """
        if the x speed of ball and y speed of the ball is 0, it means it's a new start, and click will let the ball move
        :param event: mouse detect
        """
        if self.__dx == 0 and self.__dy == 0:    # x speed and y speed is both zero
            self.set_ball_velocity()             # decide the velocity of ball
            self.move_ball()                     # ball move

    def wall_collision(self):
        """
        1.touch the wall, and it need to change the direction, beside, consider that it may not touch brick to reflect to
        paddle, so when touch the wall, go also need to change into 0
        2. ball can not touch the bottom of window, it will cause dead, using other way to figure iy out
        """
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:  # touch the right and left wall
            self.__dx = -self.__dx          # change the direction
            self.go = 0                     # it can touch the paddle now
        if self.ball.y <= 0:                # touch the up wall
            self.__dy = -self.__dy          # change the direction
            self.go = 0                     # it can touch the paddle now

    def set_ball_velocity(self):
        """
        let the ball have speed and have different way to move forward
        """
        self.__dx = random.randint(0, MAX_X_SPEED)          # choose a speed rate from 0 and MAX_X_SPEED
        self.__dy = random.randint(0, INITIAL_Y_SPEED)      # choose a speed rate from 0 and INITIAL_Y_SPEED
        if self.__dx == 0:                                  # let ball not just move up and down
            self.__dx = random.randint(0, MAX_X_SPEED)      # re-choose a x speed rate
        if self.__dy == 0:                                  # let the ball not just move left and right
            self.__dy = random.randint(0, INITIAL_Y_SPEED)  # re-choose a y speed rate
        if random.random() > 0.5:                           # let the ball have 50-50 chance to move left or right
            self.__dx = -self.__dx                          # set to have opposite way
        if random.random() > 0.5:                           # let the ball have 50-50 chance to move up or down
            self.__dy = -self.__dy                          # set to have opposite way

    def move_ball(self):
        """
        ball move with the speed __dx and __dy
        """
        self.ball.move(self.__dx, self.__dy)

    def get_dx(self):
        """
        set a getter to get x speed
        :return: the value of x speed
        """
        return self.__dx          # return the x speed

    def get_dy(self):
        """
        getter to get y speed
        :return: the value of y speed
        """
        return self.__dy    # return the y speed

    def paddle_move(self, mouse):
        """
        mouse detect to let paddle follow the mouse
        :param mouse: mouse detect
        """
        paddle_x_position = mouse.x-(self.pad_width/2)              # set into middle part of paddle
        if mouse.x + self.pad_width >= self.window.width:           # when the mouse on left side outside of windoe
            paddle_x_position = self.window.width - self.pad_width  # x set into left of window
        if mouse.x - self.pad_width <= 0:                           # when the mouse on the right side outside of window
            paddle_x_position = 0                                   # x position set into right of window
        """
        add paddle into specific location on the window
        """
        self.window.add(self.paddle, x=paddle_x_position, y=self.window.height-self.pad_offset-self.pad_height)

    def set_brick(self):
        """
        set brick into initial position
        """
        brick_width_in_window = 0                 # initial position of brick in x
        brick_height_in_window = self.bri_offset  # initial position of brick in y
        for i in range(self.bri_rows):            # for loop based on how many rows it has
            for j in range(self.bri_cols):        # for loop based on how many columns it has
                self.brick = GRect(self.bri_width, self.bri_height)  # set a brick
                self.brick.filled = True                             # True to fill with color
                if j % 4 == 0:                      # base on the columns to choose color
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                if j % 4 == 1:                      # base on the columns to choose color
                    self.brick.fill_color = 'salmon'
                    self.brick.color = 'salmon'
                if j % 4 == 2:                      # base on the columns to choose color
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                if j % 4 == 3:                      # base on the columns to choose color
                    self.brick.fill_color = 'tomato'
                    self.brick.color = 'tomato'
                self.window.add(self.brick, x=brick_width_in_window, y=brick_height_in_window)    # add brick to windows
                """
                move forward to next columns position, include brick width and spacing 
                """
                brick_width_in_window += self.bri_width
                brick_width_in_window += self.bri_spacing
            brick_width_in_window = 0                   # all the row start at x = 0
            """
            move forward to next rows position, include brick height and spacing 
            """
            brick_height_in_window += self.bri_height
            brick_height_in_window += self.bri_spacing



