import sys
import pickle
from feature import Feature
import tensorflow as tf

from sklearn.externals import joblib
clf = joblib.load('clf.pkl')

if len(sys.argv) < 2:
    sys.exit()

f = Feature()
post_feature = [f.features(sys.argv[1])]
print(clf.predict(post_feature)[0])
print(clf.predict_proba(post_feature)[0])

