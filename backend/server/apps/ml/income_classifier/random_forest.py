import joblib
import pandas as pd
import os
from apps.ml.income_classifier.base_classifier import BaseClassifier

class RandomForestClassifier(BaseClassifier):
    def __init__(self):
        # Get the absolute path to the directory containing this file
        self.model = "random_forest.joblib"
        super().__init__(self.model)
