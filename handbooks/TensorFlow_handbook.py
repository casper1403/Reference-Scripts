#
import tensorflow as tf



"""
TensorFlow works on the base of objects called tensors, which are vector which can
contain multiple objects

Each tensor has a degree or rank which denotes the dimension the vector is in

"""

# Tensor of rank 0
string = tf.Variable('this is a string', tf.string)
number = tf.Variable(324, tf.int16)
floating = tf.Variable(3.567, tf.float64)

# Tensor of rank 1
rank1_tensor = tf.Variable(['one','two'], tf.string)

# Tensor of rank 2
rank2_tensor = tf.Variable([["test", "ok"], ["test", "yes"]], tf.string)

# to check the rank of a tensor
tf.rank(rank2_tensor)

# to check the shape of a tensor ( items in each dimension)
rank2_tensor.shape

"""
The number of elements of a tensor is the product of the sizes of all its shapes.
There are often many shapes that have the same number of elements, making it convient to be able to change the shape of a tensor.

The example below shows how to change the shape of a tensor.
"""
tensor1 = tf.ones([1,2,3])  # tf.ones() creates a shape [1,2,3] tensor full of ones
tensor2 = tf.reshape(tensor1, [2,3,1])  # reshape existing data to shape [2,3,1]
tensor3 = tf.reshape(tensor2, [3, -1])  # -1 tells the tensor to calculate the size of the dimension in that place
                                        # this will reshape the tensor to [3,3]


"""
There are a number of different tensors:
    - Variable
    - Constant
    - Placeholder
    - SparseTensor
With the exeption of Variable; all these tensore are immuttable



"""
