import re

def usage(s): 
	
	print "=~"*10
	print "Usage:\n"
	print "To Compress:"
	print "python %s 1 <string to compress>\n" % s
	print "To decompress:"
	print "python %s 0 <string to decompress>\n" % s
	print "=~"*10
	exit(1)	

# compress the string s using the algorithm documented in test_compression.txt
def compress(s):

	if not re.match(r'^[A-Z]*$', s):
		raise ValueError("Input string must be all upper case letters")

	char_count = 0
	compressed = []
	i = 0
	s_len = len(s)

	while i < s_len:
		char = s[i]
		char_count = 0
		while i < s_len and s[i] == char:
			char_count += 1
			if char_count - 2 == 9:
				chars = [char*2]
				chars.append('9')
				compressed.append(''.join(chars))
				char_count = 0
			i += 1

		if char_count >= 2:
			chars = [char*2]
			chars.append(str(char_count - 2))
			compressed.append(''.join(chars))
		else:
			compressed.append(char)

	return ''.join(compressed) 

# Return the uncompressed version of s
def decompress(s):

	if not re.match(r'^(?:([A-Z])\1{1}\d{1}|[A-Z])*$', s):
		raise ValueError("Invalid compression")

	char_count = 0
	decompressed = []
	i = 0
	s_len = len(s)

	while i < s_len:
		char = s[i]
		try:
			if (i + 2) < s_len and s[i] == s[i + 1]:
				for j in range(0, int(s[i + 2]) + 2):
					decompressed.append(char)
				i += 3
			else:
				decompressed.append(char)
				i += 1
		except ValueError:
			print "Invalid Compression"
			exit(1)

	return ''.join(decompressed) 

