import tensorflow as tf
import os

tfbwriter = tf.summary.FileWriter(os.getcwd() + "/logs", tf.get_default_graph())
runops = tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE)
runmeta = tf.RunMetadata()
