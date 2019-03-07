from sklearn.externals import joblib

def load_model(model_path):
    iris_classifier = joblib.load(model_path)
    return iris_classifier
