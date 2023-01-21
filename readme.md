# Team : Quicklers
Members : 
Pratyush
Rishik 
Tejas
Rushil 
Ram

ML cancer prediction algorithm (regression model)

Only included melanoma and lung cancer as they are most complete

Confusion Matrices and Classification Reports of all models : 

# Skin Cancer (Melanoma)
Accuracy: 1.0 (100%)
Accuracy(Tuned): 1.0 (100%)
Classification Report:               precision    recall  f1-score   support

         0.0       1.00      1.00      1.00      2243
         1.0       1.00      1.00      1.00       261

    accuracy                           1.00      2504
   macro avg       1.00      1.00      1.00      2504
weighted avg       1.00      1.00      1.00      2504

Classification Report(Tuned):               precision    recall  f1-score   support

         0.0       1.00      1.00      1.00      2243
         1.0       1.00      1.00      1.00       261

    accuracy                           1.00      2504
   macro avg       1.00      1.00      1.00      2504
weighted avg       1.00      1.00      1.00      2504

Confusion Matrix:  
[[2243    0]
 [   0  261]]
Confusion Matrix(Tuned):  
[[2243    0]
 [   0  261]]
Tuned Hyperparameters : {'C': 0.1, 'penalty': 'l1', 'solver': 'liblinear'}
[1. 1. 1. 1. 1.]

# Prostate Cancer
Accuracy: 0.84 (84%)
Accuracy(Tuned): 0.88 (88%) -> +4%
Classification Report:               precision    recall  f1-score   support

           0       0.88      0.88      0.88        16
           1       0.78      0.78      0.78         9

    accuracy                           0.84        25
   macro avg       0.83      0.83      0.83        25
weighted avg       0.84      0.84      0.84        25

Classification Report(Tuned):               precision    recall  f1-score   support

           0       0.88      0.94      0.91        16
           1       0.88      0.78      0.82         9

    accuracy                           0.88        25
   macro avg       0.88      0.86      0.87        25
weighted avg       0.88      0.88      0.88        25

Confusion Matrix:  
[[14  2]
 [ 2  7]]
Confusion Matrix(Tuned):  
[[15  1]
 [ 2  7]]
Tuned Hyperparameters : {'C': 0.1, 'penalty': 'l2', 'solver': 'newton-cg'}
[0.85 0.95 0.95 0.55 0.85]

# Breast Cancer
Accuracy: 0.972027972027972 (97.2%)
Accuracy(Tuned): 0.9790209790209791 (97.9%) -> +0.7%
Classification Report:               precision    recall  f1-score   support

           0       0.97      0.99      0.98        88
           1       0.98      0.95      0.96        55

    accuracy                           0.97       143
   macro avg       0.97      0.97      0.97       143
weighted avg       0.97      0.97      0.97       143

Classification Report(Tuned):               precision    recall  f1-score   support

           0       0.98      0.99      0.98        88
           1       0.98      0.96      0.97        55

    accuracy                           0.98       143
   macro avg       0.98      0.98      0.98       143
weighted avg       0.98      0.98      0.98       143

Confusion Matrix:  
[[87  1]
 [ 3 52]]
Confusion Matrix(Tuned):  
[[87  1]
 [ 2 53]]
Tuned Hyperparameters : {'C': 100.0, 'penalty': 'l1', 'solver': 'liblinear'}
[0.97368421 1.0 0.96491228 0.96491228 0.94690265]

# Lung Cancer
Accuracy: 0.9358974358974359 (93.6%)
Accuracy(Tuned): 0.9487179487179487 (94.9%) -> +1.3%
Classification Report:               precision    recall  f1-score   support

           0       1.00      0.44      0.62         9
           1       0.93      1.00      0.97        69

    accuracy                           0.94        78
   macro avg       0.97      0.72      0.79        78
weighted avg       0.94      0.94      0.92        78

Classification Report(Tuned):               precision    recall  f1-score   support

           0       1.00      0.56      0.71         9
           1       0.95      1.00      0.97        69

    accuracy                           0.95        78
   macro avg       0.97      0.78      0.84        78
weighted avg       0.95      0.95      0.94        78

Confusion Matrix:  
[[ 4  5]
 [ 0 69]]
Confusion Matrix(Tuned):  
[[ 5  4]
 [ 0 69]]
Tuned Hyperparameters : {'C': 10.0, 'penalty': 'l2', 'solver': 'newton-cg'}
K Fold Scores(Tuned) =  [0.93548387 0.91935484 0.96774194 0.96774194 0.86885246]