##### This is the main script of the game, intended to be the entire script for the demo and the first chapter of the full game #####

label start:

    # This is the start of the game/demo. This is the first section: pregame. It lets us get acquainted with our protagonists and their bickering. 

    show cg 1
    
    "Dick looked at his reflection and tried to stay positive. However, the corners of his mouth refused to turn upwards at what he saw." 

    "An undercover mission required some level of disguise and an appearance like his was hard to mistake, to put it mildly. He was trying to hide that, but he was doing a shitty job."

    "He got this job because he was good at what he did, very good in fact. However, it was stupid moments like this that made him have doubts about his own abilities. Luckily, he wasn't being paid to do this part."

    "He was getting paid to kill someone. That was something he should have no issues with, at least."

    "Still, he couldn't help but feel some mix of disgust and disappointment as he stared at the sickly green appearance of his cheeks. This definitely wasn't his forte and he just wished by the end of it he could make his face passable."
    
    hide cg 1

    # This is a false choice: It doesn't take you out of the scene but it provides more player interactivity. it can be boring to just read for too long without something to do so I include these to keep the player awake.

    menu:
        "He feels a frigid hand on the back of his neck.":
            jump pregame_1

label pregame_1: 

    scene bg homebase

    d "What's wrong with you?"

    show dick 1 75 sulk at my_left
    with lsmovement

    "He tried to shoot daggers at the offender, but she was an immovable object." 

    show morningstar open at my_right, speak
    with rsmovement

    m "You missed that entire side of your neck with your base coat because you were hiding it with your hair. You know, the hair you plan on tying back?"

    hide morningstar
    show morningstar rbf at my_right

    "Of course, that was to be expected from the snarly character he was going to be accompanied by. She was damn good at what she did, but she sure wasn't mild-mannered."

    "That's part of what he liked about her, though."

    hide dick
    show dick 1 75 pissy at my_left, speak

    d "You know, you didn't have to do that though, you could've just told me?"

    hide dick
    show dick 1 75 sulk at my_left
    hide morningstar
    show morningstar open at my_right, speak

    m "But then you'd miss it and just do it on the other side."

    hide morningstar
    show morningstar rbf at my_right

    menu:
        "Bring the makeup brush to that side of his neck.":
            jump pregame_2

label pregame_2:

    "All Dick could do was groan until his throat hurt while he worked on that side of his neck. She was absolutely right, he did miss it, but her methods still sucked."

    hide dick
    show dick 1 75 open at my_left, speak

    d "I still can't believe you're being expected to act like a member of high society."

    hide dick
    show dick 1 75 rbf at my_left
    hide morningstar
    show morningstar frown open at my_right, speak

    m "Well I am a member in case you forgot. It's not like I'm \"some common rabble from the street being dragged in.\""

    hide morningstar
    show morningstar frown at my_right
    hide dick
    show dick 1 75 open at my_left, speak

    d "Of course you aren't. However, I do happen to recall more than a fair share of stories of your behavior."

    hide dick
    show dick 1 75 smile at my_left
    hide morningstar
    show morningstar frown open at my_right, speak

    m "Fuck does that mean?"

    hide morningstar
    show morningstar frown at my_right
    hide dick
    show dick 1 75 smile open at my_left, speak

    d "Oh..."

    hide morningstar
    show morningstar shock at my_right, tremble

    d "Just that you have a history of being overwhelmingly undersocial or getting pissdrunk to the point of causing conflict. I mean, I would hardly find that appropriate at any gathering, much less ones amongst the disgustingly rich."
 
    hide dick
    show dick 1 75 smile at my_left

    "She sputtered for a moment and looked like she was ready to bite his head off. That was always just the right reward for pushing the right button."

    hide morningstar
    show morningstar o at my_right, speak
    
    m "And who was always there when I was tipsy or hiding?"

    hide morningstar
    show morningstar smile at my_right
    hide dick
    show dick 1 75 smile open at my_left, speak

    d "Someone had to clean it up."

    hide dick
    show dick 1 75 smile at my_left
    hide morningstar
    show morningstar smile open at my_right, speak

    m "Wow, didn't know you had to clean where the sun doesn't shine."

    hide morningstar
    show morningstar smile at my_right

    "She blew a raspberry. It was utterly juvenile but still not unfunny. Even then..."

    menu:
        "He should move the conversation along.":
            jump pregame_3

