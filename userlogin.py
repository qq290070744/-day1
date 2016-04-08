#!/usr/bin/env python
# -*- coding:utf-8 -*-

import  sys
userpass={'jwh':'123456','wenhui':'654321','test':'test','test01':'abcd1234'}#用户名和密码的字典
counter=0#定义登录次数（初始值是0）

with open('suouser.txt') as f:#从文件读取已经锁定的用户
        f=f.readlines()
        a=[]
        for i in f:
                i=i.strip('\n')
                a.append(i)

while True:
    user=input("请输入要登录的用户名:")
    if user in a:#判断用户是否被锁
            print ("此用户已经被锁")
            jiesuo=input("是否需要解锁账户y/n:")
            if jiesuo=='y':

                    while True:
                        adminuser=input('请输入管理员帐号:')
                        if adminuser not in 'root':
                                print ("管理员帐号不对")
                                continue
                        else:

                                while True:
                                        adminpwd=input('请输入管理员密码:')
                                        if adminpwd != '123456':
                                                print("管理员密码不对")
                                                continue
                                        else:
                                                break
                                break
                    while True:
                        jiesuouser=input('请输入你要解锁的帐号:')

                        if jiesuouser in a:
                            a.remove(jiesuouser)
                            f=open('suouser.txt','w')
                            f.write('')
                            f.close()
                            for line in a:
                                    f=open('suouser.txt','a')
                                    f.write('%s\n'%line)
                                    f.close()


                            print ("帐号%s已经被解锁,请重新去用此用户登录" % jiesuouser)
                            sys.exit()
                        else:
                            tuichu=input('此帐号不存在或已经被解锁。是否要继续解锁其他帐号y/n:')
                            if tuichu=='y':
                              continue
                            else:
                                    sys.exit()


            else:
                    continue
    if user not  in userpass.keys():
            print ("用户名不存在")
            continue
    else:
            pass
            break


while True:
        if counter<3:
                password=input("输入密码:").strip()
                if len(password)==0:
                        print ("\033[36m密码不能为空\033[0m")
                        counter+=1
                        continue
                elif password==userpass[user]:
                        pass
                else:
                        print ("\033[37m用户名为 %s的这个用户的密码不对\033[0m" % user)
                        counter+=1
                        continue
                break
        else:
                print ("\033[32m输入密码错误3次，用户已经被锁定了\033[0m")
                f=open('suouser.txt','a')
                f.write('\n%s' %(user))#锁定用户并写入到文件
                f.close()
                sys.exit()

print("\033[34m-----------------用户%s密码验证通过,欢迎进入系统----------------\033[1m"%user)
