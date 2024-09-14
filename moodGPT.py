print("Hello, today were plannng what youre in the mood for!")
enter = int(input("press - 1 to start 2 - stop: "))

while enter != 2:
    hobby = input("Do you feel like being active today?: ").lower()
    if hobby == "yes":
        active = input("Weights or Running?: ").lower()
        if active == "running":
            running = input("easy run or tempo run?: ").lower()
            if running == "easy" or running == "easy run":
                print("make sure you dont go past your max aerobic heart rate")
            elif running == "tempo" or running == "tempo run":
                print("Get ready to sweat!") 
            print("Let's get to work.")
        elif active == "weights":
            gym_workout = int(input("How many exercises do you man on doing?: "))
            if gym_workout >= 4:
                print("thats a full workout!")
            elif gym_workout <=4:
                print("Lets add some cardio to break a sweat")
            print("Lets lift!")
    elif hobby == "no":
        indoor = input("Play Piano or Read: ").lower()
        if indoor == "play piano":
            song = input("practice or learn a song?: ").lower()
            if song == 'practice':
                print("Practice makes perfect!")
            elif song == "learn":
                new_song = input("Classical or Modern?: ").lower()
                if new_song == "classical":
                    print("Chopin is the man!")
                elif new_song == "modern":
                    print("golden hour is a nice song")
        elif indoor == "read":
            pages = int(input("How many pages do you plan on reading today?: "))
            if pages >= 10:
                print("That's great!")
            elif pages <= 10:
                print("lets try to push for more!")
            genre = input("Any specifc genre?: ")
            if genre == "mystery":
                print("The Couple next door is for you")
            elif genre == "action":
                print("The da vinci code is great")
            elif genre == "romance":
                print("The great gasby")
            else:
                print("try something new!")  
    
    print("Should we get a sweet treat today after a long day?")
    for i in range(1,4):
        if int(input("Guess a number 1 - 10: ")) == 3:
            print("You got yourself sweet treat!")
    enter = int(input("press - 1 to start 2 - stop: "))
           