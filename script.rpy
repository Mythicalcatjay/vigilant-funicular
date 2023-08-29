# The script of the game goes in this file.

# Character Variables

define d = Character("Dick")
define m = Character("Morningstar")
define fd = Character("[fd]")
define fm = Character("[fm]")

# The game starts here

label start:

    # this is the start of the game/demo. This is the first section: pregame. It lets us get acquainted with our protagonists and their bickering. 

    "Dick looked at his reflection and tried to stay positive. However, the corners of his mouth refused to turn upwards at what he saw." 

    "An undercover mission required some level of disguise and an appearance like his was hard to mistake, to put it mildly. He was trying to hide that, but he was doing a shitty job."

    "He got this job because he was good at what he did, very good in fact. However, it was stupid moments like this that made him have doubts about his own abilities. Luckily, he wasn't being paid to do this part."

    "He was getting paid to kill someone. That was something he should have no issues with, at least."

    "Still, he couldn't help but feel some mix of disgust and disappointment as he stared at the sickly green appearance of his cheeks. This definitely wasn't his forte and he just wished by the end of it he could make his face passable."
    
    scene bg homebase

    # this is a false choice: it doesn't take you out of the scene but it provides more player interactivity. it can be boring to just read for too long without something to do so I include these to keep the player awake.

    menu:
        "He feels a frigid hand on the back of his neck.":
            jump pregame_1

label pregame_1: 

    d "What's wrong with you?"

    show dick at left

    "He tried to shoot daggers at the offender, but she was an immovable object." 

    m "You missed that entire side of your neck with your base coat because you were hiding it with your hair. You know, the hair you plan on tying back?"

    "Of course, that was to be expected from the snarly character he was going to be accompanied by. She was damn good at what she did, but she sure wasn't mild-mannered."

    "That's part of what he liked about her, though."

    show morningstar at right

    d "You know, you didn't have to do that though, you could've just told me?"

    m "But then you'd miss it and just do it on the other side."

    menu:
        "Bring the makeup brush to that side of his neck.":
            jump pregame_2

label pregame_2:

    "All Dick could do was groan until his throat hurt while he worked on that side of his neck. She was absolutely right, he did miss it, but her methods still sucked."

    d "I still can't believe you're being expected to act like a member of high society."

    m "Well I am a member in case you forgot. It's not like I'm \"some common robble from the street being dragged in.\""

    d "Of course you aren't. However, I do happen to recall and remember more than a fair share of stories of your behavior."

    m "Fuck does that mean?"

    d "Oh..."

    d "Just that you have a history of being overwhelmingly undersocial or getting pissdrunk to the point of causing conflict. I mean, I would hardly find that appropriate at any gathering, much fewer ones amongst the disgustingly rich."

    "She sputtered for a moment and looked like she was ready to bite his head off. That was always just the right reward for pushing the right button."

    m "And who was always there when I was tipsy or hiding?"

    d "Someone had to clean it up."

    m "Wow, didn't know you had to clean where the sun doesn't shine."

    "She blew a raspberry. It was utterly juvenile but still not unfunny. Even then..."

    menu:
        "He should move the conversation along.":
            jump pregame_3

label pregame_3:

    d "Now I expect neither of us will be behaving like that for our job, I think it might be good to talk more about more of the details. I have everything I should need but I want to make sure you actually managed to remember it all."

    m "The hell's that supposed to mean? I was given the directions initially, not you."

    m "But if baby needs a refresher, I guess I can do it without making you get on your hands and knees. Plus we're about to make enough money to blow our dicks off."

    m "We're going to start out with a bang, killing a bride on her wedding day during the reception. Put some fear of god into everyone attending."

    m "Her name is (bullshit name), soon to be (bullshittier name). It shouldn't be hard to tell her apart though, unless someone else gets the bright idea to wear white during a wedding."

    d "Anything else?"

    m "I don't know, dipshit, does it look like we have anything else prepared?"

    d "Oh no, Madam Morningstar, I simply could never guess if we had anything else we planned on doing. I mean aren't we just going to barge right in and shoot her point blank and then go to jail for the rest of our miserable lives?"

    "At that, all he was left with was an exasperated sigh as she ignored him."

    "It was actually pretty nice getting the chance to piss each other off and push as many buttons as they'd like. It got it out of their systems before they had to go full business and nothing ever carried much real bite anyway."

    "After a few beats, it did become apparent she wasn't going to humor him at this point so he spoke up again."

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

    "Now that was a fine name."

    m "Why? Where did you get that? It sucks. You don't look like a [fd]."

    "Maybe that opinion wasn't universal."

    d "It's the name of the guy who owns that (type of store) in (other town) and I thought I'd borrow it."

    m "Ah, so you took it from someone completely miserable in that shit hole, but he's rich so it's fine."

    d "You got it."

    jump morningstar_name

label austin_powers:

    d "[fd]."

    m "Like Austin Powers?"

    d "You know it baby!"

    "Dick reow-ed like a cat, or maybe more accurately a dying one, and got a hearty chuckle back."

    m "Maybe after this mission we can see if you really shag like a mink."

    d "Groovy!"

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

    d "Isn't that the one always complaining about her husband to anyone who'd listen? She's miserable to be around."

    m "Does anyone in around here have something nice to say about their husbands?"

    d "Fair enough, even if it's a bit morbid to say when we're about to attend a wedding."

    m "That'll be the only bride to not have anything to say about her groom, nice or otherwise."

    d "That's so much worse."

    m "It's not like I'm lying. Unless her last words are telling him to fuck himself."

    jump pregame_4

label felicity_shagwell:

    m "I'm going with [fm]."

    "Morningstar didn't even have to say where she got that one from."

    d "Now is it Felicity Shagwell or Shag very well?"

    "He couldn't help but snicker at his own joke."

    m "You tell me after we get done."

    d "Oh behave!"

    jump pregame_4

label pregame_4:

    m "And we're still using my family name?"

    d "It's not like I have a good one to share, and making one up will just make us sound like posers."

    m "You'll just have to be some ugly cousin of mine. [fd] Morningstar is dogshit though."

    d "I think that's just because you go by it so it poisons everything else. So I must concede to having a worse name."

    m "Whatever you say, Dick."

    m "Are you done with your make-up yet? I think you look beautiful as a bride but we might have to get going unless we want to miss the entire wedding."

    "He gave himself a once over and by this point, he looked fine. Not necessarily good, but just fine."

    "He gave Morningstar her own once over as well. There was a level of envy that she really didn't have to do much and still looked good. Plus the formalwear was very different from what he was used to, but not bad."
   
    menu:
        "Put on the finishing touches.":
            jump pregame_5
   
label pregame_5:

    d "I know I look beautiful always, but I guess I've finally reached the level of perfection I wanted"

    m "Sorry, I forgot just how many of your own farts you sniff."

    menu:
        "Leave to investigate the venue.":
            jump investiage_1

    # Just a little message to keep you in check.

label investiage_1:

    "This is the end of the demo you are playing."

    # This ends the game.

    return
