x=int(input())
if (x%2==0 and x>1 and x<100000):
    print"Even"
elif(x%2!=0 and x>1 and x<10000):
    print"Odd"
else:
    print"invalid"
