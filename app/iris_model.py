
class DummyModel(object):
    def __init__(self):
        pass
    def predict(self, x):
        return 'placeholder'

def load_model(model_path):
    return DummyModel()
