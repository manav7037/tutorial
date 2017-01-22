a=int(raw_input("Enter a number"))
arr = []
for i in xrange(1,a):
    b=a%i
    if b==0:
     arr.append(i)
print arr

     
