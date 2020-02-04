""""Write a Program in Python to accept N numbers from user. Compute
and display maximum in list, minimum in list, sum and average of
numbers."""
till=int(input("n="))
if till<0:
    print("invalid entry")
else:
    l=[]
    for i in range(till):
        l.append(int(input()))
    output=0
    maxm=0
    minm=999999
    for i in range(till):
        if l[i]>maxm:
            maxm=l[i]
        if l[i]<minm:
            minm=l[i]
        output+=l[i]
    average=output/till
    print(output,"\n"+str(average),"\n"+str(maxm),"\n"+str(minm))
