# coding:utf-8
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line too, how?
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read()

print "This input file is %d bytes long" % len(indata)  #len() 会以数字的形式返回所传递的字符串的长度。

print "Does the ouput file exist? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file,'w').write(indata)
print "Alright, all done."

#out_file.close()  运行时此行会报错，因为out_file = open(to_file,'w').write(indata)中read()一旦运行，文件就会被读到结尾并被close掉。 
#indata.close() 运行时此行会报错，因为indata = open(from_file).read()中read()一旦运行，文件就会被读到结尾并被close掉。 
