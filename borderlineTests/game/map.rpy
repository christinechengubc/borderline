label town_map:
    call screen planets #Displaying the imagemap

screen planets: #Preparing the imagemap
    imagemap:
        ground "images/townmap.jpg"
        hover "images/hoverimage.png"
        
        # hotspot (150, 244, 184, 102) hovered ShowTransient("caption_text", txt="Here is Mercury!") clicked Jump("mercury")
        # hotspot (544, 43, 168, 104) hovered ShowTransient("caption_text", txt="Here is Venus!") clicked Jump("venus")
        # hotspot (533, 325, 197, 109) hovered ShowTransient("caption_text", txt="Here is Earth!") clicked Jump("earth") 
        hotspot (150, 244, 184, 102) hovered ShowTransient("say", what="Here is Mercury!", who=None) unhovered Hide("say") clicked Jump("mercury")
        hotspot (544, 43, 168, 104) hovered ShowTransient("say", what="Here is Venus",who=None) unhovered Hide("say") clicked Jump("venus")
        hotspot (533, 325, 197, 109) hovered ShowTransient("say", what="Here is Earth!",who=None) unhovered Hide("say") clicked Jump("earth") 


screen caption_text(txt):
    text txt xalign .5 yalign .9 text_align 0.5 color "#FFFFFF" outlines [(3, "#000", 1, 1)] size 20

label mercury:
    "It is Mercury."
    jump town_map

label venus:
    "It is Venus."
    jump town_map

label earth:
    "It is Earth."
    jump town_map
    
label mars:
    "It is Mars."
    jump town_map