"""
 ________         __            __                  _______             __                        _______               __              
/        |       /  |          /  |                /       \           /  |                      /       \             /  |             
$$$$$$$$/______  $$/   ______  $$ |  ______        $$$$$$$  |  ______  $$ |   __   ______        $$$$$$$  |  ______   _$$ |_    _______ 
   $$ | /      \ /  | /      \ $$ | /      \       $$ |__$$ | /      \ $$ |  /  | /      \       $$ |__$$ | /      \ / $$   |  /       |
   $$ |/$$$$$$  |$$ |/$$$$$$  |$$ |/$$$$$$  |      $$    $$<  $$$$$$  |$$ |_/$$/  $$$$$$  |      $$    $$< /$$$$$$  |$$$$$$/  /$$$$$$$/ 
   $$ |$$ |  $$/ $$ |$$ |  $$ |$$ |$$    $$ |      $$$$$$$  | /    $$ |$$   $$<   /    $$ |      $$$$$$$  |$$ |  $$ |  $$ | __$$      \ 
   $$ |$$ |      $$ |$$ |__$$ |$$ |$$$$$$$$/       $$ |__$$ |/$$$$$$$ |$$$$$$  \ /$$$$$$$ |      $$ |__$$ |$$ \__$$ |  $$ |/  |$$$$$$  |
   $$ |$$ |      $$ |$$    $$/ $$ |$$       |      $$    $$/ $$    $$ |$$ | $$  |$$    $$ |      $$    $$/ $$    $$/   $$  $$//     $$/ 
   $$/ $$/       $$/ $$$$$$$/  $$/  $$$$$$$/       $$$$$$$/   $$$$$$$/ $$/   $$/  $$$$$$$/       $$$$$$$/   $$$$$$/     $$$$/ $$$$$$$/  
                     $$ |                                                                                                               
                     $$ |                                                                                                               
                     $$/                                                                                                                
"""


from machine import Pin, PWM
import time


# Initialization of pins
# Btw, they can't be inline because of problems with electricity... Or my shitty soldering skills
RSL = PWM(Pin(15))
LSL = PWM(Pin(1))
RSR = PWM(Pin(13))
LSR = PWM(Pin(18))
LE = PWM(Pin(4))
RE = PWM(Pin(11))
LED = Pin(25, Pin.OUT)

# Frequencies... idk why 50 but 50 it is
RSL.freq(50)
LSL.freq(50)
RSR.freq(50)
LSR.freq(50)
LE.freq(50)
RE.freq(50)

def set_angle(servo, angle):
    min_duty = 1638
    max_duty = 8192
    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    servo.duty_u16(duty)



# Yeah, I didn't think too much when mounting the motors so now we're left with diffucult to work with angles
def move_to_neutral():
    set_angle(RSL, 25)
    set_angle(LSL, 0)
    set_angle(RSR, 40)
    set_angle(LSR, 190) # Hear me out, I know this is not supposed to go over 180 but it just works... And if it works we don't touch it
    set_angle(LE, 120)
    set_angle(RE, 0)
    time.sleep(1)
    
def turnoff_servo():
    RSL.deinit()
    LSL.deinit()
    RSR.deinit()
    LSR.deinit()
    LE.deinit()
    RE.deinit()

# doesn't lift far enough but let that be a future problem
# 0 = as far right as it can reach for now. 
def lift_right_arm(angle):
    set_angle(RSL, angle)

# Neutral = 0
# 100 = halfway
# 170-180 = all the way up
def lift_left_arm(angle):
    set_angle(LSL, angle)


# Neutral = 40
# Halfway = 120
# Uptop = 180
def move_right_arm_forward(angle):
    set_angle(RSR, angle)
    
# Neutral = 180
# Halfway = 100
# Top = 25
def move_left_arm_forward(angle):
    set_angle(LSR, angle)


# Neutral = 120
# Halfway = 20
# top = 0 (kinda top)
def move_left_elbow(angle):
    set_angle(LE, angle)

# Neutral = 0
# Halfway = 80
# Top = 150
def move_right_elbow(angle):
    set_angle(RE, angle)

