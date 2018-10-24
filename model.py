import os
from sklearn.datasets import make_classification
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier

from utils.logger import MainLogger

logger = MainLogger(__name__)


class Model(object):

    model_file = "model.pkl"

    def __init__(self):
        if not os.path.exists(self.model_file):
            self.train()

        self.model = joblib.load(self.model_file)
        logger.debug("Model loaded from {}".format(self.model_file))

    def train(self):
        X, y = make_classification(n_samples=5000,
                                   n_features=300,
                                   n_informative=100,
                                   n_redundant=50,
                                   n_repeated=0,
                                   n_classes=10,
                                   flip_y=0.01,
                                   shuffle=True)
        model = RandomForestClassifier(n_estimators=128, n_jobs=1)
        model.fit(X, y)
        joblib.dump(model, self.model_file)
        logger.debug("Model saved to {}".format(self.model_file))

    def predict(self, X):
        predictions = self.model.predict_proba(X)
        return predictions
