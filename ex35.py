# coding: utf-8
from sys import exit

def gold_room():
    print "THis room is full of gold. How much do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("you greedy bastard!")        
    
def bear_room():
    print "THere is a bear room here."
    print "The bear has a bunch of honey."
    print "THe fat bear is in front of another door."
    print "HOw are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("THe bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "THe bear has moved from the door. you can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("THe bear gets possed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "feel" in next:
        start()
    elif "head" in next:
        dead("well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "YOu are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("you stumble around the room until you starve.")

start()

