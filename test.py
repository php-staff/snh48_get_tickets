#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from PIL import Image
import os
from pytesseract import pytesseract


def image_deal():
    path = "./pic/"
    for f in os.listdir(path):
        image = Image.open(path + f)
        data = image.getdata()
        w, h = image.size
        for x in xrange(0, w):
            for y in xrange(0, h):
                center_pixel = data[w*y + x]
                if x < 3 or x > w - 3 or y < 3 or y > h - 3:
                    image.putpixel((x, y), 3)
                elif center_pixel == 0:
                    black_point = 0
                    top_pixel = data[w * (y - 1) + x]
                    left_pixel = data[w * y + (x - 1)]
                    bottom_pixel = data[w * (y + 1) + x]
                    right_pixel = data[w * y + (x + 1)]
                    top_left_pixel = data[w * (y - 1) + x - 1]
                    top_right_pixel = data[w * (y - 1) + x + 1]
                    bottom_left_pixel = data[w * (y + 1) + x - 1]
                    bottom_right_pixel = data[w * (y + 1) + x + 1]
                    right_away_pixel = data[w * y + (x + 4)]
                    left_away_pixel = data[w * y + (x - 4)]
                    if top_pixel == 0:
                        black_point += 2
                    if left_pixel == 0:
                        if left_away_pixel == 0:
                            continue
                        black_point += 2
                    if bottom_pixel == 0:
                        black_point += 2
                    if right_pixel == 0:
                        if right_away_pixel == 0:
                            continue
                        black_point += 2
                    if top_left_pixel == 0:
                        black_point += 1
                    if top_right_pixel == 0:
                        black_point += 1
                    if bottom_left_pixel == 0:
                        black_point += 1
                    if bottom_right_pixel == 0:
                        black_point += 1
                    if black_point < 3:
                        image.putpixel((x, y), 3)
        image.save('./new_pic/' + f)
        image.close()


def deal(image):
    image = image.convert('RGB')
    data = image.getdata()
    w, h = image.size

    for x in xrange(0, w):
        for y in xrange(0, h):
            center_pixel = data[w * y + x]
            if center_pixel != (0, 0, 0) and center_pixel != (255, 255, 255):
                image.putpixel((x, y), (255, 255, 255))
            if x < 3 or x > w - 3 or y < 3 or y > h - 3:
                image.putpixel((x, y), (255, 255, 255))
            elif center_pixel == (0, 0, 0):
                black_point = 0
                top_pixel = data[w * (y - 1) + x]
                left_pixel = data[w * y + (x - 1)]
                bottom_pixel = data[w * (y + 1) + x]
                right_pixel = data[w * y + (x + 1)]
                top_left_pixel = data[w * (y - 1) + x - 1]
                top_right_pixel = data[w * (y - 1) + x + 1]
                bottom_left_pixel = data[w * (y + 1) + x - 1]
                bottom_right_pixel = data[w * (y + 1) + x + 1]
                right_away_pixel = data[w * y + (x + 4)]
                left_away_pixel = data[w * y + (x - 4)]
                if top_pixel == (0, 0, 0):
                    black_point += 2
                if left_pixel == (0, 0, 0):
                    if left_away_pixel == 0:
                        continue
                    black_point += 2
                if bottom_pixel == (0, 0, 0):
                    black_point += 2
                if right_pixel == (0, 0, 0):
                    if right_away_pixel == (0, 0, 0):
                        continue
                    black_point += 2
                if top_left_pixel == (0, 0, 0):
                    black_point += 1
                if top_right_pixel == (0, 0, 0):
                    black_point += 1
                if bottom_left_pixel == (0, 0, 0):
                    black_point += 1
                if bottom_right_pixel == (0, 0, 0):
                    black_point += 1
                if black_point < 3:
                    image.putpixel((x, y), (255, 255, 255))
    return image


if __name__ == '__main__':
    image_deal()

