##################################################################################
#      This file is part of mindwave-python.                                     #
#                                                                                #
#      mindwave-python is free software: you can redistribute it and/or modify   #
#      it under the terms of the GNU General Public License as published by      #
#      the Free Software Foundation, either version 3 of the License, or         #
#      (at your option) any later version.                                       #
#                                                                                #
#      mindwave-python is distributed in the hope that it will be useful,        #
#      but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#      GNU General Public License for more details.                              #
#                                                                                #
#      You should have received a copy of the GNU General Public License         #
#      along with mindwave-python.  If not, see <http://www.gnu.org/licenses/>.  #
##################################################################################

from pymouse import PyMouse

LEFT_BUTTON = 1
RIGHT_BUTTON = 2

class BlinkInterpreter(object):
    MOVE_LEFT = 0
    MOVE_RIGHT = 1
    MOVE_UP = 2
    MOVE_DOWN = 3
    GOTO_SPEED = 4
    GOTO_CLICKS = 5
    GOTO_DRAG = 6
    GOTO_MOVEMENT = 7
    MAKE_FASTER = 8
    MAKE_SLOWER = 9
    CLICK = 10
    DOUBLE_CLICK = 11
    RIGHT_CLICK = 12
    RIGHT_DOUBLE_CLICK = 13
    CLICK_HOLD = 14
    RELEASE = 15
    RIGHT_CLICK_HOLD = 16
    RIGHT_RELEASE = 17
    STOP = 18
    NOP = 19

    def __init__(self):
        self.rowcol_to_state =  { (0,0) : BlinkInterpreter.MOVE_LEFT,
                                      (0,1) : BlinkInterpreter.MOVE_RIGHT,
                                      (0,2) : BlinkInterpreter.MOVE_UP,
                                      (0,3) : BlinkInterpreter.MOVE_DOWN,
                                      (0,4) : BlinkInterpreter.GOTO_SPEED,
                                      (0,5) : BlinkInterpreter.GOTO_DRAG,
                                      (0,6) : BlinkInterpreter.NOP,

                                      (1,0) : BlinkInterpreter.MAKE_FASTER,
                                      (1,1) : BlinkInterpreter.MAKE_SLOWER,
                                      (1,2) : BlinkInterpreter.NOP,
                                      (1,3) : BlinkInterpreter.NOP,
                                      (1,4) : BlinkInterpreter.GOTO_CLICKS,
                                      (1,5) : BlinkInterpreter.GOTO_MOVEMENT,
                                      (1,6) : BlinkInterpreter.NOP,

                                      (2,0) : BlinkInterpreter.CLICK,
                                      (2,1) : BlinkInterpreter.DOUBLE_CLICK,
                                      (2,2) : BlinkInterpreter.RIGHT_CLICK,
                                      (2,3) : BlinkInterpreter.RIGHT_DOUBLE_CLICK,
                                      (2,4) : BlinkInterpreter.GOTO_DRAG,
                                      (2,5) : BlinkInterpreter.GOTO_SPEED,
                                      (2,6) : BlinkInterpreter.NOP,

                                      (3,0) : BlinkInterpreter.CLICK_HOLD,
                                      (3,1) : BlinkInterpreter.RELEASE,
                                      (3,2) : BlinkInterpreter.RIGHT_CLICK_HOLD,
                                      (3,3) : BlinkInterpreter.RIGHT_RELEASE,
                                      (3,4) : BlinkInterpreter.GOTO_MOVEMENT,
                                      (3,5) : BlinkInterpreter.GOTO_CLICKS,
                                      (3,6) : BlinkInterpreter.NOP
                                      }
        self.state_to_rowcol = { self.rowcol_to_state[key]:key for key in self.rowcol_to_state }
        self.row = 0
        self.col = 0
        self.maxrow = max([key[0] for key in self.rowcol_to_state])
        self.maxcol = max([key[1] for key in self.rowcol_to_state])
        
        self.current_state = BlinkInterpreter.NOP
        self.mouse = PyMouse()
  
        self.handlers = {}
        for key in self.state_to_rowcol:
            self.handlers[key] = self.do_nothing
        self.handlers[BlinkInterpreter.NOP] = self.handle_nop
        self.handlers[BlinkInterpreter.MOVE_LEFT] = self.handle_move_left
        self.handlers[BlinkInterpreter.MOVE_RIGHT]= self.handle_move_right
        self.handlers[BlinkInterpreter.MOVE_UP] = self.handle_move_up
        self.handlers[BlinkInterpreter.MOVE_DOWN] = self.handle_move_down
        self.handlers[BlinkInterpreter.GOTO_SPEED] = self.handle_goto_speed
        self.handlers[BlinkInterpreter.GOTO_CLICKS] = self.handle_goto_clicks
        self.handlers[BlinkInterpreter.GOTO_DRAG] = self.handle_goto_drag
        self.handlers[BlinkInterpreter.GOTO_MOVEMENT] = self.handle_goto_movement
        self.handlers[BlinkInterpreter.MAKE_FASTER] = self.handle_make_faster
        self.handlers[BlinkInterpreter.MAKE_SLOWER] = self.handle_make_slower
        self.handlers[BlinkInterpreter.CLICK] = self.handle_click
        self.handlers[BlinkInterpreter.DOUBLE_CLICK] = self.handle_double_click
        self.handlers[BlinkInterpreter.RIGHT_CLICK] = self.handle_right_click
        self.handlers[BlinkInterpreter.RIGHT_DOUBLE_CLICK] = self.handle_right_double_click
        self.handlers[BlinkInterpreter.CLICK_HOLD] = self.handle_click_hold
        self.handlers[BlinkInterpreter.RELEASE] = self.handle_release
        self.handlers[BlinkInterpreter.RIGHT_CLICK_HOLD] = self.handle_right_click_hold
        self.handlers[BlinkInterpreter.RIGHT_RELEASE] = self.handle_right_release

    def step(self, speed, clock_divider):
        self.speed = speed
        clock_divider = self.handlers[self.current_state](clock_divider)
        return self.row, self.col, clock_divider

    def do_nothing(self, clkdiv):
        return clkdiv+1 if clkdiv < 3 else 0 

    def handle_nop(self, clkdiv):
        if clkdiv > 3:
          clkdiv = 0
          if self.col < self.maxcol:
            self.col += 1
          else:
            self.col = 0
        else:
          clkdiv += 1

        return clkdiv

    def handle_move_left(self, clkdiv):
        curx, cury = self.mouse.position()
        self.mouse.move(curx-self.speed, cury)
        return clkdiv+1 if clkdiv < 3 else 0

    def handle_move_right(self, clkdiv):
        curx, cury = self.mouse.position()
        self.mouse.move(curx+self.speed, cury)
        return clkdiv+1 if clkdiv<3 else 0

    def handle_move_up(self, clkdiv):
        curx, cury = self.mouse.position()
        self.mouse.move(curx, cury-self.speed)
        return clkdiv+1 if clkdiv<3 else 0

    def handle_move_down(self, clkdiv):
        curx, cury = self.mouse.position()
        self.mouse.move(curx, cury+self.speed)
        return clkdiv+1 if clkdiv<3 else 0

    def handle_goto_speed(self, clkdiv):
        self.row = 1
        self.col = 0
        self.current_state = BlinkInterpreter.NOP
        return clkdiv+1 if clkdiv<3 else 0

    def handle_goto_clicks(self, clkdiv):
        self.row = 2
        self.col = 0
        self.current_state = BlinkInterpreter.NOP
        return clkdiv+1 if clkdiv<3 else 0

    def handle_goto_drag(self, clkdiv):
        self.row = 3
        self.col = 0
        self.current_state = BlinkInterpreter.NOP
        return clkdiv+1 if clkdiv<3 else 0

    def handle_goto_movement(self, clkdiv):
        self.row = 0
        self.col = 0
        self.current_state = BlinkInterpreter.NOP
        return clkdiv+1 if clkdiv<3 else 0

    def handle_make_faster(self, clkdiv):
        if self.speed < 100:
          self.speed += 5
        return clkdiv+1 if clkdiv<3 else 0

    def handle_make_slower(self, clkdiv):
        if self.speed > 5:
          self.speed -= 5
        return clkdiv+1 if clkdiv<3 else 0

    def handle_click(self, clkdiv):
        curx, cury  = self.mouse.position()
        self.mouse.press(curx, cury, LEFT_BUTTON)
        self.mouse.release(curx, cury, LEFT_BUTTON)
        self.current_state = BlinkInterpreter.NOP
        return clkdiv+1 if clkdiv<3 else 0

    def handle_double_click(self, clkdiv):
        curx, cury  = self.mouse.position()
        self.mouse.press(curx, cury, LEFT_BUTTON)
        self.mouse.release(curx, cury, LEFT_BUTTON)
        self.mouse.press(curx, cury, LEFT_BUTTON)
        self.mouse.release(curx, cury, LEFT_BUTTON)
        self.current_state = BlinkInterpreter.NOP
        return clkdiv+1 if clkdiv<3 else 0

    def handle_right_click(self, clkdiv):
        curx, cury = self.mouse.position()
        self.mouse.press(curx, cury, RIGHT_BUTTON)
        self.mouse.release(curx, cury, RIGHT_BUTTON)
        self.current_state = BlinkInterpreter.NOP
        return clkdiv+1 if clkdiv<3 else 0

    def handle_right_double_click(self, clkdiv):
        curx, cury = self.mouse.position()
        self.mouse.press(curx, cury, RIGHT_BUTTON)
        self.mouse.release(curx, cury, RIGHT_BUTTON)
        self.mouse.press(curx, cury, RIGHT_BUTTON)
        self.mouse.release(curx, cury, RIGHT_BUTTON)
        self.current_state = BlinkInterpreter.NOP
        return clkdiv+1 if clkdiv<3 else 0

    def handle_click_hold(self, clkdiv):
        curx, cury = self.mouse.position()
        self.mouse.press(curx, cury, LEFT_BUTTON)
        self.current_state = BlinkInterpreter.NOP
        return clkdiv+1 if clkdiv<3 else 0

    def handle_release(self, clkdiv):
        curx, cury = self.mouse.position()
        self.mouse.release(curx, cury, LEFT_BUTTON)
        self.current_state = BlinkInterpreter.NOP
        return clkdiv+1 if clkdiv<3 else 0

    def handle_right_click_hold(self, clkdiv):
        curx, cury = self.mouse.position()
        self.mouse.press(curx, cury, RIGHT_BUTTON)
        self.current_state = BlinkInterpreter.NOP
        return clkdiv+1 if clkdiv<3 else 0

    def handle_right_release(self, clkdiv):
        curx, cury = self.mouse.position()
        self.mouse.release(curx, cury, RIGHT_BUTTON)
        self.current_state = BlinkInterpreter.NOP
        return clkdiv+1 if clkdiv<3 else 0

    def handle_eyeblink(self):
        if self.current_state == BlinkInterpreter.NOP:
          self.current_state = self.rowcol_to_state[(self.row,self.col)]
          #print "row, col = {0},{1}".format(self.row, self.col)
        else:
          self.current_state = BlinkInterpreter.NOP
          #print "STOP current operation"

