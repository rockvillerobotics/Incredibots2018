#!/usr/bin/env python2
import os
import sys
from wallaby import *
import constants as c
import actions as a
import movement as m
import linefollow as f
import utils as u

def main():
    print "Starting main()\n"
    u.setup()
    u.calibrate()
    a.only_first_three()
    # m.backwards(1300)
    m.turn_right()
    m.backwards(4500)
    u.sd()


    a.get_low_poms_cheeky()
    a.get_frisbee()
    a.get_mid_poms()
    a.get_high_poms_cheeky()
    a.get_farther_high_poms() 
    a.get_farther_mid_poms()
    a.get_farther_low_poms()
    print "Finished main\n"
    u.shutdown(86)
    

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
