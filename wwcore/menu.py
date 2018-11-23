# -*- coding: utf-8 -*-
"""
Menu file
"""
from lang.en import cmd
from script import script


def menuItem(menu):
    if menu == "not_logged_in":
        return [[cmd["option_register"], "register"],
                [cmd["option_login"],"login"],
                [cmd["option_exit"],"confirm_exit_not"]]
        
    elif menu == "logged_in":
        return [[cmd["option_run_service"],None,script],
                [cmd["option_exit"],"confirm_exit_logged"]]
        
    elif menu == "confirm_exit_logged":
        return [[cmd["option_yes"],None,exit],
                [cmd["option_no"],"logged_in"]]
                
    elif menu == "confirm_exit_not":
        return [[cmd["option_yes"],None,exit],
                [cmd["option_no"],"not_logged_in"]]            
        
    elif menu == "register":
        return [["tbd",None,script],
                [cmd["option_back"],"not_logged_in",None],
                [cmd["option_exit"],"confirm_exit_not"]]
        
    elif menu == "login":
        return [["tbd",None,script],
                [cmd["option_back"],"not_logged_in",exit],
                [cmd["option_exit"],"confirm_exit_not"]]
                
def menuHead(menu):
    if menu == "confirm_exit_logged":
        return cmd["head_confirm_exit"]
    elif menu == "confirm_exit_not":
        return cmd["head_confirm_exit"]
    else:
        return cmd["head_what_to_do"]
                

