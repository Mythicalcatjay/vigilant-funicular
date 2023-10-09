init python:
    gallery = Gallery()

    ############################### SPRITES ###############################

    ##### Morningstar Sprites #####

    gallery.button("morningstar frown open")
    gallery.image("morningstar frown open")
    gallery.unlock_image("morningstar red frown open")
    gallery.unlock_image("morningstar blue frown open")

    gallery.button("morningstar frown")
    gallery.image("morningstar frown")
    gallery.unlock_image("morningstar red frown")
    gallery.unlock_image("morningstar blue frown")

    gallery.button("morningstar o")
    gallery.image("morningstar o")
    gallery.unlock_image("morningstar red o")
    gallery.unlock_image("morningstar blue o")

    gallery.button("morningstar open")
    gallery.image("morningstar open")
    gallery.unlock_image("morningstar red open")
    gallery.unlock_image("morningstar blue open")

    gallery.button("morningstar rbf")
    gallery.image("morningstar rbf")
    gallery.unlock_image("morningstar red rbf")
    gallery.unlock_image("morningstar blue rbf")

    gallery.button("morningstar shock")
    gallery.image("morningstar shock")
    gallery.unlock_image("morningstar red shock")
    gallery.unlock_image("morningstar blue shock")

    gallery.button("morningstar smile open")
    gallery.image("morningstar smile open")
    gallery.unlock_image("morningstar red smile open")
    gallery.unlock_image("morningstar blue smile open")

    gallery.button("morningstar smile")
    gallery.image("morningstar smile")
    gallery.unlock_image("morningstar red smile")
    gallery.unlock_image("morningstar blue smile")

    gallery.button("morningstar unhinged")
    gallery.image("morningstar unhinged")
    gallery.unlock_image("morningstar red unhinged")
    gallery.unlock_image("morningstar blue unhinged")

    ##### Dick Sprites #####

    gallery.button("dick 1 sulk")
    gallery.image("dick 1 75 sulk")
    gallery.unlock_image("dick 1 50 sulk")
    gallery.unlock_image("dick 1 25 sulk")

    gallery.button("dick 1 neutral")
    gallery.image("dick 1 75 neutral")
    gallery.unlock_image("dick 1 50 neutral")
    gallery.unlock_image("dick 1 25 neutral")

    gallery.button("dick 1 open")
    gallery.image("dick 1 75 open")
    gallery.unlock_image("dick 1 50 open")
    gallery.unlock_image("dick 1 25 open")

    gallery.button("dick 1 rbf")
    gallery.image("dick 1 75 rbf")
    gallery.unlock_image("dick 1 50 rbf")
    gallery.unlock_image("dick 1 25 rbf")

    gallery.button("dick 1 smile open")
    gallery.image("dick 1 75 smile open")
    gallery.unlock_image("dick 1 50 smile open")
    gallery.unlock_image("dick 1 25 smile open")

    gallery.button("dick 1 smile")
    gallery.image("dick 1 75 smile")
    gallery.unlock_image("dick 1 50 smile")
    gallery.unlock_image("dick 1 25 smile")

    gallery.button("dick 1 pissy")
    gallery.image("dick 1 75 pissy")
    gallery.unlock_image("dick 1 50 pissy")
    gallery.unlock_image("dick 1 25 pissy")

    # Outfit Change

    gallery.button("dick frown open")
    gallery.image("dick frown open")
    gallery.condition("persistent.opening_done")
    gallery.unlock_image("dick red frown open")
    gallery.unlock_image("dick blue frown open")

    gallery.button("dick frown")
    gallery.image("dick frown")
    gallery.condition("persistent.opening_done")
    gallery.unlock_image("dick red frown")
    gallery.unlock_image("dick blue frown")

    gallery.button("dick neutral")
    gallery.image("dick neutral")
    gallery.condition("persistent.opening_done")
    gallery.unlock_image("dick red neutral")
    gallery.unlock_image("dick blue neutral")

    gallery.button("dick open")
    gallery.image("dick open")
    gallery.condition("persistent.opening_done")
    gallery.unlock_image("dick red open")
    gallery.unlock_image("dick blue open")

    gallery.button("dick rbf")
    gallery.image("dick rbf")
    gallery.condition("persistent.opening_done")
    gallery.unlock_image("dick red rbf")
    gallery.unlock_image("dick blue rbf")

    gallery.button("dick smile open")
    gallery.image("dick smile open")
    gallery.condition("persistent.opening_done")
    gallery.unlock_image("dick red smile open")
    gallery.unlock_image("dick blue smile open")

    gallery.button("dick smile")
    gallery.image("dick smile")
    gallery.condition("persistent.opening_done")
    gallery.unlock_image("dick red smile")
    gallery.unlock_image("dick blue smile")

    gallery.button("dick pissy")
    gallery.image("dick pissy")
    gallery.condition("persistent.opening_done")
    gallery.unlock_image("dick red pissy")
    gallery.unlock_image("dick blue pissy")

    ############################### CGS ###############################

    gallery.button("cg1")
    gallery.unlock_image("cg1")

    gallery.button("cg2 1 2")
    gallery.unlock_image("cg2 1 2")
    gallery.unlock_image("cg2 3")
    gallery.unlock_image("cg2 4 6")
    gallery.unlock_image("cg2 5")
    gallery.unlock_image("cg2 7 10 12")
    gallery.unlock_image("cg2 8 9 11")
    gallery.unlock_image("cg2 17 19")
    gallery.unlock_image("cg2 18")
    gallery.unlock_image("cg2 20")
    gallery.unlock_image("cg2 13 14")
    gallery.unlock_image("cg2 15")
    gallery.unlock_image("cg2 16")

    ############################### BACKGROUNDS ###############################

    ##### Investigate Backgrounds #####

    gallery.button("investigate 1")
    gallery.unlock_image("investigate 1 gloves")
    gallery.unlock_image("investigate 1")
    gallery.unlock_image("mingle 1")
    gallery.image("regular 1")
    gallery.condition("persistent.investigate_done")

    gallery.button("investigate 2")
    gallery.unlock_image("investigate 2")
    gallery.unlock_image("mingle 2")
    gallery.image("regular 2")
    gallery.condition("persistent.investigate_done")

    gallery.button("investigate 3")
    gallery.unlock_image("investigate 3")
    gallery.unlock_image("investigate 3")
    gallery.unlock_image("mingle 3")
    gallery.image("regular 3")
    gallery.condition("persistent.investigate_done")

    gallery.button("investigate 4")
    gallery.unlock_image("investigate 4")
    gallery.unlock_image("mingle 4")
    gallery.image("regular 4")
    gallery.condition("persistent.investigate_done")

