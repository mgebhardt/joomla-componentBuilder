import os
import sys
import zipfile

folders = ['..\\site', '..\\admin', '..\\media', '..\\language']

installer = zipfile.ZipFile('..\\releases\\com_osbit-0.6.0dev2.zip', mode = 'w')

try:
	for rootdir in folders:
		for root, subFolders, files in os.walk(rootdir):
			for file in files:
				installer.write(os.path.join(root, file), arcname = os.path.join(root[3:], file))
				
	root = '..\\'
	for file in os.listdir(root):
		print os.path.isdir('..\\' + file)
		if file[0] == '.':
			continue
		if os.path.isdir('..\\' + file):
			continue
			
		installer.write(os.path.join(root, file), arcname = os.path.join(root[3:], file))			
	
finally:
	installer.close()

installer.printdir();