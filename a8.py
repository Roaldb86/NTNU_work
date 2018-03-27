from collections import OrderedDict
import re

class RLEString():
	
	def __init__(self, __mystring):
			# Raise Exception if input string is not string or empty
			if re.match(r"^[A-Za-z]*$", __mystring) and __mystring != '':
					self.__mystring = __mystring
					self.__iscompressed = False         
			else:
					raise Exception("Not string")
					
	def iscompressed(self):
		"""Takes a string and evaluates if the string has been compressed with Run-length encoding, returns True or False"""
		return self.__iscompressed

	def compress(self):
		"""Takes a string as input and returns a run-length-encoded string"""
		# Raise Exception if the string is allready compressed
		if self.__iscompressed == False:
			count = 1
			prev = ''
			lst = []
			
			# Count Occurences of character and append to lst
			for character in self.__mystring:
					if character != prev:
							if prev:
									entry = (prev,count)
									lst.append(entry)
								
							count = 1
							prev = character
					else:
							count += 1
			else:
					try:
							# Add str of character and number of occurences to __mystring
							self.__mystring = ''
							entry = (character,count)
							lst.append(entry)
							for k,v in lst:
								self.__mystring  = self.__mystring  + str(v) + k
							# Set variabel __iscompressed to True after compression
							self.__iscompressed = True
					except Exception as e:
							print("Exception encountered {e}".format(e=e)) 
							return (e, 1)

					
				
		else:
				raise Exception("allready compressed")
		

	def decompress(self):
			"""Takes an encoded string as input and returns a decoded string"""
			# Raise exception if the string is not compressed
			if self.__iscompressed == True:
				# Regular expression to seperate numbers and letters into a list from the string
				list1 = re.findall('\d+|\D+', self.__mystring)
				# concatonate the list with it self
				list2 = zip(list1[::2], list1[1::2])
				self.__mystring = ''
				# Multiply each letter(value) the number of key times and add to __mystring
				for k,v in list2:
						x = (int(k) * str(v))
						self.__mystring = self.__mystring + x
				self.__iscompressed = False
# 				
			else:
				raise Exception("Not compressed")

	def __repr__(self):
		return str(self.__mystring)
	def __str__(self):
		return str(self.__mystring)


if __name__ == '__main__':
	
	org = ("TTTTTsssst")
	rle = RLEString(org)
	
	x = rle.compress()
	
	print("Compressed: %s"%(rle))
	
	y = x.decompress()
		
		




