from wallaby import *
import constants as c
import linefollow as f
import movement as m
import utils as u

#------------------------------------ Poms ------------------------

def collect_poms(msleep_time = 50, forwards_amount = 1000, amount = 1250): # Actual act of collecting poms once aligned
    m.backwards(amount)
    m.arm_slow(c.ARM_COLLECTION_POS)
    msleep(msleep_time)
    m.forwards(forwards_amount)


def get_low_poms(): # First pom set
    print "Starting get_low_poms()"
    m.arm_slow(c.ARM_UP_POS, 3, 1)
    f.backwards_through_line_lfcliff()
    f.backwards_through_line_lfcliff()
    f.align_close_fcliffs()
    collect_poms()


def get_low_poms_cheeky(): # First pom set
    print "Starting get_low_poms()"
    m.arm_slow(c.ARM_UP_POS, 3, 1)
    f.backwards_through_line_lfcliff()
    f.backwards_through_line_lfcliff()
    f.align_close_fcliffs()
    collect_poms(50, 0)
    f.forwards_until_black_lfcliff()
    m.backwards(150)


def get_frisbee():
    print "Starting get_frisbee()"
    m.arm_slow(c.ARM_UP_POS, 2, 1)
    m.backwards(900)
    m.arm_slow(c.ARM_FRISBEE_GRAB_POS, 2, 1)
    m.forwards(2000)
    m.arm_slow(c.ARM_FRISBEE_DROP_POS, 4, 1)
    m.turn_left(int(c.LEFT_TURN_TIME / 5))  # An 18 degree wiggle back and forth to shake frisbee loose
    m.turn_right(int(c.RIGHT_TURN_TIME / 5))
    m.backwards(1000)
    m.lift_arm(c.ARM_FRISBEE_FARTHER_DROP_POS)


def get_mid_poms(): # Second pom set
    print "Starting get_mid_poms()"
    f.forwards_until_black_lfcliff()
    f.align_close_fcliffs()
    m.arm_slow(c.ARM_UP_POS, 2, 1)
    m.turn_left()
    m.backwards(2680)
    m.turn_right()
    f.forwards_until_black_lfcliff()
    f.align_close_fcliffs()
    collect_poms()


def get_high_poms(): # Third pom set
    print "Starting get_high_poms()"
    f.forwards_until_line_fcliffs()
    f.align_close_cliffs()
    f.right_point_turn_until_lfcliff_senses_black()
    f.right_point_turn_until_lfcliff_senses_white()
    # m.turn_right()
    # f.left_point_turn_until_lfcliff_senses_black()  # How does it know it is on the right side of the line?
    f.lfollow_lfcliff_smooth_until_rfcliff_senses_black()
    m.backwards(1400)
    m.turn_left()
    f.backwards_through_line_lfcliff()
    f.align_close_fcliffs()
    collect_poms(50, 0)


def get_high_poms_cheeky():
    print "Starting get_high_poms_cheeky()"
    f.forwards_until_black_lfcliff()
    f.align_close_fcliffs()
    m.arm_slow(c.ARM_UP_POS, 2, 1)
    m.turn_right()
    m.forwards(2680)
    m.turn_left()
    f.forwards_until_black_lfcliff()
    f.align_close_fcliffs()
    collect_poms(10000)
    f.backwards_until_white_lfcliff()
    m.arm_slow(c.ARM_UP_POS, 2, 1)


def get_farther_high_poms():
    print "Starting get_farther_high_poms()"
    f.forwards_until_line_fcliffs()
    f.align_close_cliffs()
    m.arm_slow(c.ARM_UP_POS, 2, 1)
    f.right_point_turn_until_lfcliff_senses_black()
    f.right_point_turn_until_lfcliff_senses_white()
    f.lfollow_lfcliff_smooth_until_rfcliff_senses_black()
    f.forwards_until_white_rfcliff()
    f.right_point_turn_until_rfcliff_senses_black(2)
    f.right_point_turn_until_lfcliff_senses_black(2)
    f.right_point_turn_until_rfcliff_senses_white(2)
    f.right_point_turn_until_rfcliff_senses_black(2)
    f.backwards_until_black_lfcliff()
    # m.turn_right(int(0.5 * c.RIGHT_TURN_TIME), 2 * c.BASE_LM_POWER, -2 * c.BASE_RM_POWER)
    # m.turn_right(int(0.5 * c.RIGHT_TURN_TIME), 2 * c.BASE_LM_POWER, -2 * c.BASE_RM_POWER)
    m.backwards(1650)
    m.turn_right()
    f.forwards_until_line_fcliffs()
    f.align_close_fcliffs()
    collect_poms()


def get_farther_mid_poms():
    f.forwards_until_line_fcliffs()
    f.align_close_cliffs()
    m.arm_slow(c.ARM_UP_POS, 2, 1)
    f.right_point_turn_until_lfcliff_senses_black()
    f.right_point_turn_until_lfcliff_senses_white()
    f.lfollow_lfcliff_smooth(2)
    f.lfollow_lfcliff_smooth_until_right_depth_senses_object()
    m.forwards(1000)
    m.turn_left()
    f.backwards_through_line_lfcliff()
    f.align_close_fcliffs()
    collect_poms()


def get_farther_low_poms():
    f.forwards_until_line_fcliffs()
    f.align_close_cliffs()
    m.arm_slow(c.ARM_UP_POS, 2, 1)
    m.turn_right(int(c.RIGHT_TURN_TIME * 1.01))
    f.forwards_until_bump()
    m.backwards(200)
    m.turn_left()
    f.backwards_through_line_lfcliff()
    f.align_close_cliffs()
    collect_poms(50, 1000, 2100)


def only_first_three():
    get_low_poms()
    get_frisbee()
    get_mid_poms()
    get_high_poms_cheeky()
    