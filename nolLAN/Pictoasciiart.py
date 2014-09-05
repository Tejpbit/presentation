__author__ = 'tejp'

from PIL import Image
import random
from bisect import bisect

class Pictoasciiart(object):
    # greyscale.. the following strings represent
    # 7 tonal ranges, from lighter to darker.
    # for a given pixel tonal level, choose a character
    # at random from that range.



    # using the bisect class to put luminosity values
    # in various ranges.
    # these are the luminosity cut-off points for each
    # of the 7 tonal levels. At the moment, these are 7 bands
    # of even width, but they could be changed to boost
    # contrast or change gamma, for example.


    @staticmethod
    def get_ascii_art(source):
        greyscale = [
                " ",
                " ",
                ".,-",
                "_ivc=!/|\\~",
                "gjez2]/(YL)t[+T7Vf",
                "mdK4ZGbNDXY5P*Q",
                "W8KMA",
                "#%$"
                ]

        zonebounds=[36,72,108,144,180,216,252]

        im = Image.open(source)
        # now, work our way over the pixels
        im = im.resize((75,75), Image.ANTIALIAS)
        im = im.convert("L") # convert to mono
        # build up str


        str=""
        for y in range(0,im.size[1]):
            for x in range(0,im.size[0]):
                lum=255-im.getpixel((x,y))
                row=bisect(zonebounds,lum)
                possibles=greyscale[row]
                str=str+possibles[random.randint(0,len(possibles)-1)]
            str=str+"\n"
        return str
