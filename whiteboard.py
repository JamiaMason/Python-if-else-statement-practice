# Write a function that takes a single string as argument. The function must return an ordered list containing the
#  indexes of all capital letters in the string.
# ex: "caN yOu FInD me"
# output: [2,5,8,9,11]



def capitals(sentence):
    capitallist=[]
    for i in range(len(sentence)):
        print(sentence[i])
        if sentence[i] == sentence[i].capitalize() and sentence[i]!= " ":
            capitallist.append(i)
    return capitallist

print(capitals("caN yOu FInD me"))
