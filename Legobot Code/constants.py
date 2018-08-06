#   When possible, make values into constants so they can be easily changed throughout the code at once. 
#   Constants are subject to change, so make sure to check the values to be certain that they are right.
#   Note: All constant timings are assumed to be in milliseconds unless otherwise specified.

from wallaby import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Clone Bot Definitions~~~~~~~~~~~~~~~~~~~~~~~~
def MAIN_BOT_CHANNEL_COUNT(): 
    return(get_channel_count() == 3)

def CLONE_BOT_CHANNEL_COUNT():
    return(get_channel_count() == 4)  # If the bot has 4 camera channels, then it is the clone bot.

IS_MAIN_BOT = right_button() == 0 and MAIN_BOT_CHANNEL_COUNT() or left_button() == 1  # Left button for main

IS_CLONE_BOT = left_button() == 0 and CLONE_BOT_CHANNEL_COUNT() or right_button() == 1  # Right button for clone

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Motors, Servos, and Sensors~~~~~~~~~~~~~~~~~~~~~~~~

if IS_MAIN_BOT:
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Motors~~~~~~~~~~~~~~~~~~~~~~~~

    # Motor Ports
    LEFT_MOTOR = 3
    RIGHT_MOTOR = 2

    # Base Motor Powers
    BASE_LM_POWER = 880
    BASE_RM_POWER = -900
    LFOLLOW_SMOOTH_LM_POWER = int (.7 * BASE_LM_POWER)
    LFOLLOW_SMOOTH_RM_POWER = int (.7 * BASE_RM_POWER)

    # Motor Timings
    RIGHT_TURN_TIME = 850  # Need to test turn timings periodically. They change as battery charge changes, or on new boards.
    LEFT_TURN_TIME = 850
    DEFAULT_DRIVE_TIME = 500
    DEFAULT_BACKWARDS_TIME = 500
    PIVOT_RIGHT_TURN_TIME = 3580  # Turns 180 degrees. Not currently used.
    PIVOT_LEFT_TURN_TIME = 3400  # Ditto above.
    MOVEMENT_REFRESH_RATE = 30

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Servos~~~~~~~~~~~~~~~~~~~~~~~~

    # Servo Limits
    MAX_SERVO_POS = 1900  # Cannot physically exceed 2047 or servo will break. Metal servos are more affected.
    MIN_SERVO_POS = 100  # Cannot physically exceed 0 or servo will break. Metal servos are more affected.
    SERVO_DELAY = 500  # Time needed to move a servo (need more testing to find a good value).

    # Arm Servo
    ARM_SERVO = 0 
    ARM_DOWN_POS = 1024  # Claw should be parallel to ground.
    ARM_UP_POS = 1306
    ARM_HIGH_POS = 1700
    ARM_PUSH_CRATE_POS = 1250  # Moves above pvc so crates can be pushed.
    ARM_SECOND_CRATE_GRAB_POS = 1500
    ARM_SECOND_CRATE_UP_POS = 1700
    ARM_SECOND_CRATE_DEPOSIT_POS = 1300

    # Claw Servo
    CLAW_SERVO = 3
    CLAW_LESS_OPEN_POS = 1269
    CLAW_OPEN_POS = 1200  # 720
    CLAW_LARGE_OPEN_POS = 1100  # 690
    CLAW_BOTGUY_OPEN_POS = 1269  # 817
    CLAW_PARALLEL_CLOSE_POS = 1530
    CLAW_CLOSE_POS = 1652  # 1070  # There should be a slight space between both prongs.
    CLAW_SECOND_CRATE_GRAB_POS = 1575  # 1150
    BOTGUY_CLAW_CLOSE_POS = 1630  # 1110

    # Starting Positions
    STARTING_ARM_POS = ARM_HIGH_POS
    STARTING_CLAW_POS = CLAW_OPEN_POS

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Sensors~~~~~~~~~~~~~~~~~~~~~~~~

    # Analog Ports
    LIGHT_SENSOR = 5
    LEFT_TOPHAT = 0
    RIGHT_TOPHAT = 1
    THIRD_TOPHAT = 4

    # Analog Values
    LEFT_TOPHAT_BW = 200  # If more, black. If less, white.
    RIGHT_TOPHAT_BW = 200  # If more, black. If less, white.
    THIRD_TOPHAT_BW = 3000  # If more, black. If less, white.
    LFOLLOW_REFRESH_RATE = 30  # Default amount of time before tophats check their black/white status again.
    MAX_SENSOR_VALUE = 0
    MIN_SENSOR_VALUE = 900000 # This is only for PID line follow.

    # Digital Sensors
    BUMP_SENSOR = 0

    # Camera Colors
    YELLOW = 0
    GREEN = 2
    RED = 1

    # Camera Zones (From wallaby's perspective in center looking out)
    LEFT = -1
    MIDDLE = 0
    RIGHT = 1


