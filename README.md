joomla-componentBuilder
=======================

a python script to build install archive for Joomla! components.

This is a tiny python script, which do the component release for you. You only have to
change the version of your component in manifest file and run this script.
It will read the component's version from manifest file and create the zip archive
for you.

Please do not run this script from your components root directory. Use a subfolder
(e.g. tools) instead. Also make shure that the folder /releases exits. This scirpt
will write the archive to rootOfYourComponent/releases/<component name>-<version>.zip.

System requirements
===================

Python 2.7

A Joomla! component development directory

Some notes
==========

This script will also read the folder names for frontend, backend and media
folder from manifest. So just run this script and be happy. If you need some
language files during installation you have to place them in
rootOfYourComponent/language/ folder.

The only working/needed script is build.py. All other script are test script to
test some funktions.

Release notes
=============

Version 1.0.0
=============

Basic build functionality. This script only creates the zip archive.

Run this script from a subfolder of the component's root directory (e.g. /tools)

Searchs for manifest file in directory above.

Reads component's name, version and frontend, backend and media folder from
manifest file

Creats the zip archive /releases/<name>-<version>.zip with the content of the
frontend, backend and media folder, all not hidden files (starts not with a .)
of the root directory and the content of /language folder.

Version 1.1.0
=============

Add update server functions.

Searchs also for a updateserver section in manifest file. If there is a
updateserver section it downloads this file and adds a new update section by
copying the first one and writes the new file to
/releases/<fileNameFromServerTag>

