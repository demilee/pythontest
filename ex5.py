# coding: utf-8
# ����ı����ʹ�ӡ
# ��ʽ���ַ�����format string��
# �ַ������԰�����ʽ���ַ� %s�������֮ǰҲ�����ġ���ֻҪ����ʽ���ı����ŵ��ַ����У��ٽ�����
# һ���ٷֺ� % (percent)���ٽ����ű��������ɡ�ΨһҪע��ĵط������������Ҫ���ַ�����ͨ����ʽ
# ���ַ�������������ʱ������Ҫ�������ŵ� ( ) Բ����(parenthesis)�У����ұ���֮���� , ����(comma)��������

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74  #inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line in tricky, try to get it exactly right
print "If i add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

pi = 3.1415
print "%s" % pi  # the result is 3.1415  %s	�ַ���
print "%f" % pi  # the result is 3.141500  %f	��������(��С�������)
print "%10.2f" % pi #��ʾ �ܹ��������Ϊ10���ַ�������С��λ2λ
print "%010.2f" % pi  # ���Ϊ0000003.14�� ��ʾ �ܹ��������Ϊ10���ַ�������С��λ2λ������10λ�Ļ�����0����10λ
print "%d" % pi  # ���Ϊ3�� %d Ϊ������
print "%e" % pi
# found()��������С����������
print round(pi)  # the result is 3.0
