__author__ = 'tejp'

import pygame
import random
from Pictoasciiart import Pictoasciiart
from pygame.locals import *
from time import sleep

pygame.init()

BLACK = (0, 0, 0)
TURQUOISE = (0x09, 0xcd, 0xda)


screen = pygame.display.set_mode()

monospace8 = pygame.font.SysFont("monospace", 8)

#init screen
pygame.display.set_caption('digIT')
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(BLACK)

digitLogo = Pictoasciiart.get_ascii_art("digit.png")

def print_text_slow(row_list, (x, y)):
    """render the provided string one char at a time at specified position (x,y) is the middle of the text"""

    # calculation to render asciiart in center
    font_size = (10, 10)

    row_list = list(row_list)

    #convert all rows from strings to lists
    for row in row_list:
        row_list[row_list.index(row)] = list(row)

    # add the index of the row to the first index of the row, it'll be useful later i promise
    for i in range(0, len( row_list)):
        row_list[i].insert(0, i)

    #remove last row of list. cus it's empty for some reason, probably beacause original string ended with '\n'
    del row_list[-1]

    #list to remember how many chars has been printed in each row
    marker_list = []
    for i in row_list:
        marker_list.append(0)

    while (row_list):
        rand_row = random.choice(row_list)
        #sleep(0.001)
        marker_list[rand_row[0]] += 1
        x_pos = x + marker_list[rand_row[0]]*font_size[0] - 10 # (-10) TODO offbyone error corrected here. Why idunno?
        y_pos = y + rand_row[0]*font_size[-1]
        display_char_at_pos(rand_row.pop(1), (x_pos, y_pos)) #TODO magic numbers (font_size). size should be gotten from the font beeing used no?
        if len(rand_row) <= 1:
            row_list.remove(rand_row)

def display_char_at_pos(char, (x,y)):
    text = monospace8.render(char, 1, TURQUOISE)
    textpos = text.get_rect()
    textpos.x=x
    textpos.y=y
    background.blit(text, textpos)
    screen.blit(background, (0, 0))
    pygame.display.update(textpos)

def fade_to_black():
    blackground = pygame.Surface(screen.get_size())
    for i in range(100): #apparantly, 100 is enough.
        blackground.set_alpha(i)
        screen.blit(blackground,(0,0))
        pygame.display.flip()

def fade_in(pic, pos=(0,0), adddelay=0):
    for t in range(80):
        pic.set_alpha(t)
        screen.blit(pic,pos)
        pygame.display.flip()
        sleep(0.02+adddelay)
    sleep(1)

def get_picsize_from_asciipic(asciipic, font=monospace8):

    width = len(asciipic[0]) * 10
    height = len(asciipic) * 10
    return (width, height)

def main():
    digitAscii = Pictoasciiart.get_ascii_art("digit2.jpg").split('\n')

    # calculation to render asciiart in center
    screen_size = screen.get_size()
    center_screen = (screen_size[0]/2, screen_size[-1]/2)
    picsize = get_picsize_from_asciipic(digitAscii)
    render_pos_to_match_center = (center_screen[0] - picsize[0]/2, center_screen[-1] - picsize[-1]/2)

    del digitAscii[-1]
    print_text_slow(digitAscii, render_pos_to_match_center)
    digitPic = pygame.transform.scale(pygame.image.load('digit2.jpg'), (get_picsize_from_asciipic(digitAscii))).convert()

    #sleep(1)
    #fade_to_black()
    #fade_in(digitPic)

    digit_pic_rect = digitPic.get_rect()
    print digit_pic_rect
    fade_in(digitPic, render_pos_to_match_center, 0.03)

    #background.blit(digitPic, digit_pic_rect)
    #screen.blit(background, (0, 0))
    #pygame.display.update(digit_pic_rect)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0,0))
        pygame.display.flip()

if __name__ == "__main__": main()