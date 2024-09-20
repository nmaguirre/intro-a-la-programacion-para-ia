from iris_flower import *
from random_iris_binary_classifier import *
import csv
import sys

with open(sys.argv[1]) as f:
    data = [tuple(line) for line in csv.reader(f)]
flower_data = list()
for row in data:
    flower_item = IrisFlower.from_tuple(row).as_tuple()
    fi_ls = list(flower_item)
    iris_class = fi_ls.pop(len(fi_ls)-1)
    if iris_class == 'Iris-setosa':
        fi_ls.append(1)
    else:
        fi_ls.append(0)
    flower_data.append(tuple(fi_ls))
classifier = RandomIrisBinaryClassifier(flower_data)
classifier.split_dataset()
classifier.fit()
print(classifier.compute_confusion_matrix())
