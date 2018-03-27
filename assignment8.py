from collections import OrderedDict
import re
# class RLEstr():
# 	def __init__():

inputstr = "AAAWWWBBBBB"	
outputstr = "13A4W5T"

def compress(inputstr):
	dict = OrderedDict.fromkeys(inputstr, 0)
	
	for ch in inputstr:
		dict[ch] +=1
		
	outputstr = ''
	for key,value in dict.iteritems():
		outputstr = outputstr + str(value) + key
	return outputstr

def iscompressed():
	if outpustr < inputstr:
		return True


def decompress(text):	
	list1 = re.findall('\d+|\D+', text)
	list2 = dict(zip(list1[::2], list1[1::2]))
	
	decodestr = ''

	
	for k,v in list2.items():
		x = (int(k) * str(v))
		decodestr = decodestr + x

	return decodestr

print(decompress(outputstr))

