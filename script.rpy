##### This is the main script of the game, intended to be the entire script for the demo and the first chapter of the full game #####

label start:

    # This is the start of the game/demo. This is the first section: pregame. It lets us get acquainted with our protagonists and their bickering. 

    # Variables

    $ investigate1 = False
    $ investigate2 = False
    $ investigate3 = False
    $ investigate4 = False

    $ hotelsee = False
    $ gardensee = False
    $ archessee = False
    $ fairylightssee = False
    $ stonessee = False

    $ aislesee = False
    $ altersee = False
    $ benchessee = False
    $ extensionsee = False

    $ mingle1 = False
    $ mingle2 = False
    $ mingle3 = False
    $ mingle4 = False

    $ snakesee = False
    $ snakeinfo = False
    $ glovessee = False
    $ venommethod = 0

    $ heroin = False
    $ cokehabit = False
    $ poisonmethod = 0

    $ malemale = False
    $ femalefemale = False
    $ faultylights = False
    $ affair = False
    $ affairsnitch = False
    $ heroinsnitch = False
    $ bridetrust = False
    $ electricmethod = 0

    $ items = 0
    $ interactions = 0

    $ letter = 0

    jump game_start

label game_start:

    show cg1
    
    "Dick looked at his reflection and tried to stay positive. However, the corners of his mouth refused to turn upwards at what he saw." 

    "An undercover mission required some level of disguise and an appearance like his was hard to mistake, to put it mildly. He was trying to hide that, but he was doing a shitty job."

    "He got this job because he was good at what he did, very good in fact. However, it was stupid moments like this that made him have doubts about his own abilities. Luckily, he wasn't being paid to do this part."

    "He was getting paid to kill someone. That was something he should have no issues with, at least."

    "Still, he couldn't help but feel some mix of disgust and disappointment as he stared at the sickly green appearance of his cheeks. This definitely wasn't his forte and he just wished by the end of it he could make his face passable."
    
    hide cg1

    # This is a false choice: It doesn't take you out of the scene but it provides more player interactivity. it can be boring to just read for too long without something to do so I include these to keep the player awake.

    menu:
        "He feels a frigid hand on the back of his neck.":
            pass 

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
            pass

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
            pass

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

    m "Her name is Moira Drew, soon to be Moira Wolfe. It shouldn't be hard to tell her apart though, unless someone else gets the bright idea to wear white during a wedding."

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
        
        if not fd.strip or fd == "Dick" or fd == "dick" or fd == "":
            fd = "Mickey"

        if fd == "Austin Powers" or fd == "austin danger powers" or fd == "austin powers" or fd == "Austin Danger Powers":
            renpy.jump("austin_powers")

        if fd == "James Bond" or fd == "james bond" or fd == "Bond" or fd == "bond":
            renpy.jump("james_bond")

        if fd == "Dexter Morgan" or fd == "dexter morgan" or fd == "Kyle Butler" or fd == "kyle butler" or fd == "Jim Lindsey" or fd == "jim lindsey":
            renpy.jump(dexter_morgan)

        if fd == "Twilight" or fd == "twilight" or fd == "Agent Twilight" or fd == "agent twilight" or fd == "Loid Forger" or fd == "loid forger":
            renpy.jump(twilight)

        if fd == "Agent 47" or fd == "agent 47" or fd == "Agent Forty-Seven" or fd == "agent forty-seven":
            renpy.jump("agent_47")

        if fd == "Shithole" or fd == "shithole":
            renpy.jump("shithole")

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

    d "It's the name of the guy who owns that liqour store in (other town) and I thought I'd borrow it."

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
    hide morningstar
    show morningstar open at my_right, speak
    
    jump morningstar_name

label shithole:

    d "[fd]."

    hide dick
    show dick 1 50 smile at my_left
    hide morningstar
    show morningstar frown at my_right

    "Morningstar looked at him with the eyes of a game developer who really wanted to throttle her friends."

    hide morningstar
    show morningstar frown open at my_right, speak

    m "Fuck off."

    $ fd = "Mickey"

    hide dick
    show dick 1 50 smile at my_left
    hide morningstar
    show morningstar open at my_right, speak

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

