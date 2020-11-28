"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
File : breakout
Name : Charlie Liu
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 1000/120  # 120 frames per second.
NUM_LIVES = 3          # constant of lives


def main():
    # Add animation loop here!
    # graphics = BreakoutGraphics(brick_cols=5, brick_rows=4)
    graphics = BreakoutGraphics()  # start backoutgraphics
    lives = NUM_LIVES              # get a variable equal NUM_LIVES
    while True:
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:  # accidentally fall, lives minus 1
            lives -= 1             # live minus 1
            graphics.set_ball()    # reset the ball back to initial situation
        if lives == 0:                                                        # dead condition - all lives gone
            graphics.dead()        # start the dead method
            break                  # stop the while loop
        if graphics.move_brick == graphics.tot_brick:                         # win condition - all brick remove
            graphics.win()         # start the win method
            break                  # stop the while loop
        pause(FRAME_RATE)          # temporary stop
        graphics.move_ball()       # start the move_ball method
        graphics.wall_collision()  # start the wall_collision method
        graphics.detect_brick()    # start the detect_brick method
        graphics.detect_paddle()   # start the detect_paddle method


if __name__ == '__main__':
    main()
