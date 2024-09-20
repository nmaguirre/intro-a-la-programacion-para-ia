import random

class PerceptronIrisBinaryClassifier:

    def __init__(self, data):
        """Constructor of class. Argument data is a list of numeric tuples.
        The data list represents a labeled dataset for binary classification.
        Last element of each tuple is a binary value, the class (1 or 0).
        """
        self.__data = data
        self.__split_ratio = 0.7
        self.__epochs = 10 # one epoch by default
        self.__training_data = list()
        self.__testing_data = list()
        self.__weights = list()
        self.__bias = 0
        self.__learning_rate = 0.01
        self.__confusion_matrix = { 'TP': 0, 'FP': 0, 'TN': 0, 'FN': 0}

    def set_split_ratio(self, ratio):
        self.__split_ratio = ratio

    def set_epochs(self, epochs):
        self.__epochs = epochs

    def split_dataset(self):
        """Splits dataset into training data and testing data.
        The ration __split_ratio is used for the splitting.
        Dataset must be shuffled before splitting. Resulting training data and
        testing data are stored in __training_data and __testing_data, respectively
        """
        #TODO Implement this method

    def fit(self):
        """Trains the perceptron with the training data, the number of set epochs
        """
        #TODO Implement this method
        pass # remove when implementation ready

    def predict(self, item):
        """Apply perceptron to predict class for item
        """
        #TODO Implement this method
        pass # remove when implementation ready

    def compute_confusion_matrix(self):
        """Computes number of false positives, false negatives, true positives and true negatives 
        in the testing data.
        Values are stored in self.__confusion_matrix and returned as a dictionary"""
        #TODO Implement this method
        pass # remove when implementation ready

        

