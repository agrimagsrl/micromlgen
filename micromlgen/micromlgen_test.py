import pickle
from micromlgen import port
from sklearn.svm import SVC
from sklearn.datasets import load_iris


if __name__ == '__main__':
    test_iris = True
    if test_iris:
        iris = load_iris()
        X = iris.data
        y = iris.target
        clf = SVC(kernel='linear').fit(X, y)
        print(port(clf))
    else:
        with open('../svmporter/datasets/svm.clf', 'rb') as file:
            payload = pickle.load(file)
            clf = payload['clf']
            classmap = payload['classmap']
            # test_set = (payload['X_test'], payload['y_test'])
            print(port(clf, classmap=classmap))

