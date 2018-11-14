from wallaby import *
import constants as c
import movement as m
import utils as u

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~States~~~~~~~~~~~~~~~~~~~~~~~~

def BlackLeft():
    return(analog(c.LEFT_TOPHAT) > c.LEFT_TOPHAT_BW)

def NotBlackLeft():
    return(analog(c.LEFT_TOPHAT) < c.LEFT_TOPHAT_BW)

def BlackRight():
    return(analog(c.RIGHT_TOPHAT) > c.RIGHT_TOPHAT_BW)

def NotBlackRight():
    return(analog(c.RIGHT_TOPHAT) < c.RIGHT_TOPHAT_BW)

def BlackThird():
    return(analog(c.THIRD_TOPHAT) > c.THIRD_TOPHAT_BW)

def NotBlackThird():
    return(analog(c.THIRD_TOPHAT) < c.THIRD_TOPHAT_BW)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Basic Align Functions~~~~~~~~~~~~~~~~~~~~~~~~

def align_close():
# Aligns completely on the side of the line closest to the claw
    print "Starting align_close()"
    left_backwards_until_white()
    right_backwards_until_white()
    right_forwards_until_black()
    left_forwards_until_black()
    print "Aligned to close side of line\n"


def align_far(left_first = True):
# Aligns completely on the side of the line closest to the camera
    print "Starting align_far()"
    if left_first == True:
        right_forwards_until_white()
        left_forwards_until_white()
        left_backwards_until_black()
        right_backwards_until_black()
    else:
        left_forwards_until_white()
        right_forwards_until_white()
        right_backwards_until_black()
        left_backwards_until_black()
    print "Aligned to far side of line\n"


def align_far_safe():
# Aligns completely on the side of the line closest to the camera
    print "Starting align_far()"
    if u.not_bumped():
        right_forwards_until_white_safe()
    if u.not_bumped():
        left_forwards_until_white_safe()
    if u.not_bumped():
        left_backwards_until_black_safe()
    if u.not_bumped():
        right_backwards_until_black_safe()
    print "Aligned to far side of line\n"


def left_backwards_until_white(time = 10000, starting_speed_left = 0, stop = True):
# Left motor goes back until the left tophat senses white
    print "Starting left_backwards_until_white()"
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER, starting_speed_left)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():
        pass
    if stop == True:
        m.deactivate_motors()


def right_backwards_until_white(time = 10000, starting_speed_right = 0, stop = True):
# Right motor goes back until right tophat senses white
    print "Starting right_backwards_until_white()"
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():
        pass
    if stop == True:
        m.deactivate_motors()


def left_backwards_until_black(time = 10000, starting_speed_left = 0, stop = True):
# Left motor goes back until left tophat senses black
    print "Starting left_backwards_until_black()"
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER, starting_speed_left)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        pass
    if stop == True:
        m.deactivate_motors()


def left_backwards_until_black_safe(time = 1500, starting_speed_left = 0, stop = True):
# Left motor goes back until left tophat senses black
    print "Starting left_backwards_until_black_safe()"
    m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER, starting_speed_left)
    sec = seconds() + time / 1000.0
    while u.not_bumped() and seconds() < sec and NotBlackLeft():
        pass
    if stop == True:
        m.deactivate_motors()


def right_backwards_until_black(time = 10000, starting_speed_right = 0, stop = True):
# Right motor goes back until right tophat senses black
    print "Starting right_backwards_until_black()"
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        pass
    if stop == True:
        m.deactivate_motors()


def right_backwards_until_black_safe(time = 10000, starting_speed_right = 0, stop = True):
# Right motor goes back until right tophat senses black
    print "Starting right_backwards_until_black_safe()"
    m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER, starting_speed_right)
    sec = seconds() + time / 1000.0
    while u.not_bumped() and seconds() < sec and NotBlackRight():
        pass
    if stop == True:
        m.deactivate_motors()


def left_forwards_until_black(time = 10000, starting_speed_left = 0, stop = True):
# Left motor goes forwards until right tophat senses black
    print "Starting left_forwards_until_black()"
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER, starting_speed_left)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        pass
    if stop == True:
        m.deactivate_motors()


def right_forwards_until_black(time = 10000, starting_speed_right = 0, stop = True):
# Right motor goes forwards until right tophat senses black
    print "Starting right_forwards_until_black()"
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        pass
    if stop == True:
        m.deactivate_motors()


