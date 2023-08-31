##### This is the definitions of the game, this will include all the definitions so they don't clutter the script #####

# Main Characters

define d = Character("Dick")
define m = Character("Morningstar")
define fd = Character("[fd]")
define fm = Character("[fm]")

# Main Characters Sprites


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
