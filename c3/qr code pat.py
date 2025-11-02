##import qrcode
##name = input("enter your name : ")
##roll_no = input("enter your roll no : ")
##branch = input("enter your branch : ")
##cgpa = input("enter your cgpa : ")
##
##
##data = f"Name: {name}, Roll No: {roll_no}, Branch: {branch}, CGPA: {cgpa}"
##
### Create a QRCode object
##qr = qrcode.QRCode(
##    version=1,
##    error_correction=qrcode.constants.ERROR_CORRECT_L,
##    box_size=10,
##    border=4,
##)
##
### Add data to the QRCode
##qr.add_data(data)
##qr.make(fit=True)
##
### Create an image from the QRCode instance
##img = qr.make_image(fill_color="black", back_color="white")
##
### Display the image  
##img.save("qrcode.png")



##import heapq
##def max_sum(digits):
##    n1=0
##    n2=0
##    neg_digits=[-d for d in digits]
##    heapq.heapify(neg_digits)
##    while neg_digits:
##        if neg_digits:
##            d1=-1*heapq.heappop(neg_digits)
##            n1=n1*10+d1
##        if neg_digits:
##            d1=-1*heapq.heappop(neg_digits)
##            n2=n2*10+d1
##    print(f"fn1={n1} , n2={n2} sum={n1+n2}")
##digits=[4,3,7,1,0,9,6]
##max_sum(digits)


'''import heapq
from collections import defaultdict,counter
class Node:
    def __init__(self,char,freq):
        self.char=char
        self.freq=freq
        self.left=None
        self.right=None
    def __lt__(self,other):
        return self.freq<other.freq'''
    