label james_bond:

    d "Bond, James Bond."

    hide dick
    show dick 1 50 smile at my_left
    hide morningstar
    show morningstar shock at my_right

    "Morningstar looked dumbfounded for a moment."

    hide morningstar
    show morningstar open at my_right, speak

    m "Holy shit."

    hide morningstar
    show morningstar frown open at my_right, speak

    m "You're going to rat us out with the fakest name ever."

    hide morningstar
    show morningstar frown at my_right
    hide dick
    show dick 1 50 smile open at my_left, speak

    d "Oh come on, you know I have the charisma to pull it off."

    hide dick
    show dick 1 50 smile at my_left

    "She stared at him like he grew another head."

    hide dick
    show dick 1 50 frown open at my_left, speak

    d "Not to you, you're immune with nothing but hate in your heart for my wiles."

    hide morningstar
    show morningstar smile at my_right
    hide dick
    show dick 1 50 smile at my_left

    "She snorted. Dick was chuffed with himself that he got her with that one."

    hide morningstar
    show morningstar rbf at my_right
    hide dick
    show dick 1 50 smile open at my_left, speak

    d "Come on, think about Sidney Marlowe."

    hide morningstar
    show morningstar o at my_right, speak
    hide dick
    show dick 1 50 smile at my_left

    m "I don't think that counts."

    hide morningstar
    show morningstar rbf at my_right
    hide dick
    show dick 1 50 open at my_left, speak

    d "It does. I single-handedly got her to break up with her boyfriend without any fake cheating allegations after one conversation."

    hide morningstar
    show morningstar open at my_right, speak
    hide dick
    show dick 1 50 neutral at my_left

    m "Guess her parents were pretty happy about that."

    hide morningstar
    show morningstar rbf at my_right
    hide dick
    show dick 1 50 smile open at my_left, speak

    d "They were the ones who bribed me to do it."

    hide morningstar
    show morningstar open at my_right, speak
    hide dick
    show dick 1 50 neutral at my_left

    m "I think that says more about both of your gullability then anything on you being suave enough to pull off something as absurd as [fd]."
    hide morningstar
    show morningstar shock at my_right
    hide dick
    show dick 1 50 smile open at my_left, speak

    d "Just watch me, I mean you can be my... Pussy Galore."

    hide dick
    show dick 1 50 smile at my_left
    hide morningstar
    show morningstar open at my_right, speak

    jump morningstar_name

label twilight:

label agent_47:

label dexter_morgan:

    d "[fd]."

    hide morningstar
    show morningstar o at my_right, speak
    hide dick
    show dick 1 50 smile at my_left

    m "That name just makes you sound like a serial killer."

    hide morningstar
    show morningstar rbf at my_right
    hide dick
    show dick 1 50 open at my_left, speak

    d "I have to disagree, but even then, how wrong would it be?"

    hide morningstar
    show morningstar open at my_right, speak
    hide dick
    show dick 1 50 neutral at my_left

    m "We're assassins, I think there's a line in there somewhere."

    hide morningstar
    show morningstar rbf at my_right
    hide dick
    show dick 1 50 open at my_left, speak

    d "Then what do you think that line is?"

    hide morningstar
    show morningstar o at my_right, speak
    hide dick
    show dick 1 50 neutral at my_left

    m "Serial killers have some darkness in them, we don't."

    hide morningstar
    show morningstar neutral at my_right
    hide dick
    show dick 1 50 smile open at my_left, speak

    d "I thought it would just be that we get paid and they just do it for the thrill. Darkness is a little vague though, isn't it?"

    hide morningstar
    show morningstar o at my_right, speak
    hide dick
    show dick 1 50 smile at my_left

    m "You can't see it."

    hide morningstar
    show morningstar neutral at my_right, speak

    "She was right, she had her own... unique perspective on things. To put it some way other then to name-calling, be that on the positive or negative side."

    hide morningstar
    show morningstar open at my_right, speak

    m "We're just butchers, things have to die to keep society going even if it's other people."

    hide morningstar
    show morningstar rbf at my_right
    hide dick
    show dick 1 50 smile open at my_left, speak

    d "How vegan."

    hide morningstar
    show morningstar frown open at my_right, speak
    hide dick
    show dick 1 50 smile at my_left

    m "Oh shut the fuck up. Serial killers just jack off to it and have perpetual screams of danger where ever they go."

    hide morningstar
    show morningstar rbf at my_right
    hide dick
    show dick 1 50 open at my_left, speak

    d "I see it, half at least. Too much of sadists and not kosher enough."

    hide dick
    show dick 1 50 smile open at my_left, speak

    d "What would that make a masochist serial killer, then?"

    hide morningstar
    show morningstar smile open at my_right, speak
    hide dick
    show dick 1 50 smile at my_left

    m "Catholic."

    hide dick
    show dick 1 50 smile at my_left
    hide morningstar
    show morningstar open at my_right, speak

    jump morningstar_name

