import os
print("\t\t****WELCOME****\nHello Sir")
pat_h = input("Please Enter The Path Of Your Folder :- ")
fol_der = input("Enter The Name Of Your Folder :- ")
form_t = input("Enter Which Type Of Files You Want To Give Number :- ")
os.chdir(pat_h)
files = os.listdir(fol_der)
with open(fol_der) as f:
    file_with = f.read().split("\n")
for file in fol_der:
    if file not in file_with:
        os.rename(fol_der,fol_der.capitalize())
# def funct(path,file):
#     os.chdir(path)
#     i=1
#     files = os.listdir(file)
#     with open(file) as f:
#         filelist = f.read().split("\n")
#     for file in files:
#         if file not in filelist:
#             os.rename(file,file.capitalize())
#
#
# funct("C:\Users\acer\PycharmProjects"
#       "C:\Users\acer\PycharmProjects\firstfrog\hello.text")
