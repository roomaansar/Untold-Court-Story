from room import Room
from item import Item
from character import Enemy
from character import Friend

kitchen=Room()
ballroom=Room()
dining_hall=Room()
washroom=Room()
library=Room()
lounge=Room()

han=Friend("Han","Presiding Judge of 44, bad-tempered but a really good judge")
im=Friend("Im","Associate Presiding Judge of 44, cool but a really good and supportive judge")
park=Friend("Park","Associate Presiding Judge of 44, innocent,cool and bad-tempered but a really good judge")

ahn=Enemy("Ahn","Second Chief Justice")
sung=Enemy("Sung","Psycho Presiding Judge whose main goal is promotion")
bae=Enemy("Bae","Presiding Judge of depart 45")

han.set_conversation("Be a good judge. never be afraid of power. Judges are the most powerful")
im.set_conversation("I'm always here to help but the ones doing wrong I cannot stand")
park.set_conversation("I cannot stand the power. Court should support the unprivileged")

ahn.set_conversation("Oh! These young ambitious fools")
sung.set_conversation("I need promotion no matter what and I can do anything for that")
bae.set_conversation("I should always be on safe side. I sould side with the ones holding power and controlling courts")
kitchen.information("Kitchen","very clean room with food in bulk",ballroom,"south",han)
ballroom.information("Ball-room","vast and bright",lounge,"east",im)
dining_hall.information("Dining-hall","clean table and chairs with suitable cutlery",kitchen,"west",park)
washroom.information("Wash-room","very dirty and stingy",library,"north",bae)
library.information("Library","vast room canopied with books and journals",ballroom,"north",ahn)
lounge.information("Lounge","vast and clean",washroom,"south",sung)

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


current_room=dining_hall
while True:
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command=input('>what do you want to do? a-move b-fight c-talk \n')
    if command=="move":
        move=input("In what direction do you want to go?\n")
        if move==["south","east","west","north"]:
            current_room.move(move)

    elif command=="talk":
        inhabitant.talk()
        