label morningstar_name:

    python:
        fm = renpy.input(_("What's Morningstar's Alias"))

        fm = fm.strip() 
        
        if not fm.strip or fm == "Morningstar" or fm == "morningstar" or fm == "":
            fm = "Mallory"

        if fm == "Felicity Shagwell" or fm == "felicity shagwell":
            renpy.jump("felicity_shagwell")

        if fm == "Pussy Galore" or fm == "pussy galore" or fm == "Pussy" or fm == "pussy":
            renpy.jump("pussy_galore")

        if fm == "Black Widow" or fm == "black widow" or fm == "Natasha Romanov" or fm == "natasha romanov":
            renpy.jump("black_widow")

        if fm == "Yor Forger" or fm == "yor forger" or fm == "Thorn Princess" or fm == "thorn princess" or fm == "Yor" or fm == "yor":
            renpy.jump("yor")

        if fm == "The Bride" or fm == "the bride":
            renpy.jump("the_bride")

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

    jump pregame

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

    jump pregame

label pussy_galore:
    m "[fm]."

    hide morningstar
    show morningstar rbf at my_right
    hide dick
    show dick 1 25 open at my_left

    "That was stupid."

    hide morningstar
    show morningstar smile at my_right
    hide dick
    show dick 1 25 smile at my_left

    "That was so, so stupid."

    hide morningstar
    show morningstar smile open at my_right, jitters
    hide dick
    show dick 1 25 smile open at my_left, jitters

    "Even then after just a few moments they couldn't help but laugh."

    hide morningstar
    show morningstar smile at my_right
    hide dick
    show dick 1 25 smile open at my_left, speak

    d "How, how do you suppose other people are supposed to refer to you?"

    hide morningstar
    show morningstar smile open at my_right, speak
    hide dick
    show dick 1 25 smile at my_left

    m "They'll just have to do better then us."

    hide morningstar
    show morningstar smile at my_right
    hide dick
    show dick 1 25 smile open at my_left, speak

    d "They have to just say \"Hello, P..p..\""

    hide morningstar
    show morningstar smile at my_right
    hide dick
    show dick 1 25 pissy at my_left, speak

    d "I can't even do it."

    hide morningstar
    show morningstar smile open at my_right, speak
    hide dick
    show dick 1 25 open at my_left

    m "Well I hope you have fun trying to introduce me."

    hide morningstar
    show morningstar smile at my_right
    hide dick
    show dick 1 25 pissy at my_left, speak

    d "How d-"

    hide morningstar
    show morningstar unhinged at my_right, speak

    m "Oh come on, don't be a PUSSY."

    hide morningstar
    show morningstar smile open at my_right, jitters
    hide dick
    show dick 1 25 smile open at my_left, jitters

    "They had to both shut up for a moment and get the rest of the giggles out before they could proceed with normal conversation again."

    jump pregame

label yor:

label black_widow:

label the_bride:

label pregame:

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
            pass

    hide dick
    show dick smile open at my_left, speak

    d "I know I look beautiful always, but I guess I've finally reached the level of perfection I wanted."

    hide dick
    show dick smile at my_left
    hide morningstar
    show morningstar smile open at my_right, speak

    m "Sorry, I forgot just how many of your farts you sniff."

    hide morningstar
    show morningstar smile at my_right

    menu:
        "Leave to investigate the venue.":
            $ persistent.opening_done = True
            jump investigate_1

label investigate_1:

    hide screen arrows3
    hide screen arrows2
    hide screen leaveinvestiagte
    hide screen purse

    if glovessee == False:
        show screen gloves
        scene investigate 1 gloves
    else:
        show screen invest1
        scene investigate 1        

    if investigate1 == False:
        "It didn't take long to get to the venue, a rented hotel with an outdoor setup. Just about everyone was busy doing things like getting ready, the perfect chance to poke around."
       
        $ investigate1 = True
    else:
        pass

    if venommethod == 2:
        show screen leaveinvestiagte
    elif poisonmethod == 1:
        show screen leaveinvestiagte
    elif electricmethod >= 4:
        show screen leaveinvestiagte
    else:
        pass

    call screen arrows1

label snake:

    hide screen arrows1
    hide screen leaveinvestiagte
    hide screen invest1
    hide screen gloves

    if snakesee == False:
        show dick red pissy at my_left, speak
        with lsmovement

        d "Holy shit, that's a big snake!"

        hide dick
        show dick red rbf at my_left
        show morningstar red o at my_right, speak
        with rsmovement

        m "Do you know what kind it is?"

        hide morningstar
        show morningstar red rbf at my_right
        hide dick
        show dick red pissy at my_left, speak

        d "I have no idea."

        hide morningstar
        show morningstar red o at my_right, speak
        hide dick
        show dick red rbf at my_left

        m "That sucks, if it were venomous then we'd be onto something. But we'd probably need something to get it to spit into or like throw it."

        hide morningstar
        show morningstar red rbf at my_right
        hide dick
        show dick red frown open at my_left, speak

        d "And maybe some protection of somekind?"

        hide morningstar
        show morningstar red open at my_right, speak
        hide dick
        show dick red frown at my_left

        m "Oh, yeah sure, that too."

        hide morningstar
        show morningstar red smile open at my_right, speak

        m "If you wanna be a pussy about it."

        hide morningstar
        show morningstar red smile at my_right
        hide dick
        show dick red frown open at my_left, speak

        d "Sometimes I wonder if you have a death wish."

        hide morningstar
        hide dick

        show snakegotten
        pause
        $ snakesee = True
        $ venommethod += 1
        $ items += 1
        $ interactions += 1                
        hide snakegotten

        jump investigate_1
    else:
        
        "Eugh, that thing isn't moving anytime soon is it? At least if they come up with a plan they don't have to worry about scowering the premises for it."

        jump investigate_1

