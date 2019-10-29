##########################################
#  Developed by Everton Pereira da Cruz  #
##########################################

# https://en.wikipedia.org/wiki/BMP_file_format
# https://en.wikipedia.org/wiki/Endianness#Little
# https://pt.wikipedia.org/wiki/Raster
# http://paulbourke.net/dataformats/bitmaps/
# https://docs.microsoft.com/en-us/dotnet/framework/winforms/advanced/types-of-bitmaps
# https://tools.ietf.org/html/rfc797
# https://tools.ietf.org/html/rfc7903
# https://docs.microsoft.com/pt-br/windows/desktop/gdi/bitmap-storage
# http://www.ic.uff.br/~aconci/curso/bmp.pdf
# https://apps2.mdp.ac.id/perpustakaan/ebook/Karya%20Umum/Compressed-Image-File-Formats.pdf

import os.path

class Image:
	def __init__(self):
		self.width = 0
		self.height = 0
		self.bitsPerPixel = 0
		self.filename = ''
		self.content = []
	
	def setWidth(self, width):
		self.width = width
	
	def getWidth(self):
		return self.width
	
	def setHeight(self, height):
		self.height = height
	
	def getHeight(self):
		return self.height
	
	def setFilename(self, filename):
		# https://docs.python.org/3/library/os.path.html
		self.filename = os.path.dirname(__file__) + '\\' + filename
		if os.path.isfile( self.getFilename() ):
			# https://docs.python.org/3/tutorial/inputoutput.html
			# https://docs.python.org/3/library/functions.html#open
			# https://docs.python.org/3/library/os.html#os.open
			#import os
			#print( os.stat( self.getFilename() ) )
			file = open( self.getFilename(), 'rb' )
			
			type = file.read(2) # BM == 424d ?
			print( 'identify the BMP and DIB: ' + str(type) ) 
			
			file.seek(2)
			size = file.read(4)
			# https://docs.python.org/3/library/functions.html#format
			#print( size[3], hex(size[3] )
			#print( size[2], hex(size[2]) )
			#print( size[1], hex(size[1]) )
			#print( size[0], hex(size[0]) )
			
			a = (16**6) * size[3]
			b = (16**4) * size[2]
			c = (16**2) * size[1]
			d = (16**0) * size[0]
			size = a + b + c + d
			print( 'size of the BMP file in bytes: ' + str(size) )
			
			file.seek(0x0A)
			offsetPixelArray = file.read(4)
			#print( offsetPixelArray[3], hex(offsetPixelArray[3]) )
			#print( offsetPixelArray[2], hex(offsetPixelArray[2]) )
			#print( offsetPixelArray[1], hex(offsetPixelArray[1]) )
			#print( offsetPixelArray[0], hex(offsetPixelArray[0]) )
			a = (16**6) * offsetPixelArray[3]
			b = (16**4) * offsetPixelArray[2]
			c = (16**2) * offsetPixelArray[1]
			d = (16**0) * offsetPixelArray[0]
			offsetPixelArray = a + b + c + d
			print( 'offset pixel array: ' + str(offsetPixelArray) )
			
			file.seek(0x0E)
			sizeHeader = file.read(4)
			#print( sizeHeader[3], hex(sizeHeader[3]) )
			#print( sizeHeader[2], hex(sizeHeader[2]) )
			#print( sizeHeader[1], hex(sizeHeader[1]) )
			#print( sizeHeader[0], hex(sizeHeader[0]) )
			a = (16**6) * sizeHeader[3]
			b = (16**4) * sizeHeader[2]
			c = (16**2) * sizeHeader[1]
			d = (16**0) * sizeHeader[0]
			sizeHeader = a + b + c + d
			print( 'size header in bytes: ' + str(sizeHeader) )
			
			file.seek(0x12)
			bitmapWidth = file.read(4)
			#print( bitmapWidth[3], hex(bitmapWidth[3]) )
			#print( bitmapWidth[2], hex(bitmapWidth[2]) )
			#print( bitmapWidth[1], hex(bitmapWidth[1]) )
			#print( bitmapWidth[0], hex(bitmapWidth[0]) )
			a = (16**6) * bitmapWidth[3]
			b = (16**4) * bitmapWidth[2]
			c = (16**2) * bitmapWidth[1]
			d = (16**0) * bitmapWidth[0]
			bitmapWidth = a + b + c + d
			print( 'bitmap width in pixels: ' + str(bitmapWidth) )
			
			file.seek(0x16)
			bitmapHeight = file.read(4)
			#print( bitmapHeight[3], hex(bitmapHeight[3]) )
			#print( bitmapHeight[2], hex(bitmapHeight[2]) )
			#print( bitmapHeight[1], hex(bitmapHeight[1]) )
			#print( bitmapHeight[0], hex(bitmapHeight[0]) )
			a = (16**6) * bitmapHeight[3]
			b = (16**4) * bitmapHeight[2]
			c = (16**2) * bitmapHeight[1]
			d = (16**0) * bitmapHeight[0]
			bitmapHeight = a + b + c + d
			print( 'bitmap height in pixels: ' + str(bitmapHeight) )
			
			file.seek(0x1A)
			numberColorPlanes = file.read(2)
			#print( numberColorPlanes[1], hex(numberColorPlanes[1]) )
			#print( numberColorPlanes[0], hex(numberColorPlanes[0]) )
			a = (16**2) * numberColorPlanes[1]
			b = (16**0) * numberColorPlanes[0]
			numberColorPlanes = a + b
			print( 'number of color planes: ' + str(numberColorPlanes) )
			
			file.seek(0x1C)
			numberBitsPerPixel = file.read(2)
			#print( numberBitsPerPixel[1], hex(numberBitsPerPixel[1]) )
			#print( numberBitsPerPixel[0], hex(numberBitsPerPixel[0]) )
			a = (16**2) * numberBitsPerPixel[1]
			b = (16**0) * numberBitsPerPixel[0]
			numberBitsPerPixel = a + b
			print( 'number of bits per pixel: ' + str(numberBitsPerPixel) )
			
			file.seek(0x1E)
			compressionMethod = file.read(4)
			#print( compressionMethod[3], hex(compressionMethod[3]) )
			#print( compressionMethod[2], hex(compressionMethod[2]) )
			#print( compressionMethod[1], hex(compressionMethod[1]) )
			#print( compressionMethod[0], hex(compressionMethod[0]) )
			a = (16**6) * compressionMethod[3]
			b = (16**4) * compressionMethod[2]
			c = (16**2) * compressionMethod[1]
			d = (16**0) * compressionMethod[0]
			compressionMethod = a + b + c + d
			valueCompressionMethod = {
				 0: ['BI_RGB',				'none',								'Most common'],
				 1: ['BI_RLE8',				'RLE 8-bit/pixel',					'Can be used only with 8-bit/pixel bitmaps'],
				 2: ['BI_RLE4',				'RLE 4-bit/pixel',					'Can be used only with 4-bit/pixel bitmaps'],
				 3: ['BI_BITFIELDS',		'OS22XBITMAPHEADER: Huffman 1D',	'BITMAPV2INFOHEADER: RGB bit field masks, BITMAPV3INFOHEADER+: RGBA'],
				 4: ['BI_JPEG',				'OS22XBITMAPHEADER: RLE-24',		'BITMAPV4INFOHEADER+: JPEG image for printing[13]'],
				 5: ['BI_PNG',				'',									'BITMAPV4INFOHEADER+: PNG image for printing[13]'],
				 6: ['BI_ALPHABITFIELDS',	'RGBA bit field masks',				'only Windows CE 5.0 with .NET 4.0 or later'],
				11: ['BI_CMYK',				'none',								'only Windows Metafile CMYK[3]'],
				12: ['BI_CMYKRLE8',			'RLE-8',							'only Windows Metafile CMYK'],
				13: ['BI_CMYKRLE4',			'RLE-4',							'only Windows Metafile CMYK']
			}
			print( 'compression method: ' + str(valueCompressionMethod[compressionMethod][0]) + '/' + str(valueCompressionMethod[compressionMethod][1]) )
			
			file.seek(0x22)
			imageSize = file.read(4)
			#print( imageSize[3], hex(imageSize[3]) )
			#print( imageSize[2], hex(imageSize[2]) )
			#print( imageSize[1], hex(imageSize[1]) )
			#print( imageSize[0], hex(imageSize[0]) )
			a = (16**6) * imageSize[3]
			b = (16**4) * imageSize[2]
			c = (16**2) * imageSize[1]
			d = (16**0) * imageSize[0]
			imageSize = a + b + c + d
			print( 'image size (size in bytes, of the raw bitmap data): ' + str(imageSize) )
			
			file.seek(0x26)
			horizontalResolution = file.read(4)
			#print( horizontalResolution[3], hex(horizontalResolution[3]) )
			#print( horizontalResolution[2], hex(horizontalResolution[2]) )
			#print( horizontalResolution[1], hex(horizontalResolution[1])) )
			#print( horizontalResolution[0], hex(horizontalResolution[0]) )
			a = (16**6) * horizontalResolution[3]
			b = (16**4) * horizontalResolution[2]
			c = (16**2) * horizontalResolution[1]
			d = (16**0) * horizontalResolution[0]
			horizontalResolution = a + b + c + d
			print( 'horizontal resolution (pixel per metre, signed integer): ' + str(horizontalResolution) )
			
			file.seek(0x2A)
			verticalResolution = file.read(4)
			#print( verticalResolution[3], hex(verticalResolution[3]) )
			#print( verticalResolution[2], hex(verticalResolution[2]) )
			#print( verticalResolution[1], hex(verticalResolution[1]) )
			#print( verticalResolution[0], hex(verticalResolution[0]) )
			a = (16**6) * verticalResolution[3]
			b = (16**4) * verticalResolution[2]
			c = (16**2) * verticalResolution[1]
			d = (16**0) * verticalResolution[0]
			verticalResolution = a + b + c + d
			print( 'vertical resolution (pixel per metre, signed integer): ' + str(verticalResolution) )
			
			file.seek(0x2E)
			numberColorsPalette = file.read(4)
			#print( numberColorsPalette[3], hex(numberColorsPalette[3]) )
			#print( numberColorsPalette[2], hex(numberColorsPalette[2]) )
			#print( numberColorsPalette[1], hex(numberColorsPalette[1]) )
			#print( numberColorsPalette[0], hex(numberColorsPalette[0]) )
			a = (16**6) * numberColorsPalette[3]
			b = (16**4) * numberColorsPalette[2]
			c = (16**2) * numberColorsPalette[1]
			d = (16**0) * numberColorsPalette[0]
			numberColorsPalette = a + b + c + d
			print( 'number of colors in the color palette, or 0 to default to 2**n: ' + str(numberColorsPalette) )
			
			file.seek(0x32)
			numberImportantColors = file.read(4)
			#print( numberImportantColors[3], hex(numberImportantColors[3]) )
			#print( numberImportantColors[2], hex(numberImportantColors[2]) )
			#print( numberImportantColors[1], hex(numberImportantColors[1]) )
			#print( numberImportantColors[0], hex(numberImportantColors[0]) )
			a = (16**6) * numberImportantColors[3]
			b = (16**4) * numberImportantColors[2]
			c = (16**2) * numberImportantColors[1]
			d = (16**0) * numberImportantColors[0]
			numberImportantColors = a + b + c + d
			print( 'number of important colors used, or 0 when every color is important; generally ignored: ' + str(numberImportantColors) )
			
			rowSize = (imageSize // bitmapHeight) // (numberBitsPerPixel // 8)
			#print( imageSize )
			#print( bitmapHeight )
			#print( bitmapWidth )
			#print( numberBitsPerPixel )
			#print( rowSize )
			file.seek(offsetPixelArray) # init in offset pixel array
			self.width = bitmapWidth
			self.height = bitmapHeight
			self.bitsPerPixel = numberBitsPerPixel
			self.content = []
			#fileHTML = open( self.getFilename() + '.html', 'w' )
			#fileHTML.write( '<table align="center" border="0" cellspacing="0" cellpadding="0">\n' )
			for i in range(bitmapHeight):
				#fileHTML.write( '\t<tr>\n' )
				row = []
				for i in range(rowSize):
					rgb = file.read(3)
					r = rgb[2]
					g = rgb[1]
					b = rgb[0]
					row.append( [r,g,b] )
					#fileHTML.write( '\t\t<td style="width:1px;height:1px;background:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');"></td>\n' )
				#fileHTML.write( '\t</tr>\n' )
				########################################################################################################################
				############################## IMPORTANT ###############################################################################
				########################################################################################################################
				file.read(2) # note the value: 294 = 73 * 4 + 2 => 296 = 74 * 4
				########################################################################################################################
				########################################################################################################################
				self.content.append( row )
			#fileHTML.write( '</table>' )
			#fileHTML.close()
			file.close()
			return True
		else:
			return False
	
	def getFilename(self):
		return self.filename
	
	def setContent(self, content):
		self.content = content
	
	def getContent(self):
		return self.content
	
	def toString(self):
		return self.content # falta converter para binario
	
	def toHTML(self):
		html_open = '<html>\n'
		html_close = '</html>'
		head_open = '\t<head>\n'
		head_close = '\t</head>\n'
		style_open = '\t\t<style>\n'
		style_close = '\t\t</style>\n'
		body_open = '\t<body>\n'
		body_close = '\t</body>\n'
		table_open = '\t\t<table align="center" border="0" cellspacing="0" cellpadding="0">\n'
		table_close = '\t\t</table>\n'
		tr_open = '\t\t\t<tr>'
		tr_close = '</tr>\n'
		
		fileHTML = open( self.getFilename() + '.html', 'w' )
		
		fileHTML.write( html_open )
		fileHTML.write( head_open )
		fileHTML.write( style_open + '\t\t\ttd{\n\t\t\t\twidth:1px;\n\t\t\t\theight:1px;\n\t\t\t}\n' + style_close )
		fileHTML.write( head_close )
		fileHTML.write( body_open )
		fileHTML.write( table_open )
		for i in range(len(self.content)):
			fileHTML.write( tr_open )
			for j in range(len(self.content[i])):
				r = self.content[i][j][0]
				g = self.content[i][j][1]
				b = self.content[i][j][2]
				fileHTML.write( '<td style="background:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');"></td>' )
			fileHTML.write( tr_close )
		fileHTML.write( table_close )
		fileHTML.write( body_close )
		fileHTML.write( html_close )
		fileHTML.close()
		
if __name__ == "__main__":
	#######################################################################################
	# https://lemire.me/blog/2017/11/10/should-computer-scientists-keep-the-lena-picture/ #
	# https://i.stack.imgur.com/o1z7p.jpg                                                 #
	#                                                                                     #
	# o1z7p_24 bits.bmp                                                                   #
	# width          = 1960                                                               #
	# height         = 1960                                                               #
	# bits per pixel = 24                                                                 #
	# size           = 11.524.854 bytes                                                   #
	# size in disk   = 11.526.144 bytes                                                   #
	#######################################################################################
	image = Image()
	image.setFilename( 'o1z7p_24_bits_resize_294pixels.bmp' )
	
	print( image.getWidth() )
	print( image.getFilename() )
	image.toHTML()