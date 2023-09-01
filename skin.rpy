## TUTORIAL: THIS DOES *NOT* GO INTO THE GAME FILES ##
# 1. Go into your renpy launcher
# 2. Go into setting and select to open the renpy launcher
# 3. Open the images, replace the background image with the one I sent
# 4. Open the launcher's code.
# 5. Make a new file where the rest are called "skin.rpy"
# 6. Copy all of this code into your new file
# 7. Go back into settings and select "Custom Skin"
# 8. Enjoy!

init -2 python:
    # The color of non-interactive text.
    custom_text = "#231935"

    # Colors for buttons in various states.
    custom_idle = "#30008a"
    custom_hover = "#E8AE5D"
    custom_disable = "#202020"

    # Colors for reversed text buttons (selected list entries).
    custom_reverse_idle = "#30008a"
    reverse_hover = "#E8AE5D"
    custom_reverse_text = "#ffffff"

    # Colors for the scrollbar thumb.
    custom_scrollbar_idle = "#dfdfdf"
    custom_scrollbar_hover = "#E8AE5D"
    # An image used as a separator pattern.
    custom_pattern = "images/pattern.png"

    # A displayable used for the background of everything.
    custom_background = "images/background.png"

    # A displayable used for the background of the projects list.
    custom_projects_window = Null()

    # A displayable used the background of information boxes.
    custom_info_window = "#f9f9f9c0"

    # Colors for the titles of information boxes.
    custom_error_color = "#d15353"
    custom_info_color = "#545454"
    custom_interaction_color = "#d19753"
    custom_question_color = "#d19753"

    # The color of input text.
    custom_input_color = "#E8AE5D"

    # A displayable used for the background of windows
    # containing commands, preferences, and navigation info.
    custom_window = Frame(Fixed(Solid(custom_reverse_idle, xsize=4, xalign=0), Solid(custom_info_window, xsize=794, xalign=1.0), xsize=800, ysize=600), 0, 0, tile=True)
