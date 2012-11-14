#===============================================================================
# @version:		1.0.0
# @summary:		This python script creates install archives for Joomla componentes
# @copyright:	(C) 2012 Mathias Gebhardt
# @license:		GNU General Public License version 2 or later; see LICENSE.txt
#===============================================================================

from xml.dom.minidom import parse
import zipfile
import os
import sys

# Change to components root directory
os.chdir('..')

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

# get folders
folders = []
# get frontend and backend folder
for folder in manifest.getElementsByTagName('files'):
	folders.append(folder.attributes['folder'].value)
# get folder for media
folders.append(manifest.getElementsByTagName('media')[0].attributes['folder'].value)
# get folder for installer language
folders.append('language')

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