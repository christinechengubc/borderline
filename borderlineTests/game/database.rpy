# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image fakebg bedroom = "images/bedroom.jpg"
image fakebg sokawaii = "images/fai_kawaii.jpg"
image fakebg morningstreet = "images/street.jpg"
image sylvie = "images/sylvie.png"
image eileen = "images/eileen.png"

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