# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image fakebg bedroom = "images/bedroom.jpg"
image fakebg sokawaii = "images/start.jpg"
image fakebg morningstreet = "images/street.jpg"
image bg school = "images/school.jpg"
image bg classroom = "images/classroom.jpg"
image bg rooftop = "images/rooftop.jpg"
image sylvie = "images/sylvie.png"
image eileen = "images/eileen.png"
image haruka = "images/haruka.png"
image ojousama = "images/ojousama.png"
image icequeen = "images/icequeen.png"
image teacher = "images/teacher.png"

# Declare characters used by this game.
define OJ = Character('Ojou-sama', color="#FFFFFF", show_two_window=True, what_color="#FFFFFF")
define TCH = Character('Teacher', color="#FFFFFF", show_two_window=True, what_color="#FFFFFF")
define HRK = Character('Haruka', color="#FFFFFF", show_two_window=True, what_color="#FFFFFF")

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