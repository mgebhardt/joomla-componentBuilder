#===============================================================================
# @version:		1.1.0
# @summary:		This python script creates install archives for Joomla componentes
# @copyright:	(C) 2012 Mathias Gebhardt
# @license:		GNU General Public License version 2 or later; see LICENSE.txt
#===============================================================================

from xml.dom.minidom import parse
import zipfile
import os
import sys
import urllib2

# Change to components root directory
os.chdir('..')

#===============================================================================
# Search manifest and get some parameters
#===============================================================================

found = False

# search manifest file
for file in os.listdir('.'):
	# must be a xml file
	if '.xml' != file[-4:]:
		continue
	
	# open file and lock in it
	# create XML dom 
	manifest = parse(file)
	
	# root node must be extension
	if 'extension' == manifest.firstChild.nodeName:
		found = True
		break;

if not found:
	print 'Manifest not found!'
	sys.exit(-1)

# get name
name = manifest.getElementsByTagName('name')[0].firstChild.data.lower()

# get version
version = manifest.getElementsByTagName('version')[0].firstChild.data

# get updateServer
if len(manifest.getElementsByTagName('updateservers')) > 0:
	# if update section exsits
	updateServer = manifest.getElementsByTagName('server')[0].firstChild.data
else:
	updateServer = False

# get folders
folders = []
# get frontend and backend folder
for folder in manifest.getElementsByTagName('files'):
	folders.append(folder.attributes['folder'].value)
# get folder for media
folders.append(manifest.getElementsByTagName('media')[0].attributes['folder'].value)
# get folder for installer language
folders.append('language')

#===============================================================================
# Create zip archive
#===============================================================================

# create file name for archive
zipFileName = os.path.join('releases', '{}-{}.zip'.format(name, version))
#print zipFileName

# open archive
installer = zipfile.ZipFile(zipFileName, mode = 'w')

# try to add all files to archive
try:
	# at first add the whole folder for frontend, backend, media and language  
	for rootdir in folders:
		for root, subFolders, files in os.walk(rootdir):
			for file in files:
				installer.write(os.path.join(root, file))
	
	# add the content of component's root folder 
	for file in os.listdir('.'):
		# ignore all hidden files
		if file[0] == '.':
			continue
		# also ignore all folders
		if os.path.isdir(file):
			continue
		
		installer.write(file)
		
finally:
	# every thing added, than close
	installer.close()
	
print 'successfully created {}'.format(zipFileName)

#===============================================================================
# Get update server file and add new update section
#===============================================================================

if updateServer == False:
	# no update server found
	print 'Skipping update server'
	sys.exit(0)

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
        ('/', 1)[0] + '/' + '{}-{}.zip'.format(name, version)
# add new tag at first position
dom.getElementsByTagName('updates')[0].insertBefore(update, lastUpdate)

# get file name
updateXML = os.path.join('releases', updateServer.rsplit('/', 1)[1])

# Write dom to file
xmlFile = open(updateXML, 'w')
dom.writexml(xmlFile)
xmlFile.close()

print 'successfully created {}'.format(updateXML)