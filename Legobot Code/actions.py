# The bulk of commands should go here

from wallaby import *
import constants as c
import movement as m
import linefollow as f
import webcam as w

crate_zone = 30  # In place for ease of GitHub compilation.
botguy_zone = 30  # Ditto to above.

def get_crates():
    print "Starting get_crates()"
    print "Bot in starting box\n"
    f.drive_through_two_lines_third()
    f.right_point_turn_until_black()
    f.lfollow_right_until_left_senses_black_smooth_amount(.5, c.BASE_LM_POWER, c.BASE_RM_POWER, int (.5 * c.BASE_LM_POWER), int (.5 * c.BASE_RM_POWER), 0, 0, False)
    f.lfollow_right_until_left_senses_black_smooth_amount(.5, c.BASE_LM_POWER, c.BASE_RM_POWER, int (.7 * c.BASE_LM_POWER), int (.7 * c.BASE_RM_POWER), c.BASE_LM_POWER, c.BASE_RM_POWER, False)
    f.lfollow_right_until_left_senses_black_smooth_amount(10, c.BASE_LM_POWER, c.BASE_RM_POWER, int (.9 * c.BASE_LM_POWER), int (.9 * c.BASE_RM_POWER), c.BASE_LM_POWER, c.BASE_RM_POWER, False)
    print "Bot on center tee\n"
    if c.IS_MAIN_BOT:
        m.drive_tics(1007, c.BASE_LM_POWER, c.BASE_RM_POWER)
    else:  # Clone bot
        m.drive_tics(1120, c.BASE_LM_POWER, c.BASE_RM_POWER)
    f.right_point_turn_until_third_senses_white(10, 0, 0, False)
    f.right_point_turn_until_third_senses_black(10, c.BASE_LM_POWER, -1 * c.BASE_RM_POWER)
    f.left_backwards_until_black()
    f.right_backwards_until_black()
    m.open_claw()
    m.arm_slow(c.ARM_DOWN_POS)
    m.claw_slow(c.CLAW_LESS_OPEN_POS)
    m.backwards(1400)
    print "Bot driving backwards to get crates\n"
    m.close_claw()
    print "\n\nFinished getting crates\n\n"


def approach_t():
    print "Starting approach_t()"
    f.right_point_turn_until_left_senses_black()
    f.lfollow_left_inside_line_until_right_senses_black_smooth(15, 0, 0, False)
    f.drive_through_line_left(2, c.BASE_LM_POWER, c.BASE_RM_POWER)
    f.align_far()
    print "The robot has reached the 'T'"


def put_crates_in_correct_zone():
    approach_t()
    w.check_zones_full()
    deliver_first_crate()
    deliver_second_crate()


