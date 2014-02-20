# coding: utf-8
from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C(^c)."
print "If you do what that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'a+')

print "Truncating the file. Goodbay!"
#target.truncate()

print "Now i'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

#读写模式:r只读,r+读写,w新建(会覆盖原有文件),a追加,b二进制文件
