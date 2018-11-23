# -*- coding: utf-8 -*-
"""
General commands
"""
import os
import json


title = """           .---.  ,---,                   ___                        .---.  ,---,                   ___     
          /. ./|,--.' |                 ,--.'|_                     /. ./|,--.' |                 ,--.'|_   
      .--'.  ' ;|  |  :                 |  | :,'                .--'.  ' ;|  |  :                 |  | :,'  
     /__./ \ : |:  :  :                 :  : ' :  .--.--.      /__./ \ : |:  :  :                 :  : ' :  
 .--'.  '   \' .:  |  |,--.  ,--.--.  .;__,'  /  /  /    ' .--'.  '   \' .:  |  |,--.  ,--.--.  .;__,'  /   
/___/ \ |    ' '|  :  '   | /       \ |  |   |  |  :  /`.//___/ \ |    ' '|  :  '   | /       \ |  |   |    
;   \  \;      :|  |   /' :.--.  .-. |:__,'| :  |  :  ;_  ;   \  \;      :|  |   /' :.--.  .-. |:__,'| :    
 \   ;  `      |'  :  | | | \__\/: . .  '  : |__ \  \    `.\   ;  `      |'  :  | | | \__\/: . .  '  : |__  
  .   \    .\  ;|  |  ' | : ," .--.; |  |  | '.'| `----.   \.   \    .\  ;|  |  ' | : ," .--.; |  |  | '.'| 
   \   \   ' \ ||  :  :_:,'/  /  ,.  |  ;  :    ;/  /`--'  / \   \   ' \ ||  :  :_:,'/  /  ,.  |  ;  :    ; 
    :   '  |--" |  | ,'   ;  :   .'   \ |  ,   /'--'.     /   :   '  |--" |  | ,'   ;  :   .'   \ |  ,   /  
     \   \ ;    `--''     |  ,     .-./  ---`-'   `--'---'     \   \ ;    `--''     |  ,     .-./  ---`-'   
      '---"                `--`---'                             '---"                `--`---'               
                                                                                                            """
                                                                                                            
def loadConfig():
    """Loads the config file and creates a new one of not exisiting"""
    if os.path.isfile("config.json"):
        # File found
        return json.loads("config.json")
    else:
        #file not found
        conf = {"conf_ver":1,
                "number":"",
                "key":"",
                "aut_valid":False}
        return conf
        
def saveConf(conf):
    with open("config.json","w") as outfile:
        json.dump(conf,outfile)
        
        
        
def cls():
    os.system('cls')
    

    
    

