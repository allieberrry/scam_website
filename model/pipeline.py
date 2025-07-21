#importing libraries

import pandas as pd
import numpy as np

from skmultilearn.model_selection import iterative_train_test_split

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import classification_report

#----------------------------------------------------------------------

file_path = '/Users/aryanpatel/Documents/summerscam/data/processed_scam_data.csv'
scam_df = pd.read_csv(file_path)

#list of columns we need from our data frame 
columns_to_keep= ['scam_id', "description", 'label_a', 'label_c', 'label_f', 'label_l', 'label_p', 'label_r', 'label_s', 'label_t', 'label_u']

#updating the scam_df to only have the necessary information
scam_df = scam_df[columns_to_keep]

#Cleaning the data (if needed), dropping any rows that might have a missing description
scam_df = scam_df.dropna(subset=["description"])
scam_df = scam_df.reset_index(drop=True)

#----------------------------------------------------------------------

# seperating the features from the targets

#features
features = scam_df["description"]

#reshaping the features into a 2D array (2d shape required for splitting)
features = features.values.reshape(-1,1) 

#targets
PTs = ['label_a', 'label_c', 'label_f', 'label_l', 'label_p', 'label_r', 'label_s', 'label_t', 'label_u']

targets = scam_df[PTs].values

#----------------------------------------------------------------------

X_train, y_train, X_test, y_test = iterative_train_test_split(
    features,
    targets, 
    test_size = 0.2   #20 pecent fo the data will be tests on (80% is trained)

)

# faltten the X_train and X_test into a 1D array (required for fitting the pipeline)
X_train_flat = X_train.ravel()
X_test_flat = X_test.ravel()

#----------------------------------------------------------------------

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer( 
        lowercase = True, #lowercasing all the tokens
        stop_words = "english", #removing any stopwords
        ngram_range = (1,3) #will generate unigram, bigram, and trigram vectors for the scam descriptions
    )),
    ("clf", OneVsRestClassifier(
        MLPClassifier(
            hidden_layer_sizes = (100,), #Setting one hidden layer, 100 neurons in that layer
            max_iter = 500, #max iterations the neural network will run
            
        )
    ))  
])

#----------------------------------------------------------------------

pipeline.fit(X_train_flat, y_train)

#----------------------------------------------------------------------

predictions = pipeline.predict(X_test_flat)
print(classification_report(y_test, predictions, target_names=PTs))

#----------------------------------------------------------------------