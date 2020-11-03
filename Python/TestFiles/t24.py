from sklearn.neighbors import *
x = [[0],[1],[2],[3]]
y = [0,0,1,1]
#n_neighbors设置为3，使用最近的3个邻居作为分类
neigh = KNeighborsClassifier(n_neighbors=3,weights='uniform',algorithm='auto')
#将训练数据x和标签y送入分类器进行学习
neigh.fit(x,y)
#输入测试点[1.1],[2.1]
text = [[1.1],[2.1]]
data = neigh.predict(text)
print(data)
#print(neigh.score(x,y))
