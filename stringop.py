import argparse

def fileOpen(fileName):  

	with open(fileName,'r') as f:
		stringList = f.read().split()
	return stringList

def findString(word, stringList):

	if any(word in s for s in stringList):
		print 'String is found\n'
		print stringList
	else:
		print 'String is not found\n'
	
def argParser(): 

	parser = argparse.ArgumentParser(description = 'String Operation')
	parser.add_argument('filename', help = 'name of the file')
	parser.add_argument('word', help = 'word for searching strings in the file')	
	parser.add_argument('-r', default='', help = 'word for replacing strings in the file')
	args = parser.parse_args()
	return args

def main():

	args = argParser()
	fileName = args.filename	
	word = args.word
	#print args.word
	stringList = fileOpen(fileName) 
  	findString(word, stringList)
  	replace = args.r
  	stringListReplace = [w.replace(word, replace) for w in stringList]
	#print stringListReplace
	with open(fileName,'w') as f:
		f.write(str(stringListReplace))
	print stringListReplace

if __name__ == '__main__':
	main()