label pregame_3:

    hide dick
    show dick 1 50 open at my_left, speak

    d "Now, I expect neither of us will be behaving like that for our job. I think it might be good to talk more about more of the details. I have everything I should need but I want to make sure you actually managed to remember it all."

    hide dick
    show dick 1 50 neutral at my_left
    hide morningstar
    show morningstar o at my_right, speak

    m "The hell's that supposed to mean? I was given the directions initially, not you."

    hide morningstar
    show morningstar smile open at my_right, speak

    m "But if baby needs a refresher, I guess I can do it without making you get on your hands and knees. Plus we're about to make enough money to blow our dicks off."

    hide morningstar
    show morningstar unhinged at my_right, speak

    m "We're going to start out with a bang, killing a bride on her wedding day during the reception. Put some fear of god into everyone attending."

    hide morningstar
    show morningstar smile open at my_right, speak

    m "Her name is (bullshit name), soon to be (bullshittier name). It shouldn't be hard to tell her apart though, unless someone else gets the bright idea to wear white during a wedding."

    hide morningstar
    show morningstar rbf at my_right
    hide dick
    show dick 1 50 open at my_left, speak
    
    d "Anything else?"

    hide dick
    show dick 1 50 neutral at my_left
    hide morningstar
    show morningstar frown open at my_right, speak

    m "I don't know, dipshit, does it look like we have anything else prepared?"

    hide morningstar
    show morningstar frown at my_right
    hide dick
    show dick 1 50 smile open at my_left, speak
    
    d "Oh no, Madam Morningstar, I simply could never guess if we had anything else we planned on doing. I mean aren't we just going to barge right in and shoot her point blank and then go to jail for the rest of our miserable lives?"

    hide dick
    show dick 1 50 neutral at my_left

    "At that, all he was left with was an exasperated sigh as she ignored him."

    hide dick
    show dick 1 50 smile at my_left

    "It was actually pretty nice getting the chance to piss each other off and push as many buttons as they'd like. It got it out of their systems before they had to go full business and nothing ever carried much real bite anyway."

    hide dick
    show dick 1 50 rbf at my_left

    "After a few beats, it did become apparent she wasn't going to humor him at this point so he spoke up again."

    hide dick
    show dick 1 50 open at my_left, speak

    d "So, do you remember our names? I'm going with..."

    # Here is the name code, modified straight from Renp'y. Even then, it tends not to work properly so you still have to insert your own and if you enter in nothing it just sets your name to nothing. Oops, lol. 
    
    python:
        fd = renpy.input(_("What's Dick's Alias"))

        fd = fd.strip() 
        
        if not fd.strip or fd == "Dick" or fd == "":
            fd = "Mickey"

        if fd == "Austin" or fd == "austin" or fd == "Austin Powers" or fd == "austin danger powers" or fd == "austin powers" or fd == "Austin Danger Powers":
            renpy.jump("austin_powers")

    d "[fd]."

    hide dick
    show dick 1 50 smile at my_left

    "Now that was a fine name."

    hide morningstar
    show morningstar o at my_right, speak

    m "Why? Where did you get that? It sucks. You don't look like a [fd]."

    hide morningstar
    show morningstar rbf at my_right

    "Maybe that opinion wasn't universal."

    hide dick
    show dick 1 50 open at my_left, speak

    d "It's the name of the guy who owns that (type of store) in (other town) and I thought I'd borrow it."

    hide dick
    show dick 1 50 neutral at my_left
    hide morningstar
    show morningstar open at my_right, speak

    m "Ah, so you took it from someone completely miserable in that shit hole, but he's rich so it's fine."

    hide morningstar
    show morningstar rbf at my_right
    hide dick
    show dick 1 50 smile open at my_left, speak

    d "You got it."

    hide dick
    show dick 1 50 smile at my_left
    
    jump morningstar_name

label austin_powers:

    d "[fd]."

    hide dick
    show dick 1 50 smile at my_left
    hide morningstar
    show morningstar smile open at my_right, speak

    m "Like Austin Powers?"

    hide morningstar
    show morningstar smile at my_right
    hide dick
    show dick 1 50 smile open at my_left, speak

    d "You know it, baby!"

    hide dick
    show dick 1 50 smile at my_left

    "Dick rrreow-ed like a cat, or maybe more accurately a dying one, and got a hearty chuckle back."

    hide morningstar
    show morningstar smile open at my_right, speak

    m "Maybe after this mission we can see if you really shag like a mink."

    hide morningstar
    show morningstar smile at my_right
    hide dick
    show dick 1 50 smile open at my_left, speak

    d "Groovy!"

    hide dick
    show dick 1 50 smile at my_left
    hide morningstar
    show morningstar open at my_right, speak

    jump morningstar_name

