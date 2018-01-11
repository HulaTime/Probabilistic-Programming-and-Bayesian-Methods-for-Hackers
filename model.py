import pymc as pm
import numpy as np
import scipy.stats as stats

from IPython.core.pylabtools import figsize
from matplotlib import pyplot as plt

count_data = np.loadtxt("data/txtdata.csv") #count_data holds our data set (num texts per day)
alpha = 1.0 / count_data.mean()
n_count_data = len(count_data)

def plot(n_count_data, count_data):
  plt.bar(np.arange(n_count_data), count_data, color="#348ABD")
  plt.xlabel("Time (days)")
  plt.ylabel("count of text-msgs received")
  plt.title("Did the user's texting habits change over time?")
  plt.xlim(0, n_count_data)
  plt.show();
