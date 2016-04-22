# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import errno
import os
import sys 

class pascalBuildHandler(object):
    
    _CUSTOM__PATH = False
    _BUILD_EXTENSION = ".lua"
    _LAST_FILE = None
    _LAST_DIRECTORY = None
    
    def __init__(self): # this method creates the class object.
        self._CUSTOM__PATH = False
        self._BUILD_EXTENSION = ".lua"
        self._LAST_FILE = None
        self._Last_DIRECTORY = None
        pass
    
    def _create_file(self, name):
        if( self._LAST_DIRECTORY == None):
            self._LAST_FILE = open(name+self._BUILD_EXTENSION,'w')
        else:
            #fix the use of slash for directory later.
            self._LAST_FILE = open(self._LAST_DIRECTORY+"/"+name+self._BUILD_EXTENSION,'w')
         
        pass
    
    def _build_file(self):
        self._LAST_FILE.close()
    
    def _create_output_dir(self, name):
        try:
            self._LAST_DIRECTORY = name
            os.makedirs(name)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
        pass