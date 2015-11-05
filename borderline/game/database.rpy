# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image fakebg bedroom = "bedroom.jpg"
image fakebg sokawaii = "Fai_is_kawaii.jpg"
image fakebg morningstreet = "street.jpg"
image sylvie = "sylvie.png"
image eileen = "eileen.png"

# Declare characters used by this game.
define OJ = Character('Ojou-sama', color="#FFFFFF")

init python:
    
    class CharacterName:
        def __init__(self,firstName,lastName):
            self.firstName = firstName
            self.lastName = lastName
            
        def setFirstName(self, firstName):
            self.firstName = firstName
            
        def setLastName(self, lastName):
            self.lastName = lastName
            
            
init:
    
    python:
        fakeMcName = CharacterName("Default","Name")
    
    $ confirmedName = False
    
    $ MC = Character("[fakeMcName.firstName] [fakeMcName.lastName]", color = "#FFFFFF", show_two_window=True, what_color="#FFFFFF")
    $ OJ = Character("Ojou-sama", color = "#FFFFFF", show_two_window=True, what_color="#FFFFFF")
