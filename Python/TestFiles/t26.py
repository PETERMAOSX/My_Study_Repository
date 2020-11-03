from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split    
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
def knn_iris():
    iris = load_iris()
    #划分数据集
    x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,random_state=30)
    #标准化->数据预处理
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    #测试集做标准化

    #Knn
    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train,y_train)
    #模型评估
    y_predict = estimator.predict(x_test)
    print("y_predict:\n",y_predict)
    print("直接比对真实值和预测值:\n",y_test == y_predict)
    score= estimator.score(x_test,y_test)
    print("准确率是:\n",score)
    ##计算准确值
    return None

def knn_iris_gscv():
    iris = load_iris()
    x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,random_state=30)
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    
    estimator = KNeighborsClassifier()
    param_dict = {'n_neighbors':[1,3,5,7,9,11,13]}
    estimator = GridSearchCV(estimator=estimator,param_grid=param_dict,cv=10)

    estimator.fit(x_train,y_train)
    
    print("查看最佳参数:\n",estimator.best_params_)
    print("查看最佳结果:\n",estimator.best_score_)
    print("最佳估计器:\n",estimator.best_estimator_)
    print("交叉验证结果:\n",estimator.cv_results_)

    return None


if __name__ == "__main__":
    # knn_iris()
    knn_iris_gscv()