label morningstar_name:

    python:
        fm = renpy.input(_("What's Morningstar's Alias"))

        fm = fm.strip() 
        
        if not fm.strip or fm == "Morningstar" or fm == "":
            fm = "Mallory"

        if fm == "Felicity" or fm == "felicity" or fm == "Felicity Shagwell" or fm == "felicity shagwell":
            renpy.jump("felicity_shagwell")

    m "I'm going with [fm], like that one pastor's wife with the lopsided boobjob."

    hide morningstar
    show morningstar rbf at my_right
    hide dick
    show dick 1 25 open at my_left, speak

    d "Isn't that the one always complaining about her husband to anyone who'd listen? She's miserable to be around."

    hide dick
    show dick 1 25 neutral at my_left
    hide morningstar
    show morningstar o at my_right, speak

    m "Does anyone in around here have something nice to say about their husbands?"

    hide morningstar
    show morningstar rbf at my_right
    hide dick
    show dick 1 25 open at my_left, speak

    d "Fair enough, even if it's a bit morbid to say when we're about to attend a wedding."

    hide dick
    show dick 1 25 neutral at my_left
    hide morningstar
    show morningstar smile open at my_right, speak

    m "That'll be the only bride to not have anything to say about her groom, nice or otherwise."

    hide morningstar
    show morningstar smile at my_right
    hide dick
    show dick 1 25 pissy at my_left, speak

    d "That's so much worse."

    hide dick
    show dick 1 25 rbf at my_left
    hide morningstar
    show morningstar open at my_right, speak

    m "It's not like I'm lying. Unless her last words are telling him to fuck himself."

    jump pregame_4

label felicity_shagwell:

    hide morningstar
    show morningstar smile open at my_right, speak

    m "I'm going with [fm]."

    hide morningstar
    show morningstar smile at my_right

    "Morningstar didn't even have to say where she got that one from."

    hide dick
    show dick 1 25 smile open at my_left, speak

    d "Now is it Felicity Shagwell or Shag-very-well?"

    hide dick
    show dick 1 25 smile at my_left

    "He couldn't help but snicker at his own joke."

    hide morningstar
    show morningstar smile open at my_right, speak

    m "You tell me after we get done."

    hide morningstar
    show morningstar smile at my_right
    hide dick
    show dick 1 25 smile open at my_left, speak

    d "Oh behave!"

    hide dick
    show dick 1 25 smile at my_left

    jump pregame_4

label pregame_4:

    hide morningstar
    show morningstar open at my_right, speak
    
    m "And we're still using my family name?"

    hide morningstar
    show morningstar rbf at my_right
    hide dick
    show dick 1 25 open at my_left, speak

    d "It's not like I have a good one to share, and making one up will just make us sound like posers."

    hide dick
    show dick 1 25 neutral at my_left
    hide morningstar
    show morningstar open at my_right, speak

    m "You'll just have to be some ugly cousin of mine. [fd] Morningstar is dogshit, though."

    hide morningstar
    show morningstar rbf at my_right
    hide dick
    show dick 1 25 smile open at my_left, speak

    d "I think that's just because you go by it, so it poisons everything else. So I must concede to having a worse name."

    hide dick
    show dick 1 25 smile at my_left
    hide morningstar
    show morningstar open at my_right, speak

    m "Whatever you say, *Dick*."

    hide dick
    show dick 1 25 sulk at my_left

    m "Are you done with your make-up yet? I think you look beautiful as a bride, but, we might have to get going unless we want to miss the entire wedding."

    hide morningstar
    show morningstar rbf at my_right
    
    "He gave himself a once over and by this point, he looked fine. Not necessarily good, but just fine."

    hide dick
    show dick 1 25 neutral at my_left

    "He gave Morningstar her own once over as well. There was a level of envy that she really didn't have to do much and still looked good. Plus, the formalwear was very different from what he was used to, but not bad."
   
    menu:
        "Put on the finishing touches.":
            jump pregame_5
   
label pregame_5:

    hide dick
    show dick at my_left, speak

    d "I know I look beautiful always, but I guess I've finally reached the level of perfection I wanted."

    hide dick
    show dick at my_left
    hide morningstar
    show morningstar smile open at my_right, speak

    m "Sorry, I forgot just how many of your farts you sniff."

    hide morningstar
    show morningstar smile at my_right

    menu:
        "Leave to investigate the venue.":
            jump investiage_1

label investiage_1:

    scene investiagte_1

    ""

    # Just a little message to keep you in check.

    "This is the end of the demo you are playing."

    # This ends the game.

    return
