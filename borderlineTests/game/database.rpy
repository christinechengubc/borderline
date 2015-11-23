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
    
    # instantiating calendar
    calendar = SimpleCalendar(1,"January")
    
    # instantiating locations
    school = Location("School. Your most favorite place in the whole wide world.", 150, 244, 184, 102, "school")
    city_hall = Location("City Hall. You can do stuff here.", 544, 43, 168, 104, "city_hall")
    profile = Location("Feeling good? Check yourself out.", 533, 325, 197, 109, "profile")
    home = Location("Go home and watch some anime. Don't bother coming out again.", 910, 247, 186, 108, "home")
    #current location is initialized as the first location that jumps to the map
    current_location = profile
    
    locations = [school, city_hall, profile, home]
        
     
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