label gloves:

    hide screen arrows1
    hide screen leaveinvestiagte
    hide screen invest1
    hide screen gloves

    show dick red smile open at my_left, speak
    with lsmovement      

    d "Look at what the cat dragged in!"

    hide dick
    show dick red open at my_left, speak

    d "Or more accurately what a lazy landscaper left."

    hide dick
    show dick red smile at my_left
    show morningstar red o at my_right, speak
    with rsmovement

    m "You look too excited to see just a pair of fucking gloves."

    hide morningstar
    show morningstar red rbf at my_right
    hide dick
    show dick red smile open at my_left, speak

    d "Why wouldn't I be? They're one of our best tools for any job."

    hide dick
    show dick red smile at my_left
    hide morningstar
    show morningstar red frown at my_right, speak

    m "..."

    hide morningstar
    show morningstar red frown at my_right
    hide dick
    show dick red neutral at my_left

    "Her gaze showed she clearly did not agree."

    hide morningstar
    show morningstar red frown open at my_right, speak
    hide dick
    show dick red smile open at my_left

    m "Aren't you already wearing gloves though?"

    hide morningstar
    show morningstar red frown at my_right
    hide dick
    show dick red smile open at my_left, speak

    d "Yes, but, these are rubber and mine are just cloth. They're protective and textured."

    hide dick
    show dick red open at my_left, speak

    d "Plus, you aren't wearing any."

    hide morningstar
    show morningstar red shock at my_right
    hide dick
    show dick red smile at my_left

    "Her face twisted at even just the thought of putting them on."

    hide morningstar
    show morningstar red frown open at my_right, speak
    hide dick
    show dick red smile at my_left

    m "I'd rather cut my palm open."

    hide morningstar
    show morningstar red frown at my_right
    hide dick
    show dick red rbf at my_left

    "Dick wasn't impressed, but still stowed them away just in case she needed them later or if he may need an upgrade."

    hide morningstar
    hide dick

    show glovesgotten
    $ glovessee = True
    $ venommethod += 1
    $ items += 1
    $ interactions += 1
    hide glovesgotten
    hide screen gloves

    jump investigate_1

label hotel:

    hide screen arrows1
    hide screen leaveinvestiagte
    hide screen invest1
    hide screen gloves

    if hotelsee == False:
        show morningstar red open at my_right, speak
        with rsmovement

        m "I feel like hotel wedding screams more trashy then fancy to me."

        hide morningstar
        show morningstar red rbf at my_right
        show dick red smile open at my_left, speak
        with lsmovement   

        d "Depends on how many stars it has. Less then 3, trashy, but 4 or 5 is riding high."

        hide morningstar
        show morningstar red open at my_right, speak

        m "It looks like a-"

        hide morningstar
        show morningstar red shock at my_right
        hide dick
        show dick red smile open at my_left, speak, jitters

        d "This one's a nice one: multiple pools, hot tubs, a personal jacuzzi..."

        hide morningstar
        show morningstar red frown at my_right

        "It didn't even look like Dick was listening to a word Morningstar said."

        hide morningstar
        show morningstar red frown open at my_right, speak

        m "Ground control to Major Tom."

        hide morningstar
        show morningstar red frown at my_right

        d "A day spa, they probably even have some specialty bath products, constant roomservice that means you can have as many towels as you want..."

        hide morningstar
        show morningstar red frown at my_right
        with Pause(1.0)
        show morningstar red smile at my_right
        with Pause (1.0)
        show morningstar red frown at my_right

        m "..."

        hide dick
        show dick red open at my_left, speak

        d "What did you say?"

        hide morningstar
        show morningstar red o at my_right, speak
        hide dick
        show dick red neutral at my_left

        m "How about we go somewhere else."

        $ hotelsee = True
        $ interactions += 1

        hide morningstar
        hide dick        

        jump investigate_1
    else:
        "Looking at the hotel again, maybe it was a good idea to do a pool day, spa day, something day sometime in the near future."

        jump investigate_1

