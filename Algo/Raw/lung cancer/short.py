import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import cross_val_score, KFold
import numpy as np
import warnings
from sklearn import metrics

warnings.filterwarnings('ignore')

def pred(arr):
    data = pd.read_csv('/Users/PratyushBalaji/Desktop/codefest/lung cancer/data.csv')

    inputColumns = ['GENDER','AGE','SMOKING','YELLOW_FINGERS','ANXIETY','PEER_PRESSURE','CHRONIC_DISEASE','FATIGUE','ALLERGY','WHEEZING','ALCOHOL_CONSUMING','COUGHING','SHORTNESS_OF_BREATH','SWALLOWING_DIFFICULTY','CHEST_PAIN']

    X = data[inputColumns]
    y = data['LUNG_CANCER']

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 5)

    parameters = {
        'penalty' : ['l1','l2'],
        'C' : np.logspace(-3,3,7),
        'solver'  : ['newton-cg', 'lbfgs', 'liblinear'],
    }

    log_tuned = LogisticRegression(C = 10.0, penalty = 'l2', solver = 'newton-cg')
    log_tuned.fit(X_train, y_train)

    return log_tuned.predict([arr])