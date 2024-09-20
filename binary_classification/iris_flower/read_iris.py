import csv
from iris_flower import *

with open(argv[1]) as f:
    data = [tuple(line) for line in csv.reader(f)]
#TODO create a list of IrisFlower objects from list data
#TODO print list of IrisFlower objects

