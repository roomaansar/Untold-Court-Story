import sys
class Character():

    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print( self.name + " is here! A character who is "+self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + "  doesn't want to fight with you")
        return True

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness=None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def describe_weakness(self):
        print("\t\t\t\t\t##SECRET TIP: The weakness of "+self.name+" is "+self.weakness)

    def fight(self, combat_item):
        if combat_item==self.weakness:
            print("I destroy you with your gift,"+ combat_item)
            return True
        else:
            print("No way, you cannot win against "+self.name)
##            print("\n!!!!!YOU DIED!!!!!")
##            print("THE END\nPLEASE RESTART THE GAME")
##            sys.exit()
            return False

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

    def fist_bump(self):
        print("\n")
        print(self.name+" bumps fist with you my friend")
