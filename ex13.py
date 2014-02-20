# coding:utf-8
from sys import argv #把 sys 模组 import 进来

script, first, second, third = argv  #把 argv 中的东西解包，将所有的参数依次赋予左边的变量名

print "The script is called: ", script
print "Your first variable is：", first
print "your sencond variable is: ", second
print "your third variable is: ", third

# testing
test1 = raw_input("what are you doing?")
print "I am %s." % test1