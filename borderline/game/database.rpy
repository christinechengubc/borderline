# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image fakebg bedroom = "images/bedroom.jpg"
image fakebg sokawaii = "images/start.jpg"
image fakebg morningstreet = "images/street.jpg"
image bg school = "images/school.jpg"
image bg classroom = "images/classroom.jpg"
image bg rooftop = "images/rooftop.jpg"
image bg city_night = "images/city_night.jpg"
image bg subway = "images/subway.jpg"
image bg alleyway = "images/alleyway.jpg"
image bg warehouse = "images/warehouse.jpg"
image bg warehouse_red = "images/warehouse_red.jpg"
image bg train = "images/train.jpg"

image shade red = "images/red.png"

image sylvie = "images/sylvie.png"
image eileen = "images/eileen.png"
image haruka = "images/haruka.png"
image ojousama = "images/ojousama.png"
image icequeen = "images/icequeen.png"
image teacher = "images/teacher.png"
image miyu = "images/miyu.png"
image baddie = "images/baddie.png"

# Declare characters used by this game.
# Prologue characters
define OJ = Character('Ojou-sama', color="#FFFFFF", show_two_window=True, what_color="#FFFFFF")
define TCH = Character('Teacher', color="#FFFFFF", show_two_window=True, what_color="#FFFFFF")
define HRK = Character('Haruka', color="#FFFFFF", show_two_window=True, what_color="#FFFFFF")
define MY = Character('Miyu', color="#FFFFFF", show_two_window=True, what_color="#FFFFFF")
define ESF = Character('Esfir', color="#FFFFFF", show_two_window=True, what_color="#FFFFFF")
define BD = Character('???', color="#FFFFFF", show_two_window=True, what_color="#FFFFFF")
# main characters
define K = Character('Kohaku', color="#FFFFFF", show_two_window=True, what_color="#FFFFFF")

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