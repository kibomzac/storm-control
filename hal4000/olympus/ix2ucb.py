#!/usr/bin/python
#
# Olympus IX2-UCB filter wheel control
#
# Hazen 12/10
#

import halLib.RS232 as RS232
import time

class IX2UCB(RS232.RS232):
    def __init__(self, port = "COM4", baud = 9600):
        self.position = 0
        try:
            # open port
            RS232.RS232.__init__(self, port, None, baud, "\r", 0.05)

            # verify that we can talk to the filter wheel
            assert not(self.commWithResp("1LOG IN") == None)

        except:
            self.live = 0
            print "Failed to connect to the IX2-UCB controller at port", port

    def amMoving(self):
        resp = self.commWithResp("1MU?")
        if resp:
            position = resp[:-1]
            status = position.split(" ")[-1]
            if status == "X":
                return True
            else:
                return False
        else:
            print "IX2-UCB: Failed query motion status"

    def getPosition(self):
        resp = self.commWithResp("1MU?")
        if resp:
            position = resp[:-1]
            temp = position.split(" ")[-1]
            if temp == "X":
                print "IX2-UCB: Filter wheel is still moving"
                return 1
            else:
                self.position = int(temp)
                return self.position
        else:
            print "IX2-UCB: Failed to get filter wheel position"
            return 1

    def setPosition(self, position):
        if (position < 1):
            position = 1
        if (position > 6):
            position = 6
        self.commWithResp("1MU " + str(position))

#
# Testing
#

if __name__ == "__main__":
    ix2 = IX2UCB()

    print ix2.getPosition()
    ix2.setPosition(1)
    while ix2.amMoving():
        time.sleep(0.1)
    print ix2.getPosition()

    ix2.setPosition(3)
    while ix2.amMoving():
        time.sleep(0.1)
    print ix2.getPosition()

    ix2.setPosition(1)

#
# The MIT License
#
# Copyright (c) 2010 Zhuang Lab, Harvard University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