label arches:

    hide screen arrows1
    hide screen leaveinvestiagte
    hide screen invest1
    hide screen gloves

    if archessee == False:
        show morningstar red open at my_right, speak
        with rsmovement

        m "They have way too many of those."

        hide morningstar
        show morningstar red rbf at my_right
        show dick red smile open at my_left, speak
        with lsmovement

        d "Well, if you're rich, why not live in excess?"

        hide morningstar
        show morningstar red open at my_right, speak
        hide dick
        show dick red smile at my_left

        m "They aren't even real, though. It's garbage."

        hide morningstar
        show morningstar red rbf at my_right
        hide dick
        show dick red smile at my_left

        "Dick couldn't deny that, the leaves only looked faker next to the real thing only feet away. It was too obvious to the point of being distracting."

        hide morningstar
        show morningstar red rbf at my_right
        hide dick
        show dick red smile open at my_left, speak

        d "Maybe it's expensive garbage, at least? Could be nicer then you assume."

        hide morningstar
        show morningstar red frown at my_right
        hide dick
        show dick red neutral at my_left

        "She wasn't impressed."

        hide morningstar
        show morningstar red rbf at my_right
        hide dick
        show dick red open at my_left, speak

        d "I'm trying to be respectful, there are always worse they could do."

        hide morningstar
        show morningstar red frown open at my_right, speak
        hide dick
        show dick red frown at my_left

        m "Just say it looks like shit and move on."

        hide morningstar
        show morningstar red rbf at my_right
        hide dick
        show dick red frown open at my_left, speak

        d "Fine, it looks like shit."

        hide morningstar
        show morningstar red smile at my_right
        hide dick
        show dick red frown at my_left

        "He looked somewhere between relieved and liked he had to force himself to say it."

        $ archessee = True
        $ interactions += 1

        hide morningstar
        hide dick

        jump investigate_1
    else:
        "Fake plastic arches."

        jump investigate_1

label fairylights:

    hide screen arrows1
    hide screen leaveinvestiagte
    hide screen invest1
    hide screen gloves

    if fairylightssee == False:
        show dick red open at my_left, speak
        with lsmovement

        d "Aren't those a bit redundant? It's about 7 in the morning."

        hide dick
        show dick red neutral at my_left
        show morningstar red smile open at my_right, speak
        with rsmovement

        m "It would be enteratining if someone broke one of those?"

        hide morningstar
        show morningstar red unhinged at my_right, speak

        m "The glass everywhere and electricity would be dangerous on those arches."

        hide morningstar
        show morningstar red smile at my_right
        hide dick
        show dick red open at my_left, speak

        d "That's not quite what I consider entertaining but if we are still here and it's dark outside than you can break one."

        hide morningstar
        show morningstar red unhinged at my_right
        hide dick
        show dick red open at my_left, tremble

        "She looked a little too excited at that proposition."

        $ fairylightssee = True
        $ interactions += 1

        hide morningstar
        hide dick

        jump investigate_1
    else:
        "Those are just a waste of electricity."

        jump investigate_1

label stones:

    hide screen arrows1
    hide screen leaveinvestiagte
    hide screen invest1
    hide screen gloves

    if stonessee == False:
        show dick red open at my_left, speak
        with lsmovement

        d "That's stylish I guess, you don't normally see that outside of private residences much."

        hide dick
        show dick red neutral at my_left
        show morningstar red o at my_right, speak
        with rsmovement

        m "Because it's a great way to get put on a hitlist by someone in a wheelchair."

        hide morningstar
        show morningstar red rbf at my_right
        hide dick
        show dick red frown open at my_left, speak

        d "Touche, touche."

        hide dick
        show dick red open at my_left, speak

        d "Can't they be fined miserably for it?"

        hide morningstar
        show morningstar red open at my_right, speak
        hide dick
        show dick red neutral at my_left

        m "Probably."

        hide morningstar
        show morningstar red rbf at my_right
        hide dick
        show dick red open at my_left, speak

        d "Well that's good."

        hide dick
        show dick red smile open at my_left, speak

        d "Maybe when we get back we can report it, truly hurt them."

        hide morningstar
        show morningstar red smile at my_right
        hide dick
        show dick red smile at my_left

        "Morningstar's eyes seemed to glitter."

        hide morningstar
        show morningstar red smile open at my_right, speak
        hide dick
        show dick red neutral at my_left

        m "The hotel owner will want to die."

        hide morningstar
        show morningstar red smile at my_right, speak
        hide dick
        show dick red rbf at my_left

        "She wasn't wrong, but that wasn't quite the point."

        $ stonessee = True
        $ interactions += 1

        hide morningstar
        hide dick

        jump investigate_1
    else:
        "Those still look like a fall hazard."

        jump investigate_1

