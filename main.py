from sys import argv, exit
from compression import compress, decompress, usage

if len(argv) < 3:
	usage(argv[0])

if int(argv[1]) == 1:
	print "%r compressed is %r" % (argv[2], compress(argv[2]))
elif int(argv[1]) == 0:
	print "%r decompressed is %r" % (argv[2], decompress(argv[2]))
else:
	usage(argv[0])