# Optimilized this to run via a loop instead of code spam
def wave_left():
    move_left_arm_forward(30)
    for _ in range(4):
        lift_left_arm(0)
        time.sleep(0.4)
        lift_left_arm(20)
        time.sleep(0.4)
        
    move_to_neutral()

"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣀⣀⠀⠀⣀⡠⠴⠒⠚⠉⠉⠓⠒⠦⣄⣶⠒⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡷⢬⣉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠠⡌⠻⣧⢻⣧⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣖⠗⡋⢹⠀⠀⢰⡄⠀⠀⢸⣷⡀⠀⣠⠽⣆⢼⣇⢻⣸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⣡⣶⢋⡏⠙⢢⣏⣇⠀⠀⠈⣇⡵⡏⠀⠀⢹⡏⢾⣿⠃⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⢿⢻⣏⣿⡇⡄⣾⠀⠹⡄⠄⠀⡇⠀⠹⣤⠈⠹⣿⣾⢸⠀⢘⣷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣯⣿⣽⣿⣷⢸⡗⠦⣄⡹⣼⣄⣿⣴⠛⠹⡄⡇⣿⣿⠾⠚⢹⢿⢽⣽⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣞⣾⣿⢿⣯⢻⢻⡴⠞⠁⠈⠻⣿⣌⡉⠓⣿⣰⡿⠀⠀⠀⠸⡜⡾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣡⠊⢸⣹⠁⠈⠙⣾⡄⠁⠀⢰⠛⠉⠉⠉⢳⣀⣿⣿⠃⠀⠀⣀⣀⣧⣿⡞⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⡴⠁⠀⠸⢿⣤⣤⣤⣹⣿⣷⣶⣾⣷⣶⣶⣺⣋⣽⣿⣷⠶⠟⠛⠋⢧⠀⠀⠸⡜⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠁⡰⠁⠀⠀⢠⡿⠀⠀⠀⠉⠉⠉⠙⢻⡟⣹⣿⠃⣿⠋⠁⠀⠀⠀⠀⠀⠸⡄⠀⠀⢣⠹⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⡀⢠⠇⠀⠀⢠⡿⠁⠀⠀⠀⠀⣤⣶⡴⠚⢻⠡⣸⠀⢹⣆⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠸⡄⢻⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⣼⠁⢸⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⢻⣿⣧⣀⣬⠋⠁⠀⣠⣿⣶⣆⠀⠀⠀⠀⠀⡇⠀⠀⠀⡇⠈⣿⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣸⣿⠀⡇⠀⢰⣸⡟⠀⠀⠀⣀⣠⠴⠚⣟⣻⣧⣯⣗⣤⣾⣿⣿⡿⠋⠀⠀⠀⠀⣸⣤⠀⠀⠀⡇⡆⢻⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⢸⡀⣇⠀⣸⣿⡁⠀⣾⣻⡁⣀⣤⣶⠟⠋⠉⠛⢿⣋⣻⡏⠉⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⣷⡇⣸⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠇⠀⢧⢸⠀⣿⡿⠇⠀⠈⠛⠛⠋⠉⠀⠀⠀⠀⠀⡟⠀⣿⠇⠀⠀⠀⠀⠀⢠⣿⣿⡇⠀⠀⣰⡿⣧⣿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣄⣹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⣿⠀⠀⠀⠀⠀⠀⣸⡿⢸⠁⢠⣾⠋⢰⣿⡏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣶⣶⡿⠀⠀⠀⠀⠀⠀⠉⠁⢸⣶⡟⠁⠀⠾⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""



"""
  _____                                   _   _             
 |  __ \                                 | | (_)            
 | |__) |__  ___  ___       ___  ___  ___| |_ _  ___  _ __  
 |  ___/ _ \/ __|/ _ \     / __|/ _ \/ __| __| |/ _ \| '_ \ 
 | |  | (_) \__ \  __/     \__ \  __/ (__| |_| | (_) | | | |
 |_|   \___/|___/\___|     |___/\___|\___|\__|_|\___/|_| |_|
                                                            
                                                            
"""



