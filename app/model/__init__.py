from sklearn.externals import joblib
from .iris import iris_knn

def train_iris_knn(k, model_path):
    iris_classifier = iris_knn(k)
    joblib.dump(iris_classifier, model_path)
    
