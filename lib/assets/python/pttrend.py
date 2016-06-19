import sys
import pickle
import sqlite3
from feature import Feature
import tensorflow as tf
from sklearn.externals import joblib
from argparse import ArgumentParser, ArgumentTypeError

parser = ArgumentParser(prog='pttrend')
parser.add_argument("-i", action="store_true", help="Predict from stdin")
parser.add_argument("-p", nargs=1, help="Predict a specific article ID (same as `id` in sqlite database)")
parser.add_argument("-o", action="store_true", help="Print testing content")
parser.add_argument("-l", action="store_true", help="Print only 3 result vars, first is if it is politics-related, second is the probability of politics-related, third is the rating (number of 推 - number of 噓). Each var is separated by newline.")
parsed_args = parser.parse_args()
clf = joblib.load('clf.pkl')

if parsed_args.p:
    db = sqlite3.connect('ptt.db')
    test = db.execute('SELECT content FROM articles WHERE id='+parsed_args.p[0]).fetchone()[0]
elif parsed_args.i:
    test = sys.stdin.read()
else:
    parser.print_help()
    exit()

if not test:
    print("Empty input")
if parsed_args.o:
    print(test)

f = Feature()
sess = tf.Session()
W = tf.Variable(tf.random_uniform([300000, 1], -1.0, 1.0), name="Weigh")
b = tf.Variable(tf.zeros([1]), name="Bias")
saver = tf.train.Saver()
saver.restore(sess, 'my-model-20000')
x = f.features_for_tensorflow(test)
y = tf.add(tf.matmul(W, x, transpose_a=True), b)
comment = sess.run(y)

# output
if parsed_args.l:
    print(clf.predict([f.features(test)]))
    print(clf.predict_proba([f.features(test)]))
    print(comment[0][0])
else:
    print("Result:")
    if clf.predict([f.features(test)]):
        print("The content is politics-related")
    else:
        print("The content is not politics-related")
    print("Probability of the content being politics-related: "+str(clf.predict_proba([f.features(test)])))
    print("Predicted rating (推數減噓數): "+str(comment[0][0]))