label garden:

    hide screen arrows1
    hide screen leaveinvestiagte
    hide screen invest1
    hide screen gloves

    if gardensee == False:
        show dick red open at my_left, speak
        with lsmovement

        d "How very... HOA."

        hide dick
        show dick red neutral at my_left
        show morningstar red open at my_right, speak
        with rsmovement

        m "What?"

        hide morningstar
        show morningstar red rbf at my_right
        hide dick
        show dick red open at my_left, speak

        d "Normally you'd see a nice variety of stuff, but this is all just so cookie cutter."

        hide morningstar
        show morningstar red frown open at my_right,speak
        hide dick
        show dick red neutral at my_left

        m "And the bush isn't even cut right."

        hide morningstar
        show morningstar red frown at my_right
        hide dick
        show dick red neutral at my_left
        with Pause (1.0)
        show dick red frown at my_left
        with Pause (0.5)
        show dick red open at my_left
        with Pause (0.5)
        show dick red pissy at my_left, speak

        d "And the bush isn't even cut right..."

        hide dick
        show dick red open at my_left, speak

        d "That's just depressing. Maybe their landscaper was interrupted midway?"

        hide morningstar
        show morningstar red open at my_right, speak
        hide dick
        show dick red frown at my_left

        m "And if he was, maybe he left us some goodies."

        $ gardensee = True
        $ interactions += 1

        hide morningstar
        hide dick

        jump investigate_1
    else:
        "Such a drab little thing."

        jump investigate_1

label investigate_2:
    
    hide screen arrows1
    hide screen leaveinvestiagte
    hide screen invest1
    hide screen gloves

    show screen invest2
    scene investigate 2    

    if investigate2 == False:
        "The ceremony area was somewhat cute, but a little claustrophobic despite being in such an open field. It all had an strange energy."
        
        $ investigate2 = True 
    else:
        pass

    if venommethod == 2:
        show screen leaveinvestiagte
    elif poisonmethod == 1:
        show screen leaveinvestiagte
    elif electricmethod >= 4:
        show screen leaveinvestiagte
    else:
        pass

    call screen arrows2

label purse:

    hide screen arrows2
    hide screen leaveinvestiagte
    hide screen invest2

    if heroin == True:
        "Hopefully whoever owns that purse won't miss what was inside."

        jump investigate_2
    else:
        show morningstar red unhinged at my_right, speak
        with rsmovement
            
        m "Don't mind if I do!"

        hide screen purse
        hide morningstar
        show cg2 1 2

        "Didn't take long for her to get all up in whoever's purse."

        show cg2 3

        m "That's a shit-load of wrappers. How does the owner even remember what's in here?"

        show cg2 1 2

        d "Then maybe..."

        show cg2 4 6

        m "No."

        show cg2 5

        d "I didn't even ask yet."

        show cg2 4 6

        m "And I know what you're going to say."

        show cg2 7 10 12
        
        m "But there's something way better then money in here."
    
        show cg2 8 9 11

        "With that she pulls out a little baggie with white powder in it and a needle."

        d "Well, someone's looking to party tonight I guess."

        show cg2 7 10 12

        m "I think it's a good idea to keep a hold onto it, not just because it's possible to kill someone with, but because it's great blackmail."

        show cg2 8 9 11

        d "At least I know you aren't crazy enough to try it so I'm up for it."

        show cg2 7 10 12

        m "Don't tempt me with a shitty time."

        show heroingotten
        pause
        $ heroin = True
        $ poisonmethod += 1
        $ items += 1
        $ interactions += 1
        hide heroingotten

        show cg2 8 9 11

        "There's still more inside the purse, so..."

        menu:
            "Morningstar checks the side pocket.":
                jump letter
            "Morningstar checks the wallet.":
                jump money

label letter:

    show cg2 13 14

    "Inside it was surprisingly barren, execpt for a piece of paper."

    show cg2 15

    m "There's something strange in here."

    show cg2 13 14

    "She pulled it out so both her and Dick could read it."

    show letter1
    pause
    hide letter1

    d "You're right. Maybe we can keep a hold on that too?"

    show cg2 16

    m "That's probably a good idea."

    $ letter += 1

    jump investigate_2

label money:

    show cg2 17 19

    "There wasn't much inside the wallet that was interesting other then the usual."

    show cg2 18

    m "I think we're good unless we want to shovel through gum wrappers."

    show cg2 17 19

    d "What about borrowing a few buck there? The owner has heroin, there's always plenty in there that disappears fast."

    "She hesitated for a moment before giving his nasty look and a few bills."

    show cg2 20

    m  "If you can find a way to kill someone using only paper money, I'll be impressed beyond words."

    jump investigate_2

