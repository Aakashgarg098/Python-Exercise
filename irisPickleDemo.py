import pickle, requests
r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
li = r.split("\n")
for i in li:
    if i!='':
# print(li)
        print(i.split(","))