screen gallery_navigation:
    vbox:
        spacing 20
        xoffset -100
        textbutton "Sprites" action ShowMenu("gallery_sprites") 
        textbutton "CGS" action ShowMenu("gallery_cgs") 
        textbutton "Backgrounds" action ShowMenu("gallery_backgrounds")
        textbutton "Endings" action ShowMenu("gallery_endings")
        
        textbutton "Return":
            action Return()
            yoffset 200

screen gallery_sprites:
    vbox:
        spacing 20
        xoffset -100
        textbutton "Morningstar" action ShowMenu("gallery_morningstar") 
        textbutton "Dick" action ShowMenu("gallery_dick") 
        
        textbutton "Return":
            action Return()
            yoffset 200

screen gallery_endings:
    vbox:
        spacing 20
        xoffset -100
        textbutton "Back" action ShowMenu("gallery_navigation")
        
        textbutton "Return":
            action Return()
            yoffset 200

screen gallery_morningstar:
    tag menu

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        
        use gallery_sprites

        grid 3 3: 
            add gallery.make_button(name="morningstar frown open",unlocked= im.Scale("morningstar/frown open.png",200,400),locked="dick.png")
            add gallery.make_button(name="morningstar frown",unlocked= im.Scale("morningstar/frown.png",200,400),locked="dick.png")
            add gallery.make_button(name="morningstar o",unlocked= im.Scale("morningstar/o.png",200,400),locked="dick.png")
            add gallery.make_button(name="morningstar open",unlocked= im.Scale("morningstar/open.png",200,400),locked="dick.png")
            add gallery.make_button(name="morningstar rbf",unlocked= im.Scale("morningstar/rbf.png",200,400),locked="dick.png")
            add gallery.make_button(name="morningstar shock",unlocked= im.Scale("morningstar/shock.png",200,400),locked="dick.png")
            add gallery.make_button(name="morningstar smile",unlocked= im.Scale("morningstar/smile.png",200,400),locked="dick.png")
            add gallery.make_button(name="morningstar smile open",unlocked= im.Scale("morningstar/smile open.png",200,400),locked="dick.png")
            add gallery.make_button(name="morningstar unhinged",unlocked= im.Scale("morningstar/unhinged.png",200,400),locked="dick.png")
            spacing 15

