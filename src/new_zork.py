import items

#This is where the magic happens, the while loop is always true but in the case that the player dies or wins, using the ded() function they can leave the game, breaking the while loop.

def Play_Zork():
    print("---------------------------------------------------------")
    print("Welcome to Zork - The Unofficial Python Version.")
    room = 4
    item_list=[]
    while True:
        user_input= get_user_input(room)
        
        if room == 1:
                room = room1(user_input)
        elif room == 2:
                room = room2(user_input)
        elif room == 3:
                room = room3(user_input)
        elif room == 4:
                room = room4(user_input)
        elif room == 5:
                room = room5(user_input)
        elif room == 6:
                room = room6(user_input)
        elif room == 7:
                room = room7(user_input)
        elif room == 8:
                room = room8(user_input)
        elif room == 9:
                room = room9(user_input)
        elif room == 10:
                room = room10(user_input)
        elif room == 11:
                room = room11(user_input)
        elif room == 12:
                room = room12(user_input)


#This function helps clean up some redundant code and deals with resetting/ quitting the game when they win or die     
def ded():
        ded_input=input('Do you want to continue? Y/N ')
        if ded_input.lower() == ('n'):
                exit()
        elif ded_input.lower() == ('y'):
                Play_Zork()

#This gives the user output for each function
def get_user_input(room):
    print("---------------------------------------------------------")
    if room == 1:
        print("You find yourself at the edge of a beautiful lake aside rolling hills.")
        print("A small pier juts out into the lake.")
        print("A fishing rod rests on the pier.")
        print("(You can see a white house in the distance to the south.)")
        
    elif room == 2:
        print("You find yourself behind the house, unkempt ivy creeps up the beautiful old estate.")
        print("Going west towards, the house there is a rickety window, but it's open!")
        print("Going south will take you back to the front of the house.")
        
    elif room == 3:
        print("You find yourself in a dimly lit kitchen with dust covering the floor.")
        print("A lantern rests on the kitchen island.")
        print("A set of stairs leads up to another room")
        
    elif room == 4:
        print("You are standing in an open field west of a white house, with a boarded front door.")
        print("You can see a small lake to the north.")
        print("Going east around the house there is a gate that leads to the back of the home.")
        print("(A secret path leads southwest into the forest.)")
        print("There is a Small Mailbox.")
        
    elif room == 5:
        print("You come up the stairs to a dusty old attic.")
        print("The staircase is behind you")
        
    elif room == 6:
        print("Venturing into the next chamber you find yourself at the entrance to an ancient maze.")
        print("You can see the cave entrance back to the North.")
        print("The Maze looms to your south")
        
    elif room == 7:
        print("The stone walls grow close around you, there is a fork in the path before you but all ways are dark.")
        print("A foul stench reaches you, something lives in here.")
        print("You can stil flee, the entrance is to the north!")
            
        
    elif room == 8:
        print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
        print("You see a mountain range poking above the trees to the west.")
        
    elif room == 9:
        print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
        print("There is an open grating, descending into darkness.")

    elif room == 10:
        print("You are in a tiny cave with a dark, forbidding staircase leading down.")
        print("There is a skeleton of a human male in one corner.")
        print("To the south there is something in the depths of the cave, but you cant make it out.")

    elif room == 11:
        print("You have entered a mud-floored room.")
        print("Lying half buried in the mud is an old trunk, bulging with jewels.")
    elif room == 12:
        print("You come to the feet of the Nandic Mountans! Their towering, snowcapped peakes loom to the west,.")
        print("A powerful river rages to the north and the evil lands lie to the south.")

    user_input= input("What do you do? ")
        
    return user_input.lower()


##################################################################
########These are the room functions##############################
##################################################################
def room1(user_input):
        room = 1
        if user_input == ("go south"):
                room = 4
        elif user_input == ("swim"):
                print("---------------------------------------------------------")
                print("You don't have a change of clothes and you aren't here on vacation.")
        elif user_input == ("fish"):
                print("---------------------------------------------------------")
                print("You spend some time fishing but nothing seems to bite.")
        elif user_input == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                ded()
        else:
                print("---------------------------------------------------------")
        return room

def room2(user_input):
        room = 2
        if user_input == ("go south"):
                room = 4
        elif user_input == ("go west"):
                room = 3
                print("---------------------------------------------------------")
                print("Opening a rickety window you climb into the house")
        elif user_input == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")

                ded()
        else:
                print("---------------------------------------------------------")
        return room

def room3(user_input):
        room = 3
        if user_input == ("go up staircase"):
                print("---------------------------------------------------------")
                print("You climb the creaking stairs...")
                room = 5
        elif user_input == ("pick up lantern"):
                print("---------------------------------------------------------")
                print("LANTERN added to inventory!")
        elif user_input == ("go east"):
                print("---------------------------------------------------------")
                print("You hop out the window")
                room = 2
        elif user_input == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")

                ded()
        else:
                print("---------------------------------------------------------")
        return room 
