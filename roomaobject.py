from room import Room
from item import Item
from character import Enemy
from character import Friend
from creatorinfo import CreatorInfo

miss_hammurabi=CreatorInfo("Miss Hammurabi")
miss_hammurabi.welcome()

CreatorInfo.info()
CreatorInfo.author="Rooma Ansar"

kitchen=Room()
ballroom=Room()
dining_hall=Room()
washroom=Room()
library=Room()
lounge=Room()
print("There are "+ str(Room.number_of_rooms)+" rooms to explore")

han=Friend("Han","Presiding Judge of 44, bad-tempered but a really good judge")
im=Friend("Im","Associate Presiding Judge of 44, cool but a really good and supportive judge")
park=Friend("Park","Associate Presiding Judge of 44, innocent,cool and bad-tempered but a really good judge")

ahn=Enemy("Ahn","Second Chief Justice")
sung=Enemy("Sung","Psycho Presiding Judge whose main goal is promotion")
bae=Enemy("Bae","Presiding Judge of depart 45 who only worship power")

han.set_conversation("Be a good judge. never be afraid of power. Judges are the most powerful")
im.set_conversation("I'm always here to help but the ones doing wrong I cannot stand")
park.set_conversation("I cannot stand the power. Court should support the unprivileged")

ahn.set_conversation("Oh! These young ambitious fools")
sung.set_conversation("I need promotion no matter what and I can do anything for that")
bae.set_conversation("I should always be on safe side. I sould side with the ones holding power and controlling courts")

ahn.set_weakness("supreme court")
sung.set_weakness("demotion")
bae.set_weakness("power")

kitchen.information("Kitchen","very clean room with food in bulk",ballroom,"south")
ballroom.information("Ball-room","vast and bright",lounge,"east")
dining_hall.information("Dining-hall","clean table and chairs with suitable cutlery",kitchen,"west")
washroom.information("Wash-room","very dirty and stingy",library,"north")
library.information("Library","vast room canopied with books and journals",ballroom,"north")
lounge.information("Lounge","vast and clean",washroom,"south")

kitchen.set_character(han)
ballroom.set_character(im)
dining_hall.set_character(park)
washroom.set_character(bae)
library.set_character(ahn)
lounge.set_character(sung)

glass=Item()
gun=Item()
glass.set_name("Glass")
glass.item_room("Bathroom")
glass.set_description("Clean and swift")
glass.link_items(gun,'Dining_hall')

gun.set_description("Clean and swift")
gun.set_name("Gun")
gun.item_room("Dining_hall")
gun.link_items(glass,'bathroom')

current_room=washroom

while True:
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    if isinstance(inhabitant, Friend)==True:
        inhabitant.fist_bump()
    command=input('\n>what do you want to do? \na-move \nb-fight \nc-talk \n')
    if command=="move":
        move=input("In what direction do you want to go?\n")
        if move in ["south","east","west","north"]:
            current_room=current_room.move(move)
        else:
            print("Error!!You cannot go that way!!!")

    elif command=="talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("No one is here to talk")

    elif command=="fight":
        if isinstance(inhabitant, Enemy)==True:
            inhabitant.describe_weakness()
            fight_item=input("Enemy Alert!!! what do you want to fight with?")
            if inhabitant.fight(fight_item)==True:
                current_room.set_character(None)
            else:
                print("\n!!!!!!!!!!!!!!!!!!!!!!YOU DIED, GAME OVER!!!!!!!!!!!!!!!!!!!!!!\n") 
                break
        else:
            print("No enemy here to fight")
CreatorInfo.credits()

##elif command == "fight":
##        if inhabitant is not None and isinstance(inhabitant, Enemy):
##            # Fight with the inhabitant, if there is one
##            print("What will you fight with?")
##            fight_with = input()
##            if inhabitant.fight(fight_with) == True:
##                # What happens if you win?
##                print("Hooray, you won the fight!")
##                current_room.set_character(None)
##            else:
##                # What happens if you lose?
##                print("Oh dear, you lost the fight.")
##        else:
##            print("There is no one here to fight with")       
            
            


##    elif command == "hug":
##        if inhabitant is not None:
##            if isinstance(inhabitant, Enemy):
##                print("I wouldn't do that if I were you...")
##            else:
##                inhabitant.hug()
##        else:
##            print("There is no one here to hug :(")



