#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'am_mm_NO.1'
import sys

dic= {
    "广东":{
        "广州":{
            "天河":["体育西","天河南"],
            "越秀":["五羊","穗丰"],
            "海珠":["昌岗","礼岗"]
            },
        "深圳":{
            "南山":["蛇口","科技园"],
            "福田":["车公庙","华强北"]
        }
    },
    "湖北":{
        "武汉":{
            "武昌":["黄鹤","火车站"],
            "汉口":["长江大桥","汉正街"]
        },
        "天门":{
            "净谭":["蒋三台","马峪乡"],
            "卢市":["和乡","新家园乡"]
        }
    }
}

for a in dic:
    print(a)
while True:
    district_name = input("请输入您要查看的省（q可退出）：")
    if district_name=='q':
        sys.exit()
    elif district_name in dic.keys():
        sheng_name = dic[district_name]
        for b in sheng_name:
            print(b)
        while True:
            city_name = input("请输入您要查看的市（b可返回上级，q可退出）：")
            if city_name=='q':
                sys.exit()
            elif city_name=='b':
                break
            elif city_name in  dic[district_name].keys():
                shi_name = dic[district_name][city_name]
                for c in shi_name:
                    print(c)
                while   True:
                    try:
                        qu_name= input("请输入您要查看的区（b可返回上级，q可退出）：")
                        if qu_name=='q':
                            sys.exit()
                        elif qu_name=='b':
                            break

                        qu_name=dic[district_name][city_name][qu_name]
                    except KeyError:
                        print("您的输入有误，请重新输入")
                        continue
                    else:

                        for d in qu_name:
                            print(d)
                        continue

            else:
                print("您的输入有误，请重新输入")
                continue
    else:
        print("您的输入有误，请重新输入")
        continue