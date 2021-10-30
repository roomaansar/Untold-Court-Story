class CreatorInfo():

    author="Anonymus"
    def __init__(self,game_title):
        self.name=game_title

    def welcome(self):
        print("        \t\t\t\t-----------------------------------------------")
        print("        \t\t\t\t|                                             |")
        print("        \t\t\t\t|    ******Welcome to "+self.name+"******    |")
        print("        \t\t\t\t|                                             |")
        print("        \t\t\t\t-----------------------------------------------")
        

    @staticmethod
    def info():
        print("\n      \t\t\t\t\t>>>>>Made using OOP Python (c) Rooma Ansar<<<<<<\n")

    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print("Created by "+ cls.author)
        
