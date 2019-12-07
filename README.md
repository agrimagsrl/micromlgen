# Introducing MicroML

MicroML is an attempt to bring Machine Learning algorithms to microcontrollers.
Please refer to [this blog post](https://agrimagsrl.github.io/EloquentArduino/2019/11/introducing-microml/)
to an introduction to the topic.

## Install

`pip install micromlgen`

## Use

```python
from micromlgen import port
from sklearn.svm import SVC
from sklearn.datasets import load_iris


if __name__ == '__main__':
    iris = load_iris()
    X = iris.data
    y = iris.target
    clf = SVC(kernel='linear').fit(X, y)
    print(port(clf))
```

You may pass a classmap to get readable class names in the ported code

```python
from micromlgen import port
from sklearn.svm import SVC
from sklearn.datasets import load_iris


if __name__ == '__main__':
    iris = load_iris()
    X = iris.data
    y = iris.target
    clf = SVC(kernel='linear').fit(X, y)
    print(port(clf, classmap={
        0: 'setosa',
        1: 'virginica',
        2: 'versicolor'
    }))
```

You can pass a test set to generate self test code

```python
from micromlgen import port
from sklearn.svm import SVC
from sklearn.datasets import load_iris


if __name__ == '__main__':
    iris = load_iris()
    X_train, X_test = iris.data[:-10, :], iris.data[-10:, :]
    y_train, y_test = iris.target[:-10], iris.target[-10:]
    clf = SVC(kernel='linear').fit(X_train, y_train)
    print(port(clf, test_set=(X_test, y_test)))
```