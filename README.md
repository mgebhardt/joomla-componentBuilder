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

This script will also read the folder names for frontend, backend and media folder from
manifest. So just run this script and be happy. If you need some language files during
installation you have to place them in rootOfYourComponent/language/ folder.

The only working/needed script is build.py. All other script are test script to test
some funktions.