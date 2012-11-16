#===============================================================================
# @version:        1.0.0
# @summary:        Test script for version compare function
# @copyright:      (C) 2012 Mathias Gebhardt
# @license:        GNU General Public License version 2 or later; see LICENSE.txt
#===============================================================================

from xml.dom.minidom import parse, parseString
import zipfile
import os
import sys
import urllib2
import re

#===============================================================================
# Checks whether version1 is newer than version2
#===============================================================================
def version_compare(version1, version2):
    #===========================================================================
    # 
    #===========================================================================
    def text_to_number(text):
        text = text.lower()
        if text == '':
            number = 7
        elif text == 'dev':
            number = 1
        elif text == 'alpha' or text == 'a':
            number = 2
        elif text == 'beta' or text == 'b':
            number = 3
        elif text == 'rc':
            number = 4
        elif text == '#':
            number = 5
        elif text == 'pl' or text == 'p':
            number = 6
        else:
            number = 0
            
        return number
    
    #===========================================================================
    # Normalize version
    # Replace _, - and + with . and split string at the dots
    #===========================================================================
    def normalize_version(version):
        # replace _, - and + with .
        version.replace('_', '.')
        version.replace('-', '.')
        version.replace('+', '.')
        # add dots befor and after text
        version = re.sub(r'([^\d\.]+)', r'.\1.', version)
        version = re.sub(r'\.{2,}', r'.', version)
        # split at the dots
        version = version.split('.')
        
        # convert to int and fill up all 3 release numbers with 0
        for i in range(0, 5):
            if len(version) <= i:
                if i != 3:
                    # normaly append 0
                    version.append(0)
                else:
                    # if text not set append 7
                    version.append(7)
                    version.append(0)
                    break
            else:
                if i != 3:
                    # normaly convert string to int
                    version[i] = int(version[i])
                else:
                    # if text use conversion method
                    version[i] = text_to_number(version[i])
        
        return version
    
    version1 = normalize_version(version1.lower()) 
    version2 = normalize_version(version2.lower())
            
    # check major/minor/maintenance release number
    for i in range(0,5):
        if version1[i] > version2[i]:
        # that's it; new major/minor/maintenance release
            return 1
        elif version1[i] < version2[i]:
        # version 2 has a new major/minor/maintenance release
            return -1
        
    # versions are equal
    return 0
        
version1 = '0.6.0dev2'
print version_compare(version1, '0.6.0dev1')
print version_compare(version1, '0.6.0dev2')
print version_compare(version1, '0.6.0dev3')
print version_compare(version1, '0.6.0alpha1')
print version_compare(version1, '0.6.0hallo1')
print version_compare(version1, '0.6')        
