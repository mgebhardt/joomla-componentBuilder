#===============================================================================
# @version:        1.0.0
# @summary:        Test script for update server xml creating
# @copyright:      (C) 2012 Mathias Gebhardt
# @license:        GNU General Public License version 2 or later; see LICENSE.txt
#===============================================================================

from xml.dom.minidom import parse, parseString
import zipfile
import os
import sys
import urllib2

os.chdir('..')

updateServer = 'https://github.com/downloads/mgebhardt/osbit/osbit-update.xml'
version = '0.6.0dev5'
zipFileName = 'com_osbit-0.6.0dev5.zip'

file = urllib2.urlopen(updateServer)
dom = parse(file)

# get first update and copy it
# first and last child are \n
# so you you have to search for update
# TODO: search latest update
lastUpdate = dom.getElementsByTagName('update')[0]
update = lastUpdate.cloneNode(True)

# update version
update.getElementsByTagName('version')[0].firstChild.data = version
# update download url
update.getElementsByTagName('downloadurl')[0].firstChild.data = \
    update.getElementsByTagName('downloadurl')[0].firstChild.data.rsplit \
        ('/', 1)[0] + '/' + zipFileName

# add new tag at first position
dom.getElementsByTagName('updates')[0].insertBefore(update, lastUpdate)

xmlFile = open(os.path.join('releases', updateServer.rsplit('/', 1)[1]), 'w')
dom.writexml(xmlFile)
xmlFile.close()


print dom.toxml()