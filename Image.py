##########################################
#  Developed by Everton Pereira da Cruz  #
##########################################

# https://en.wikipedia.org/wiki/BMP_file_format
import os.path
import math

class Image:
	def __init__(self):
		self.filename = ''
		self.width = 0
		self.height = 0
		self.bitsPerPixel = 0
		self.content = []
	
	def setFilename(self, filename):
		self.filename = filename
	
	def setWidth(self, width):
		self.width = width
	
	def setHeight(self, height):
		self.height = height
	
	def setContent(self, content):
		self.content = content
	
	def getWidth(self):
		return self.width
	
	def getHeight(self):
		return self.height
	
	def getFilename(self):
		return self.filename
	
	def getContent(self):
		return self.content
	
	def loadContent(self):
		if not os.path.isfile( self.getFilename() ):
			return False
		else:
			file = open( self.getFilename(), 'rb' )
			if file.read(2) != b'BM':
				return False
			else:
				file.seek(0x02)
				tmp = file.read(4)
				size = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
				
				file.seek(0x0A)
				tmp = file.read(4)
				offsetPixelArray = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x0E)
				tmp = file.read(4)
				sizeHeader = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x12)
				tmp = file.read(4)
				bitmapWidth = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x16)
				tmp = file.read(4)
				bitmapHeight = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x1A)
				tmp = file.read(2)
				numberColorPlanes = (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x1C)
				tmp = file.read(2)
				numberBitsPerPixel = (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x1E)
				tmp = file.read(4)
				compressionMethod = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
				if compressionMethod != 0:
					return False
				
				file.seek(0x22)
				tmp = file.read(4)
				imageSize = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x26)
				tmp = file.read(4)
				horizontalResolution = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x2A)
				tmp = file.read(4)
				verticalResolution = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x2E)
				tmp = file.read(4)
				numberColorsPalette = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
				if numberColorsPalette != 0:
					return False
				
				file.seek(0x32)
				tmp = file.read(4)
				numberImportantColors = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(offsetPixelArray) # init in offset pixel array
				self.width = bitmapWidth
				self.height = bitmapHeight
				self.bitsPerPixel = numberBitsPerPixel
				self.content = []
				fill = int( math.ceil(numberBitsPerPixel * bitmapWidth / 32.0) * 4 ) - (numberBitsPerPixel//8) * bitmapWidth
				for i in range(bitmapHeight):
					row = []
					for i in range(bitmapWidth):
						rgb = file.read(3)
						r = rgb[2]
						g = rgb[1]
						b = rgb[0]
						row.append( [r,g,b] )
					file.read(fill)
					self.content.append( row )
				file.close()
				return True
	
	def toBase64(self):
		# https://en.wikipedia.org/wiki/Base64
		#base64 = {	 0:'A', 16:'Q', 32:'g', 48:'w',
		#			 1:'B', 17:'R', 33:'h', 49:'x',
		#			 2:'C', 18:'S', 34:'i', 50:'y',
		#			 3:'D', 19:'T', 35:'j', 51:'z',
		#			 4:'E', 20:'U', 36:'k', 52:'0',
		#			 5:'F', 21:'V', 37:'l', 53:'1',
		#			 6:'G', 22:'W', 38:'m', 54:'2',
		#			 7:'H', 23:'X', 39:'n', 55:'3',
		#			 8:'I', 24:'Y', 40:'o', 56:'4',
		#			 9:'J', 25:'Z', 41:'p', 57:'5',
		#			10:'K', 26:'a', 42:'q', 58:'6',
		#			11:'L', 27:'b', 43:'r', 59:'7',
		#			12:'M', 28:'c', 44:'s', 60:'8',
		#			13:'N', 29:'d', 45:'t', 61:'9',
		#			14:'O', 30:'e', 46:'u', 62:'+',
		#			15:'P', 31:'f', 47:'v', 63:'/' }
		base64 = [	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
					'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
					'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
					'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/' ]
		#print( base64 )
		file = open( self.getFilename(), 'rb' )
		contentASCII = file.read()
		contentBase64 = ''
		lengthBase64 = len(contentASCII) - (len(contentASCII)%3)
		i = 0
		while i < lengthBase64:
			b1 = ( contentASCII[i] >> 2) & 0x3F
			contentBase64 = contentBase64 + base64[b1]
			b2 = ((contentASCII[i] & 0x03) << 4) | ((contentASCII[i+1] >> 4) & 0x0F)
			contentBase64 = contentBase64 + base64[b2]
			b3 = ((contentASCII[i+1] & 0x0F) << 2) | ((contentASCII[i+2] >> 6) & 0x03)
			contentBase64 = contentBase64 + base64[b3]
			b4 = contentASCII[i+2] & 0x3F
			contentBase64 = contentBase64 + base64[b4]
			i = i + 3
		lengthBase64 = len(contentASCII) % 3
		if lengthBase64 == 1:
			b1 = ( contentASCII[i] >> 2) & 0x3F
			contentBase64 = contentBase64 + base64[b1]
			b2 = ((contentASCII[i] & 0x03) << 4) | ((contentASCII[i+1] >> 4) & 0x0F)
			contentBase64 = contentBase64 + base64[b2]
			b3 = ((contentASCII[i+1] & 0x0F) << 2) | 0x00
			contentBase64 = contentBase64 + base64[b3]
			contentBase64 = contentBase64 + '='
		elif lengthBase64 == 2:
			b1 = ( contentASCII[i] >> 2) & 0x3F
			contentBase64 = contentBase64 + base64[b1]
			b2 = ((contentASCII[i] & 0x03) << 4) | ((contentASCII[i+1] >> 4) & 0x0F)
			contentBase64 = contentBase64 + base64[b2]
			contentBase64 = contentBase64 + '=='
		
		fileHTML = open( self.getFilename() + '.img.html', 'w' )
		fileHTML.write( '<img src="data:image/bmp;base64,' + contentBase64 + '" /></body>' )
		fileHTML.close()
	
	def toHTML(self, typeFilter='original', value=128):
		# https://en.wikipedia.org/wiki/HTML
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
		for i in range(len(self.content)-1, -1, -1):
			fileHTML.write( tr_open )
			for j in range(len(self.content[i])):
				r = g = b = 0
				if typeFilter == 'original':
					# origal
					r = self.content[i][j][0]
					g = self.content[i][j][1]
					b = self.content[i][j][2]
				elif typeFilter == 'onlyRed':
					# delete two layer: green and blue
					r = self.content[i][j][0]
					g = 0x00
					b = 0x00
				elif typeFilter == 'onlyGreen':
					# delete two layer: red and blue
					r = 0x00
					g = self.content[i][j][1]
					b = 0x00
				elif typeFilter == 'onlyBlue':
					# delete two layer: red and green
					r = 0x00
					g = 0x00
					b = self.content[i][j][2]
				elif typeFilter == 'negative':
					# negative
					r = (~ self.content[i][j][0]) & 0xFF
					g = (~ self.content[i][j][1]) & 0xFF
					b = (~ self.content[i][j][2]) & 0xFF
				elif typeFilter == 'grayscale':
					# https://en.wikipedia.org/wiki/Grayscale
					r = self.content[i][j][0]
					g = self.content[i][j][1]
					b = self.content[i][j][2]
					r = g = b = int( 0.299 * r + 0.587 * g + 0.114 * b )
				elif typeFilter == 'thresold':
					# thresold
					r = self.content[i][j][0]
					g = self.content[i][j][1]
					b = self.content[i][j][2]
					r = 255 if r >= value else 0
					g = 255 if g >= value else 0
					b = 255 if b >= value else 0
				fileHTML.write( '<td style="background:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');"></td>' )
			fileHTML.write( tr_close )
		fileHTML.write( table_close )
		fileHTML.write( body_close )
		fileHTML.write( html_close )
		fileHTML.close()