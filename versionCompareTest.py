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
#  Enum class for text in version string
#===============================================================================
class version_text(object):
        not_defined = 0
        dev = 7
        alpha = 2
        beta = 3
        rc = 4
        hash = 5
        pl = 6
        none = 7
        
        #=======================================================================
        # Converts text to enum
        #=======================================================================
        def to_enum(text):
            if text == '':
                text = version_text.none
            elif text == 'dev':
                text = version_text.dev
            elif text == 'alpha' or version == 'a':
                text = version_text.alpha
            elif text == 'beta' or version == 'b':
                text = version_text.beta
            elif text == 'rc':
                text = version_text.rc
            elif text == 'pl' or version == 'p':
                text = version_text.pl
            else:
                text = version_text.not_defined
                
            return text
        
        #=======================================================================
        # Converts enum to text
        #=======================================================================
        def to_text(enum):
            if enum == version_text.none:
                text = ''
            elif enum == version_text.dev:
                text = 'dev'
            elif enum == version_text.alpha:
                text = 'alpha'
            elif enum == version_text.beta:
                text = 'beta'
            elif enum == version_text.rc:
                text = 'rc'
            elif enum == version_text.pl:
                text = 'pl'
#===============================================================================
# Checks whether version1 is newer than version2
#===============================================================================
def version_compare(version1, version2):
        
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
        version = re.sub(r'.{2,}', r'.', version)
        # split at the dots
        version = version.split('.')
        
        # convert to int and fill up all 3 release numbers with 0
        for i in range(0, 2):
            if i < len(version):
                version.append(0)
            else:
                version[i] = int(version[i])
        
        # add the text element
        if len(version) < 4:
            version[4] = version_text.none
        elif version == 'dev':
            version = version_text.dev
        elif version == 'alpha' or version == 'a':
            version = version_text.alpha
        elif version == 'b' or version == 'b':
            version = 'beta'
        elif version == 'p':
            version = 'pl'
        
        # add the 4th number or change it to int
        if len(version) == 5:
            version[5] = int(version[5])
        else:
            version.append(0)
        
        return version
    
    #===========================================================================
    # Compares both text with dev < alpha = a < beta = b < RC = rc < # < pl = p < ''
    # Returns -1 if text1 lt text2, 0 if eq and 1 if gt
    #===========================================================================
    def text_compare(text1, text2):
        # nd is not defined
        order = ['nd', 'dev', 'alpha', 'beta', 'rc', '#', 'pl']
        if not(text1 in order):
            text1 = 'nd'
        if not(text2 in order):
            text2 = 'nd'
    
    version1 = normalize_version(version1.lower()) 
    version2 = normalize_version(version2.lower())
            
    # check major/minor/maintenance release number
    for i in range(0,2):
        if version1[i] > version2[i]:
        # that's it; new major/minor/maintenance release
            return True
        elif version1[i] < version2[i]:
        # version 2 has a new major/minor/maintenance release
            return False
    
    # now check for dev < alpha = a < beta = b < RC = rc < # < pl = p < ''
    if len(version1) == 3 and len(version2) > 3:
    
    
        
        
version1 = '0.6'
version2 = '0.6.0dev2'
print version_compare(version1, version2)        
