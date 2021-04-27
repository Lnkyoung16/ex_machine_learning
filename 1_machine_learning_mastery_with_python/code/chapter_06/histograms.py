# Univariate Histograms
from matplotlib import pyplot
from pandas import read_csv
filename = '1_machine_learning_mastery_with_python/code/chapter_06/pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
data.hist()
pyplot.show()
