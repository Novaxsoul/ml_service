import joblib
import pandas as pd
import os

class RandomForestClassifier:
    def __init__(self):
        # Get the absolute path to the directory containing this file
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        path_to_artifacts = os.path.join(BASE_DIR, "../../../../../research/")
        self.values_fill_missing = joblib.load(os.path.join(path_to_artifacts, "train_mode.joblib"))
        self.encoders = joblib.load(os.path.join(path_to_artifacts, "encoders.joblib"))
        self.model = joblib.load(os.path.join(path_to_artifacts, "random_forest.joblib"))

    def preprocessing(self, input_data):
        # JSON to pandas DF
        input_data = pd.DataFrame(input_data, index=[0])
        # Fill missing values
        input_data.fillna(self.values_fill_missing)
        # convert categoricals
        for column in [
            "workclass",
            "education",
            "marital-status",
            "occupation",
            "relationship",
            "race",
            "sex",
            "native-country",
        ]:
            categorical_convert = self.encoders[column]
            input_data[column] = categorical_convert.transform(input_data[column])

        return input_data
    
    def predict(self, input_data):
        return self.model.predict_proba(input_data)
    
    def postprocessing(self, input_data):
        label = "<=50K"
        if input_data[1] > 0.5:
            label = ">50K"
        return {"probability": input_data[1], "label": label, "status": "OK"}
    
    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)[0] # Only one sample
            prediction = self.postprocessing(prediction)
        except Exception as e:
            return {"status": "error", "message": str(e)}
        
        return prediction