# Choreography is not choreographying properly so we're retreating to a safer pose based approach
# To put it plainly I'll just make functions for poses which we'll switch during the pwerformance to create the illusion that we know what we're doing
def airplane_pose():
    print("Airplace pose initiated")
    lift_left_arm(150)
    lift_right_arm(0) # Lifts it halfway, need it to lift it 'bout a quarter less but I am unable to test it right now
    move_left_arm_forward(180) # So the weight of the arm made it fall so I had to put some currect through this to lock it in place
    time.sleep(1) # In case you're wondering why this exists it is for the servos to have time to move because the commands get executed in miliseconds.... But will actually anybody other than me read this?

def T_pose():
    print("T pose Initiated")
    lift_right_arm(0)
    lift_left_arm(100)
    time.sleep(1)

def elbows_up_pose():
    print("Elbows up pose")
    move_left_elbow(20)
    move_right_elbow(80)
    time.sleep(1)

# It's like the elbows_up pose but the left arm is also lifted
def elbows_up_and_leftArm():
    print("Elbows up and left arm pose")
    move_left_elbow(20)
    move_left_arm_forward(100)
    move_right_elbow(80)
    time.sleep(0.7)
    
# Yup, you guessed it
def elbows_up_and_rightArm():
    print("Elbows up and right arm pose")
    move_left_elbow(20)
    move_right_arm_forward(120)
    move_right_elbow(80)
    time.sleep(0.7)
    
# These poses start to demand commentary as I am getting lost in how to name these fancy moves
# This one uses the position of elbows up and right arm but uses the shouder lift servo to lower the forearm to the chest
def right_forearm_to_chest():
    move_left_elbow(20)
    move_right_arm_forward(120)
    move_right_elbow(80)
    lift_right_arm(0)
    time.sleep(1)
    
def left_forearm_to_chest():
    move_left_elbow(20)
    move_left_arm_forward(100)
    move_right_elbow(80)
    lift_left_arm(100)
    time.sleep(1)
    
def both_forearms_to_chest():
    move_left_elbow(20)
    move_left_arm_forward(100)
    lift_left_arm(100)

    move_right_elbow(80)
    move_right_arm_forward(120)
    lift_right_arm(0)

    time.sleep(1)

"""
  _____                         __  __                       _____           _   _             
 |  __ \                       |  \/  |                     / ____|         | | (_)            
 | |  | | __ _ _ __   ___ ___  | \  / | _____   _____      | (___   ___  ___| |_ _  ___  _ __  
 | |  | |/ _` | '_ \ / __/ _ \ | |\/| |/ _ \ \ / / _ \      \___ \ / _ \/ __| __| |/ _ \| '_ \ 
 | |__| | (_| | | | | (_|  __/ | |  | | (_) \ V /  __/      ____) |  __/ (__| |_| | (_) | | | |
 |_____/ \__,_|_| |_|\___\___| |_|  |_|\___/ \_/ \___|     |_____/ \___|\___|\__|_|\___/|_| |_|
                                                                                               
                                                                                               
"""


# Function section for dance moves
# Poses motionalized into dance moves via a loop, ain't the simplicity beautiful?
# At least in code for my experience tells me it will not work as intended during testing
def train_whistle_left():
    for _ in range(4):
        elbows_up_and_leftArm()
        move_left_arm_forward(180)
        time.sleep(0.5)
        
def train_whistle_right():
    for _ in range(4):
        elbows_up_and_rightArm()
        move_right_arm_forward(40)
        time.sleep(0.5)

def train_whistle_both():
    for _ in range(4):
        elbows_up_and_leftArm()
        elbows_up_and_rightArm()
        move_left_arm_forward(180)
        move_right_arm_forward(40)
        time.sleep(0.5)

def elbows_up_move():
    for _ in range(4): # btw, this just repeats the move 4 times is anybody cares... 
        elbows_up_pose()
        # lower to neutral
        move_left_elbow(120)
        move_right_elbow(0)
        time.sleep(0.6)

