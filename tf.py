import tensorflow as tf
import numpy as np
from feature import Feature
import sqlite3
import pickle

db = sqlite3.connect('ptt.db')
cur = db.execute('SELECT * FROM ARTICLES LIMIT 1000')


# Create 100 phony x, y data points in NumPy, y = x * 0.1 + 0.3
f = Feature()
post_data = []
push_data = []
boo_data = []
for i in cur:
    post_data.append(f.features_for_tensorflow(i[5]))
    push_data.append(i[7])
    boo_data.append(i[8])

y_data = np.array(push_data) - np.array(boo_data)

x_data = np.array(post_data)
x = tf.placeholder(tf.float32, shape=(300000, 1))
# Try to find values for W and b that compute y_data = W * x_data + b
# (We know that W should be 0.1 and b 0.3, but Tensorflow will
# figure that out for us.)
W = tf.Variable(tf.random_uniform([300000, 1], -1.0, 1.0), name="Weigh")
b = tf.Variable(tf.zeros([1]), name="Bias")
y = tf.add(tf.matmul(W, x, transpose_a=True), b)

# Minimize the mean squared errors.
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.0000005)
train = optimizer.minimize(loss)

# Before starting, initialize the variables.  We will 'run' this first.
init = tf.initialize_all_variables()

# Launch the graph.
saver = tf.train.Saver([W, b])
sess = tf.Session()
sess.run(init)

# Fit the line.
for step in range(20001):
    for data in x_data:
        sess.run(train, feed_dict={x: data})
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))
    if step % 1000 == 0:
        # Append the step number to the checkpoint name:
        saver.save(sess, 'my-model', global_step=step)

