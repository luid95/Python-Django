# try:
#     f = open('simple.txt', 'r')
#     r.write("Test write to simple text!")
# except IOError:
#     print("ERROR: Could not find file or read data!")
# else:
#     print("SECCESS!")
#     f.close()
#
# print("Hello World!")
try:
    f = open('simple.txt', 'r')
    f.write("Test write to simple text!")
except:
    print("ERROR: Could not find file or read data!")
finally:
    print("I always work no matter what!")
