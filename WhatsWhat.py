# -*- coding: utf-8 -*-

from wwcore import gen
from wwcore.menu import menuItem, menuHead
from wwcore.lang.en import cmd

gen.cls()


config = gen.loadConfig()

if config["aut_valid"]:
    menu = "logged_in"
else:
    menu = "not_logged_in"
    

while True:
    gen.cls()
    print gen.title
    print menuHead(menu)
    for i in range(len(menuItem(menu))):
        print "[" + str(i+1) + "] " + menuItem(menu)[i][0]
    choice = raw_input(cmd["your_choice"])
    if choice.isdigit():
        choice = int(choice)-1
        if choice in range(len(menuItem(menu))):
            if menuItem(menu)[choice][1] == None:
                menuItem(menu)[choice][2]()
            else:
                menu = menuItem(menu)[choice][1]
    
