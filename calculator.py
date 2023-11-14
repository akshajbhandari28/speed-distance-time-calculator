print()
print("WELCOME TO SPEED, DISTANCE, TIME CALCULATOR")
print()

user_input = input("please enter what you want to calculate (speed, distance, time) :- ").lower()

if "speed" in user_input:
    user_input_distance = int(input(" please enter your distance in meters :- "))
    user_input_time = int(input("please enter your time in seconds :- "))
    if user_input_time == 0:
        print("sorry time cannot be 0 to calculate speed")
        exit()
    output_speed = round(user_input_distance / user_input_time, 2)
    print(f"your speed is:- {output_speed} m/s")

elif "distance" in user_input:
    user_input_speed = int(input("please enter your speed in m/s :- "))
    user_input_time = int(input("please enter your time in seconds :- "))
    output_distance = round(user_input_speed * user_input_time, 2)
    print(f"your distance is:- {output_distance} meters ")

elif "time" in user_input:
    user_input_distance = int(input(" please enter your distance in meters :- "))
    user_input_speed = int(input("please enter your speed in m/s :- "))
    if user_input_speed == 0:
        print("sorry speed cannot be 0 to calculate time")
        exit()
    output_time = round(user_input_distance / user_input_speed, 2)
    print(f"your time is :- {output_time} seconds")

elif "speed" or "distance" or "time" not in user_input:
    print()
    print("sorry that is the wrong input please makesure that the words speed, distance and time are there in the input")
