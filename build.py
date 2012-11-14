from xml.dom.minidom import parseString
import zipfile
import os
import sys

# Change to components root directory
os.chdir('..')

# @TODO: method to get manifest file
file = open('osbit.xml', 'r')
data = file.read()
file.close()

# create XML dom 
dom = parseString(data)

# get version
version = dom.getElementsByTagName('version')[0].firstChild.data
# print version

# get folders
folders = []
# get frontend and backend folder
for folder in dom.getElementsByTagName('files'):
	folders.append(folder.attributes['folder'].value)
# get folder for media
folders.append(dom.getElementsByTagName('media')[0].attributes['folder'].value)
# get folder for installer language
folders.append('language')

# create file name for archive
zipFileName = os.path.join('releases', 'com_osbit-{0}.zip'.format(version))
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
	
print 'successfully created {}', zipFileName