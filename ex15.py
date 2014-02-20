# coding: utf-8
from sys import argv  #sys 是一个代码库，这句话的意思是从库里取出 argv 这个功能来

script, filename = argv

txt = open(filename)   #通过open函数获取一个file object，然后调用read()，write()等方法对文件进行读写操作。

print "Here's your file %r:" % filename
print txt.read()
txt.close()    #使用open打开文件后一定要记得调用文件对象的close()方法

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)
print txt_again.read()
txt_again.close()