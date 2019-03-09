from .pyconfig import config
from .iris_model import load_model

def test_model_load():
    model = load_model(config['MODEL'])
    test_results = model.predict_proba([[1, 1, 1, 1]])
    assert all(model.classes_ == [0, 1, 2])
    assert test_results.shape == (1, 3)

