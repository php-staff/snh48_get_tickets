#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from PIL import Image
import os


# 暴力识别，好蠢啊。。。报警了
def judge(image):
    num = {}
    index = 0
    data = image.getdata()
    w, h = image.size
    for x in xrange(0, w - 7):
        for y in xrange(0, h - 9):
            # 判断0
            if data[w * (y + 1) + x + 3] == (0, 0, 0) and data[w * (y + 1) + x + 4] == (0, 0, 0) and \
                            data[w * (y + 4) + x] == (0, 0, 0) and data[w * (y + 4) + x + 7] == (0, 0, 0) and \
                            data[w * (y + 5) + x] == (0, 0, 0) and data[w * (y + 5) + x + 7] == (0, 0, 0) and \
                            data[w * (y + 8) + x + 3] == (0, 0, 0) and data[w * (y + 8) + x + 4] == (0, 0, 0) and \
                            data[w * (y + 6) + x] == (0, 0, 0) and data[w * (y + 6) + x + 7] == (0, 0, 0) and \
                            data[w * y + x + 3] == (0, 0, 0) and data[w * y + x + 4] == (0, 0, 0) and \
                            data[w * (y + 9) + x + 3] == (0, 0, 0) and data[w * (y + 9) + x + 4] == (0, 0, 0):
                num[index] = 0
                index += 1
                if index > 3:
                    return num
                x += 7
            # 判断9
            elif data[w * (y + 5) + x + 3] == (0, 0, 0) and data[w * (y + 5) + x + 4] == (0, 0, 0) and \
                        data[w * (y + 5) + x + 6] == (0, 0, 0) and data[w * (y + 5) + x + 7] == (0, 0, 0) and \
                        data[w * (y + 7) + x + 6] == (0, 0, 0) and data[w * (y + 7) + x + 7] == (0, 0, 0) and \
                        data[w * y + x + 3] == (0, 0, 0) and data[w * y + x + 4] == (0, 0, 0) and \
                        data[w * (y + 9) + x + 3] == (0, 0, 0) and data[w * (y + 9) + x + 4] == (0, 0, 0) and \
                        data[w * (y + 1) + x + 1] == (0, 0, 0) and data[w * (y + 2) + x + 1] == (0, 0, 0) and \
                        data[w * (y + 3) + x + 1] == (0, 0, 0):
                num[index] = 9
                index += 1
                if index > 3:
                    return num
                x += 7
            # 判断6
            elif data[w * (y + 4) + x + 3] == (0, 0, 0) and data[w * (y + 4) + x + 4] == (0, 0, 0) and \
                        data[w * (y + 5) + x] == (0, 0, 0) and data[w * (y + 6) + x] == (0, 0, 0) and \
                        data[w * (y + 6) + x + 6] == (0, 0, 0) and data[w * (y + 7) + x + 6] == (0, 0, 0) and \
                        data[w * (y + 6) + x + 7] == (0, 0, 0) and data[w * (y + 7) + x + 7] == (0, 0, 0) and \
                        data[w * y + x + 3] == (0, 0, 0) and data[w * y + x + 4] == (0, 0, 0) and \
                        data[w * (y + 9) + x + 3] == (0, 0, 0) and data[w * (y + 9) + x + 4] == (0, 0, 0) and \
                        data[w * (y + 1) + x + 1] == (0, 0, 0) and data[w * (y + 2) + x + 1] == (0, 0, 0) and \
                        data[w * (y + 3) + x + 1] == (0, 0, 0):
                num[index] = 6
                index += 1
                if index > 3:
                    return num
                x += 7
            # 判断5
            elif data[w * y + x] == (0, 0, 0) and data[w * (y + 1) + x] == (0, 0, 0) and \
                        data[w * y + x + 1] == (0, 0, 0) and data[w * (y + 1) + x + 1] == (0, 0, 0) and \
                        data[w * (y + 4) + x + 1] == (0, 0, 0) and data[w * (y + 4) + x + 2] == (0, 0, 0) and \
                        data[w * (y + 5) + x + 7] == (0, 0, 0) and data[w * (y + 7) + x + 7] == (0, 0, 0) and \
                        data[w * y + x + 2] == (0, 0, 0) and data[w * y + x + 6] == (0, 0, 0) and \
                        data[w * (y + 4) + x] == (0, 0, 0) and data[w * (y + 6) + x + 7] == (0, 0, 0) and \
                        data[w * y + x + 3] == (0, 0, 0) and data[w * y + x + 4] == (0, 0, 0) and \
                        data[w * (y + 9) + x + 3] == (0, 0, 0) and data[w * (y + 9) + x + 4] == (0, 0, 0) and \
                        data[w * (y + 1) + x + 1] == (0, 0, 0) and data[w * (y + 2) + x + 1] == (0, 0, 0) and \
                        data[w * (y + 3) + x + 1] == (0, 0, 0):
                num[index] = 5
                index += 1
                if index > 3:
                    return num
                x += 7
            # 判断8
            elif data[w * (y + 4) + x + 3] == (0, 0, 0) and data[w * (y + 4) + x + 4] == (0, 0, 0) and \
                        data[w * (y + 2) + x] == (0, 0, 0) and data[w * (y + 2) + x + 7] == (0, 0, 0) and \
                        data[w * (y + 4) + x + 3] == (0, 0, 0) and data[w * (y + 4) + x + 4] == (0, 0, 0) and \
                        data[w * (y + 7) + x + 1] == (0, 0, 0) and data[w * (y + 7) + x + 6] == (0, 0, 0) and \
                        data[w * y + x + 3] == (0, 0, 0) and data[w * y + x + 4] == (0, 0, 0) and \
                        data[w * (y + 9) + x + 3] == (0, 0, 0) and data[w * (y + 9) + x + 4] == (0, 0, 0) and \
                        data[w * (y + 1) + x + 1] == (0, 0, 0) and data[w * (y + 2) + x + 1] == (0, 0, 0) and \
                        data[w * (y + 3) + x + 1] == (0, 0, 0):
                num[index] = 8
                index += 1
                if index > 3:
                    return num
                x += 7
            # 判断3
            elif data[w * (y + 1) + x] == (0, 0, 0) and data[w * (y + 1) + x + 1] == (0, 0, 0) and \
                        data[w * (y + 8) + x + 5] == (0, 0, 0) and data[w * (y + 4) + x + 4] == (0, 0, 0) and \
                        data[w * (y + 2) + x + 7] == (0, 0, 0) and data[w * (y + 6) + x + 7] == (0, 0, 0) and \
                        data[w * (y + 7) + x + 7] == (0, 0, 0) and data[w * (y + 8) + x] == (0, 0, 0) and \
                        data[w * y + x + 3] == (0, 0, 0) and data[w * y + x + 4] == (0, 0, 0) and \
                        data[w * (y + 9) + x + 3] == (0, 0, 0) and data[w * (y + 9) + x + 4] == (0, 0, 0):
                num[index] = 3
                index += 1
                if index > 3:
                    return num
                x += 7
            # 判断2
            elif data[w * (y + 2) + x] == (0, 0, 0) and data[w * (y + 2) + x + 1] == (0, 0, 0) and \
                        data[w * (y + 2) + x + 6] == (0, 0, 0) and data[w * (y + 2) + x + 7] == (0, 0, 0) and \
                        data[w * (y + 6) + x + 3] == (0, 0, 0) and data[w * (y + 7) + x + 3] == (0, 0, 0) and \
                        data[w * (y + 9) + x] == (0, 0, 0) and data[w * (y + 9) + x + 7] == (0, 0, 0) and \
                        data[w * y + x + 3] == (0, 0, 0) and data[w * y + x + 4] == (0, 0, 0) and \
                        data[w * (y + 9) + x + 3] == (0, 0, 0) and data[w * (y + 9) + x + 4] == (0, 0, 0):
                num[index] = 2
                index += 1
                if index > 3:
                    return num
                x += 7
            # 判断1
            elif data[w * (y + 2) + x + 1] == (0, 0, 0) and data[w * (y + 2) + x + 4] == (0, 0, 0) and \
                        data[w * (y + 2) + x + 3] == (0, 0, 0) and data[w * (y + 2) + x + 4] == (0, 0, 0) and \
                        data[w * (y + 3) + x + 3] == (0, 0, 0) and data[w * (y + 3) + x + 4] == (0, 0, 0) and \
                        data[w * (y + 6) + x + 3] == (0, 0, 0) and data[w * (y + 6) + x + 4] == (0, 0, 0) and \
                        data[w * (y + 8) + x + 3] == (0, 0, 0) and data[w * (y + 5) + x + 4] == (0, 0, 0) and \
                        data[w * (y + 9) + x + 1] == (0, 0, 0) and data[w * (y + 9) + x + 6] == (0, 0, 0) and \
                        data[w * (y + 9) + x + 3] == (0, 0, 0) and data[w * (y + 9) + x + 4] == (0, 0, 0):
                num[index] = 1
                index += 1
                if index > 3:
                    return num
                x += 7
            # 判断7
            elif data[w * y + x] == (0, 0, 0) and data[w * y + x + 7] == (0, 0, 0) and \
                        data[w * (y + 2) + x + 6] == (0, 0, 0) and data[w * (y + 2) + x + 7] == (0, 0, 0) and \
                        data[w * (y + 5) + x + 3] == (0, 0, 0) and data[w * (y + 6) + x + 3] == (0, 0, 0) and \
                        data[w * (y + 8) + x] == (0, 0, 0) and data[w * (y + 9) + x] == (0, 0, 0) and \
                        data[w * y + x + 3] == (0, 0, 0) and data[w * y + x + 4] == (0, 0, 0):
                num[index] = 7
                index += 1
                if index > 3:
                    return num
                x += 7
            # 判断4
            elif data[w * y + x + 5] == (0, 0, 0) and data[w * y + x + 6] == (0, 0, 0) and \
                            data[w * (y + 2) + x + 5] == (0, 0, 0) and data[w * (y + 2) + x + 6] == (0, 0, 0) and \
                            data[w * (y + 6) + x + 5] == (0, 0, 0) and data[w * (y + 6) + x + 6] == (0, 0, 0) and \
                            data[w * (y + 9) + x + 5] == (0, 0, 0) and data[w * (y + 9) + x + 6] == (0, 0, 0) and \
                            data[w * (y + 5) + x] == (0, 0, 0) and data[w * (y + 6) + x] == (0, 0, 0):
                num[index] = 4
                index += 1
                if index > 3:
                    return num
                x += 7
    return num
