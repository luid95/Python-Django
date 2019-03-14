#Functions excercises
#given a list of integers, return True if the sequence of numbers 1,2,3
#appears in the list somewhere

num = [5,6,1,2,3,4]

def arrayCheck(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True

    return False

r = arrayCheck(num)
print(r)

#######################################
#Problema 2
def stringBits(mystring):

    result = ""
    for i in range(len(mystring)):
        if i%2 == 0:
            result = result + mystring[i]

    return result

#####################################
#Problema 3 - si una lista esta dentro de otra

def end_other(a,b):
    a = a.lower()
    b = b.lower()

    return a[-(len(b))] == b or a == b[-(len(a))]

##############################################333333
def doubleChar(mystring):
    result = ""
    for char in mystring:
        result += char*2
    return result    
