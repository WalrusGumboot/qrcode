+++++++++++++++++++++++++
+                       +
+   QR CODE GENERATOR   +
+                       +
+++++++++++++++++++++++++

Hi! This is a document which should guide you through
getting everything to run on your machine.

First off, the code requires some prerequisites.
You will need:
1. A working Python 3.x install, along with pip
	(on your machine this should all already be fine)
2. The following Python libraries:
 - json
 - zlib
 - base45
 - cbor2
 - qrcode
 - code
 	(you can make sure these are installed by copying
	 the following command into a terminal, NOT into IDLE:

	 pip3 install json zlib base45 cbor2 qrcode cose

	 This will either reinstall the libraries if they were
	 already installed or install them if they weren't.)


+++ FILE DESCRIPTIONS +++

The pers_test.json file functions as the source for the algorithm.

The encode.py file turns it into a QR code signed with a random key.

To reiterate, this isn't a valid NHS code and will not grant you
access to any events. Then again, apparently the same goes for most
actual official NHS codes. Oh well.

The decode.py file serves no real purpose but I left it in for
completeness' sake.

Everything in the /docs directory is also redundant, but I kinda just
zipped the whole working directory so it's still in there.

+++ USAGE +++

All you have to do is, into a terminal, type the following:

	python encode.py

The program will do the rest.
The QR code will be saved to a file called output.png; if that file
already exists it will overwrite it.
