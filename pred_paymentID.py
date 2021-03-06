import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics as ms

#Algorithms packages from scikit-learn
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import Perceptron

df_no_datetime = pd.read_csv("./Github/NYC-College-Taxi/extracted_data/no_datetime.csv")
df_min_pickup = pd.read_csv("./Github/NYC-College-Taxi/extracted_data/pickup_in_mins.csv")
df_hrs_pickup = pd.read_csv("./Github/NYC-College-Taxi/extracted_data/pickup_in_hrs.csv")

print df_no_datetime.shape, df_min_pickup.shape, df_hrs_pickup.shape

lr = LogisticRegression(random_state=1)
rfc = RandomForestClassifier(random_state=1)
gnb = GaussianNB()
ada = AdaBoostClassifier(random_state=1)
knn = KNeighborsClassifier()
mlp = MLPClassifier()
svc = LinearSVC()
lp = Perceptron()

file_list = [df_no_datetime, df_min_pickup, df_hrs_pickup]

for i in file_list:
    X = i.iloc[:, :]
    X = X.drop("payment_type", 1)
    y = i.payment_type
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    eclf1 = VotingClassifier(
        estimators=[('lr', lr), ('rf', rfc), ('gnb', gnb), ('ada', ada), ('knn', knn), ('mlp', mlp)],
        voting='hard')
    eclf1 = eclf1.fit(X_train, y_train)
    y_pred1 = eclf1.predict(X_test)

    eclf2 = VotingClassifier(
        estimators=[('lr', lr), ('rf', rfc), ('gnb', gnb), ('ada', ada), ('knn', knn), ('mlp', mlp)],
        voting='soft')
    eclf2 = eclf1.fit(X_train, y_train)
    y_pred2 = eclf1.predict(X_test)
    print ms.accuracy_score(y_test, y_pred1), ms.accuracy_score(y_test, y_pred2)

for i in file_list:
    X = i.iloc[:, :]
    X = X.drop("payment_type", 1)
    y = i.payment_type
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    lr = lr.fit(X_train, y_train)
    rfc = rfc.fit(X_train, y_train)
    gnb = gnb.fit(X_train, y_train)
    ada = ada.fit(X_train, y_train)
    knn = knn.fit(X_train, y_train)
    mlp = mlp.fit(X_train, y_train)
    svc = svc.fit(X_train, y_train)
    lp = lp.fit(X_train, y_train)
    lr_pred = lr.predict(X_test)
    rfc_pred = rfc.predict(X_test)
    gnb_pred = gnb.predict(X_test)
    ada_pred = ada.predict(X_test)
    knn_pred = knn.predict(X_test)
    mlp_pred = mlp.predict(X_test)
    svc_pred = svc.predict(X_test)
    lp_pred = lp.predict(X_test)

    print "Logistic Regression: ",ms.accuracy_score(y_test, lr_pred)
    print "Random Forest Classifier: ",ms.accuracy_score(y_test, rfc_pred)
    print "Naive Bayes: ",ms.accuracy_score(y_test, gnb_pred)
    print "ADA Boost: ",ms.accuracy_score(y_test, ada_pred)
    print "K Nearest Neighbour: ",ms.accuracy_score(y_test, knn_pred)
    print "Multi-layer Perceptron classifier: ",ms.accuracy_score(y_test, mlp_pred)
    print "Linear SVM: ",ms.accuracy_score(y_test, svc_pred)
    print "Perceptron: ", ms.accuracy_score(y_test, lp_pred)

