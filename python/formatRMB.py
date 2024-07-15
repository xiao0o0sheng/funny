# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2/7/2023 02:52
# @Author : Xiaosheng Jin
# @Email : xiaosheng.jin@ericsson.com
# @File : 人民币转换.py
# @Software: PyCharm

ref = {'1': '壹', '2': '贰', '3': '叁', '4': '肆', '5': '伍', '6': '陆', '7': '柒', '8': '捌', '9': '玖'}


def int_read(s):
    ans = ''
    for i in range(4):
        if i == 0 and s[i] == '0':
            continue
        elif i == 0:
            ans += ref[s[i]] + '仟'
        elif i == 1 and s[i] == '0':
            if s[0] == '0':
                continue
            elif s[2] == s[3] == '0':
                break
            else:
                ans += '零'
        elif i == 1:
            ans += ref[s[i]] + '佰'
        elif i == 2 and s[i] == '0':
            if s[0] == s[1] == '0':
                continue
            elif s[1] == '0':
                continue
            elif s[3] == '0':
                break
            else:
                ans += '零'
        elif i == 2:
            if s[i] != '1':
                ans += ref[s[i]] + '拾'
            else:
                ans += '拾'
        elif s[i] == '0':
            break
        else:
            ans += ref[s[i]]
    return ans


def point_read(s):
    ans = ''
    if s == '00':
        ans += '整'
    elif s[0] == '0':
        ans += ref[s[1]] + '分'
    elif s[1] == '0':
        ans += ref[s[0]] + '角'
    else:
        ans += ref[s[0]] + '角' + ref[s[1]] + '分'
    return ans


def read(s):
    s = str(s).split('.')
    s1 = "{0:0>12s}".format(s[0])
    dr = ['亿', '万', '圆']
    ans = ''
    for i in range(0, 9, 4):
        j = i // 4
        if s1[i:i + 4] == '0000' and dr[j] == '亿':
            continue
        elif dr[j] == '亿':
            ans += int_read(s1[i:i + 4]) + dr[j]
        elif s1[i:i + 4] == '0000' and dr[j] == '万':
            if ans == '':
                continue
            elif s1[8:12] == '0000':
                ans += '元'
                break
            else:
                ans += '零'
        elif dr[j] == '万':
            if s1[i] == '0' and ans != '':
                ans += '零' + int_read(s1[i:i + 4]) + dr[j]
            elif s1[i] == '0':
                ans += int_read(s1[i:i + 4]) + dr[j]
            else:
                ans += int_read(s1[i:i + 4]) + dr[j]
        elif s1[i:i + 4] == '0000':
            if ans != '':
                ans += dr[j]
            else:
                break
        elif s1[i] == '0' and s1[0:4] != '0000' and s1[4:8] == '0000':
            ans += int_read(s1[i:i + 4]) + dr[j]
        elif s1[i] == '0':
            if ans != '':
                ans += '零' + int_read(s1[i:i + 4]) + dr[j]
            else:
                ans += int_read(s1[i:i + 4]) + dr[j]
        else:
            ans += int_read(s1[i:i + 4]) + dr[j]
    if len(s) > 1:
        s2 = s[1]
        ans += point_read(s2)
    return '人民币 ' + ans


while True:
    try:
        print(read(input('请输入人名币金额:\t')))
        # break
    except:
        break
