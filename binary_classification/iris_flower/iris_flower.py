class IrisFlower:

    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, iris_class):
        self.__sepal_length = sepal_length
        self.__sepal_width = sepal_width
        self.__petal_length = petal_length
        self.__petal_width = petal_width
        self.__iris_class = iris_class

    def set_sepal_length(self, new_sepal_length):
        self.__sepal_length = new_sepal_length

    def set_sepal_width(self, new_sepal_width):
        #TODO implement this method
        pass # remove when implemented

    def set_petal_length(self, new_petal_length):
        #TODO implement this method
        pass # remove when implemented

    def set_petal_width(self, new_petal_width):
        #TODO implement this method
        pass # remove when implemented

    def set_iris_class(self, new_iris_class):
        #TODO implement this method
        pass # remove when implemented

    def get_sepal_length(self):
        #TODO implement this method
        pass # remove when implemented

    def get_sepal_width(self):
        #TODO implement this method
        pass # remove when implemented

    def get_petal_length(self):
        #TODO implement this method
        pass # remove when implemented

    def get_petal_width(self):
        #TODO implement this method
        pass # remove when implemented

    def get_iris_class(self):
        return self.__iris_class

    def as_tuple(self):
        """Returns object as tuple (sl, sw, pl, pw, ic) of values.
        The returned tuple is in the following order:
        sepal length, sepal width, petal length, petal width, iris class
        """
        #TODO implement this method
        pass # remove when implemented

    def __str__(self):
        """Returns a string representation of the state of self
        """
        result = f'(sepal length: {self.__sepal_length}, '
        result = result + f'sepal width: {self.__sepal_width}, '
        result = result + f'petal length: {self.__petal_length}, '
        result = result + f'petal width: {self.__petal_width}, '
        result = result + f'iris class: {self.__iris_class})'
        return result

    def __eq__(self, other):
        """Compares an iris class object with another by equality
        """
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def from_tuple(t):
        """Class method that creates an IrisFlower object from a tuple of strings
        """
        sepal_length = float(t[0])
        sepal_width = float(t[1])
        petal_length = float(t[2])
        petal_width = float(t[3])
        iris_class = str(t[4])
        return IrisFlower(sepal_length, sepal_width, petal_length, petal_width, iris_class)

