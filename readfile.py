def readFile(filepath):
	""" Reads a file line by line and returns a list """

	# Open the file in read mode
	with open(filepath, 'r') as file:
		lines = file.readlines()  # Read all lines into a list

	# Strip newline characters and create a list of elements
	elements_list = [line.strip() for line in lines]

	return elements_list