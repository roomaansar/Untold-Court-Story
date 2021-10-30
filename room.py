class Room():
    
    number_of_rooms=0
    
    def __init__(self):
        self.linked_rooms={}
        self.name=None
        self.description=None
        self.character=None
        Room.number_of_rooms=Room.number_of_rooms + 1

    def information(self,room_name,room_description,room_to_link,direction):
        self.name=room_name
        self.description=room_description
        self.linked_rooms[direction]=room_to_link
        self.character=None

    def set_character(self,new_character):
        self.character=new_character

    @property
    def character(self):
        print_character=str(self._character)
        return print_character

    @character.setter
    def character(self,new_character):
        self._character=new_character
        
    def get_name(self):
        return self.name
 
    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)


    def get_character(self):
        return self.character

##    def link_room(self, room_to_link, direction):
##        self.linked_rooms[direction]=room_to_link
##        #print( self.name + " linked rooms :" + repr(self.linked_rooms))

    def get_details(self):
        for direction in self.linked_rooms:
            room= self.linked_rooms[direction]
            print("\nCurrently, You are in "+self.get_name()+". This room's details are as follows:")
            print("- The room is "+ self.get_description())
            print('- The '+room.get_name()+' is '+  direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You cannot go that way")
            return self

    
