# The script of the game goes in this file.

# Character Variables

define d = Character("Dick")
define m = Character("Morningstar")
define fd = Character("[fd]")
define fm = Character("[fm]")

# The game starts here

label start:

    # this is the start of the game/demo. This is the first section: pregame. It lets us get acquainted with our protagonists and their bickering. 

  "I look at my reflection and try to stay positive. However, I can't get the corner of my mouth to turn upwards at what I see."

  "An undercover mission required some level of disguise and an appearance like mine was hard to mistake, to put it mildly. I was trying to hide that, but I was doing a shit job."

	"I got this job because I'm good at what I do, very good in fact. However, it was stupid moments like this that made me have doubts about my own abilities. Luckily, I wasn't being paid to do this part."

	"I was getting paid to kill someone. That was something I should have no issues with, at least."

	"Still, I can't help but feel some mix of disgust and disappointment as I stare at the sickly green appearance of my cheeks. This definitely wasn't my forte and I just wish by the end of it I could make my face passable."
    
    scene bg homebase

    # this is a false choice: it doesn't take you out of the scene but it provides more player interactivity. it can be boring to just read for too long without something to do so I include these to keep the player awake.

    menu
        "I feel a frigid hand on the back of my neck.":
            jump pregame_1

label pregame_1: 

    d "What's wrong with you?"

    show dick at left

    "I try to shoot daggers at the offender, but she's an immovable object." 

    m "You missed that entire side of your neck with your base coat because you were hiding it with your hair. You know, the hair you plan on tying back?"

    "Of course, that was to be expected from the snarly character I was going to be accompanied by. She's damn good at what she does, but she sure wasn't mild-mannered."

    "That's part of what I like about her, though."

    show morningstar at right

    d "You know, you didn't have to do that though, you could've just told me?"

    m "But then you'd miss it and just do it on the other side."

    "All I could do was groan until my throat hurt while I started work on that side of my neck. She was absolutely right, I did miss it, but her methods still sucked."

    d "I still can't believe you're being expected to act like a member of high society."

    m "Well, I was raised as one so of course I know how to act. It's not like I'm \"some common robble from the street being dragged in,\" you ass."

    d "Of course you aren't. However, I do happen to recall and remember more than a fair share of stories of your behavior."

    m "What is that supposed to mean?"

    d "Oh..."

    d "Just that you have a history of being overwhelmingly undersocial or getting pissdrunk to the point of causing conflict. I mean, I would hardly find that appropriate at any gathering, much fewer ones amongst the disgustingly rich."

    "She sputters for a moment and looks like she's ready to bite my head off. That was always just the right reward for pushing the right button."

    m "Well, who was always right there when I hid or got a little too tipsy?"

    d "Someone had to clean it up."

    m "Oh, sorry Pepe Le Pew, I didn't know that you were that kind of cleaner."

    "She ends with a raspberry. It was utterly juvenile but still not unfunny. Even then..."

    menu
        "I should move the conversation along.":
            jump pregame_2

label pregame_2:

    d "Now I expect neither of us will be behaving like that for our job, I think it might be good to talk more about more of the details. I have everything I should need but I want to make sure you actually managed to remember it all."

    m "Of course I do, I was the one who received the directions in the first place."

    m "Plus with the amount of money we're getting paid I don't think I could ever forget."

    m "We're going to start out with a bang, killing a bride on her wedding day during the reception. Put the fear of god into everyone watching."

    m "Her name is (bullshit name), soon to be (bullshittier name). It shouldn't be hard to tell her apart though, unless someone else gets the bright idea to wear white during a wedding."

    d "Anything else?"

    m "I don't know, dipshit, does it look like we have anything else prepared?"

    d "Oh no, Madam Morningstar, I simply could never guess if we had anything else we planned on doing. I mean aren't we just going to barge right in and shoot her point blank and then go to jail for the rest of our miserable lives?"

    "At that, all I was left with was an exasperated sigh as she started to ignore me."

    "It was actually pretty nice getting the chance to piss each other off and push as many buttons as we'd like. It got it out of our systems before we had to go full business and nothing ever carried much real bite anyway."

    "After a few beats, it did become apparent she wasn't going to humor me anymore, so I opted to start up again."

    d "So, do you remember our names? I'm going with..."

    # Here is the name code, modified straight from Renp'y. Even then, it tends not to work properly so you still have to insert your own and if you enter in nothing it just sets your name to nothing. Oops, lol. 
    
    python:
        fd = renpy.input(_("What's Dick's Alias"))

        fd = fd.strip() 
        
        if not fd.strip:
            fd = "Austin"

    d "[fd]."

    "Now that was a fine name."

    m "Where'd you find that one?"

    "Maybe that opinion wasn't universal."

    d "It's the name of the guy who owns that (type of store) in (other town)."

    m "Ah, so just another someone miserable in that shit hole, but he's rich so it's fine."

    d "You got it."

    python:
        fm = renpy.input(_("What's Morningstar's Alias"))

        fm = fm.strip() 
        
        if not fm.strip:
            fm = "Jora"

    m "I think I'm going with [fm], like that pastor's wife."

    d "Isn't that the one always complaining about her pastor husband?"

    m "Does anyone in around here have something nice to say about their husbands?"

    d "Fair enough, even if it's a bit morbid to say when we're about to attend a wedding."

    m "That'll be the only bride to not have anything to say about her groom, nice or otherwise."

    m "And we're still using my family name, correct?"

    d "It's not like I have a good one to share, and making one up will just make us sound like posers."

    m "I understand. Even if [fd] Morningstar is a pretty shitty name."

    d "I think that's just because you go by it so it poisons everything else. So I must concede to having a worse name."

    m "Whatever you say, Richard."

    m "Are you done with your make-up yet? I think you look beautiful as a bride but we might have to get going unless we want to miss the entire wedding."

    "I'm giving myself a once over and by this point, and somehow, I looked fine. Not necessarily good, but just fine."

    "I gave Morningstar her own once over as well. There was a level of envy that she really didn't have to do much and still looked good. Plus the formalwear was very different from what I was used to, but not bad."

    d "I know I look beautiful always, but I guess I've finally reached the level of perfection I wanted"

    m "Sorry, I forgot your vanity knows no bounds."

    # Just a little message to keep you in check.

    "This is the end of the demo you are playing."

    # This ends the game.

    return
