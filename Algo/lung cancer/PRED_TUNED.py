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

data = pd.read_csv('/Users/PratyushBalaji/Desktop/codefest/lung cancer/data.csv')

inputColumns = ['GENDER','AGE','SMOKING','YELLOW_FINGERS','ANXIETY','PEER_PRESSURE','CHRONIC_DISEASE','FATIGUE','ALLERGY','WHEEZING','ALCOHOL_CONSUMING','COUGHING','SHORTNESS_OF_BREATH','SWALLOWING_DIFFICULTY','CHEST_PAIN']

X = data[inputColumns]
y = data['LUNG_CANCER']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 5)

#kf = KFold(n_splits=5, shuffle=True, random_state=5)

log = LogisticRegression()
log.fit(X_train, y_train)

y_pred =  log.predict(X_test)
#cv_scores = cross_val_score(log, X, y, cv=kf)

#print(cv_scores)


parameters = {
    'penalty' : ['l1','l2'],
    'C' : np.logspace(-3,3,7),
    'solver'  : ['newton-cg', 'lbfgs', 'liblinear'],
}

clf = GridSearchCV(log,                    # model
                   param_grid = parameters,   # hyperparameters
                   scoring='accuracy',        # metric for scoring
                   cv=10)                     # number of folds

log_tuned = LogisticRegression(C = 10.0, penalty = 'l2', solver = 'newton-cg')
log_tuned.fit(X_train, y_train)

y_tuned_pred = log_tuned.predict(X_test)
clf.fit(X_train,y_train)
print("Accuracy:",log.score(X_test, y_test))
print("Classification Report: " + classification_report(y_test, y_pred))
print("Confusion Matrix: ", confusion_matrix(y_test, y_pred))

print("Tuned Hyperparameters :", clf.best_params_)
print("Accuracy(Tuned):",log_tuned.score(X_test, y_test))
print("Classification Report(Tuned): " + classification_report(y_test, y_tuned_pred))
print("Confusion Matrix(Tuned): ", confusion_matrix(y_test, y_tuned_pred))

sns.heatmap(data.corr(),annot=True)
plt.show()