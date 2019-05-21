import argparse

def fileData(fileName,stringListReplace):
	
	with open(fileName,'w') as f:
		f.write(str(stringListReplace))
	print stringListReplace

def replaceString(replace,stringList,fileName,word):

	rep = replace.upper()
	stringListReplace = ' '
  	for w in stringList:
  		stringListReplace = w.replace(word, rep)
  	fileData(fileName,stringListReplace)

def findString(word, stringList):
	
	for s in stringList:
		if word in s:
			print ('{} is found\n'.format(word.upper()))
			#print stringList
		else:
			print 'String is not found\n'
			exit()		
	
def fileOpen(fileName):  

	with open(fileName,'r') as f:
		stringList = f.read().split(',')
	return stringList

def argParser(): 

	parser = argparse.ArgumentParser(description = 'String Operation')
	parser.add_argument('filename', help = 'name of the file')
	parser.add_argument('s',help = 'word for searching strings in the file')	
	parser.add_argument('-r', help = 'word for replacing strings in the file')
	args = parser.parse_args()
	return args

def main():

	args = argParser()
	fileName = args.filename	
	word = args.s
	replace = args.r
	if args.s is not None:
		stringList = fileOpen(fileName) 
  		findString(word, stringList)
  	else:
		exit()
		#print args.word
	
  	if replace is None:
  		print stringList
  		exit()
  	
  	else:
  		replaceString(replace,stringList,fileName,word)
  		
if __name__ == '__main__':
	main()
