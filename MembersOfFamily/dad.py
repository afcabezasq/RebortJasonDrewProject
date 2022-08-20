from familyMember import FamilyMember

class Dad(FamilyMember): # Dad a class that is inheriting from FamilyMember

    def __init__(self, input_name, input_age):
        FamilyMember.__init__(self, input_name, input_age)

    def whistle(self):
        print("Dad's whistling")