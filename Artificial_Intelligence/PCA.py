import functools
import warnings
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import tensorflow.compat.v2 as tf
import tensorflow_probability as tfp
from tensorflow_probability import bijectors as tfb
from tensorflow_probability import distributions as tfd

tf.enable_v2_behavior()

plt.style.use('ggplot')
warnings.filterwarnings('ignore') # Suppress warnings

def probabilistic_pca(data_dim, latent_dim, num_datapoints, stddv_datapoints):
  w = yield tfd.Normal(loc=tf.zeros([data_dim, latent_dim]),
                       scale=2.0 * tf.ones([data_dim, latent_dim]),
                       name="w")
  z = yield tfd.Normal(loc=tf.zeros([latent_dim, num_datapoints]),
                       scale=tf.ones([latent_dim, num_datapoints]),
                       name="z")
  x = yield tfd.Normal(loc=tf.matmul(w, z),
                       scale=stddv_datapoints,
                       name="x")
