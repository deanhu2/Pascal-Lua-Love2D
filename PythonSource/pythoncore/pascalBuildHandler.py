# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import os
import errno

class pascalBuildHandler(object):
    
    _CUSTOM__PATH=False
    
    def __init__(self): # this method creates the class object.
        _CUSTOM__PATH=False
        pass
    
    def _create_output_dir(self,name):
        try:
            os.makedirs(name)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
        pass