else:  # Clone Bot ----------------------------------------------------------------------------------------------------------------
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Clone Motors~~~~~~~~~~~~~~~~~~~~~~~~

    # Clone Motor Ports
    LEFT_MOTOR = 3
    RIGHT_MOTOR = 2

    # Clone Base Motor Powers
    BASE_LM_POWER = 900  # 680 on plastic motor.
    BASE_RM_POWER = -900
    LFOLLOW_SMOOTH_LM_POWER = int (.7 * BASE_LM_POWER)
    LFOLLOW_SMOOTH_RM_POWER = int (.7 * BASE_RM_POWER)

    # Clone Motor Timings
    RIGHT_TURN_TIME = 900  # Need to test turn timings periodically. They change as battery charge changes, or on new boards.
    LEFT_TURN_TIME = 900  # 90 degrees
    DEFAULT_DRIVE_TIME = 500
    DEFAULT_BACKWARDS_TIME = 500
    PIVOT_RIGHT_TURN_TIME = 3900  # Turns 180 degrees. Not currently used.
    PIVOT_LEFT_TURN_TIME = 3900  # Ditto above.
    MOVEMENT_REFRESH_RATE = 30

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Clone Servos~~~~~~~~~~~~~~~~~~~~~~~~

    # Clone Servo Limits
    MAX_SERVO_POS = 1900  # Cannot physically exceed 2047 or servo will break. Metal servos are more affected.
    MIN_SERVO_POS = 100  # Cannot physically exceed 0 or servo will break. Metal servos are more affected.
    SERVO_DELAY = 500  # Time needed to move a servo (need more testing to find a good value).

    # Clone Arm Servo
    ARM_SERVO = 0 
    ARM_DOWN_POS = 1118  # Claw should be parallel to ground.
    ARM_UP_POS = 1400
    ARM_HIGH_POS = 1900
    ARM_PUSH_CRATE_POS = 1250  # Moves above pvc so crates can be pushed.
    ARM_SECOND_CRATE_GRAB_POS = 1600
    ARM_SECOND_CRATE_UP_POS = 1785
    ARM_SECOND_CRATE_DEPOSIT_POS = 1350

    # Clone Claw Servo
    CLAW_SERVO = 3
    CLAW_LESS_OPEN_POS = 1245
    CLAW_OPEN_POS = 1150
    CLAW_LARGE_OPEN_POS = 1100
    CLAW_BOTGUY_OPEN_POS = 1250
    CLAW_PARALLEL_CLOSE_POS = 1500
    CLAW_CLOSE_POS = 1652  # There should be a slight space between both prongs.
    CLAW_SECOND_CRATE_GRAB_POS = 1570
    BOTGUY_CLAW_CLOSE_POS = 1580

    # Clone Starting Positions
    STARTING_ARM_POS = ARM_HIGH_POS
    STARTING_CLAW_POS = CLAW_OPEN_POS  # 1010

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Clone Sensors~~~~~~~~~~~~~~~~~~~~~~~~

    # Clone Analog Ports
    LIGHT_SENSOR = 5
    LEFT_TOPHAT = 0
    RIGHT_TOPHAT = 1
    THIRD_TOPHAT = 4

    # Clone Analog Values
    LEFT_TOPHAT_BW = 1627 #1800  # If more, black. If less, white.
    RIGHT_TOPHAT_BW = 1783  # If more, black. If less, white.
    THIRD_TOPHAT_BW = 2121 # If more, black. If less, white.
    LFOLLOW_REFRESH_RATE = 30  # Default amount of time before tophats check their black/white status again.
    MAX_SENSOR_VALUE = 0
    MIN_SENSOR_VALUE = 900000 # This is only for PID line follow.

    # Clone Digital Sensors
    BUMP_SENSOR = 0

    # Clone Camera Colors
    YELLOW = 0
    GREEN = 2
    RED = 1

    # Clone Camera Zones (From wallaby's perspective in center looking out)
    LEFT = -1
    MIDDLE = 0
    RIGHT = 1
