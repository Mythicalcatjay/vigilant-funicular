##### This is the definitions of the game, this will include all the definitions so they don't clutter the script #####

# Main Characters

define d = Character("Dick", color="#91CEC7")
define m = Character("Morningstar", color="#E7935C")
define fd = Character("[fd]", color="#91CEC7")
define fm = Character("[fm]", color="#E7935C")

# Main Characters Sprites
image dick 1 25 neutral ="dick/dick 1 25/neutral.png"
image dick 1 25 open ="dick/dick 1 25/open.png"
image dick 1 25 pissy ="dick/dick 1 25/pissy.png"
image dick 1 25 rbf ="dick/dick 1 25/rbf.png"
image dick 1 25 smile ="dick/dick 1 25/smile.png"
image dick 1 25 smile open ="dick/dick 1 25/smile open.png"
image dick 1 25 sulk ="dick/dick 1 25/sulk.png"

image dick 1 50 neutral ="dick/dick 1 50/neutral.png"
image dick 1 50 open ="dick/dick 1 50/open.png"
image dick 1 50 pissy ="dick/dick 1 50/pissy.png"
image dick 1 50 rbf ="dick/dick 1 50/rbf.png"
image dick 1 50 smile ="dick/dick 1 50/smile.png"
image dick 1 50 smile open ="dick/dick 1 50/smile open.png"
image dick 1 50 sulk ="dick/dick 1 50/sulk.png"

image dick 1 75 neutral ="dick/dick 1 75/neutral.png"
image dick 1 75 open ="dick/dick 1 75/open.png"
image dick 1 75 pissy ="dick/dick 1 75/pissy.png"
image dick 1 75 rbf ="dick/dick 1 75/rbf.png"
image dick 1 75 smile ="dick/dick 1 75/smile.png"
image dick 1 75 smile open ="dick/dick 1 75/smile open.png"
image dick 1 75 sulk ="dick/dick 1 75/sulk.png"

image morningstar frown open = "morningstar/frown open.png"
image morningstar frown = "morningstar/frown.png"
image morningstar o = "morningstar/o.png"
image morningstar open = "morningstar/open.png"
image morningstar rbf = "morningstar/rbf.png"
image morningstar shock = "morningstar/shock.png"
image morningstar smile open = "morningstar/smile open.png"
image morningstar smile = "morningstar/smile.png"
image morningstar unhinged = "morningstar/unhinged.png"

image morningstar red frown open = "morningstar red/frown open.png"
image morningstar red frown = "morningstar red/frown.png"
image morningstar red o = "morningstar red/o.png"
image morningstar red open = "morningstar red/open.png"
image morningstar red rbf = "morningstar red/rbf.png"
image morningstar red shock = "morningstar red/shock.png"
image morningstar red smile open = "morningstar red/smile open.png"
image morningstar red smile = "morningstar red/smile.png"
image morningstar red unhinged = "morningstar red/unhinged.png"

image morningstar blue frown open = "morningstar blue/frown open.png"
image morningstar blue frown = "morningstar blue/frown.png"
image morningstar blue o = "morningstar blue/o.png"
image morningstar blue open = "morningstar blue/open.png"
image morningstar blue rbf = "morningstar blue/rbf.png"
image morningstar blue shock = "morningstar blue/shock.png"
image morningstar blue smile open = "morningstar blue/smile open.png"
image morningstar blue smile = "morningstar blue/smile.png"
image morningstar blue unhinged = "morningstar blue/unhinged.png"

image dick neutral ="dick/dick/neutral.png"
image dick open ="dick/dick/open.png"
image dick pissy ="dick/dick/pissy.png"
image dick rbf ="dick/dick/rbf.png"
image dick smile ="dick/dick/smile.png"
image dick smile open ="dick/dick/smile open.png"
image dick frown ="dick/dick/frown.png"
image dick frown open ="dick/dick/frown open.png"

image dick red neutral ="dick/dick red/neutral.png"
image dick red open ="dick/dick red/open.png"
image dick red pissy ="dick/dick red/pissy.png"
image dick red rbf ="dick/dick red/rbf.png"
image dick red smile ="dick/dick red/smile.png"
image dick red smile open ="dick/dick red/smile open.png"
image dick red frown ="dick/dick red/frown.png"
image dick red frown open ="dick/dick red/frown open.png"

image dick blue neutral ="dick/dick blue/neutral.png"
image dick blue open ="dick/dick blue/open.png"
image dick blue pissy ="dick/dick blue/pissy.png"
image dick blue rbf ="dick/dick blue/rbf.png"
image dick blue smile ="dick/dick blue/smile.png"
image dick blue smile open ="dick/dick blue/smile open.png"
image dick blue frown ="dick/dick blue/frown.png"
image dick blue frown open ="dick/dick blue/frown open.png"

