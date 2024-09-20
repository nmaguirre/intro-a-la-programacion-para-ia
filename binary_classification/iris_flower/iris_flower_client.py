from iris_flower import *

iris_object = IrisFlower(5.1, 3.5, 1.4, 0.2, "Iris-setosa")
iris_object_2 = IrisFlower(5.1, 3.5, 1.4, 0.2, "Iris-setosa")
print(iris_object == iris_object_2)
print(iris_object.get_iris_class())
iris_object.set_sepal_length(5.11)
print(iris_object == iris_object_2)
print(iris_object)
print(iris_object_2)
iris_object_1 = IrisFlower.from_tuple(('7.0','3.2','4.7','1.4','Iris-versicolor'))
print(iris_object_1)
