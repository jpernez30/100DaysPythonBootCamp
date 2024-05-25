# move the robot right whenever possible
# go straight if not possible
# last move is turn left

def face_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
    
while not at_goal():
    if right_is_clear():
        face_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
        