# Demo Characters


# Demo Characters Sprites


# CGs

image cg1 = "cgs/cg1.png"
image cg2 = "cgs/cg2.png"

# BGs

image investigate 1 = "backgrounds/investigate 1.png"

# Info Pictures

image snakegotten = "info/placeholder.png"
image heroingotten = "info/placeholder.png"
image glovesgotten = "info/placeholder.png"

# Transformations

transform my_left:
    xalign 0.0 yalign -0.3
transform my_right:
    xalign 1.0 yalign -0.3 
transform speak:
    on show:
        linear 0.2 zoom 1.10 yalign -0.2
transform tremble:
    on show:
        linear 0.12 xoffset 4
        linear 0.12 xoffset -4
        linear 0.12 xoffset 4
        linear 0.12 xoffset -4
        repeat
transform jitters:
    on show:
        linear 0.12 yoffset 4
        linear 0.12 yoffset -4
        linear 0.12 yoffset 4
        linear 0.12 yoffset -4
        repeat

# Extra Definitions

define lsmovement = MoveTransition(
                        delay=0.3,
                        enter=offscreenleft,
                        leave=None,
                        old=False,
                        layers=['master'],
                        time_warp=_warper.ease_back,
                        enter_time_warp=None,
                        leave_time_warp=None)

define rsmovement = MoveTransition(
                        delay=0.3,
                        enter=offscreenright,
                        leave=None,
                        old=False,
                        layers=['master'],
                        time_warp=_warper.ease_back,
                        enter_time_warp=None,
                        leave_time_warp=None)

# Image Buttons

screen arrows1:
        imagebutton:
            xalign 0.0
            yalign 0.5
            idle "buttons/arrow_left.png"
            action Jump("investigate_2")
        imagebutton:
            xalign 1.0
            yalign 0.5
            idle "buttons/arrow_right.png"
            action Jump("investigate_3")

screen arrows2:
        imagebutton:
            xalign 1.0
            yalign 0.5
            idle "buttons/arrow_right.png"
            action Jump("investigate_1")

screen arrows3:
        imagebutton:
            xalign 0.0
            yalign 0.5
            idle "buttons/arrow_left.png"
            action Jump("investigate_1")
        imagebutton:
            xalign 1.0
            yalign 0.5
            idle "buttons/arrow_right.png"
            action Jump("investigate_4")

screen arrows4:
        imagebutton:
            xalign 0.0
            yalign 0.5
            idle "buttons/arrow_left.png"
            action Jump("investigate_3")

screen leaveinvestiagte:
        imagebutton:
            xalign 0.0
            yalign 0.0
            idle "buttons/leave.png"
            action Jump("investigate_leave")


screen invest1:
    tag menu
    vbox:
        xalign 0.0
        yalign 0.0
        imagebutton:
            xpos 780
            ypos 0.0
            idle "investigate buttons/garden_idle.png"
            hover "investigate buttons/garden_hover.png"
            action Jump("garden")
        imagebutton:
            xpos 0.0
            ypos -920
            idle "investigate buttons/arches_idle.png"
            hover "investigate buttons/arches_hover.png"
            action Jump("arches")
        imagebutton:
            xpos 1230
            ypos -1110
            idle "investigate buttons/stones_idle.png"
            hover "investigate buttons/stones_hover.png"
            action Jump("stones")
        imagebutton:
            xpos 1500
            ypos -2550
            idle "investigate buttons/hotel_idle.png"
            hover "investigate buttons/hotel_hover.png"
            action Jump("hotel")
        imagebutton:
            xpos 0.0
            ypos -3540
            idle "investigate buttons/fairylights_idle.png"
            hover "investigate buttons/fairylights_hover.png"
            action Jump("fairylights")
        imagebutton:
            xpos 1.112
            ypos -3251
            idle "investigate buttons/snake_idle.png"
            hover "investigate buttons/snake_hover.png"
            action Jump("snake")

screen gloves:
        imagebutton:
            xanchor 0.0
            yanchor 0.0
            xpos 1.5
            ypos 1.0
            idle "investigate buttons/gloves_idle.png"
            hover "investigate buttons/gloves_hover.png"
            action Jump("gloves")

screen purse:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.28
            idle "investigate buttons/purse_idle.png"
            hover "investigate buttons/purse_hover.png"
            action Jump("purse")
