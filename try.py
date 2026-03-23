import pickle

data=[1,2,3,4,5]

loaded=pickle.dumps(data)
print(loaded)
print(pickle.loads(loaded))
#loaded=pickle.load(open('data.pkl','rb'))

# loaded=pickle.load(data,open('data.pkl','rb'))
# print(loaded)
