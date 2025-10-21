import pygame
from scripts.functions import lighten_color
from scripts.functions import blit_render_multiline


#FUNCTIONS

def button(x, y, width, height, color, selected_color, text, event, mouse_pos, x_align, y_align):
    btn_pressed = False
    global clicked

    #Set minimal width / height if a text is given
    if text != 0:
        width = max(width, text.get_width() + 10)
        height = max(height, text.get_height())

    #set alignment
    match x_align: # L (left), M (middle), R (right)
        case "M": x -= width / 2
        case "R": x -= width
    match y_align: # T (top), M (middle), B (bottom)
        case "M": y -= height / 2
        case "B": y -= height

    #draw Button and check for Clicks
    if event.type == pygame.MOUSEBUTTONUP:
        clicked = False
    if x <= mouse_pos[0] <= x+width and y <= mouse_pos[1] <= y+height:
        if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
            clicked = True
            btn_pressed = True
        pygame.draw.rect(surface, selected_color, [x, y, width, height], 0, 10)
    else:
        pygame.draw.rect(surface, color, [x, y, width, height], 0, 10)

    #draw Text if Text is given
    if text != 0:
        text_x_align = x - (text.get_width() / 2)
        text_y_align = y - (text.get_height() / 2)
        surface.blit(text, (text_x_align + (width / 2), text_y_align + (height / 2)))

    #Return if the Button is pressed
    return btn_pressed

#Setup
pygame.init()
surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ETS2TC")
ico = pygame.image.load('assets/icon.png')
pygame.display.set_icon(ico)
#Other vars
ico = pygame.transform.scale(ico, (200, 200))
button_col = (63, 73, 92)
text_col = (255, 255, 255)
clicked = False
current_screen = 0
selected_input = 0
user_input = ["", "", ""]
timer_switch_interval = 500
clock = pygame.time.Clock()
timer_last_switch = 0
timer_state = False
#render texts
main_font = pygame.font.SysFont('comicsans', 30)
text_button_1 = main_font.render('Euro Truck Time --> Real Time', True, text_col)
text_button_2 = main_font.render('Real Time --> Euro Truck Time', True, text_col)
text_ets_hrs = main_font.render('Euro Truck Hours', True, text_col)
text_ets_min = main_font.render('Euro Truck Minutes', True, text_col)
text_irl_hrs = main_font.render('Real Hours', True, text_col)
text_irl_min = main_font.render('Real Minutes', True, text_col)
text_button_back = main_font.render('<', True, text_col)



def selection_screen():
    mouse = pygame.mouse.get_pos()
    surface.blit(ico, (300, 10))
    global current_screen

    #Buttons
    if button(surface.get_width() / 2, 300, 400, 50,button_col, lighten_color(button_col, 0.5), text_button_1, event, mouse, 'M', 'T'):
        current_screen = 1
    if button(surface.get_width() / 2, 400, 400, 50,button_col, lighten_color(button_col, 0.5), text_button_2, event, mouse, 'M', 'T'):
        current_screen = 2

