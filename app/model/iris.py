from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

def iris_knn(k):
    iris = load_iris()
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(iris['data'], iris['target'])
    return knn