label aisle:

    hide screen arrows2
    hide screen leaveinvestiagte
    hide screen invest2

    if aislesee == False:
        "words"

        $ aislesee = True
        $ interactions += 1

        hide morningstar
        hide dick       

        jump investigate_2
    else:
        "What's a wedding without an aisle, especially one so good at protecting from grass stains? Maybe it would be a bit better if those arches weren't in the way."

        jump investigate_2

label alter:

    hide screen arrows2
    hide screen leaveinvestiagte
    hide screen invest2

    if altersee == False:
        "words"

        $ altersee = True
        $ interactions += 1

        hide morningstar
        hide dick       

        jump investigate_2
    else:
        "The world's most meaningful malformed cube."

        jump investigate_2

label benches:

    hide screen arrows2
    hide screen leaveinvestiagte
    hide screen invest2

    if benchessee == False:
        show morningstar red open at my_right, speak
        with rsmovement

        m "Ready for our asses to hurt?"

        hide morningstar
        show morningstar red rbf at my_right
        show dick red open at my_left, speak
        with lsmovement   

        d "Oh hush. They're just benches. You'll be fine."



        m "Whatever, at least it looks like people who are in the back saved their seats, or at least left random shit there."



        d "It's a good idea if you're early, especially since most guests trust everyone here."



        m "Sucks to be them."



        d "Absolutely, but you can understand why. It's their family members, in-laws, and buisness partners. You want to keep them close."



        m "No such things as friends here, ey?"



        d "Of course not."   

        $ benchessee == True
        $ interactions += 1

        hide morningstar
        hide dick       

        jump investigate_2
    elif heroin == True or malemale == True:
        show dick red open at my_left, speak
        with lsmovement   

        d "These were shockingly bountiful."

        hide dick
        show dick red neutral at my_left
        show morningstar red open at my_right, speak
        with rsmovement

        m "I don't know if that makes us sound like thieves or farmers."



        "He just looked a bit taken aback by that, but it wasn't exactly wrong." 

        hide morningstar
        hide dick       

        jump investigate_2
    else:
        "They're fasionable, in some way, but it's unlikely those would be comfortable for a long period of time."

        jump investigate_2

label extension:

    hide screen arrows2
    hide screen leaveinvestiagte
    hide screen invest2

    if extensionsee == False:
        show dick red frown open at my_left, speak
        with lsmovement   

        d "I don't know if that's just plain laziness or if we are just too early."

        hide dick
        show dick red neutral at my_left
        show morningstar red open at my_right, speak
        with rsmovement

        m "We're too early, but I like it being both."



        d "Touche, there's a lot amiss at this time I guess."


        
        d "This is just a little much to just have sitting out. Maybe they had an issue somwhere along the line?"



        m "I hope so."



        d "Spoken like a true electrition. I just hope we are able to do it without killing ourselves."



        m "What a way to go out, at least. I wouldn't even be that mad."



        d "Yes, because you'd be dead."



        m "Only a minor roadblock."

        $ extensionsee = True
        $ interactions += 1

        hide morningstar
        hide dick       

        jump investigate_2
    else:
        "A beautiful wedding, funded by someone hauling ass to a departmet store right before the ceremony."

        jump investigate_2

label malemale:

    hide screen arrows2
    hide screen leaveinvestiagte
    hide screen invest2

    if malemale == False:
        show morningstar red open at my_right, speak
        with rsmovement

        m "I've never seen a cord like that before."

        hide morningstar
        show morningstar red rbf at my_right
        show dick red open at my_left, speak
        with lsmovement   

        d "Good, I'd hope not."
        


        m "What's with that cryptic-ass answer?"



        d "It's a suicide cable, it's because if you plug both ends in it'll cause a fire, electrocute you, or any awful fate inbetween."



        m "Now you're talking."



        d "I don't even know where they got one of these, they're illegal. I know since I got the lovely task of trying to buy one a few years back."



        m "That's weird, still it's a great tool."



        m "Maybe whoever decorated with all those fairylights ordered it from some shady online retailor."



        d "Rich people don't tend to cut corners like that though, they tend to like to go all out, you know? Flex a little, especially at weddings."



        m "I'd never guess since I live with a wannabe."



        d "Oh hush. I think it is smart to put a pin in it that though."



        m "Could be good to bring up in conversation, but i just want to find a way to get the bride to try it out."

        $ malemale = True
        $ items += 1
        $ interactions += 1

        hide morningstar
        hide dick       

        jump investigate_2
    else:
        "The illustrious male-male cable. Just like a male-male seatbelt, trying to use it instead of finding some alternate solution is a fantastic way to get yourself killed."

        jump investigate_2

