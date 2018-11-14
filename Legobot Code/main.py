#!/usr/bin/env python2
import os
import sys
from wallaby import *
import constants as c
import actions as a
import linefollow as f
import movement as m
import webcam as w
import utils as u

def main():
    print "Starting main()\n"
    u.setup()
    u.calibrate()
    a.get_crates()
    a.put_crates_in_correct_zone()
    a.get_botguy()
    a.put_botguy_on_side()
    u.shutdown()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
