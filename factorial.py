n=int(input("ingrese n:\n"))
factorial=1
if (n<0):
    print("ten cuidado")
else:
    # print("yohohohohohohohohohohohohoho")
    if(n==0):
        factorial=1
    else:
        for i in range(1,n+1):
            factorial=factorial*i
        
print("factorial(%d):%g ",(n,factorial))