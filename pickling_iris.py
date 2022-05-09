import pickle

import requests
t = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
spl_it = t.split("\n")
spl_it2  = [item.split(",") for item in spl_it if len(item)!=0]
iris_pkl = "iris.pkl"
with open(iris_pkl,'wb') as i:
    m = pickle.dump(spl_it2,i)
with open(iris_pkl,'rb') as i:
    print(pickle.load(i))
