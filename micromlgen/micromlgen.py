import os
import re
from math import factorial
from jinja2 import FileSystemLoader, Environment


def port(clf, test_set=None, classmap=None, platform='arduino', **kwargs):
    assert type(clf).__name__ == 'SVC', 'Only sklearn.svm.SVC is supported for now'
    support_v = clf.support_vectors_
    template_data = {
        'KERNEL_TYPE': clf.kernel,
        'KERNEL_GAMMA': clf.gamma,
        'KERNEL_COEF': clf.coef0,
        'KERNEL_DEGREE': clf.degree,
        'FEATURES_DIM': len(support_v[0]),
        'VECTORS_COUNT': len(support_v),
        'CLASSES_COUNT': len(clf.n_support_),
        'DECISIONS_COUNT': factorial(len(clf.n_support_)),
        'support_v': support_v,
        'n_support': clf.n_support_,
        'intercepts': clf.intercept_,
        'coefs': clf.dual_coef_,
        'X': test_set[0] if test_set else None,
        'y': test_set[1] if test_set else None,
        'classmap': classmap,
        'F': {
            'enumerate': enumerate,
        },
        'isAttiny': platform == 'attiny',
    }
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    loader = FileSystemLoader(dir_path + '/templates')
    template = Environment(loader=loader).get_template('svm.jinja')
    code = template.render(template_data)
    code = re.sub(r'\n\s*\n', '\n', code)

    return code