screen gallery_dick:
    tag menu

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        
        use gallery_sprites

        grid 5 3: 
            add gallery.make_button(name="dick 1 sulk",unlocked= im.Scale("dick/dick 1 75/sulk.png",200,400),locked="dick.png")
            add gallery.make_button(name="dick 1 neutral",unlocked= im.Scale("dick/dick 1 75/neutral.png",200,400),locked="dick.png")
            add gallery.make_button(name="dick 1 open",unlocked= im.Scale("dick/dick 1 75/open.png",200,400),locked="dick.png")
            add gallery.make_button(name="dick 1 rbf",unlocked= im.Scale("dick/dick 1 75/rbf.png",200,400),locked="dick.png")
            add gallery.make_button(name="dick 1 smile",unlocked= im.Scale("dick/dick 1 75/smile.png",200,400),locked="dick.png")
            add gallery.make_button(name="dick 1 smile open",unlocked= im.Scale("dick/dick 1 75/smile open.png",200,400),locked="dick.png")
            add gallery.make_button(name="dick 1 pissy",unlocked= im.Scale("dick/dick 1 75/pissy.png",200,400),locked="dick.png")

            add gallery.make_button(name="dick frown open",unlocked= im.Scale("dick/dick/frown open.png",200,400),locked="dick.png")
            add gallery.make_button(name="dick frown",unlocked= im.Scale("dick/dick/frown.png",200,400),locked="dick.png")
            add gallery.make_button(name="dick neutral",unlocked= im.Scale("dick/dick/neutral.png",200,400),locked="dick.png")
            add gallery.make_button(name="dick open",unlocked= im.Scale("dick/dick/open.png",200,400),locked="dick.png")
            add gallery.make_button(name="dick rbf",unlocked= im.Scale("dick/dick/rbf.png",200,400),locked="dick.png")
            add gallery.make_button(name="dick smile",unlocked= im.Scale("dick/dick/smile.png",200,400),locked="dick.png")
            add gallery.make_button(name="dick smile open",unlocked= im.Scale("dick/dick/smile open.png",200,400),locked="dick.png")
            add gallery.make_button(name="dick pissy",unlocked= im.Scale("dick/dick/pissy.png",200,400),locked="dick.png")
            spacing 15

screen gallery_cgs:
    tag menu

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        
        use gallery_navigation

        grid 3 3: 
            add gallery.make_button(name="cg1",unlocked= im.Scale("cgs/cg1.png",468,264),locked="dick.png")
            add gallery.make_button(name="cg2",unlocked= im.Scale("cgs/cg2 1 2.png",468,264),locked="dick.png")
            spacing 15

screen gallery_backgrounds:
    tag menu

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        
        use gallery_navigation

        grid 3 3: 
            add gallery.make_button(name="investigate 1",unlocked= im.Scale("backgrounds/investigate 1.png",468,264),locked="dick.png")
            add gallery.make_button(name="investigate 2",unlocked= im.Scale("backgrounds/investigate 2.png",468,264),locked="dick.png")
            spacing 15
