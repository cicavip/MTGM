import numpy as np
import matplotlib.pyplot as plt
import math
import mpl_toolkits.mplot3d
import tensorflow as tf
from sklearn import datasets

sess = tf.InteractiveSession()
gamma = tf.constant(-1.0)
x, y = np.mgrid[-2:2:0.01, -2:2:0.01]

x_data = tf.placeholder(shape=[400, 400], dtype=tf.float32)
y_data = tf.placeholder(shape=[400, 400], dtype=tf.float32)

Kernel = tf.exp(tf.multiply(gamma, tf.add((x_data*x_data),(y_data*y_data))))
Kernel = sess.run(Kernel, feed_dict={x_data: x,y_data: y})

ax = plt.subplot(111, projection='3d')
ax.plot_surface(x, y, Kernel, rstride=1, cstride=1, cmap='rainbow', alpha=0.9)#绘面
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Kernel')
plt.show()