def left_forwards_until_white(time = 10000, starting_speed_left = 0, stop = True):
# Left motor goes forwards until right tophat senses white
    print "Starting left_forwards_until_white()"
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER, starting_speed_left)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():
        pass
    if stop == True:
        m.deactivate_motors()


def left_forwards_until_white_safe(time = 1500, starting_speed_left = 0, stop = True):
# Left motor goes forwards until right tophat senses white
    print "Starting left_forwards_until_white_safe()"
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER, starting_speed_left)
    sec = seconds() + time / 1000.0
    while u.not_bumped() and seconds() < sec and BlackLeft():
        pass
    if stop == True:
        m.deactivate_motors()


def left_forwards_until_third_senses_black(time = 10000, starting_speed_left = 0, stop = True):
# Left motor goes forwards until right tophat senses white
    print "Starting left_forwards_until_third_senses_black()"
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER, starting_speed_left)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        pass
    if stop == True:
        m.deactivate_motors()


def left_forwards_until_third_senses_white(time = 10000, starting_speed_left = 0, stop = True):
# Left motor goes forwards until right tophat senses white
    print "Starting left_forwards_until_third_senses_white()"
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER, starting_speed_left)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackThird():
        pass
    if stop == True:
        m.deactivate_motors()


def left_backwards_until_third_senses_black(time = 10000, starting_speed_left = 0, stop = True):
# Left motor goes forwards until right tophat senses white
    print "Starting left_forwards_until_third_senses_black()"
    m.av(c.LEFT_MOTOR, -c.BASE_LM_POWER, starting_speed_left)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        pass
    if stop == True:
        m.deactivate_motors()


def left_backwards_until_third_senses_white(time = 10000, starting_speed_left = 0, stop = True):
# Left motor goes forwards until right tophat senses white
    print "Starting left_forwards_until_third_senses_white()"
    m.av(c.LEFT_MOTOR, -c.BASE_LM_POWER, starting_speed_left)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackThird():
        pass
    if stop == True:
        m.deactivate_motors()


def right_forwards_until_third_senses_black(time = 10000, starting_speed_right = 0, stop = True):
# Left motor goes forwards until right tophat senses white
    print "Starting left_forwards_until_third_senses_black()"
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        pass
    if stop == True:
        m.deactivate_motors()


def right_forwards_until_third_senses_white(time = 10000, starting_speed_right = 0, stop = True):
# Left motor goes forwards until right tophat senses white
    print "Starting left_forwards_until_third_senses_white()"
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackThird():
        pass
    if stop == True:
        m.deactivate_motors()


