# coding: utf-8
from sys import argv  #sys ��һ������⣬��仰����˼�Ǵӿ���ȡ�� argv ���������

script, filename = argv

txt = open(filename)   #ͨ��open������ȡһ��file object��Ȼ�����read()��write()�ȷ������ļ����ж�д������

print "Here's your file %r:" % filename
print txt.read()
txt.close()    #ʹ��open���ļ���һ��Ҫ�ǵõ����ļ������close()����

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)
print txt_again.read()
txt_again.close()