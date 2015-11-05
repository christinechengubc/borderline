# You can place the script of your game in this file.


# The game starts here.
label start:
    
    
    scene fakebg sokawaii
    with dissolve
    
    "Salutations. I'm glad you can come here today. I hope you've been doing well."
    
    "Now before we begin, there are some questions I would like you to answer."

    while confirmedName == False:    
    
        $ firstName = renpy.input("First, what is your first name?", default = "Yuu")

        $ firstName = firstName.strip()
        $ lastName = renpy.input("I see. Now, what is your last name?", default = "Shijou")

        $ lastName = lastName.strip()
    
    
        "'%(firstName)s %(lastName)s'. Is this your name?"
       
        menu: 
            "'%(firstName)s %(lastName)s'. Is this your name?"
            "Yes.":
                $ confirmedName = True 
                $ fakeMcName.setFirstName(firstName)
                $ fakeMcName.setLastName(lastName)
            "No.":
                "Very well. I shall ask you again then."
    
    "It's a pleasure to meet you, [fakeMcName.firstName] [fakeMcName.lastName]."
    
    "Now that we have the introductions out of our way, I do believe it is time for you to begin your story."
    
    "Have fun."
        
    scene black
    with dissolve
    
    "..."
    
    "I open my eyes."
    
    scene fakebg bedroom
    with fade
    
    "It was morning, and as my friend didn’t wake me up, it must have been a weekend. The autumn sun was bright but heatless, streaming from the bare windows. "
    
    "I rolled over onto my back, before pushing myself upwards. My mind was still slow, but at the very least, my eyes could read the digital display of the alarm clock."
    
    MC "8:40AM… Monday…"
        
    "I yawn luxuriously, my brain kicking to normal capacity after that extra burst of oxygen."
    
    MC "Wait, Monday?"
    
    "Monday was a school day. And school starts at 9AM."
    
    "It takes me 15 minutes to take the bus there, and 30 minutes to walk there."
    
    "But the bus that I normally would have taken, the sluggish Number 16, had 20 minute intervals between each one. So, ultimately…"
    
    MC "Shit!"
    
    "I roll out of bed, bounce into my school uniform, grab my bag, ignore my breakfast-lusting stomach, and run out."
    
    "Halfway through the hallway, I pat my pockets to ensure that everything was in place: cellphone, wallet, and house keys, before rushing out."
    
    scene fakebg morningstreet
    with dissolve
    
    "Outside the two-floor dormitory that I lived in, the bus had already puttered off, obnoxiously mocking me with its semi-visible exhaust fumes."
    
    MC "Ugh…why didn’t Childhood Friend wake me up today? Was she sick or something?"
    
    "But she lived right across the street, or could have texted me, so…"
    
    "A smile tugged at my lips, despite the dire situation."
    
    MC "Well, it can’t be helped."
    
    "I stretch my arms, shake my legs, and run off."
    
    #no scene available yet
    scene black
    with dissolve
    
    "My name is [fakeMcName.firstName] [fakeMcName.lastName]."
    
    "I’m a normal first year in High School, and my parents work abroad, so I live in the dormitories."
    
    "I honestly just want to enjoy a regular life, but it seems that my luck is usually on the rotten side of things. "
    
    "Mornings are my weakness as well, and usually, my childhood friend would have woken me up…"
    
    "but, as misfortune would have it, she didn’t."
    
    MC "And on today of all days! There goes good fi- Uwah!"
    
    show eileen
    with dissolve
    
    "As I turned a corner, a woman with snow-white hair appears, and I jump to the side, only barely managing to avoid her. "
    
    "No surprise showed up in her ice-chip eyes, and the well-tailored clothes she wore shared that same ‘untouchable’ feel. "
    
    "A proper ice queen, it looked like."
    
    "Ah, but there’s no time to think of such things now!"
    
    MC "Sorry about that!"
    
    hide eileen
    with dissolve
    
    "With that, I run. Chances are, I’d see her again anyways."
    
    "After all, for some uncanny reason, every cute girl I meet seemed to get wrapped up in my life one way or the other. "
    
    "Foreigner-chan would probably pop up later during the day as a new occupant in the dormitories. Maybe show up as a high school teacher, even?"
    
    "If it rains, perhaps she’ll be caught outside without an umbrella or something."
    
    #school bell rings
    #not sure what bg for this or how to insert
    scene fakebg morningstreet
    with fade
                                                                                               
    MC "Ah, is it already too late?"
    
    MC "Just my luck…"
    
    #car engine noise
    #Ojou-sama enters with car
    show sylvie
    with dissolve
    
    OJ "Ohohoho, my betrothed, in a bind? Saitama-san didn’t wake you up?"
    
    MC "Oh, Ojou-sama, morning to you too."
    
    OJ "Not simply a morning, but a gorgeous morning, my beloved. Please,"
    
    #car door opens
    #car door click sound
    
    OJ "Come in. I’ll make sure that you get to school on time, my darling."
    
    MC "Ah, thanks!"
    
    #scene change?
    
    "Ojou-sama is such a good friend! I really should find a way to express my thanks in the future, but what would I even give such a wealthy lady?"
    
    "She looks at me with expectant eyes as I relax in the plush interior of the luxury vehicle. "
    
    "The surround sound stereo was playing warm, romantic music, and the fragrance of vanilla, Ojou-sama’s signature perfume, was strong in the air."
    
    "Energy drinks lined the miniature drink bar as well, probably because she always worked so hard,"
    
    "and her chauffeur must have been a man who understood that the mistress needed privacy, for the driver’s seat was sealed off from the rest of the spacious car."
    
    "I look back at her and smile, before turning my attention to the tinted windows and the passing scenery."
    
    OJ "Sigh… I suppose one should have expected such a vanilla response from honey."
    
    MC "Uh..ok?"
    
    scene black
    with fade
    
    "end of scene 1"
    
    jump scene2
    
    
    
    
    
    return
