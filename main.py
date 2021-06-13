import tensorflow as tf  # now import the tensorflow module
print(tf.version)  # make sure the version is 2.x

tensor1 = tf.zeros([1, 2, 3])  # tf.ones() creates a shape [1,2,3] tensor full of ones
tensor2 = tf.reshape(tensor1, [6])  # reshape existing data to shape [2,3,1]
tensor3 = tf.reshape(tensor2, [3, -1])  # -1 tells the tensor to calculate the size of the dimension in that place
# this will reshape the tensor to [3,3]

# The numer of elements in the reshaped tensor MUST match the number in the original

print(tensor1)
print(tensor2)
print(tensor3)