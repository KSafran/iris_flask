import numpy as np
from .iris import iris_knn

def train_iris_knn(k, model_path):
    iris_classifier = iris_knn(k)
    np.save(model_path, iris_classifier)
    
