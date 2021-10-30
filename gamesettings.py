from room import Room
from item import Item

glass=Item()
gun=Item()
glass.set_name("Glass")
glass.item_room("Bathroom")
glass.set_description("Clean and swift")
gun.set_description("Clean and swift")
glass.link_items(gun,'dining_hall')
glass.get_details()


gun.set_name("Gun")
gun.item_room("Dining_hall")


kitchen=Room()
ballroom=Room()
dining_hall=Room()

kitchen.set_name("Kitchen")
kitchen.set_description("Clean and busy")
kitchen.link_room(dining_hall,'south')

ballroom.set_name("Ball room")
ballroom.set_description("Not necessary")
ballroom.link_room(kitchen,'west')

dining_hall.set_name("Dining hall")
dining_hall.set_description("required room")
dining_hall.link_room(kitchen,'east')

#kitchen.get_details()
#ballroom.get_details()
#dining_hall.get_details()

current_room=ballroom
while True:
    current_room.get_details()
    command=input('>')
    current_room=current_room.move(command)




