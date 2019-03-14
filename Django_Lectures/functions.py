def my_func(param1="default"):
    print("My first python function! {a}".format(a=param1))

def hello():
    return "Hello"

def addNum(num1, num2):
    return num1+num2

my_func()
my_func("thanks")
r = hello()
print(r)

r2 =addNum(2,3)
print(r2)
print(type(r2))

##################################33
#Lambda Expression

#filter
mylist =[1,2,3,4,5,6,7,8,9]
def even_bool(num):
    return num%2 ==0

evens = filter(even_bool, mylist)
print(list(evens))

###############################
tweet = "Go sports! #Sports"
r = tweet.split("#")
print(r)
################################
print('x' in [1,2,3])
print('x' in [1,2,3,'x'])
