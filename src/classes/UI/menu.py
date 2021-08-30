#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# class Menu:
#     menubar = tkinter.Menu(window)
#
#     # 第6步，创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）
#         filemenu = tkinter.Menu(menubar, tearoff=0)
#         # 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
#         menubar.add_cascade(label='File', menu=filemenu)
#
#         # 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
#         filemenu.add_command(label='New', command=self.do_job)
#         filemenu.add_command(label='Open', command=self.do_job)
#         filemenu.add_command(label='Save', command=self.do_job)
#         filemenu.add_separator()  # 添加一条分隔线
#         filemenu.add_command(label='Exit', command=window.quit)  # 用tkinter里面自带的quit()函数
#
#         # 第7步，创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
#         editmenu = tkinter.Menu(menubar, tearoff=0)
#         # 将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中
#         menubar.add_cascade(label='Edit', menu=editmenu)
#
#         # 同样的在 Edit 中加入Cut、Copy、Paste等小命令功能单元，如果点击这些单元, 就会触发do_job的功能
#         editmenu.add_command(label='Cut', command=self.do_job)
#         editmenu.add_command(label='Copy', command=self.do_job)
#         editmenu.add_command(label='Paste', command=self.do_job)
#
#         # 第8步，创建第二级菜单，即菜单项里面的菜单
#         submenu = tkinter.Menu(filemenu)  # 和上面定义菜单一样，不过此处实在File上创建一个空的菜单
#         filemenu.add_cascade(label='Import', menu=submenu, underline=0)  # 给放入的菜单submenu命名为Import
#
#         # 第9步，创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令（有点拗口，笑~~~）
#         submenu.add_command(label='Submenu_1', command=self.do_job)  # 这里和上面创建原理也一样，在Import菜单项中加入一个小菜单命令Submenu_1
#
#         # 第11步，创建菜单栏完成后，配置让菜单栏menubar显示出来
#         window.config(menu=menubar)
# def do_job(self):
#     print("do job")