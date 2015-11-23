label town_map:
    scene black
    call screen city #Displaying the imagemap

screen city: #Preparing the imagemap
    viewport:
        child_size (1280, 720)
        draggable True
        xinitial current_location.x
        yinitial current_location.y
    
        imagemap:
            ground "images/townmap.jpg"
            hover "images/hoverimage.png"
            
            for location in locations:
                hotspot location.getHotspot() hovered ShowTransient("say", what=location.description, who=None) unhovered Hide("say") clicked [SetVariable("current_location", location), Jump(location.label)]
            
            # hotspot (150, 244, 184, 102) hovered ShowTransient("caption_text", txt="Here is Mercury!") clicked Jump("mercury")
            # hotspot (544, 43, 168, 104) hovered ShowTransient("caption_text", txt="Here is Venus!") clicked Jump("venus")
            # hotspot (533, 325, 197, 109) hovered ShowTransient("caption_text", txt="Here is Earth!") clicked Jump("earth") 
            # hotspot (150, 244, 184, 102) hovered ShowTransient("say", what="School. Your most favorite place in the whole wide world.", who=None) unhovered Hide("say") clicked Jump("school")
            # hotspot (544, 43, 168, 104) hovered ShowTransient("say", what="City Hall. You can do stuff here.",who=None) unhovered Hide("say") clicked Jump("city_hall")
            # hotspot (533, 325, 197, 109) hovered ShowTransient("say", what="Feeling good? Check yourself out.",who=None) unhovered Hide("say") clicked Jump("profile") 
            # hotspot (910, 247, 186, 108) hovered ShowTransient("say", what="Go home and watch some anime. Don't bother coming out again.", who=None) unhovered Hide("say") clicked Jump("home")
            
        $ tVal = False
        ### Potentially iterating to find where the location marker will be place
        ##      TODO:
        #          - create Location class (?)
        #          - create Event class (?)
        #          - Decide on coupling
        # showif tVal:
        #    add "images/event_marker.png" pos (150, 244)
        
        # for e in events:
        #    if e.important:
        #        add "images/event_marker.png" pos e.location.pos

    frame: 
        xpadding 10
        ypadding 10
        xalign 0.0
        yalign 0.0
        xsize 250
        
        python: 
            after = "th"
            if (calendar.day == 1 or calendar.day == 21 or calendar.day == 31):
                after = "st"
            if (calendar.day == 2 or calendar.day == 22):
                after = "nd"
            if (calendar.day == 3 or calendar.day == 23):
                after = "rd"
                
        vbox:
            text "Date: " + "[calendar.day]" + after + " of " + calendar.get_month()
            null height 10
            text "Time: "
            null height 10
            text "Weather: "
            null height 10
        

screen caption_text(txt):
    text txt xalign .5 yalign .9 text_align 0.5 color "#FFFFFF" outlines [(3, "#000", 1, 1)] size 20


label school:
    "Your school is a beautiful place. If only we had its background image."
    jump town_map

label city_hall:
    "The city hall is currently empty."
    jump town_map

label profile:
    "Too bad. Not much to see here."
    jump town_map
    
label home:
    "Turn off the lights. Slip under the blankets. Bring out the body pillow of your Waifu."
    jump town_map