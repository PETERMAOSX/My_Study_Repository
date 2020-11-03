from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import jieba
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
def datasets_demo():
    iris = load_iris()
    # print("鸢尾花数据集: \n",iris)
    # #print(type(iris))
    # print("查看数据集描述: \n",iris["DESCR"])
    # print("查看特征值的名字: \n",iris.feature_names)

    #数据集划分
    x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.2,random_state=22)
    print("训练集的特征值: \n",x_train,x_train.shape)
    print("测试集的特征值: \n",x_test,x_test.shape)
    print("训练集的目标值: \n",y_train,y_train.shape)
    print("测试集的目标值: \n",y_test,y_test.shape)
    print("==============================")
    #print(iris)

    return None

def dict_demo():
    #字典特征提取 类别->one hot 编码
    data = [{'city':'北京','temperature':100},{'city':'上海','temperature':60},{'city':'深圳','temperature':30}]
    #1. 实例化一个转换器类
    transfer = DictVectorizer(sparse=False)
    data_new = transfer.fit_transform(data)  #默认返回Sparse矩阵,稀疏矩阵：将非零值表示出来。使用稀疏矩阵可以节省内存
    print("data_new: \n",data_new)
    print("names: \n",transfer.get_feature_names())
    return None

def text_demo():
    #文本提取
    text = ["life life is short,i like python","life is too long ,i dislike python"]
    transfer = CountVectorizer()
    data_new = transfer.fit_transform(text)
    print("Data_new: \n",data_new.toarray())
    print("特征名字: \n",transfer.get_feature_names())
    #样本特征值出现的次数

def text_chinese_demo():
    #jieba分词处理
    
    text = ["实验室流传输(LSL)是一种协议，可以简化和同步收集多台计算机上的时间序列测量值。LSL功能旨在支持亚毫秒级定时精度的研究实验，并允许EmotivPRO与其他第三方软件和设备之间进行高效的双向通信。EmotivPRO的LSL功能允许用户跨多个设备同步数据流，并允许在第三方应用程序中实时处理EEG数据。LSL还可以在不同计算设备上发送不同的标记，并在设备之间同步标记。"]
    data_newpro = []
    for sent in text:
        data_newpro.append(cut_chinese_word(sent))
    transfer = TfidfVectorizer(stop_words=['一种']) #stop_words
    data_new = transfer.fit_transform(data_newpro)
    print("Data_new: \n",data_new.toarray())
    print("特征值: \n",transfer.get_feature_names())


def cut_chinese_word(text):
    return " ".join(list(jieba.cut(text)))
    
def stand_demo():
    #1.获取数据
    data = pd.read_csv("dataing.csv")
    data = data.iloc[:,:3]
    #2.实例化一个转换器类
    transfer = StandardScaler(feature_range=[2,3])
    #3.调用fit_transform
    data_new = transfer.fit_transform(data)
    print("Data_new: \n",data_new)
    return None


#dict_demo()
#text_demo()
text_chinese_demo()
#print(cut_chinese_word("我来自贵州铜仁，我叫毛少雄。"))