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
    # Put the command from actions you want to run here. 
    # Don't write out your entire command out here; it gets to cluttered.
    u.shutdown()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