def deliver_first_crate():
    print "Starting first_crate_delivery()"
    m.drive(500)
    if crate_zone == c.LEFT:
        print "Starting deliver_left()"
        f.snap_to_line_left()
        f.lfollow_left_until_right_senses_black_smooth(13, c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        f.lfollow_left_smooth(1, c.BASE_LM_POWER, c.BASE_RM_POWER)
        f.right_point_turn_until_left_senses_white(10, 0, 0, False)
        f.right_point_turn_until_left_senses_black(10, c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, False)
        f.right_point_turn_until_left_senses_white(10, c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, False)
        f.right_point_turn_until_left_senses_black(10, c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, False)
        f.right_point_turn_until_left_senses_white(10, c.BASE_LM_POWER, -1 * c.BASE_RM_POWER)
        f.lfollow_left_until_right_senses_black_smooth(7)
        if c.IS_MAIN_BOT:
            f.right_point_turn_until_black_after(c.RIGHT_TURN_TIME, 0, 0, False)
            f.right_point_turn_until_white(1, c.BASE_LM_POWER, -1 * c.BASE_RM_POWER)
        else:  # Clone bot
            f.right_point_turn_until_black_after(c.RIGHT_TURN_TIME)
    elif crate_zone == c.MIDDLE:
        print "Starting deliver_middle()"
        f.snap_to_line_right()
        f.lfollow_right_until_left_senses_black_smooth(13, c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        f.lfollow_right_smooth(1, c.BASE_LM_POWER, c.BASE_RM_POWER)
        f.left_point_turn_until_right_senses_white(10, 0, 0, False)
        f.left_point_turn_until_right_senses_black(10, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        f.left_point_turn_until_right_senses_white(10, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        f.left_point_turn_until_right_senses_black(10, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        f.left_point_turn_until_right_senses_white(10, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER)
        f.lfollow_right_until_left_senses_black_smooth(7)
        f.drive_until_white_left()
        f.right_forwards_until_left_senses_black(10, 0, False)
        f.right_forwards_until_left_senses_white(10, c.BASE_RM_POWER)
        f.lfollow_left_inside_line_until_right_senses_black_smooth(10, 0, 0, False)
        #f.left_forwards_until_black()
        f.drive_until_white_right(2, c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        if c.IS_MAIN_BOT:
            f.lfollow_left_inside_line_smooth(2.5, c.BASE_LM_POWER, c.BASE_RM_POWER)
        else:  # Clone bot
            f.lfollow_left_inside_line_smooth(2.7, c.BASE_LM_POWER, c.BASE_RM_POWER)
        m.turn_left()
        f.align_in_zone_safely()
        f.drive_through_line_third(10, 0, 0, False)
        m.drive(700, c.BASE_LM_POWER, c.BASE_RM_POWER, c.BASE_LM_POWER, c.BASE_RM_POWER)
    elif crate_zone == c.RIGHT:
        print "Starting deliver_right()"
        f.snap_to_line_right()
        f.lfollow_right_until_left_senses_black_smooth(13, c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        f.lfollow_right_smooth(1, c.BASE_LM_POWER, c.BASE_RM_POWER)
        f.left_point_turn_until_right_senses_white(10, 0, 0, False)
        f.left_point_turn_until_right_senses_black(10, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        f.left_point_turn_until_right_senses_white(10, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        f.left_point_turn_until_right_senses_black(10, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        f.left_point_turn_until_right_senses_white(10, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER)
        f.lfollow_right_until_left_senses_black_smooth(7)
        f.left_point_turn_until_black_after(c.LEFT_TURN_TIME, 0, 0, False)
        f.left_point_turn_until_white(1, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER)
        m.backwards(200)
    m.arm_slow(c.ARM_DOWN_POS)
    msleep(300)  # This pause helps keep the second crate from tipping over
    m.claw_slow(c.CLAW_LARGE_OPEN_POS)
    m.arm_slow(c.ARM_PUSH_CRATE_POS, 2, 1)
    m.backwards(500)
    print "First crate delivered\n\n"


def deliver_second_crate():
    print "Starting second_crate_delivery()"
    m.drive(250)
    m.arm_slow(c.ARM_SECOND_CRATE_GRAB_POS, 2, 1)
    m.backwards(100)
    m.claw_slow(c.CLAW_SECOND_CRATE_GRAB_POS, 3, 1)
    m.lift_arm(c.ARM_SECOND_CRATE_UP_POS)
    m.wait(100)
    if crate_zone == c.LEFT:
        f.left_point_turn_until_black()
        if c.IS_MAIN_BOT:
            f.lfollow_left_smooth_amount(.7, c.BASE_LM_POWER, c.BASE_RM_POWER, int (.5 * c.BASE_LM_POWER), int (.5 * c.BASE_RM_POWER), 0, 0, False)
            f.lfollow_left_smooth(.8, c.BASE_LM_POWER, c.BASE_RM_POWER)
        else:  # Clone bot
            f.lfollow_left_smooth(1.5)
        f.left_point_turn_until_right_senses_black()
        f.lfollow_right_inside_line_until_left_senses_black_smooth_amount(1, c.BASE_LM_POWER, c.BASE_RM_POWER, int (.4 * c.BASE_LM_POWER), int (.4 * c.BASE_RM_POWER), 0, 0, False)
        f.lfollow_right_inside_line_until_left_senses_black_smooth(10, 0, 0, False)
        m.drive(150, c.BASE_LM_POWER, c.BASE_RM_POWER, c.BASE_LM_POWER, c.BASE_RM_POWER)
        m.turn_right()
        f.align_in_zone_safely()
    elif crate_zone == c.MIDDLE:
        f.right_point_turn_until_black()
        f.lfollow_right_smooth(1.5)
        f.right_point_turn_until_left_senses_black()
        f.lfollow_left_inside_line_until_right_senses_black_smooth_amount(1, c.BASE_LM_POWER, c.BASE_RM_POWER, int (.4 * c.BASE_LM_POWER), int (.4 * c.BASE_RM_POWER), 0, 0, False)
        f.lfollow_left_inside_line_until_right_senses_black_smooth(10, 0, 0, False)
        m.drive(180, c.BASE_LM_POWER, c.BASE_RM_POWER, c.BASE_LM_POWER, c.BASE_RM_POWER)
        f.right_point_turn_until_black(5, 0, 0, False)
        f.right_point_turn_until_white(5, c.BASE_LM_POWER, -1* c.BASE_RM_POWER, False)
        f.right_point_turn_until_black(5, c.BASE_LM_POWER, -1* c.BASE_RM_POWER, False)
        f.right_point_turn_until_left_senses_black(5, c.BASE_LM_POWER, -1* c.BASE_RM_POWER, False)
        m.turn_right(c.RIGHT_TURN_TIME, c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, c.BASE_LM_POWER, -1 * c.BASE_RM_POWER)
        f.align_in_zone_safely()
    elif crate_zone == c.RIGHT:
        f.drive_until_white_third(10, 0, 0, False)
        m.drive(300, c.BASE_LM_POWER, c.BASE_RM_POWER, c.BASE_LM_POWER, c.BASE_RM_POWER)
        f.right_point_turn_until_black()
        f.lfollow_right(3)
        f.right_point_turn_until_left_senses_black()
        f.lfollow_left_inside_line_until_right_senses_black_smooth_amount(2, c.BASE_LM_POWER, c.BASE_RM_POWER, int (.4 * c.BASE_LM_POWER), int (.4 * c.BASE_RM_POWER), 0, 0, False)
        f.lfollow_left_inside_line_until_right_senses_black_smooth(10, c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        m.drive(200, c.BASE_LM_POWER, c.BASE_RM_POWER, c.BASE_LM_POWER, c.BASE_RM_POWER)
        m.turn_left()
        f.align_in_zone_safely()
    f.drive_through_line_third(10, 0, 0, False)
    m.drive(800, c.BASE_LM_POWER, c.BASE_RM_POWER, c.BASE_LM_POWER, c.BASE_RM_POWER)
    m.arm_slow(c.ARM_SECOND_CRATE_DEPOSIT_POS, 2, 1)
    m.claw_slow(c.CLAW_LARGE_OPEN_POS, 3, 1)
    m.arm_slow(c.ARM_PUSH_CRATE_POS, 2, 1)
    m.backwards(600)
    msleep(10)
    m.drive(200)
    m.arm_slow(c.ARM_HIGH_POS, 2, 1)
    print "Second crate delivered\n\n"


def get_botguy():
    print "Starting get_botguy()"
    if crate_zone == c.LEFT:
        print "I'm in the left zone and going to botguy"
        f.drive_through_line_left()  # Bot on middle line
        f.snap_to_line_left()
        f.lfollow_left_until_right_senses_black_smooth(20, 0, 0, False)
        f.drive_until_white(5, c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        f.lfollow_left_until_third_senses_black_smooth(5, c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        m.drive_tics(300, c.BASE_LM_POWER, c.BASE_RM_POWER)
        f.left_point_turn_until_third_senses_white(5 * c.LEFT_TURN_TIME, 0, 0)
    elif crate_zone == c.MIDDLE:
        print "I'm in the middle zone and going to botguy"
        m.turn_right()
        m.drive(1500)
        m.turn_left()
        f.drive_through_line_left()  # Bot on middle line
        f.align_far()
        f.snap_to_line_left()
        f.lfollow_left_until_right_senses_black_smooth(20, 0, 0, False)
        f.drive_until_white(5, c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        f.lfollow_left_until_third_senses_black_smooth(5, c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        m.drive_tics(300, c.BASE_LM_POWER, c.BASE_RM_POWER)
        f.left_point_turn_until_third_senses_white(5 * c.LEFT_TURN_TIME, 0, 0)
    elif crate_zone == c.RIGHT:
        print "I'm in the right zone and going to botguy"
        f.drive_through_line_left()  # Bot on middle line
        f.align_far()
        f.snap_to_line_right()
        f.lfollow_right_until_left_senses_black_smooth(20, 0, 0, False)
        if c.IS_MAIN_BOT:
            m.drive_tics(1007, c.BASE_LM_POWER, c.BASE_RM_POWER)
        else:  # Clone bot
            m.drive_tics(1120, c.BASE_LM_POWER, c.BASE_RM_POWER)
        f.right_point_turn_until_third_senses_white(5 * c.RIGHT_TURN_TIME / 1000, 0, 0, False)
        f.right_point_turn_until_third_senses_black(10, c.BASE_LM_POWER, -1 * c.BASE_RM_POWER)
    else:
        print "What zone am I in again? I have no idea. This is an error message"
        print "You already know I'm guessing it's in that right zone tho\n"
        exit(86)
    f.left_backwards_until_black()
    f.right_backwards_until_black()
    m.open_claw(c.CLAW_BOTGUY_OPEN_POS)
    m.arm_slow(c.ARM_DOWN_POS)
    #f.right_point_turn_until_third_senses_black()  # To do: Run more tests on this command
    f.lfollow_backwards_smooth(4.5)
    m.arm_slow(c.ARM_UP_POS)
    m.backwards(490)
    m.arm_slow(c.ARM_PUSH_CRATE_POS, 2, 1)
    m.close_claw(c.CLAW_CLOSE_POS)
    m.arm_slow(c.ARM_DOWN_POS)
    m.backwards(100)
    m.close_claw(c.BOTGUY_CLAW_CLOSE_POS)
    print "Finished getting botguy\n\n"


def put_botguy_on_side():
    print "Starting put_botguy_on_side()"
    approach_t()
    f.right_point_turn_until_third_senses_black(.2)
    f.drive_until_white_third(5, 0, 0, False)
    m.drive(300, c.BASE_LM_POWER, c.BASE_RM_POWER, c.BASE_LM_POWER, c.BASE_RM_POWER)
    f.right_point_turn_until_left_senses_black(10, 0, 0, False)
    f.right_point_turn_until_left_senses_white(10, c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, False)
    f.right_point_turn_until_left_senses_black(10, c.BASE_LM_POWER, -1 * c.BASE_RM_POWER)


def put_botguy_in_correct_zone():
    approach_t()
    f.right_point_turn_until_third_senses_black(.2)
    print "Starting deliver_botguy()"
    if botguy_zone == c.LEFT:
        print "Starting deliver_left()"
        f.snap_to_line_left()
        f.lfollow_left_until_right_senses_black_smooth(13, c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        f.lfollow_left_smooth(1, c.BASE_LM_POWER, c.BASE_RM_POWER)
        f.right_point_turn_until_left_senses_white(10, 0, 0, False)
        f.right_point_turn_until_left_senses_black(10, c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, False)
        f.right_point_turn_until_left_senses_white(10, c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, False)
        f.right_point_turn_until_left_senses_black(10, c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, False)
        f.right_point_turn_until_left_senses_white(10, c.BASE_LM_POWER, -1 * c.BASE_RM_POWER)
        f.lfollow_left_until_right_senses_black_smooth(7)
        f.right_point_turn_until_black_after(c.RIGHT_TURN_TIME, 0, 0, False)
        m.turn_right(int (c.RIGHT_TURN_TIME / 2), c.BASE_LM_POWER, -1 * c.BASE_RM_POWER, c.BASE_LM_POWER, -1 * c.BASE_RM_POWER)
        m.claw_slow(c.CLAW_LARGE_OPEN_POS, 3, 1)
    elif botguy_zone == c.MIDDLE:
        print "Starting deliver_middle()"
        f.drive_until_white_third(5, 0, 0, False)
        m.drive(300, c.BASE_LM_POWER, c.BASE_RM_POWER, c.BASE_LM_POWER, c.BASE_RM_POWER)
        f.left_point_turn_until_right_senses_black(10, 0, 0, False)
        f.left_point_turn_until_right_senses_white(10, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        f.left_point_turn_until_right_senses_black(10, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER)
        f.backwards_through_line_left()
        f.align_close()
        if False:  # crate_zone == c.LEFT:
            m.turn_right(int (c.RIGHT_TURN_TIME / 8))
            m.backwards(900)
            m.turn_right(int (c.RIGHT_TURN_TIME / 10))
        elif False:  # crate_zone == c.RIGHT:
            m.turn_left(int (c.LEFT_TURN_TIME / 8))
            m.backwards(900)
            m.turn_left(int (c.LEFT_TURN_TIME / 20))
        m.claw_slow(c.CLAW_LARGE_OPEN_POS, 3, 1)
        m.backwards(1000)
    elif botguy_zone == c.RIGHT:
        print "Starting deliver_right()"
        f.snap_to_line_right()
        f.lfollow_right_until_left_senses_black_smooth(13, c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        f.lfollow_right_smooth(1, c.BASE_LM_POWER, c.BASE_RM_POWER)
        f.left_point_turn_until_right_senses_white(10, 0, 0, False)
        f.left_point_turn_until_right_senses_black(10, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        f.left_point_turn_until_right_senses_white(10, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        f.left_point_turn_until_right_senses_black(10, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        f.left_point_turn_until_right_senses_white(10, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER)
        f.lfollow_right_until_left_senses_black_smooth(7)
        m.turn_left(c.LEFT_TURN_TIME, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        m.turn_left(c.LEFT_TURN_TIME, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER, False)
        m.turn_left(int (c.LEFT_TURN_TIME / 2), -1 * c.BASE_LM_POWER, c.BASE_RM_POWER, -1 * c.BASE_LM_POWER, c.BASE_RM_POWER)
        m.claw_slow(c.CLAW_LARGE_OPEN_POS, 3, 1)
    m.arm_slow(c.ARM_PUSH_CRATE_POS, 3, 1)
    m.backwards(300)
    print "Botguy delivered\n\n" 

