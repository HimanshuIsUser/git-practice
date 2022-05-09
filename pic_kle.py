import pickle
# file = ["car", "bike", "auto", "truck", "bus"]
# with open("file.pkl",'wb') as f:
#     t=pickle.dump(file,f)
# #
with open("file.pkl",'rb') as f:
    print(pickle.load(f))
