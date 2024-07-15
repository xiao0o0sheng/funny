# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/15 17:29
# @Author : Xiaosheng Jin
# @Email : xiao0o0sheng@126.com
# @File : 超级大乐透历史数据采集.py
# @Software: PyCharm

import csv

import parsel
import requests

from datetime import datetime

current_year = datetime.now().year


with open('luckydata.csv', mode='w+', encoding='gbk', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['期数','A1','A2','A3','A4','A5','B1','B2'])
    print('开始查询中奖数据并保存...')
    try:
        for i in range(2020, int(current_year) + 1):
            url = f'https://www.55128.cn/zs/12_96.htm?year={i}'
            # print(url)
            response = requests.get(url)
            response.encoding = response.apparent_encoding
            html_data = response.text
            selector = parsel.Selector(html_data)
            trs = selector.xpath('//*[@id="chartData"]/tr')
            for tr in trs:
                res = []
                rr = []
                date = tr.xpath('td[@class="brl"]/text()').getall()
                r1 = tr.xpath('td[@class="chartball_red1"]/text()').getall()
                r2 = tr.xpath('td[@class="chartball_red2"]/text()').getall()
                r3 = tr.xpath('td[@class="chartball_blue"]/text()').getall()
                rr.extend(r1)
                rr.extend(r2)
                rr = sorted(rr)
                res.extend(date)
                res.extend(rr)
                res.extend(r3)

                writer.writerow(res)
    except Exception as e:
        print(e)
        
print('历史中将数据保存完毕!')
print('最新一期的中奖号码是：\t',res[1:])