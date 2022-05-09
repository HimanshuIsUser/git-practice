import os
print(dir(os)) # it used for checking which funtions can apply on os module
print(os.getcwd())  # It help us to know in which directry we are working
# os.chdir("c://")        #to change current working directry
print(os.getcwd())
print(os.listdir("c://"))   # to check the files in current folder or given path
#os.makedev("this")         # to make directry of given name
# os.makedirs("this/that")        # to make directry and sub directry of given name
#  os.rename("args and kwargs.py","jo marzi naam daal do") # to change the files names
# print(os.environ.get('path'))
# print(os.path.join("c://","/harry.text"))       # help to perfectly connect the path
print(os.path.exists("c:"))     # to know given path has pressence or not
print(os.path.isfile("harry.text")) # to know this given name  is file or not
print(os.path.isdir("physical programme.text")) #to know given name file is directry or not