def left_forearm_to_chest_move():
    for _ in range (4):
        move_left_elbow(20)
        move_left_arm_forward(100)
        move_right_elbow(80)
        lift_left_arm(100)
        time.sleep(1)
        lift_left_arm(0)
        time.sleep(1)
       
# this one doesn't work very good due to servo constrains so it probably won't be used
def right_forearm_to_chest_move():
    for _ in range (3):
        move_left_elbow(20)
        move_right_arm_forward(120)
        move_right_elbow(80)
        lift_right_arm(40)
        time.sleep(1)
        lift_right_arm(0)
        time.sleep(1)


# Main choreography... idk how to dance
def dance():
    airplane_pose()
    time.sleep(1)
    move_to_neutral()
    time.sleep(0.5)
    T_pose()
    time.sleep(0.7)
    move_to_neutral()
    time.sleep(0.5)
    train_whistle_right()
    time.sleep(0.5)
    move_to_neutral()
    time.sleep(0.5)
    airplane_pose()
    time.sleep(1)
    move_to_neutral()
    time.sleep(0.5)
    elbows_up_move()
    time.sleep(0.5)
    elbows_up_and_leftArm()
    time.sleep(0.5)
    move_to_neutral()
    time.sleep(0.7)
    left_forearm_to_chest_move()
    time.sleep(0.7)
    both_forearms_to_chest()
    time.sleep(1)
    move_to_neutral()
    time.sleep(0.5)
    airplane_pose()
    time.sleep(0.5)
    move_to_neutral()
    time.sleep(0.5)
    elbows_up_and_rightArm()
    time.sleep(0.5)
    
    
    
    time.sleep(0.8)
    move_to_neutral()
    
    
    
    
