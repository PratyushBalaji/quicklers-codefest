import pandas as pd
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

data = pd.read_csv('C:/Users/LENOVO/Downloads/GroundTruth.csv')


inputColumns = ['NV', 'BCC', 'AKIEC', 'BKL', 'DF', 'VASC']

X = data[inputColumns]
y = data['MEL']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 5)

kf = KFold(n_splits=5, shuffle=True, random_state=5)

log = LogisticRegression()
log.fit(X_train, y_train)

y_pred = log.predict(X_test)


#print(cv_scores)


parameters = {
    'penalty' : ['l1','l2'],
    'C' : np.logspace(-3,3,7),
    'solver' : ['newton-cg', 'lbfgs', 'liblinear'],
}

clf = GridSearchCV(log,                    # model
                   param_grid = parameters,   # hyperparameters
                   scoring='accuracy',        # metric for scoring
                   cv=kf)                     # number of folds

log_tuned = LogisticRegression(C = 10.0, penalty = 'l1', solver = 'liblinear')
log_tuned.fit(X_train, y_train)

y_tuned_pred = log_tuned.predict(X_test)
cv_scores = cross_val_score(log_tuned, X, y, cv=kf)



clf.fit(X_train,y_train)
print("Accuracy:",log.score(X_test, y_test))
print("Accuracy(Tuned):",log_tuned.score(X_test, y_test))

print("Classification Report: " + classification_report(y_test, y_pred))
print("Classification Report(Tuned): " + classification_report(y_test, y_tuned_pred))

print("Confusion Matrix: ", confusion_matrix(y_test, y_pred))
print("Confusion Matrix(Tuned): ", confusion_matrix(y_test, y_tuned_pred))

print("Tuned Hyperparameters :", clf.best_params_)
print(cv_scores)