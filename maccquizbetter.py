#!/usr/bin/python
#This is a backend system for MACC quiz system
#Version 0.1 (Alpha)
#Any GHS student may alter and redistrbute this program as long as this notice is perserved.
#To Do:  Add score system, Add questions, finish implmenting point system
import sys
import random

#This section is the opening prompts for the program
#REMEMBER TO ADD PASSPHRASE BEFORE PUBLISHING
print('''
Welcome to MACC Quiz. Created in 2017 by William Brannock
Any Galax High School student is free to alter and redistrbute this
program to other GHS students as long as this notice is
preserved.
''')



cat = input("What is your prefered subject? a) Science b) Social Studies c) Math d) English ")

#This area should be reserved for setting up a scoring system imp in progress
score = 0.0

#Science Section
if cat is "a":
    print("Excellent Choice.  Here come the questions ")
    class Question(object):
        global score
        def __init__(self, question, answer, options):
            self.question = question
            self.answer = answer
            self.options = options

        def ask(self):
            global score
            print(self.question + "?")
            for n, option in enumerate(self.options):
                print("%d) %s" % (n + 1, option))

            response = int(sys.stdin.readline().strip())   # answers are integers
            if response == self.answer:
                print("CORRECT")
                score = score+5
                print("Your score is now ",score,"")
            else:
                print("wrong")
                score = score-3
                print("Your score is now ",score,"")

    questions = [
        Question("How many legs on a horse", 4, ["one", "two", "three", "four", "five"]),
        Question("How many wheels on a bicycle", 2, ["one", "two", "three", "twenty-six"]),

        # more verbose formatting
        Question(question="What colour is a swan in Australia",
                 answer=1,
                 options=["black", "white", "pink"]),    # the last one can have a comma, too
        ]

    random.shuffle(questions)    # randomizes the order of the questions

    for question in questions:
        question.ask()

#English Section
if cat is "d":
    print("Wow, you must like books! Here come the questions.")
    class Question(object):
        score = 0
        def __init__(self, question, answer, options):
            self.question = question
            self.answer = answer
            self.options = options

        def ask(self):
            print(self.question + "?")
            for n, option in enumerate(self.options):
                print("%d) %s" % (n + 1, option))

            response = int(sys.stdin.readline().strip())   # answers are integers
            if response == self.answer:
                print("CORRECT")
            else:
                print("wrong")

    questions = [
        Question("How many legs on a dog", 4, ["one", "two", "three", "four", "five"]),
        Question("How many wheels on a motorcycle", 2, ["one", "two", "three", "twenty-six"]),

        # more verbose formatting
        Question(question="What colour is a swan in Australia",
                 answer=1,
                 options=["black", "white", "pink"]),    # the last one can have a comma, too
        ]

    random.shuffle(questions)    # randomizes the order of the questions

    for question in questions:
        question.ask()
