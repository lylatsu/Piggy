#!/usr/bin python3
from collections import OrderedDict
from teacher import PiggyParent
import sys
import time

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 80
        self.RIGHT_DEFAULT = 80
        self.SAFE_DISTANCE = 300
        self.CLOSE_DISTANCE = 30
        self.MIDPOINT = 1525  # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)
        
    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "d": ("Dance", self.dance),
                "o": ("Obstacle count", self.obstacle_count),
                "s": ("Shy", self.shy),
                "f": ("Follow", self.follow),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''

    def dance(self):
        """A higher-ordered algorithm to make your robot dance"""
        if not self.safe_to_dance():
            return False # SHUT THE DANCE DOWN
        
        #lower-ordered example..
        
        for x in range(6):
            self.bunny_hop()
            self.the_twister()
            self.moonwalk()
            self.tango()
            self.boogie()
            self.quinnshuffle()
            self.spin
        self.stop()


    def bunny_hop(self):
        """small short forward movement"""
        for x in range(3):
            self.fwd()
            self.servo(1000) #swivel head
            time.sleep(.1)
            self.stop()
            self.fwd() #move forward
            time.sleep(.1)
            self.stop()
            self.fwd()
            time.sleep(.1)
            self.stop()

    def the_twister(self):
        """turn to the left 180 degress"""
        for x in range(2):
            self.turn_by_deg(-180)
            self.servo(2000)
            time.sleep(.3)
            self.stop()
            self.turn_by_deg(180)
            time.sleep(.3)
            self.stop()
    
    def moonwalk(self):
        """scoot straight back with head bob"""
        for x in range(3):
            self.back()
            self.servo(1000)
            time.sleep(.5)
            self.stop()
            self.turn_by_deg(-45)
            time.sleep(.5)
            self.turn_by_deg(45)
            self.stop()
        
            
    def safe_to_dance(self):
        """Does a 360 distance check and returns true if safe"""
        # check for all fail/early-termination conditions
        for x in range(4):
            if self.read_distance() < 300:
                print("NOT SAFE TO DANCE!")
                return False
            else:
                self.turn_by_deg(90)
        # after all checks have been done. We deduce it's safe
                print("SAFE TO DANCE!")
        return True

    def tango(self):
        """Forward and slow shimmy to the right and left"""
        for x in range(3):
            self.fwd()
            self.servo(1000) 
            time.sleep(.3)
            self.right()
            time.sleep(.3)
            self.left()
            self.servo(2000) #swivel head
            time.sleep(.3)
            self.fwd()
            time.sleep(.3)
            self.right() #boogie right
            time.sleep(.3)
            self.left() #boogie left
            time.sleep(.3)
            self.stop()

    def boogie(self):
        """smoothly glide back"""
        for x in range(4):
            self.back()
            self.servo(1000)
            time.sleep(.3)
            self.stop
            

    # thanks quinny for the shuffle
    def quinnshuffle(self):
        """head shake and backward scoot shimmy"""
        for x in range(12):
            self.right(primary=-60, counter=0)
            time.sleep(.1)
            self.left(primary=-60, counter=0)
            time.sleep(.1)
            self.stop

    def spin(self):
        """quick spin"""
        for x in range(6):
            self.turn_by_deg(360)
            time.sleep(.1)
            self.stop


    def shake(self):
        self.deg_fwd(360)
        time.sleep(.2)
        self.stop()
        
    
    def example_move(self):
        """this is an example dance move that should be replaced by student-created content"""
        self.right() # start rotating right
        time.sleep(1) # turn for a second
        self.stop() # stop
        self.servo(1000) # look right
        time.sleep(.25) # give your head time to move
        self.servo(2000) # look left

    def scan(self):
        """Sweep the servo and populate the scan_data dictionary"""
        for angle in range(self.MIDPOINT-350, self.MIDPOINT+350, 10):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()
        # sort the scan data for easier analysis
        self.scan_data = OrderedDict(sorted(self.scan_data.items()))

    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        # do a scan of the area in front of the robot
        count = 0
        for x in range(4):
            self.scan()
            for angle in self.scan_data:
            dist = self.scan_data[angle]
            if dist < self.SAFE_DISTANCE and not see_an_object:
                see_an_object = True
                count += 1
                print("I SEE SOMETHING!!")
            elif dist > self.SAFE_DISTANCE and see_an_object:
                see_an_object = False
                print("I guess the object ended")
                
            
            print("ANGLE: %d | DIST: %d" % (angle, dist))
            print("\nI saw %d objects" % count)
            self.turn_by_deg(90)
  
        # FIGURE OUT HOW MANY OBSTACLES THERE WERE
        see_an_object = False


    def quick_check(self):
        """Moves the servo to three angles and performs a distance check"""
        # loop three times and move the servo
        for ang in range(self.MIDPOINT - 100, self.MIDPOINT + 101, 100):
            self.servo(ang)
            time.sleep(.05)
            if self.read_distance() < self.SAFE_DISTANCE:
                return False
        # if the three-part check didn't freak out
        return True

    
    def turn_until_clear(self):
        """ Rotate right until no obstacle is seen """
        print("----TURNING UNTIL CLEAR!!!----")
        # make sure we're looking straight
        self.servo(self.MIDPOINT)
        while self.read_distance() < self.SAFE_DISTANCE:
            self.left(primary=40, counter=-40)
            time.sleep(.05)
        # stop motion before we end the method
        self.stop()
    
    def nav(self):
        """ Auto-pilot program """
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        while True:
            if not self.quick_check():
                self.stop()
                self.turn_until_clear()
            else:
                self.fwd()
        
        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict
        


###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  
