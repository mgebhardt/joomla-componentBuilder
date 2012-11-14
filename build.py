from xml.dom.minidom import parseString
import zipfile
import os
import sys

# Change to components root directory
os.chdir('..')

file = open('osbit.xml', 'r')
data = file.read()
file.close()

dom = parseString(data)
version = dom.getElementsByTagName('version')[0].firstChild.data
print version

folders = []
for folder in dom.getElementsByTagName('files'):
	folders.append(folder.attributes['folder'].value)
	
folders.append(dom.getElementsByTagName('media')[0].attributes['folder'].value)
folders.append('language')

zipFileName = os.path.join('releases', 'com_osbit-{0}.zip'.format(version))
print zipFileName

installer = zipfile.ZipFile(zipFileName, mode = 'w')

try:
	for rootdir in folders:
		for root, subFolders, files in os.walk(rootdir):
			for file in files:
				installer.write(os.path.join(root, file))
				
	for file in os.listdir('.'):
		if file[0] == '.':
			continue
		if os.path.isdir(file):
			continue
			
		installer.write(file)
	
finally:
	installer.close()