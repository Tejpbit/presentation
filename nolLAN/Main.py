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

def print_text_slow(string):

    row_list = string.split('\n')

    #convert all rows from strings to lists
    for row in row_list:
        row_list[row_list.index(row)] = list(row)

    # add the index of the row to the first index of the row, it'll be useful later i promise
    for i in range(0, len( row_list)):
        row_list[i].insert(0, i)

    #remove last row of list. cus it's empty for some reason
    del row_list[-1]

    #list to remember how many chars has been printed in each row
    marker_list = []
    for i in row_list:
        marker_list.append(0)

    font_size = 8
    ascii_art_size = (font_size * (len(row_list[0])-2), font_size * len(row_list))
    screen_size = screen.get_size()
    offset_to_centralize_ascii_art = (screen_size[0]/2 - ascii_art_size[0]/2, screen_size[-1]/2 - ascii_art_size[-1]/2)

    while (row_list):
        rand_row = random.choice(row_list)
        #sleep(0.001)
        marker_list[rand_row[0]] += 1
        display_char_at_pos(rand_row.pop(1), (offset_to_centralize_ascii_art[0] + marker_list[rand_row[0]]*font_size, offset_to_centralize_ascii_art[-1] + rand_row[0]*font_size)) #TODO magic numbers (font_size). size should be gotten from the font beeing used no?
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
    size = font.size(''.join(asciipic[0]))
    height = len(asciipic) * size[1]
    return (size[0], height)

def main():

    digitAscii = Pictoasciiart.get_ascii_art("digit.png")
    print_text_slow(digitAscii)
    digitPic = pygame.transform.scale(pygame.image.load('digit.png'), (get_picsize_from_asciipic(digitAscii))).convert()

    #sleep(1)
    #fade_to_black()
    fade_in(digitPic)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0,0))
        pygame.display.flip()

if __name__ == "__main__": main()