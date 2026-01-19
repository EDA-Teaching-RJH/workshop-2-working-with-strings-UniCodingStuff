import math  

def main():
    A = int(input("A value:")) # DO NOT PICK 5 AND 6
    B = int(input("B value:"))
    pythag(A,B)

def pythag(A,B):
    x = math.pow(A,2) + math.pow(B,2) # please remember pythagoras, you fool
    y = math.sqrt(x)
    print(y)


main()
