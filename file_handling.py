# f=open('student.txt',mode='r')
# print('file name;',f.name)
# print('file mode;',f.mode)
# print('file readable;',f.readable())
# print('file writable;',f.writable())
# print('file closed;',f.closed)
# f.close()
# print('file closed;',f.closed)



# f=open('student.txt',mode='w')
# n=f.write('hello')
# print(n)
# f.close()


# f=open('student.txt',mode='a')
# st=['ram\n','shyam\n','laxman\n']


# import os
# print(os.path.isfile('student12.txt'))

import os
if os.path.isfile('C:\\Users\\dell\\Desktop\\file handling\\fuloo.txt'):
    print('file exists')
else:
    