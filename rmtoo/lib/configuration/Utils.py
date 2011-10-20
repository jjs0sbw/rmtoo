'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Configuration Utilities.
 
 (c) 2011 by flonatel

 For licensing details see COPYING
'''

from types import DictType

class Utils:
    '''Configuration Utilities.
       This class contains functions to work on different
       aspects of the configuration.'''

    def __init__(self):
        '''Hidden constructor.'''
        assert(False)

    @staticmethod
    def internal_merge_dictionary(orig_dict, new_dict):
        '''Copies all the values from the new_dict into the
           orig_dict.  If a value already exists, it is overwritten.'''
        assert(type(orig_dict) == DictType)
        print("NDT ORIG [%s]" % orig_dict)
        print("NDT NEW  [%s]" % new_dict)
        print("NDT [%s]" % type(new_dict))
        assert(type(new_dict) == DictType)

        for key, value in new_dict.iteritems():
            if key not in orig_dict:
                orig_dict[key] = value
                continue
            if type(orig_dict[key]) == DictType and type(value) == DictType:
                print("RECURSIVE CALL [%s] [%s]" % (orig_dict[key], value))
                Utils.internal_merge_dictionary(orig_dict[key], value)
            else:
                orig_dict[key] = value
