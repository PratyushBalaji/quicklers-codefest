import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import cross_val_score, KFold


data = pd.read_csv('/Users/PratyushBalaji/Desktop/codefest/melanoma/data.csv')


inputColumns = ['NV','BCC','AKIEC','BKL','DF','VASC']

X = data[inputColumns]
y = data['MEL']

'''
Columns : 
MEL : MELanoma
NV : melanocytic NeVi
BCC : Basal Cell Carcinoma
AKIEC : Actinic Keratoses and IntraEpithelial Carcinoma (bowen's disease)
BKL : Benign Keratosis-like Lesions
DF : DermatoFibroma
VASC : VASCular lesions

'''

data.drop('image', inplace=True, axis=1)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state = 0)

log = LogisticRegression()
log.fit(X_train, y_train)

y_pred_log = [int(i+0.5) for i in log.predict(X_test)]

# 0.0,0.0,0.0,0.0,0.0,0.0
# expected : 1.0
# received : 1.
# log.predict([[0.0,0.0,0.0,0.0,0.0,0.0]])

sns.heatmap(data.corr(),annot=True)

# sns.pairplot(data)
plt.show()