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

# Demo Characters


# Demo Characters Sprites


# CGs


# BGs


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
