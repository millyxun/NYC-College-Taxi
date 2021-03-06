import pandas as pd
from sklearn.model_selection import train_test_split

#Algorithms packages from scikit-learn
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC
#For Pipelining
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline


pred_amt_with_all_columns = pd.read_csv("./Github/NYC-College-Taxi/extracted_data/pred_amt_with_all_columns.csv")

print pred_amt_with_all_columns.shape

file_list = [pred_amt_with_all_columns]
print pred_amt_with_all_columns.shape
print pred_amt_with_all_columns.columns.values
# Construct some pipelines

pipeline_lr = Pipeline([('scl', StandardScaler()),
                    ('pca', PCA(n_components=15)),
                    ('lr', LogisticRegression())])

pipeline_svm = Pipeline([('scl', StandardScaler()),
                     ('pca', PCA(n_components=15)),
                     ('svc', LinearSVC())])

pipeline_rf = Pipeline([('scl', StandardScaler()),
                    ('pca', PCA(n_components=15)),
                    ('rfc', RandomForestClassifier(random_state=1))])

pipeline_gnb = Pipeline([('scl', StandardScaler()),
                     ('pca', PCA(n_components=15)),
                     ('gnb', GaussianNB())])

pipeline_ada = Pipeline([('scl', StandardScaler()),
                     ('pca', PCA(n_components=15)),
                     ('ada', AdaBoostClassifier(random_state=1))])

pipeline_knn = Pipeline([('scl', StandardScaler()),
                     ('pca', PCA(n_components=15)),
                     ('mlp', MLPClassifier())])

pipeline_mlp = Pipeline([('scl', StandardScaler()),
                     ('pca', PCA(n_components=15)),
                     ('knn', KNeighborsClassifier())])

pipelines = [pipeline_lr, pipeline_svm, pipeline_rf, pipeline_gnb, pipeline_ada, pipeline_knn, pipeline_mlp]

X = pred_amt_with_all_columns.iloc[:, :]
X = X.drop("total_amount", 1)
y = pred_amt_with_all_columns.total_amount
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

pipeline_dictionary = {0: 'Logistic Regression',
                       1: 'Support Vector Machine',
                       2: 'Random Forest',
                       3: 'Gaussian Naive Bayes',
                       4: 'ADABoost',
                       5: 'K-Nearest Neighbour',
                       6: 'Multi-Layer Perceptron'
                       }

for pipe in pipelines:
    pipe.fit(X_train, y_train)

for index, value in enumerate(pipelines):
    print('%s pipeline accuracy: %.3f' % (pipeline_dictionary[index], value.score(X_test, y_test)))