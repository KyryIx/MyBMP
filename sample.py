##########################################
#  Developed by Everton Pereira da Cruz  #
##########################################

import os.path
from Image import Image

#######################################################################################
# https://lemire.me/blog/2017/11/10/should-computer-scientists-keep-the-lena-picture/ #
# https://i.stack.imgur.com/o1z7p.jpg                                                 #
#                                                                                     #
# Lena.bmp                                                                            #
# width          = 294                                                                #
# height         = 294                                                                #
# bits per pixel = 24                                                                 #
# size           = 259.950 bytes                                                      #
# size in disk   = 262.144 bytes                                                      #
#######################################################################################
if __name__ == "__main__":
	#filename = os.path.dirname(__file__) + '\\' + 'Lena.bmp'
	filename = 'Lenna.bmp'
	print( filename )
	image = Image()
	image.setFilename( filename )
	
	if image.loadContent():
		print( 'Image information:' )
		print( 'Width: ' + str(image.getWidth()) + ' pixels' )
		print( 'Width: ' + str(image.getHeight()) + ' pixels' )
		print( 'Filename: ' + image.getFilename() )
		#print( image.getContent() )
		#image.toBase64()
		image.toHTML( 'thresold', 128 ) # filter are: 'original', 'onlyRed', 'onlyGreen', 'onlyBlue', 'negative', 'grayscale', 'thresold' (with value of thresold)
		
	else:
		print( 'Image not imported' )