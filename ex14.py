# coding:utf-8
from sys import argv

script, user_name = argv
prompt = '>'  #���ǽ��û���ʾ������Ϊ���� prompt���������ǾͲ���Ҫ��ÿ���õ� raw_input ʱ�ظ�������ʾ�û����ַ��ˡ����������Ҫ����ʾ���޸ĳɱ���ִ�����ֻҪ��һ��λ�þͿ����ˡ�

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