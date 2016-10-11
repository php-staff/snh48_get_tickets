#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""SNH48 Get Tickets

Usage:
    tickets.py <group> <team> <date>

Options:
    -h --help       Show this screen
    -v --version    Show version

Help:
    group:  ALL/SNH/BEJ/GNZ
    team:   ALL/SII/NII/HII/X/XII/B/E/G/NIII
    date:   aw(全部)/tw(本周)/nw(下周)

Example:
    tickets SNH SII aw
"""

from docopt import docopt
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from prettytable import PrettyTable
from nameset import snh
import time
from test import deal
from selenium import webdriver
import sys
from PIL import Image
from judge import judge
from selenium.webdriver.common.keys import Keys

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
reload(sys)
sys.setdefaultencoding("utf-8")

dic = {}
tabs = {}


class TicketsCollection(object):
    header = u'公演名称 时间 代号'.split()

    def __init__(self, rows):
        self.rows = rows

    @property
    def tickets(self):
        for row in self.rows:
            t = row['start_playdate'][6:-5]
            time_array = time.localtime(float(t))
            other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
            dic[row['tickets_name']] = row['tickets_id']
            ticket = [
                row['tickets_name'],
                other_style_time,
                row['tickets_id']
            ]
            yield ticket

    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for ticket in self.tickets:
            pt.add_row(ticket)
        print pt


def cmd():
    arguments = docopt(__doc__, version='SNH Get Tickets 0.0.1 Author: Emilio')
    group = snh.get(arguments['<group>'])
    team = snh.get(arguments['<team>'])
    date = snh.get(arguments['<date>'])
    url = 'http://shop.48.cn/Home/IndexTickets?brand_id={}&team_type={}&date_type={}'\
        .format(group, team, date)
    # print url
    r = requests.get(url)
    rows = r.json()
    # print json.dumps(rows, sort_keys=True, indent=4)
    tickets = TicketsCollection(rows)
    tickets.pretty_print()


if __name__ == '__main__':
    cmd()
    ticset = map(int, raw_input("请输入待切的票代号(若有多种请用空格分隔离)").split())
    for item in ticset:
        print item
    # 设置浏览器路径
    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
    driver.maximize_window()
    suc = False
    # TODO(Emilio) 添加验证码错误重置，监听alert
    driver.get('http://user.snh48.com/login.php')
    username = driver.find_element_by_id('username')
    username.clear()
    username.send_keys(u'YourAccount')
    password = driver.find_element_by_id('password')
    password.clear()
    password.send_keys(u'YourPassword')
    while not suc:
        driver.find_element_by_id('getcode_num').click()
        time.sleep(1)
        # 设置截图保存位置
        driver.save_screenshot('YourScreenShot')

        ocr = driver.find_element_by_id('img')
        location = ocr.location
        size = ocr.size
        r = int(location['x']), int(location['y']), int(location['x'] + size['width']), int(
            location['y'] + size['height'])
        pic = Image.open('YourScreenShot')
        frame = pic.crop(r)
        frame = deal(frame)
        num = judge(frame)
        s = ''
        for x in num.itervalues():
            s += str(x)
        if s.__len__() < 4:
            continue
        ocr = driver.find_element_by_id('code_num')
        ocr.send_keys(s)
        check = driver.find_element_by_name('remember')
        check.click()
        login = driver.find_element_by_id('btn')
        login.click()
        if driver.current_url != u'http://user.snh48.com/code/login_nodb.php':
            suc = True

    # TODO(Emilio) 线程方式完成多页面点选，增加超时重启
    num = 0
    tabs[str(num)] = driver.current_window_handle
    for i in range(ticset.__len__()):
        body = driver.find_element_by_tag_name('body')
        body.send_keys(Keys.CONTROL + 't')
        h = driver.window_handles
        for tab in h:
            if tab in tabs.values():
                continue
            else:
                driver.switch_to.window(tab)
                url = 'http://shop.48.cn/tickets/item/{}'.format(ticset[num])
                driver.get(url)
                num += 1
                tabs[str(num)] = tab
                a = driver.find_element_by_id('seattype2')
                if a.get_attribute('class') is not None:
                    a.click()
            break
