# coding:utf-8
from sys import argv

script, user_name = argv
prompt = '>'  #我们将用户提示符设置为变量 prompt，这样我们就不需要在每次用到 raw_input 时重复输入提示用户的字符了。而且如果你要将提示符修改成别的字串，你只要改一个位置就可以了。

print "Hi %s, i am the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
like = raw_input('<')

print "Where do you like live %s?" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
you live in %r. Not sure where it is.
And you have a %r computer. Nice
""" % (like, lives, computer)