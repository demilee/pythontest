# coding:utf-8
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line too, how?
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read()

print "This input file is %d bytes long" % len(indata)  #len() �������ֵ���ʽ���������ݵ��ַ����ĳ��ȡ�

print "Does the ouput file exist? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file,'w').write(indata)
print "Alright, all done."

#out_file.close()  ����ʱ���лᱨ����Ϊout_file = open(to_file,'w').write(indata)��read()һ�����У��ļ��ͻᱻ������β����close���� 
#indata.close() ����ʱ���лᱨ����Ϊindata = open(from_file).read()��read()һ�����У��ļ��ͻᱻ������β����close���� 