def right_backwards_until_third_senses_black(time = 10000, starting_speed_right = 0, stop = True):
# Left motor goes forwards until right tophat senses white
    print "Starting right_backwards_until_third_senses_black()"
    m.av(c.RIGHT_MOTOR, -c.BASE_RM_POWER, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        pass
    if stop == True:
        m.deactivate_motors()


def right_backwards_until_third_senses_white(time = 10000, starting_speed_right = 0, stop = True):
# Left motor goes forwards until right tophat senses white
    print "Starting right_backwards_until_third_senses_white()"
    m.av(c.RIGHT_MOTOR, -c.BASE_RM_POWER, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackThird():
        pass
    if stop == True:
        m.deactivate_motors()


def right_forwards_until_white(time = 10000, starting_speed_right = 0, stop = True):
# Right motor goes forwards until right tophat senses white
    print "Starting right_forwards_until_white()"
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():
        pass
    if stop == True:
        m.deactivate_motors()


def right_forwards_until_white_safe(time = 1500, starting_speed_right = 0, stop = True):
    print "Starting right_forwards_until_white_safe()"
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER, starting_speed_right)
    sec = seconds() + time / 1000.0
    while u.not_bumped() and seconds() < sec and BlackRight():
        pass
    if stop == True:
        m.deactivate_motors()


def left_point_turn_until_black(time = 10000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting left_point_turn_until_black()"
    m.activate_motors(-1 * c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        pass
    if stop == True:
        m.deactivate_motors()


def left_point_turn_until_black_after(time = 10000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting left_point_turn_until_black_after(" + str(time) + ")"
    m.activate_motors(-1 * c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    msleep(time)
    while NotBlackLeft():
        pass
    if stop == True:
        m.deactivate_motors()


def left_point_turn_until_white(time = 10000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting left_point_turn_until_white()"
    m.activate_motors(-1 * c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():
        pass
    if stop == True:
        m.deactivate_motors()


def left_point_turn_until_right_senses_black(time = 10000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting left_point_turn_until_right_senses_black()"
    m.activate_motors(-1 * c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        pass
    if stop == True:
        m.deactivate_motors()


def left_point_turn_until_right_senses_white(time = 10000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting left_point_turn_until_right_senses_white()"
    m.activate_motors(-1 * c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():
        pass
    if stop == True:
        m.deactivate_motors()
 

def right_point_turn_until_left_senses_black(time = 10000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting right_point_turn_until_left_senses_black()"
    m.activate_motors(c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        pass
    if stop == True:
        m.deactivate_motors()


def right_point_turn_until_left_senses_white(time = 10000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting right_point_turn_until_left_senses_white()"
    m.activate_motors(c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():
        pass
    if stop == True:
        m.deactivate_motors()


def right_point_turn_until_black(time = 10000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting right_point_turn_until_black()"
    m.activate_motors(c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        pass
    if stop == True:
        m.deactivate_motors()


def right_point_turn_until_black_after(time = 10000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting right_point_turn_until_black_after(" + str(time) + ")"
    m.activate_motors(c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    msleep(time)  # Do a normal turn for "time" ms before checking for black
    while NotBlackRight():
        pass
    if stop == True:
        m.deactivate_motors()


def right_point_turn_until_white(time = 10000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting right_point_turn_until_white()"
    m.activate_motors(c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():
        pass
    if stop == True:
        m.deactivate_motors()


def right_forwards_until_left_senses_black(time = 10000, starting_speed_right = 0, stop = True):
    print "Starting right_forwards_until_left_senses_black()"
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        pass
    if stop == True:
        m.deactivate_motors()


def right_forwards_until_left_senses_white(time = 10000, starting_speed_right = 0, stop = True):
    print "Starting right_forwards_until_left_senses_white()"
    m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():
        pass
    if stop == True:
        m.deactivate_motors()


def left_forwards_until_right_senses_black(time = 10000, starting_speed_left = 0, stop = True):
    print "Starting left_forwards_until_right_senses_black()"
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER, starting_speed_left)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        pass
    if stop == True:
        m.deactivate_motors()


def left_forwards_until_right_senses_white(time = 10000, starting_speed_left = 0, stop = True):
    print "Starting left_forwards_until_right_senses_white()"
    m.av(c.LEFT_MOTOR, c.BASE_LM_POWER, starting_speed_left)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():
        pass
    if stop == True:
        m.deactivate_motors()


def left_point_turn_until_third_senses_black(time = 10000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting left_point_turn_until_third_senses_black()"
    m.activate_motors(-1 * c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        pass
    if stop == True:
        m.deactivate_motors()


def right_point_turn_until_third_senses_black(time = 10000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting right_point_turn_until_third_senses_black()"
    m.activate_motors(c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        pass
    if stop == True:
        m.deactivate_motors()


def left_point_turn_until_third_senses_white(time = 10000, lptutsw_left_power = -1 * c.BASE_LM_POWER, lptutsw_right_power = c.BASE_RM_POWER, stop = True):  # To-do: Add starting_speed_left = 0, starting_speed_right = 0
    print "Starting left_point_turn_until_third_senses_white()"
    m.activate_motors(-1 * c.BASE_LM_POWER, c.BASE_RM_POWER)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackThird():
        pass
    if stop == True:
        m.deactivate_motors()


def right_point_turn_until_third_senses_white(time = 10000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting right_point_turn_until_third_senses_white()"
    m.activate_motors(c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackThird():
        pass
    if stop == True:
        m.deactivate_motors()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Driving Align Functions~~~~~~~~~~~~~~~~~~~~~~~~

def snap_to_line_left():
    drive_through_line_third()
    left_point_turn_until_black()


def snap_to_line_right():
    drive_through_line_third()
    right_point_turn_until_black()


def drive_until_black_left(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting drive_until_black_left()"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        pass
    if stop == True:
        m.deactivate_motors()
    print "Line sensed, stopped driving\n"


def drive_until_black_right(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting drive_until_black_right()"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        pass
    if stop == True:
        m.deactivate_motors()
    print "Line sensed, stopped driving\n"


def drive_until_black_third(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting drive_until_black_third()"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        pass
    if stop == True:
        m.deactivate_motors()
    print "Line sensed, stopped driving\n"


def drive_until_black(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting drive_until_black()"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft() and NotBlackRight():
        pass
    if stop == True:
        m.deactivate_motors()
    print "Line sensed, stopped driving\n"


def drive_until_white_left(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting drive_until_white_left()"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():
        pass
    if stop == True:
        m.deactivate_motors()
    print "White sensed, stopped driving\n"


def drive_until_white_right(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting drive_until_white_right()"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():
        pass
    if stop == True:
        m.deactivate_motors()
    print "White sensed, stopped driving\n"


def drive_until_white_third(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting drive_until_white_third()"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackThird():
        pass
    if stop == True:
        m.deactivate_motors()
    print "White sensed, stopped driving\n"


def drive_until_white(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting drive_until_white()"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft() and BlackRight():
        pass
    if stop == True:
        m.deactivate_motors()
    print "White sensed, stopped driving\n"


def drive_through_line_left(time = 10000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    drive_until_black_left(time, starting_speed_left, starting_speed_right, False)
    drive_until_white_left(time, c.BASE_LM_POWER, c.BASE_RM_POWER, stop)


def drive_through_line_right(time = 10000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    drive_until_black_right(time, starting_speed_left, starting_speed_right, False)
    drive_until_white_right(time, c.BASE_LM_POWER, c.BASE_RM_POWER, stop)


def drive_through_line_third(time = 10000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    drive_until_black_third(time, starting_speed_left, starting_speed_right, False)
    drive_until_white_third(time, c.BASE_LM_POWER, c.BASE_RM_POWER, stop)


def drive_through_two_lines_third(time = 10000):  # Drives without stopping the motors in between
    drive_until_black_third(time, 0, 0, False)
    drive_until_white_third(time, c.BASE_LM_POWER, c.BASE_RM_POWER, False)
    drive_until_black_third(time, c.BASE_LM_POWER, c.BASE_RM_POWER, False)
    drive_until_white_third(time, c.BASE_LM_POWER, c.BASE_RM_POWER)


def backwards_until_black_left(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting backwards_until_black_left()"
    m.activate_motors(-1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        pass        
    if stop == True:
        m.deactivate_motors()
    print "Line sensed, stopped driving\n"


def backwards_until_black_right(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting backwards_until_black_right()"
    m.activate_motors(-1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        pass       
    if stop == True:
        m.deactivate_motors()
    print "Line sensed, stopped driving\n"


def backwards_until_black_third(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting backwards_until_black_third()"
    m.activate_motors(-1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight() and NotBlackLeft():
        pass
    print "Line sensed, stopped driving\n"
    if stop == True:
        m.deactivate_motors()


def backwards_until_black_third_safe(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting backwards_until_black_third_safe()"
    m.activate_motors(-1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while u.not_bumped() and seconds() < sec and NotBlackRight() and NotBlackLeft():
        pass
    print "Line sensed, stopped driving\n"
    if stop == True:
        m.deactivate_motors()


def backwards_until_white_left(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting backwards_until_white_left()"
    m.activate_motors(-1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackLeft():
        pass
    if stop == True:
        m.deactivate_motors()
    print "White sensed, stopped driving\n"


def backwards_until_white_right(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting backwards_until_white_right()"
    m.activate_motors(-1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight():
        pass
    if stop == True:
        m.deactivate_motors()
    print "White sensed, stopped driving\n"


def backwards_until_white_third(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True):
    print "Starting backwards_until_white_third()"
    m.activate_motors(-1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and BlackRight() and BlackLeft():
        pass
    print "Line sensed, stopped driving\n"
    if stop == True:
        m.deactivate_motors()


def backwards_through_line_left(time = 10000):
    backwards_until_black_left(time, 0, 0, False)
    backwards_until_white_left(time, -1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER)


def backwards_through_two_lines_in_calibration(time = 1200):
    backwards_until_black_third(time, 0, 0, False)
    backwards_until_white_third(time, -1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, False)
    if c.IS_CLONE_BOT:
        backwards_until_black_left(time, -1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, False)
        # The need for this stems from a weird interaction. More testing is needed to discover the cause.
    backwards_until_white_left(time, -1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, False)
    backwards_until_black_left(time, -1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, False)
    backwards_until_white_left(time, -1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER)


def align_in_zone_safely():
    print "Starting align_in_zone_safely()"
    backwards_until_black_third_safe()
    align_far_safe()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Line Follow Functions~~~~~~~~~~~~~~~~~~~~~~~~


def lfollow_both(time, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow using both tophats until time is reached.
    print "Starting lfollow_both()\n"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if BlackRight() and BlackLeft():
            m.drive_no_print(30)
        elif BlackRight() and NotBlackLeft():
            mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
        elif NotBlackRight() and BlackLeft():
            mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        elif NotBlackRight and NotBlackRight():
            mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
            mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_left(time, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow with the left tophat until time is reached.
    print "Starting lfollow_left()\n"
    first_black = True
    first_white = True
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if first_black and BlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER, starting_speed_left)
            first_black = False
            first_white = True
        elif first_white and NotBlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER, starting_speed_right)
            first_black = True
            first_white = False
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_both_motors()


def lfollow_left_smooth(time, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow smoothly with the left tophat for time.
    print "Starting lfollow_left_smooth()\n"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if BlackLeft():
            mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
            mav(c.RIGHT_MOTOR, c.LFOLLOW_SMOOTH_RM_POWER)
        else:
            mav(c.LEFT_MOTOR, c.LFOLLOW_SMOOTH_LM_POWER)
            mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_left_smooth_amount(time, left_speed = c.BASE_LM_POWER, right_speed = c.BASE_RM_POWER, left_smooth_speed = c.LFOLLOW_SMOOTH_LM_POWER, right_smooth_speed = c.LFOLLOW_SMOOTH_RM_POWER, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# IGNORE THIS, ALSO WORK ON THIS LATER
    print "Starting lfollow_left_smooth_amount()\n"
    m.activate_motors(left_speed, right_speed, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if BlackLeft():
            mav(c.LEFT_MOTOR, left_speed)
            mav(c.RIGHT_MOTOR, right_smooth_speed)
        else:
            mav(c.LEFT_MOTOR, left_smooth_speed)
            mav(c.RIGHT_MOTOR, right_speed)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_left_until_right_senses_black(time, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow with the left tophat until right tophat senses black or time is reached.
    print "Starting lfollow_left_until_right_senses_black()\n"
    first_black = True
    first_white = True
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        if first_black and BlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER, starting_speed_left)
            first_black = False
            first_white = True
        elif first_white and NotBlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER, starting_speed_right)
            first_black = True
            first_white = False
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_left_until_right_senses_black_smooth(time = 10000, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow smoothly with the left tophat until right tophat senses black or time is reached.
    print "Starting lfollow_left_until_right_senses_black_smooth()\n"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        if  NotBlackLeft():
            mav(c.LEFT_MOTOR, c.LFOLLOW_SMOOTH_LM_POWER)
            mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        elif BlackLeft():
            mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
            mav(c.RIGHT_MOTOR, c.LFOLLOW_SMOOTH_RM_POWER)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_left_inside_line(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow with the left tophat inside the line until time is reached.
    print "Starting lfollow_left_inside_line()\n"
    first_black = True
    first_white = True
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if first_black and BlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER, starting_speed_right)
            first_black = False
            first_white = True
        elif first_white and NotBlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER, starting_speed_left)
            first_black = True
            first_white = False
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_left_inside_line_smooth(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow smoothly with the left tophat inside the line until time is reached.
    print "Starting lfollow_left_inside_line_smooth()\n"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if BlackLeft():
            mav(c.LEFT_MOTOR, c.LFOLLOW_SMOOTH_LM_POWER)
            mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        else:
            mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
            mav(c.RIGHT_MOTOR, c.LFOLLOW_SMOOTH_RM_POWER)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_left_inside_line_until_right_senses_black(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow with the left tophat inside the line until the right tophat senses black or time is reached.
    print "Starting lfollow_left_inside_line_until_right_senses_black()\n"
    first_black = True
    first_white = True
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        if first_black and BlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER, starting_speed_right)
            first_black = False
            first_white = True
        elif first_white and NotBlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER, starting_speed_left)
            first_black = True
            first_white = False
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_left_inside_line_until_right_senses_black_smooth(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow smoothly with the left tophat inside the line until the right tophat senses black or time is reached.
    print "Starting lfollow_left_inside_line_until_right_senses_black_smooth()\n"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        if  NotBlackLeft():
            mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
            mav(c.RIGHT_MOTOR, c.LFOLLOW_SMOOTH_RM_POWER)
        elif BlackLeft():
            mav(c.LEFT_MOTOR, c.LFOLLOW_SMOOTH_LM_POWER)
            mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_both_motors()


def lfollow_left_inside_line_until_right_senses_black_smooth_amount(time = 20000, left_speed = c.BASE_LM_POWER, right_speed = c.BASE_RM_POWER, left_smooth_speed = c.LFOLLOW_SMOOTH_LM_POWER, right_smooth_speed = c.LFOLLOW_SMOOTH_RM_POWER, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# IGNORE THIS, ALSO WORK ON THIS LATER
    print "Starting lfollow_left_inside_line_until_right_senses_black_smooth_amount()\n"
    m.activate_motors(left_speed, right_speed, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        if  NotBlackLeft():
            mav(c.LEFT_MOTOR, left_speed)
            mav(c.RIGHT_MOTOR, right_smooth_speed)
        elif BlackLeft():
            mav(c.LEFT_MOTOR, left_smooth_speed)
            mav(c.RIGHT_MOTOR, right_speed)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_left_until_third_senses_black(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow with the left tophat until the third tophat senses black or the time is reached.
    print "Starting lfollow_left_until_third_senses_black()\n"
    first_black = True
    first_white = True
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        if first_black and BlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER, starting_speed_left)
            first_black = False
            first_white = True
        elif first_white and NotBlackLeft():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER, starting_speed_right)
            first_black = True
            first_white = False
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_left_until_third_senses_black_smooth(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow smoothly with the left tophat until the third tophat senses black or the time is reached.
    print "Starting lfollow_left_until_third_senses_black_smooth()\n"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        if  NotBlackLeft():
            mav(c.LEFT_MOTOR, c.LFOLLOW_SMOOTH_LM_POWER)
            mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        elif BlackLeft():
            mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
            mav(c.RIGHT_MOTOR, c.LFOLLOW_SMOOTH_RM_POWER)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_right(time, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow with the right tophat until time is reached.
    print "Starting lfollow_right()\n"
    first_black = True
    first_white = True
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if first_black and BlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER, starting_speed_right)
            first_black = False
            first_white = True
        elif first_white and NotBlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER, starting_speed_left)
            first_black = True
            first_white = False
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_right_smooth(time, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow smoothly with the right tophat until time is reached.
    print "Starting lfollow_right_smooth()\n"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if BlackRight():
            mav(c.LEFT_MOTOR, c.LFOLLOW_SMOOTH_LM_POWER)
            mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        elif NotBlackRight():
            mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
            mav(c.RIGHT_MOTOR, c.LFOLLOW_SMOOTH_RM_POWER)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_right_until_left_senses_black(time, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow with the right tophat until left tophat senses black or time is reached.
    print "Starting lfollow_right_until_left_senses_black()\n"
    first_black = True
    first_white = True
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        if first_black and BlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER, starting_speed_right)
            first_black = False
            first_white = True
        elif first_white and NotBlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER, starting_speed_left)
            first_black = True
            first_white = False
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_right_until_left_senses_black_smooth(time = 30000, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):  # Must begin code while touching the line
# Line follow smoothly with the right tophat until left tophat senses black or time is reached.
    print "Starting lfollow_right_until_left_senses_black_smooth()\n"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        if BlackRight():
            mav(c.LEFT_MOTOR, c.LFOLLOW_SMOOTH_LM_POWER)
            mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        elif NotBlackRight():
            mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
            mav(c.RIGHT_MOTOR, c.LFOLLOW_SMOOTH_RM_POWER)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_right_until_left_senses_black_smooth_amount(time, left_speed = c.BASE_LM_POWER, right_speed = c.BASE_RM_POWER, left_smooth_speed = c.LFOLLOW_SMOOTH_LM_POWER, right_smooth_speed = c.LFOLLOW_SMOOTH_RM_POWER, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):  # Must begin code while touching the line
# IGNORE THIS, ALSO WORK ON THIS LATER
    print "Starting lfollow_right_until_left_senses_black_smooth_amount()\n"
    m.activate_motors(left_speed, right_speed, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        if BlackRight():
            mav(c.LEFT_MOTOR, left_smooth_speed)
            mav(c.RIGHT_MOTOR, right_speed)
        elif NotBlackRight():
            mav(c.LEFT_MOTOR, left_speed)
            mav(c.RIGHT_MOTOR, right_smooth_speed)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_right_inside_line(time, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow with the right tophat inside the line until time is reached.
    print "Starting lfollow_right_inside_line()\n"
    first_black = True
    first_white = True
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if first_black and BlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER, starting_speed_left)
            first_black = False
            first_white = True
        elif first_white and NotBlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER, starting_speed_right)
            first_black = True
            first_white = False
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_right_inside_line_smooth(time, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow smoothly with the right tophat inside the line until time is reached.
    print "Starting lfollow_right_inside_line_smooth()\n"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if BlackRight():
            mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
            mav(c.RIGHT_MOTOR, c.LFOLLOW_SMOOTH_RM_POWER )
        elif NotBlackRight():
            mav(c.LEFT_MOTOR, c.LFOLLOW_SMOOTH_LM_POWER )
            mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_right_inside_line_until_left_senses_black(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow with the right tophat inside the line until the left tophat senses black or time is reached.
    print "Starting lfollow_right_inside_line_until_left_senses_black()\n"
    first_black = True
    first_white = True
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        if first_black and BlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER, starting_speed_left)
            first_black = False
            first_white = True
        elif first_white and NotBlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER, starting_speed_right)
            first_black = True
            first_white = False
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_right_inside_line_until_left_senses_black_smooth(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow smoothly with the right tophat inside the line until the left tophat senses black or time is reached.
    print "Starting lfollow_right_inside_line_until_left_senses_black_smooth()\n"
    m.activate_motors(c.BASE_LM_POWER, c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        if BlackRight():
            mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
            mav(c.RIGHT_MOTOR, c.LFOLLOW_SMOOTH_RM_POWER)
        elif NotBlackRight():
            mav(c.LEFT_MOTOR, c.LFOLLOW_SMOOTH_LM_POWER)
            mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_right_inside_line_until_left_senses_black_smooth_amount(time = 20000, left_speed = c.BASE_LM_POWER, right_speed = c.BASE_RM_POWER, left_smooth_speed = c.LFOLLOW_SMOOTH_LM_POWER, right_smooth_speed = c.LFOLLOW_SMOOTH_RM_POWER, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# IGNORE THIS, THIS IS A WORKING COMMAND BUT IS CONVALUTED.
    print "Starting lfollow_right_inside_line_until_left_senses_black_smooth_amount()\n"
    m.activate_motors(left_speed, right_speed, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackLeft():
        if BlackRight():
            mav(c.LEFT_MOTOR, left_speed)
            mav(c.RIGHT_MOTOR, right_smooth_speed)
        elif NotBlackRight():
            mav(c.LEFT_MOTOR, left_smooth_speed)
            mav(c.RIGHT_MOTOR, right_speed)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_right_until_third_senses_black(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow with the right tophat until the third tophat senses black or time is reached.
    print "Starting lfollow_right_until_third_senses_black()\n"
    first_black = True
    first_white = True
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        if first_black and BlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, c.BASE_RM_POWER, starting_speed_right)
            first_black = False
            first_white = True
        elif first_white and NotBlackRight():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, c.BASE_LM_POWER, starting_speed_left)
            first_black = True
            first_white = False
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_right_until_third_senses_black_smooth(time = 20000, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow smoothly with the right tophat until the third tophat senses black or time is reached.
    print "Starting lfollow_right_until_third_senses_black_smooth()\n"
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackThird():
        if BlackRight():
            mav(c.LEFT_MOTOR, c.LFOLLOW_SMOOTH_LM_POWER)
            mav(c.RIGHT_MOTOR, c.BASE_RM_POWER)
        elif NotBlackRight():
            mav(c.LEFT_MOTOR, c.BASE_LM_POWER)
            mav(c.RIGHT_MOTOR, c.LFOLLOW_SMOOTH_RM_POWER)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_backwards(time, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow backwards with the third tophat until time is reached.
    print "Starting lfollow_backwards()\n"
    first_black = True
    first_white = True
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if first_black and BlackThird():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER, starting_speed_right)
            first_black = False
            first_white = True
        elif first_white and NotBlackThird():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER, starting_speed_left)
            first_black = True
            first_white = False
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_backwards_smooth(time, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow backwards smoothly with the third tophat until time is reached.
    print "Starting lfollow_backwards_smooth()\n"
    m.activate_motors(-1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if BlackThird():
            mav(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
            mav(c.RIGHT_MOTOR, -1 * c.LFOLLOW_SMOOTH_RM_POWER)
        elif NotBlackThird():
            mav(c.LEFT_MOTOR, -1 * c.LFOLLOW_SMOOTH_LM_POWER)
            mav(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_both_motors()


def lfollow_backwards_inside_line(time, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow backwards with the third tophat inside the line until time is reached.
    print "Starting lfollow_backwards_inside_line()\n"
    first_black = True
    first_white = True
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if first_black and BlackThird():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER, starting_speed_left)
            first_black = False
            first_white = True
        elif first_white and NotBlackThird():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER, starting_speed_right)
            first_black = True
            first_white = False
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_backwards_inside_line_smooth(time, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow backwards smoothly with the third tophat inside the line until time is reached.
    print "Starting lfollow_backwards_inside_line_smooth()\n"
    m.activate_motors(-1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec:
        if BlackThird():
            mav(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
            mav(c.RIGHT_MOTOR, -1 * c.LFOLLOW_SMOOTH_RM_POWER)
        elif NotBlackThird():
            mav(c.LEFT_MOTOR, -1 * c.LFOLLOW_SMOOTH_LM_POWER)
            mav(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_backwards_inside_line_until_right_senses_black(time, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow backwards with the third tophat inside the line until the right tophat senses black or time is reached.
    print "Starting lfollow_backwards_inside_line_until_right_senses_black()\n"
    first_black = True
    first_white = True
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        if first_black and BlackThird():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER, starting_speed_left)
            first_black = False
            first_white = True
        elif first_white and NotBlackThird():
            mav(c.LEFT_MOTOR, 0)
            mav(c.RIGHT_MOTOR, 0)
            m.av(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER, starting_speed_right)
            first_black = True
            first_white = False
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()


def lfollow_backwards_inside_line_until_right_senses_black_smooth(time, starting_speed_left = 0, starting_speed_right = 0, stop = True, refresh_rate = c.LFOLLOW_REFRESH_RATE):
# Line follow backwards smoothly with the third tophat inside the line until the right tophat senses black or time is reached.
    print "Starting lfollow_backwards_inside_line_until_right_senses_black_smooth()\n"
    m.activate_motors(-1 * c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, starting_speed_left, starting_speed_right)
    sec = seconds() + time / 1000.0
    while seconds() < sec and NotBlackRight():
        if BlackThird():
            mav(c.LEFT_MOTOR, -1 * c.BASE_LM_POWER)
            mav(c.RIGHT_MOTOR, -1 * c.LFOLLOW_SMOOTH_RM_POWER)
        elif NotBlackThird():
            mav(c.LEFT_MOTOR, -1 * c.LFOLLOW_SMOOTH_LM_POWER)
            mav(c.RIGHT_MOTOR, -1 * c.BASE_RM_POWER)
        msleep(refresh_rate)
    if stop == True:
        m.deactivate_motors()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Debug~~~~~~~~~~~~~~~~~~~~~~~~

def debug_right_tophat():
    if BlackRight():
        print "Right tophat senses black: " + str(analog(c.RIGHT_TOPHAT))
    elif NotBlackRight():
        print "Right tophat see white: " + str(analog(c.RIGHT_TOPHAT))
    else:
        print "Error in defining BlackRight and NotBlackRight"
        exit(86)


def debug_left_tophat():
    if BlackLeft():
        print "Left tophat senses black: " + str(analog(c.LEFT_TOPHAT))
    elif NotBlackLeft():
        print "Left tophat senses white: " + str(analog(c.LEFT_TOPHAT))
    else:
        print "Error in defining BlackLeft and NotBlackLeft"
        exit(86)