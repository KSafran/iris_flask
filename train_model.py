from app.model import train_iris_knn
from app.pyconfig import config

train_iris_knn(config['K'], config['MODEL'])