"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣫⣟⢯⡓⢆⡼⣙⢮⡹⢭⢿⡣⡙⡜⡸⢙⣧⣓⠨⢍⢻⣷⣄⠐⠌⢂⠇⣊⠹⢳⣟⣿⣟⣯⣝⡝⢯⢻⡝⣟⠿⣿⣿⣿⣿⣿⣿⣿⣽⣫⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣴⢻⣌⠳⣉⠦⠓⡌⠦⡑⢎⠺⡇⠀⠑⠠⠁⢺⣷⣄⠀⠂⢻⣟⣧⡀⠀⡈⠀⠄⠈⠹⣎⢻⣽⡞⣿⢮⣣⠞⣭⣛⢶⣹⡻⣿⣿⣿⣿⣿⣿⣿⣘⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⡼⡏⡶⢈⠇⢁⠊⠡⠈⠄⠁⠌⠓⡽⠀⠠⠁⢀⠂⣏⠻⣄⠀⠄⢷⠩⢿⣄⠀⠐⠀⡈⠀⠸⡆⢻⡽⠾⣍⡟⡻⣶⣭⣟⣷⣻⡷⣯⣿⣿⣿⣿⣿⣿⣶⡉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡸⢒⡇⢳⠈⠐⡀⠀⠄⠂⠀⠌⠀⡈⢼⠀⠀⡐⠀⢈⡗⡀⠙⣦⠀⠸⡇⠈⠻⣆⠀⠂⢀⠐⠀⢻⡀⢻⣧⣂⠉⠱⣌⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠢⣙⠌⣿⢸⡀⠄⠀⠄⠀⠠⠁⠀⠂⢀⠨⡄⠀⠀⡐⢸⠇⠀⠀⢈⣧⠀⢻⡤⠤⢽⣆⠀⡀⠀⠂⠀⣧⠀⣿⣿⣷⣦⡈⠓⢤⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⠐⡊⣽⡎⣇⠀⠈⢀⠐⠀⡀⠁⠐⠀⡀⡇⠀⠂⠀⣾⣠⠶⠚⠉⠉⢷⡸⣇⠀⠀⠸⣆⠀⠀⠂⠁⢹⠀⠸⣎⡻⢿⣿⣶⣄⠙⢤⠈⠙⢿⣿⣿⢯⣿⣿⣿⣽⣿⣿⣿⡄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⠘⠰⣘⣷⣻⡀⠈⠀⡀⠄⠀⠠⠁⠠⠀⠆⠀⠐⠀⡟⠀⠀⠀⠀⠀⠈⢳⣿⢀⠀⣠⠹⡆⠀⡐⠀⢸⡄⠀⢻⡳⢯⡺⣟⣿⣿⣦⣈⠢⠄⡈⠛⢿⣿⣿⣿⣿⣽⣿⣿⣿⣆⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⢿⡿⣿⢿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠨⢁⠆⣿⢯⢧⠀⠁⢀⠀⠂⠁⢀⠐⠀⢸⠀⢀⣸⠃⠀⠀⣠⠖⢁⣤⣶⣿⠿⠶⠷⣴⣻⡄⠀⠠⢸⡇⠀⢸⣿⣀⡻⣌⠻⣟⣿⣿⣿⣦⣔⠠⣀⠈⠛⢿⣿⣯⣿⣿⣿⣿⣧⠹⣿⣭⣭⣽⣷⣶⣶⣶⣾⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣟⣿⢻⣿⠀⢀⠡⠌⢿⠘⣟⣇⠀⠂⢀⠐⠈⠀⠠⠈⣼⠀⢠⡇⠀⠀⢸⣡⣴⢿⣽⣶⣿⢿⣷⣦⡈⠹⣷⠀⢀⠠⡇⠀⠀⣷⡛⢿⣿⣷⡌⢻⣟⣿⠿⣿⣿⣶⣬⣒⠠⢈⡙⠿⣿⣿⣿⣿⣷⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⠀⣿⡆⠀⠂⢌⢺⡇⣸⣿⣆⠀⠂⠀⠄⠁⡀⠂⣯⠀⡾⠀⠀⠀⢰⣵⡟⠼⠿⣟ ⡔⠋⠺⣽⣿⡄⠘⡆⠀⢰⡇⠀⡀⡿⡇⠀⢹⣿⣿⣧⣜⢻⣷⣟⣿⣞⡿⣟⡿⣷⢶⣦⣄⣙⡻⢿⣿⣿⣌⠻⣿⣿⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣻⣿⠀⢻⣻⡀⠠⠌⡰⢿⡃⠘⢾⣆⠀⡁⢀⠂⢀⢰⡇⣰⠃⠀⠀⠀⢠⢿⠀⠀⠀⢸⡄⠀⡀⢹⠟⢻⣀⣷⠀⢸⠁⢀⠀⣧⣿⡀⠈⣿⣿⣿⣿⣦⣝⢻⡿⣿⣽⣯⣿⢾⣯⣞⣽⢻⡿⣿⡾⣽⣿⣷⣝⢻⣼⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠈⣿⢷⡀⠐⣠⠙⣧⠀⠈⢿⣧⠀⠠⠀⠂⣾⣰⠃⠀⠀⠀⠀⠀⠈⠃⠀⢻⣿⠛⠦⣴⠞⠂⣠⠋⢹⠀⣾⠀⢀⢀⣿⠛⠋⢰⣯⣉⣉⣉⣭⣽⣷⣝⡫⣿⢷⣶⣿⣿⣿⣍⠛⣿⣷⣳⣌⠙⠻⣿⣿⣦⣭⣛⠻⠿⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢁⣸⣯⣷⡄⠐⡍⡞⣧⠀⢀⣿⣷⣄⠁⠰⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠙⢤⡀⢀⣠⠞⠁⠀⣺⢀⡏⠀⠠⢸⡿⠀⣀⣾⣿⣟⣿⣿⣿⣿⣿⣿⣿⣮⣟⣭⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠛⢿⣿⣿⣿⣳⢶⣶⣶⣬⣭⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⡆⠈⣿⣿⡿⣆⠰⢹⣸⣷⣿⠁⠿⣿⣆⣹⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠈⠉⠉⠀⠀⠀⠀⣸⡾⡏⠀⠰⣾⣿⣿⣿⠿⠉⠁⠀⠉⠿⣿⣿⣿⣿⣿⣿⣿⣷⣏⣷⣿⣿⣿⣿⣾⣿⣿⣿⣿⣷⣆⠹⣿⣿⣿⣷⣎⣉⠹⠿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⡅⣻⣿⣿⣿⣧⣂⢳⣻⣿⡄⢀⣨⣖⢘⣿⢋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢣⡇⡀⢷⣿⡟⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⢿⣿⣿⣿⣿⣿⣷⣯⣿⣻⢿⣿⣿⣿⣿⣿⣿⣷⣭⣿⣿⣿⣿⣿⣿⣿⣷
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣔⣻⣿⣿⣿⣿⣦⣳⣻⣧⠀⠹⣏⡻⣾⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⣼⠀⡙⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣷⣿⣾⣷⣿⣿⣿⣟⣿⡟⣻⡽⢻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⡿⣿⣿⣿⣿⣿⣷⣿⣷⡐⠚⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣼⡿⢀⣽⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣽⣟⡿⣿⣿⣿⣿⣿⣿⣿⣽⣹⣿⢡⢿⣽⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡻⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣼⣿⡟⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣾⣽⢿⣻⣿⣿⣿⣿⣿⣿⣾⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣝⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⢀⣰⣿⣿⣿⣿⣿⡿⡗⠸⣿⣇⠀⠀⠀⠀⠀⠀⠀⢀⣿⣇⠀⣼⣿⣿⣿⣿⣿⣿⣿⣷⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠽⠫⠀⠀⠀⠠⣸⣿⣿⣿⣿⣿⣿⣿⡳⠀⠀⢻⣿⡇⠀⠀⠀⠀⠀⢀⡞⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⢿⣿⣿⣮⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣒⣶⣤⣤⣀⣀⣀⣤⢞⡿⣿⣽⣿⣿⣿⡟⠁⠁⠀⠀⠸⣿⣧⢀⠀⠀⢀⣠⢿⣀⣼⠋⢿⡿⡇⣽⣻⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⢯⡻⣿⣿⠱⢮⣶⣬⣙⢟⣿⠿⠉⡀⢄⠂⠰⢀⠀⣿⣿⡆⠠⢀⣴⠋⢸⣿⡷⢈⢂⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⢯⡟⣵⢫⣿⣷⢂⠦⣉⠭⣉⠆⡆⢣⠔⢢⠘⡐⠢⢌⢸⣾⣧⡱⢈⡄⢪⣿⡗⣻⡘⢦⢊⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⣏⢷⢫⣏⣿⣯⡞⣥⣳⢬⣛⣬⢃⢮⣡⢋⡜⡱⢊⢾⣿⣿⡑⢦⣘⣻⣿⡔⢿⣿⢣⣭⢛⣿⣟⣻⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢷⣻⣿⣿⣟⡿⣿⣯⣶⣭⢿⣻⣽⣷⣯⣷⣯⣶⢯⣖⢧⣏⢶⣩⡓⢮⣿⣿⠼⣑⣾⣿⣿⠺⣥⣟⡳⣼⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣻⣽⣻⡿⣷⣷⣫⢟⡽⣿⠿⣿⣾⣻⡾⡷⣷⢿⣯⣿⣿⡷⣿⣿⣿⣳⢿⣽⣯⣽⢾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣯⣿⣽⣯⣟⣿⡿⣿⣾⣿⣷⣯⢷⣝⣳⣭⣷⣛⣾⣧⣿⣿⣿⢾⣷⣟⣻⣞⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""


# Main program starting here:
led.value(1) # Due to problems with the USB port on the Pico we indicate successful start of the prgram by turning this LED on
move_to_neutral()
led.value(0) # After indicating startup and oving the robot to the neural position we can turn the LED off
time.sleep(5) # We wait 5 seconds to allow us to get out of the stage
for _ in range(2): # We repeat the dance choreography 2 times
    dance()
    
time.sleep(0.7)
move_to_neutral()
time.sleep(1)
wave_left() # We wave the judges goodbye
time.sleep(0.7)
turnoff_servo() # At the end we can rest the servos
