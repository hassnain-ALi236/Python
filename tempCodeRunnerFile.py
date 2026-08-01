for i in range(1,51,1):
    if(i%2 ==0 or i**0.5 % i ==0 ):
        print("this is a prime number")
        i+=1
    print(i)