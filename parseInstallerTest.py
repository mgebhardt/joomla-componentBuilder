#===============================================================================
# @version:        1.0.0
# @summary:        Test script for manifest parseing
# @copyright:      (C) 2012 Mathias Gebhardt
# @license:        GNU General Public License version 2 or later; see LICENSE.txt
#===============================================================================

from xml.dom.minidom import parse, parseString
import zipfile
import os
import sys

# Change to components root directory
os.chdir('..')

dom = parse('osbit.xml').getElementsByTagName('extension')[0]
print dom.toxml()
#version = dom.getElementsByTagName('version')[0].firstChild.data
#print version

#folders = []
#for folder in dom.getElementsByTagName('files'):
#	folders.append(folder.attributes['folder'].value)
#	
#folders.append(dom.getElementsByTagName('media')[0].attributes['folder'].value)
#folders.append('language')

#print folders