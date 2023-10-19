screen achievements:
    tag menu

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        textbutton "Regular" action ShowMenu("achievements_regular") 
        textbutton "Challenger" action ShowMenu("achievements_challenger") 

screen achievements_regular:
    tag menu

    use game_menu(_("Achievements"), scroll="viewport"):

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            
            use achievements

            text "Test"

screen achievements_challenger:
    tag menu

    use game_menu(_("Achievements"), scroll="viewport"):

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            
            use achievements

            text "Evil Test"
