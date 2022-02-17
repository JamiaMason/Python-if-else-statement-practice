#code  number test- Print out all cubed numbers up to the total value 1000, if the cubed
#number is over 1000, break the loop

for i in range (1,1001):
    print (i, i*i*i)




#Get prime numbers up to 100

for num in range(2,101):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print (num)


#Take in a users input for their age. If younger than 18 print kids, if 18 to 65 print 
#adults. Else seniors

#I took the steps I felt were necessary, but could not figure out the error.

age = int(input ('Please enter your age:'))

if age <= 18:
    print('kids')

if age >=18 and age <=65:
    print ('adult')

else:
    print ('Senior')