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

sess = tf.Session()
W = tf.Variable(tf.random_uniform([300000, 1], -1.0, 1.0), name="Weigh")
b = tf.Variable(tf.zeros([1]), name="Bias")
saver = tf.train.Saver()
saver.restore(sess, 'my-model-20000')
x = f.features_for_tensorflow(sys.argv[1])
y = tf.add(tf.matmul(W, x, transpose_a=True), b)
comment = sess.run(y)
print(comment[0][0])