label arches2:

    hide screen arrows2
    hide screen leaveinvestiagte
    hide screen invest2

    if archessee == False:
        show morningstar red open at my_right, speak
        with rsmovement

        m "They have way too many of those."

        hide morningstar
        show morningstar red rbf at my_right
        show dick red smile open at my_left, speak
        with lsmovement

        d "Well, if you're rich, why not live in excess?"

        hide morningstar
        show morningstar red open at my_right, speak
        hide dick
        show dick red smile at my_left

        m "They aren't even real, though. It's garbage."

        hide morningstar
        show morningstar red rbf at my_right
        hide dick
        show dick red smile at my_left

        "Dick couldn't deny that, the leaves only looked faker next to the real thing only feet away. It was too obvious to the point of being distracting."

        hide morningstar
        show morningstar red rbf at my_right
        hide dick
        show dick red smile open at my_left, speak

        d "Maybe it's expensive garbage, at least? Could be nicer then you assume."

        hide morningstar
        show morningstar red frown at my_right
        hide dick
        show dick red neutral at my_left

        "She wasn't impressed."

        hide morningstar
        show morningstar red rbf at my_right
        hide dick
        show dick red open at my_left, speak

        d "I'm trying to be respectful, there are always worse they could do."

        hide morningstar
        show morningstar red frown open at my_right, speak
        hide dick
        show dick red frown at my_left

        m "Just say it looks like shit and move on."

        hide morningstar
        show morningstar red rbf at my_right
        hide dick
        show dick red frown open at my_left, speak

        d "Fine, it looks like shit."

        hide morningstar
        show morningstar red smile at my_right
        hide dick
        show dick red frown at my_left

        "He looked somewhere between relieved and liked he had to force himself to say it."

        $ archessee = True
        $ interactions += 1

        hide morningstar
        hide dick

        jump investigate_2
    else:
        "Fake plastic arches."

        jump investigate_2

label fairylights2:

    hide screen arrows2
    hide screen leaveinvestiagte
    hide screen invest2

    if fairylightssee == False:
        show dick red open at my_left, speak
        with lsmovement

        d "Aren't those a bit redundant? It's about 7 in the morning."

        hide dick
        show dick red neutral at my_left
        show morningstar red smile open at my_right, speak
        with rsmovement

        m "It would be enteratining if someone broke one of those?"

        hide morningstar
        show morningstar red unhinged at my_right, speak

        m "The glass everywhere and electricity would be dangerous on those arches."

        hide morningstar
        show morningstar red smile at my_right
        hide dick
        show dick red open at my_left, speak

        d "That's not quite what I consider entertaining but if we are still here and it's dark outside than you can break one."

        hide morningstar
        show morningstar red unhinged at my_right
        hide dick
        show dick red open at my_left, tremble

        "She looked a little too excited at that proposition."

        $ fairylightssee = True
        $ interactions += 1

        hide morningstar
        hide dick

        jump investigate_2
    else:
        "Those are just a waste of electricity."

        jump investigate_2

label investigate_3:

    hide screen arrows1
    hide screen arrows4
    hide screen invest1
    hide screen gloves
    hide screen leaveinvestiagte

    scene investigate 3

    if investigate3 == False:
        "Here was the reception area, where everything will fall apart in just a few hours. This might be the most important area here. Plenty of things can go wrong here."
        
        $ investigate3 = True
    else:
        pass

    if venommethod == 2:
        show screen leaveinvestiagte
    elif poisonmethod == 1:
        show screen leaveinvestiagte
    elif electricmethod >= 4:
        show screen leaveinvestiagte
    else:
        pass

    call screen arrows3 

label unplugged:

label investigate_4:

    hide screen arrows3
    hide screen leaveinvestiagte

    scene investigate 4

    if investigate4 == False:
        "A hallway, connecting between the wedding area and the rest of the hotel. It's bare in a lot of ways, but in those doors may be something interesting."

        $ investigate4 = True
    else:
        pass

    if venommethod == 2:
        show screen leaveinvestiagte
    elif poisonmethod == 1:
        show screen leaveinvestiagte
    elif electricmethod >= 4:
        show screen leaveinvestiagte
    else:
        pass

    call screen arrows4

label closet:

label bathrooms:

label investigate_leave:

    "Are you done investigating?"

    menu:
        "Yes, it's time to wait to attend the ceremony":
            pass
        "No, there's still more to find around here.":
            jump investigate_1

    hide screen arrows1
    hide screen arrows2
    hide screen arrows3
    hide screen arrows4
    hide screen invest1
    hide screen gloves
    hide screen leaveinvestiagte
    scene black
    $ persistent.investigate_done = True

    "It didn't take too long waiting for the other guests to arrive. They were able to bide their time for the ceremony without much of a fuss."

    jump end

label end:

    # Just a little message to keep you in check.

    "This is the end of the demo you are playing."

    return
