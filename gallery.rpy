init python:
    gallery = Gallery()

    gallery.button("morningstar frown open")
    gallery.unlock_image("morningstar frown open")

    gallery.button("morningstar frown")
    gallery.unlock_image("morningstar frown")

    gallery.button("morningstar o")
    gallery.unlock_image("morningstar o")

    gallery.button("morningstar open")
    gallery.unlock_image("morningstar open")

    gallery.button("morningstar rbf")
    gallery.unlock_image("morningstar rbf")

    gallery.button("morningstar shock")
    gallery.unlock_image("morningstar shock")

    gallery.button("morningstar smile open")
    gallery.unlock_image("morningstar smile open")

    gallery.button("morningstar smile")
    gallery.unlock_image("morningstar smile")

    gallery.button("morningstar unhinged")
    gallery.unlock_image("morningstar unhinged")

screen gallery:
    tag menu

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        grid 3 3: 
            add gallery.make_button(name="morningstar frown open",unlocked="morningstar/frown open.png",locked="dick.png")
            add gallery.make_button(name="morningstar frown",unlocked="morningstar/frown.png",locked="dick.png")
            add gallery.make_button(name="morningstar o",unlocked="morningstar/o.png",locked="dick.png")
            add gallery.make_button(name="morningstar open",unlocked="morningstar/open.png",locked="dick.png")
            add gallery.make_button(name="morningstar rbf",unlocked="morningstar/rbf.png",locked="dick.png")
            add gallery.make_button(name="morningstar shock",unlocked="morningstar/shock.png",locked="dick.png")
            add gallery.make_button(name="morningstar smile",unlocked="morningstar/smile open.png",locked="dick.png")
            add gallery.make_button(name="morningstar smile open",unlocked="morningstar/smile.png",locked="dick.png")
            add gallery.make_button(name="morningstar unhinged",unlocked="morningstar/unhinged.png",locked="dick.png")
            spacing 15

        textbutton "Return" action Return()
