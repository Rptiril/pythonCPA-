# A spam comment is defined as a text containing the following keywords:
# "make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.

comment = input("Enter your comment : ")

# SpamComments = []
spam = False

if  "make a lot of money" in comment:
    spam = True
elif "buy now" in comment:
    spam = True
elif "subscribe this" in comment:
    spam = True
elif "click here" in comment:
    spam = True
elif "subscribe now" in comment:
    spam = True
else:
    print("Comment accepted.")

if(spam):
    print("A Spam Message.")