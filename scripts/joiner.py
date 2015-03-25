import os
import codecs

print('Lets start..!')

targetFilename = '_all.json'						# condense into this file
target = codecs.open(targetFilename, 'w', 'utf-8')			# as utf-6
target.write('{\n')							# start main object

firstLine = True
for dirname, dirnames, filenames in os.walk('.'):			# traverse current dir
	for filename in filenames:					# foreach file
		name, ext = os.path.splitext(filename)			# get extension
		if(ext == '.json' and filename != targetFilename):	# only for json files
			print('Processing ' + filename)
			
			if(firstLine == True):
				firstLine = False
			else:
				target.write(',\n')			# trick to write commas not in last line
			
			target.write('"' + filename + '":[')		# start an array for this file; filename is key
			with codecs.open(filename, 'r', 'utf-8') as currentFile:
    				target.write(currentFile.read())
			target.write(']')

target.write('\n}')							# end main object

print('Thanks!')
