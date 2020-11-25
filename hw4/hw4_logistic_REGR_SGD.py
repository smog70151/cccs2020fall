import os
import sys
import pdb
import math
import numpy as np
from pyspark import SparkConf, SparkContext
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import LogisticRegressionWithSGD

def getSparkContext():
    """
    Gets the Spark Context
    """
    conf = (SparkConf()
         .setMaster("local") # run on local
         .setAppName("Logistic Regression") # Name of App
         .set("spark.executor.memory", "1g")) # Set 1 gig of memory
    sc = SparkContext(conf = conf)
    return sc

def mapper(line):
    """
    Mapper that converts an input line to a feature vector
    """
    feats = line.strip().split(",")
    # labels must be at the beginning for LRSGD
    label = feats[len(feats) - 1]
    feats = feats[: len(feats) - 1]
    # feats.insert(0,label)
    features = [ float(feature) for feature in feats ] # need floats
    return LabeledPoint(label, features)
    # return np.array(features)

def reduceGradient(g1, g2):
	return [g1[i]+g2[i] for i in range(len(g2))]

sc = getSparkContext()

# Load and parse the data
data = sc.textFile("file:///opt/bitnami/spark/hw4/hw4_train.txt")
parsedData = data.map(mapper)

# Hyperparams
epochs = 10
iters = 100
lr = 0.001
w = np.zeros(4).astype(np.float128)

# Training Phase
for epoch in range(epochs):
	for iter in range(iters):
		g = parsedData.sample(False, 10).map(lambda p: (1/(1+np.exp(-w.dot(p.features))) - p.label) * p.features).reduce(reduceGradient)
		w = w - np.array(g).astype(np.float128) * lr
		w = w.astype(np.float128)

print ("[+] Prediction Phase Start...")
# Prediction Phase
labelsAndPreds = parsedData.map(lambda p: (p.label, ( 1/(1+np.exp(-w.dot(p.features))) ).round()))

print ("[+] Evaluation Phase Start...")
# Evaluating the model on training data
trainErr = labelsAndPreds.filter(lambda p: p[0] != p[1]).count() / float(parsedData.count())

# Print some stuff
print("Training Error = " + str(trainErr))
