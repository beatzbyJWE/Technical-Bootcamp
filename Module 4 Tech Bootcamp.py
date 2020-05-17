# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:28:50 2020

@author: jeldr
"""
#Exercise 1: Print the Time

import datetime
print(datetime.datetime.now())

#Exercise 2: Make a Simple Stopwatch
def timerun():
    a=datetime.datetime.now()
    print(a-datetime.datetime.now())

timerun()

#Exercise 3: Print a Word Provided by the User

b=input("Type something here:")
print(b)

#Exercise 4: Validate User Input
#For this I installed the Enchant library using 'pip install pyenchant'
import enchant
#It looked like only one dictionary at a time was available at least easily. So I used the US dictionary.
d = enchant.Dict('en_US')
i=1

#I had to initialize i as 1 before the loop. So i=1 would be a global setting needed for this program. Did I need to define it that way?
def runit():
    global i
    while i==1:
        e=input("Type a word here:")
        print(e)
        while(d.check(e) is False):
            e=input("Please type an English word:")
            print(e)
#I had to use an extra if statement here to get the same result that I did in R using recursion. I don't know if that's because I'm doing something wrong here.            
        if(d.check(e) is False):
            runit()
        i+=1
   
#Exercise 5: Record and Print a List
    #The user is required to define the size of the list first

f=[]
n = int(input("Enter # of items in your list:"))
for i in range(0,n):
    print("Enter item into list")
    g = input()
    f.append(g)
    print(f)