def room4(user_input):
        room = 4
        if user_input == ("take mailbox"):
                print("---------------------------------------------------------")
                print("It is securely anchored.")
        elif user_input == ("open mailbox"):
                print("---------------------------------------------------------")
                print("Opening the small mailbox reveals a leaflet.")
        elif user_input == ("go east"):
                room = 2
        elif user_input == ("go north"):
                room = 1
        elif user_input == ("fuckem"):
                room = 11
                print("RULE #1 FUCKEM")
                print("THE GODS OF THE UNIVERSE RECOGNIZE YOUR WISEDOM! YOU'RE TRANSPORTED TO THE FINAL ROOM")
        elif user_input == ("open door"):
                print("---------------------------------------------------------")
                print("The door cannot be opened.")
        elif user_input == ("take boards"):
                print("---------------------------------------------------------")
                print("The boards are securely fastened.")
        elif user_input == ("look at house"):
                print("---------------------------------------------------------")
                print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
        elif user_input == ("go southwest"):
                room = 8
        elif user_input == ("read leaflet"):
                print("---------------------------------------------------------")
                print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
        elif user_input == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")

                ded()
        else:
                print("---------------------------------------------------------")
        return room

def room5(user_input):
        room = 5
        if user_input == ("descend staircase"):
                room =3
        elif user_input == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                ded()
        else:
                print("---------------------------------------------------------")
        return room

def room6(user_input):
        room = 6
        if user_input == ("go north"):
                room = 10
                print("---------------------------------------------------------")
                print("You head back to the first chamber in the cave.")
        elif user_input == ("go south"):
                room = 7
                print("---------------------------------------------------------")
                print("You enter the maze and are greeted by the stench of death.")
        elif user_input == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                ded()
        else:
                print("---------------------------------------------------------")
        return room

def room7(user_input):
        room = 7
        if user_input == ("go north"):
                print("---------------------------------------------------------")
                print("You escaped the maze, something was off about that place.")
                room = 6
        else:
                print("You were eaten by the grue! You should've left the maze while you had the chance.")
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                ded()
        return room
def room8(user_input):
        room = 8
        if user_input == ("go west"):
                print("---------------------------------------------------------")
                print("After a long day's walk you arrive at the feet of the distant mountains")
                room = 12
        elif user_input == ("go north"):
                print("---------------------------------------------------------")
                print("The forest becomes impenetrable to the North.")
        elif user_input == ("go northeast"):
                room = 4
        elif user_input == ("go south"):
                print("---------------------------------------------------------")
                print("Storm-tossed trees block your way.")
        elif user_input == ("go east"):
                room = 9
        elif user_input == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                ded()
        else:
                print("---------------------------------------------------------")
        return room

def room9(user_input):
        room = 9
        if user_input == ("go south"):
                print("---------------------------------------------------------")
                print("You see a large ogre and turn around.")
        elif user_input == ("descend grating"):
                room = 10
        elif user_input == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")

                ded()
        else:
                print("---------------------------------------------------------")
        return room     
def room10(user_input):
        room = 10
        if user_input == ("descend staircase"):
                room = 11
        elif user_input == ("go south"):
                print("---------------------------------------------------------")
                print("You walk deeper into the cave...")
                room = 6
        elif user_input == ("take skeleton"):
                print("---------------------------------------------------------")
                print("Why would you do that? Are you some sort of sicko?")
        elif user_input == ("smash skeleton"):
                print("---------------------------------------------------------")
                print("Sick person. Have some respect mate.")
        elif user_input == ("light up room"):
                print("---------------------------------------------------------")
                print("You would need a torch or lamp to do that.")
        elif user_input == ("break skeleton"):
                print("---------------------------------------------------------")
                print("I have two questions: Why and With What?")
        elif user_input == ("go down staircase"):
                room = 11
        elif user_input == ("scale staircase"):
                room = 11
        elif user_input == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                ded()
        else:
                print("---------------------------------------------------------")
        return room       
def room11(user_input):
        room = 11
        if user_input == ("open trunk"):
                print("---------------------------------------------------------")
                print("You have found the Jade Statue and have completed your quest!")
                ded()
                
        elif user_input == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                ded()
        else:
                print("---------------------------------------------------------")
def room12(user_input):
        room = 12
        if user_input == ("go east"):
              print("---------------------------------------------------------")
              print ("You return to the forest.")
              room = 8
        elif user_input == ("go west"):
              print("---------------------------------------------------------")
              print("The mountains are impassiblble this time of year.")
        elif user_input == ("go north"):
              print("---------------------------------------------------------")
              print("A roaring river blocks your way.")
        elif user_input == ("go south"):
              print("---------------------------------------------------------")
              print("You wander into the evil lands and are killed by uruks")
              ded()
        elif user_input == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                ded()
        else:
                print("---------------------------------------------------------")
        return room  
        
        
