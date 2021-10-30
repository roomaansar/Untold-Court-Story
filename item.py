class Item():
    def __init__(self):
        self.name=None
        self.description=None
        self.linked_items={}

    def set_name(self,item_name):
        self.name=item_name
    
    def get_name(self):
        return self.name

    def set_description(self,item_description):
        self.description=item_description
        
    def get_description(self):
        return self.description

    def item_room(self, room_where_the_item_is):
        self.items_room= room_where_the_item_is

    def link_items(self, item_to_link, room):
        self.linked_items[room]= item_to_link
        #print( self.name + " linked items :" + repr(self.linked_items))

    def get_details(self):
        for room in self.linked_items:
            item=self.linked_items[room]
            print("\nThe "+self.get_name()+"'s details are:")
            print("- The item is "+ self.description)
            print(item.get_name())
            print('->This linked item is in '+ repr(room))
