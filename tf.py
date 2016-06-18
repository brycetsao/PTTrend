import tensorflow as tf
import numpy as np
from feature import Feature
import sqlite3

db = sqlite3.connect('ptt.db')
cur = db.execute('SELECT * FROM ARTICLES LIMIT 100')


# Create 100 phony x, y data points in NumPy, y = x * 0.1 + 0.3
f = Feature()
post_data = []
y_data = []
for i in cur:
    post_data.append(f.features_for_tensorflow(i[5]))
    y_data.append(i[7])

x_data = np.array(post_data)
x = tf.placeholder(tf.float32, shape=(300000, 1))
# Try to find values for W and b that compute y_data = W * x_data + b
# (We know that W should be 0.1 and b 0.3, but Tensorflow will
# figure that out for us.)
W = tf.Variable(tf.random_uniform([300000, 1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = tf.matmul(W, x, transpose_a=True) + b

# Minimize the mean squared errors.
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.00000005)
train = optimizer.minimize(loss)

# Before starting, initialize the variables.  We will 'run' this first.
init = tf.initialize_all_variables()

# Launch the graph.
sess = tf.Session()
sess.run(init)

# Fit the line.
for step in range(201):
    for data in x_data:
        sess.run(train, feed_dict={x: data})
    #if step % 20 == 0:
    print(step, sess.run(W), sess.run(b))

# Learns best fit is W: [0.1], b: [0.3]
