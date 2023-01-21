import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

data = pd.read_csv('/Users/PratyushBalaji/Desktop/codefest/data.csv')


inputColumns = ['GENDER','AGE','SMOKING','YELLOW_FINGERS','ANXIETY','PEER_PRESSURE','CHRONIC_DISEASE','FATIGUE','ALLERGY','WHEEZING','ALCOHOL_CONSUMING','COUGHING','SHORTNESS_OF_BREATH','SWALLOWING_DIFFICULTY','CHEST_PAIN']

X = data[inputColumns]
y = data['LUNG_CANCER']

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state = 0)

lin = LinearRegression()
lin.fit(X_train, y_train)

y_pred_lin = [int(i+0.5) for i in lin.predict(X_test)]

log = LogisticRegression()
log.fit(X_train, y_train)

y_pred_log = [int(i+0.5) for i in log.predict(X_test)]


print(confusion_matrix(y_test, y_pred_lin))
print(classification_report(y_test, y_pred_lin))

print(roc_auc_score(y_test, y_pred_log))
print(confusion_matrix(y_test, y_pred_log))
print(classification_report(y_test, y_pred_log))

'''
TEST SETS
1,59,1,1,1,2,1,2,1,2,1,2,2,1,2,1
2,69,1,2,2,1,1,2,1,2,2,2,2,2,2,2
'''


'''
linear vs logistic test : 

Linear :
[[ 4  6]
 [ 1 67]]
              precision    recall  f1-score   support

           0       0.80      0.40      0.53        10
           1       0.92      0.99      0.95        68

    accuracy                           0.91        78
   macro avg       0.86      0.69      0.74        78
weighted avg       0.90      0.91      0.90        78

Logistic :
[[ 6  4]
 [ 1 67]]
              precision    recall  f1-score   support

           0       0.86      0.60      0.71        10
           1       0.94      0.99      0.96        68

    accuracy                           0.94        78
   macro avg       0.90      0.79      0.83        78
weighted avg       0.93      0.94      0.93        78


logistic wins, switch model to logistic for rest of testing
'''