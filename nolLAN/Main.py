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

monospace10 = pygame.font.SysFont("monospace", 10)

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

    while (row_list):
        rand_row = random.choice(row_list)
        #sleep(0.001)
        marker_list[rand_row[0]] += 1
        display_char_at_pos(rand_row.pop(1), (marker_list[rand_row[0]]*10, rand_row[0]*10))
        if len(rand_row) <= 1:
            print "removing row %s" % rand_row
            row_list.remove(rand_row)

def display_char_at_pos(char, (x,y)):
    text = monospace10.render(char, 1, TURQUOISE)
    textpos = text.get_rect()
    textpos.x=x
    #print "y: %s" % y
    textpos.y=y
    background.blit(text, textpos)
    screen.blit(background, (0, 0))
    pygame.display.update(textpos)

def main():

    asciiPic = Pictoasciiart.get_ascii_art("digit.png")
    asciiPic = asciiPic.replace("\t", " ")
    print_text_slow(asciiPic)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0,0))
        pygame.display.flip()

if __name__ == "__main__": main()