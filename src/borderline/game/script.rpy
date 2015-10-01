# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")

init python:
    class CharacterName:
        def __init__(self,firstName,lastName):
            self.firstName = firstName
            self.lastName = lastName
            
        def setFirstName(self, firstName):
            self.firstName = firstName
            
        def setLastName(self, lastName):
            self.lastName = lastName


# The game starts here.
label start:
    python:
        fakeMcName = CharacterName("Default","Name")
    
    $ confirmedName = False
    "Salutations. I'm glad you can come here today. I hope you've been doing well."
    
    "Now before we begin, there are some questions I would like you to answer."

    while confirmedName == False:    
    
        $ firstName = renpy.input("First, what is your first name?", default = "Yuu")

        $ firstName = firstName.strip()
        $ lastName = renpy.input("I see. Now, what is your last name?,", default = "Shijou")

        $ lastName = lastName.strip()
    
    
        
        "'%(firstName)s %(lastName)s'. Is this your name?"
        menu:
            "Yes.":
                $ confirmedName = True 
                $ fakeMcName.setFirstName(firstName)
                $ fakeMcName.setLastName(lastName)
            "No.":
                "Very well. I shall ask you again then."
    
    "It's a pleasure to meet you, [fakeMcName.firstName] [fakeMcName.lastName]."
    
    "Now that we have the introductions out of our way, I do believe it is time for you to begin your story."
    
    "Have fun."
    
    
    return
