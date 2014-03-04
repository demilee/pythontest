#coding:utf-8
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "THere's  %d items now." % len(stuff)

print "There we go: ", stuff  # There we go:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]  # print the last one parameters in the list
print stuff.pop() # pop(n), n指明在列表中的位置， 如果pop() 则默认弹出最后一个元素
print stuff
print ' '.join(stuff)
print '#'.join(stuff[3:6])

#testing
"""
class Song(object):

    def __init__(self, lyrice):
        self.lyrice = lyrice

    def sing_me_a_song(self):
        for line in self.lyrice:
            print line

happy_bday = Song(["Happy birthady to you",
                 "I don't want to get sued",
                 "So i'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                    "with pockers full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()           
"""                                             