def ets_to_irl_screen():
    mouse = pygame.mouse.get_pos()
    #import vars
    global current_screen
    global selected_input
    global user_input
    global timer_state
    hrs_button_col = button_col
    min_button_col = button_col

    #get pressed numbers
    if event.type == pygame.KEYDOWN:
        if chr(event.key).isdigit():
            user_input[0] += chr(event.key)
        elif event.key == pygame.K_BACKSPACE:
            user_input[0] = user_input[0][:-1]

    #decide which input should be written to
    match selected_input:
        case 1:
            user_input[1] = user_input[0]
            hrs_button_col = lighten_color(button_col, 0.5)
            text_user_input_hrs = main_font.render(user_input[1] + "_", True, text_col)
            text_user_input_min = main_font.render(user_input[2], True, text_col)
        case 2:
            user_input[2] = user_input[0]
            min_button_col = lighten_color(button_col, 0.5)
            text_user_input_hrs = main_font.render(user_input[1], True, text_col)
            text_user_input_min = main_font.render(user_input[2] + "_", True, text_col)
        case _:
            text_user_input_hrs = main_font.render("", False, (0, 0, 0))
            text_user_input_min = main_font.render("", False, (0, 0, 0))


    minutes = int(0)
    hours = int(0)
    if user_input[1] != "":
        hours = int(user_input[1])
    if user_input[2] != "":
        minutes = int(user_input[2])

    #turn ours into minutes and real ets2 timescale
    minutes = (minutes + (hours * 60)) / 19

    #turn calculated minutes back into Hours
    hours = minutes // 60
    minutes = minutes % 60

    #render output
    blit_render_multiline(surface.get_width() / 2, 400, main_font,
                          f"{user_input[1] if user_input[1] else 0} Hours and {user_input[2] if user_input[2] else 0} Minutes in ETS2 are\n{int(hours)} Hours and {int(minutes)} Minutes IRL.",
                          True, text_col, surface, "M", "T")


    #buttons
    surface.blit(text_ets_hrs, (250, 130))
    if button(surface.get_width() / 2, 180, 300, 50, hrs_button_col, hrs_button_col, text_user_input_hrs, event, mouse, 'M', 'T'):
        selected_input = 1
        user_input[0] = ""
        user_input[1] = ""
    surface.blit(text_ets_min, (250, 250))
    if button(surface.get_width() / 2, 300, 300, 50, min_button_col, min_button_col, text_user_input_min, event, mouse, 'M', 'T'):
        selected_input = 2
        user_input[0] = ""
        user_input[2] = ""
    if button(20, 20, 50, 50, button_col, lighten_color(button_col, 0.5), text_button_back, event, mouse, 'L', 'T'):
        current_screen = 0

def irl_to_ets_screen():
    mouse = pygame.mouse.get_pos()
    # import vars
    global current_screen
    global selected_input
    global user_input
    hrs_button_col = button_col
    min_button_col = button_col

    # get pressed numbers
    if event.type == pygame.KEYDOWN:
        if chr(event.key).isdigit():
            user_input[0] += chr(event.key)
        elif event.key == pygame.K_BACKSPACE:
            user_input[0] = user_input[0][:-1]

    # decide which input should be written to
    match selected_input:
        case 1:
            user_input[1] = user_input[0]
            hrs_button_col = lighten_color(button_col, 0.5)
            text_user_input_hrs = main_font.render(user_input[1] + "_", True, text_col)
            text_user_input_min = main_font.render(user_input[2], True, text_col)
        case 2:
            user_input[2] = user_input[0]
            min_button_col = lighten_color(button_col, 0.5)
            text_user_input_min = main_font.render(user_input[2] + "_", True, text_col)
            text_user_input_hrs = main_font.render(user_input[1], True, text_col)
        case _:
            text_user_input_hrs = main_font.render("", False, (0, 0, 0))
            text_user_input_min = main_font.render("", False, (0, 0, 0))

    minutes = int(0)
    hours = int(0)
    if user_input[1] != "":
        hours = int(user_input[1])
    if user_input[2] != "":
        minutes = int(user_input[2])

    # turn ours into minutes and real ets2 timescale
    minutes = (minutes + (hours * 60)) * 19

    # turn calculated minutes back into Hours
    hours = minutes // 60
    minutes = minutes % 60

    # render output
    blit_render_multiline(surface.get_width() / 2, 400, main_font,
                          f"{user_input[1] if user_input[1] else 0} Hours and {user_input[2] if user_input[2] else 0} Minutes IRL are\n{int(hours)} Hours and {int(minutes)} Minutes in ETS2.",
                          True, text_col, surface, "M", "T")

    # buttons
    surface.blit(text_irl_hrs, (250, 130))
    if button(surface.get_width() / 2, 180, 300, 50, hrs_button_col, hrs_button_col, text_user_input_hrs, event, mouse,'M', 'T'):
        selected_input = 1
        user_input[0] = ""
        user_input[1] = ""
    surface.blit(text_irl_min, (250, 250))
    if button(surface.get_width() / 2, 300, 300, 50, min_button_col, min_button_col, text_user_input_min, event, mouse,'M', 'T'):
        selected_input = 2
        user_input[0] = ""
        user_input[2] = ""
    if button(20, 20, 50, 50, button_col, lighten_color(button_col, 0.5), text_button_back, event, mouse, 'L', 'T'):
        current_screen = 0

program_running = True
while program_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_running = False

        surface.fill((29, 30, 35))
        match current_screen:
            case 0:
                selection_screen()
            case 1:
                ets_to_irl_screen()
            case 2:
                irl_to_ets_screen()

    pygame.display.flip()

pygame.quit()

