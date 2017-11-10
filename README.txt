MAIN.PY
X	Input dataset matrix where each row is a training example
y	Output dataset matrix where each row is a training example
l0	First Layer of the Network, specified by the input data
l1	Second Layer of the Network, otherwise known as the hidden layer
syn0	First layer of weights, Synapse 0, connecting l0 to l1.
*	Elementwise multiplication, so two vectors of equal size are multiplying corresponding values 1-to-1 to generate a final vector of identical size.
-	Elementwise subtraction, so two vectors of equal size are subtracting corresponding values 1-to-1 to generate a final vector of identical size.
x.dot(y)	If x and y are vectors, this is a dot product. If both are matrices, it's a matrix-matrix multiplication. If only one is a matrix, then it's vector matrix multiplication.


SECONDMAIN.PY
X	Input dataset matrix where each row is a training example
y	Output dataset matrix where each row is a training example
l0	First Layer of the Network, specified by the input data
l1	Second Layer of the Network, otherwise known as the hidden layer
l2	Final Layer of the Network, which is our hypothesis, and should approximate the correct answer as we train.
syn0	First layer of weights, Synapse 0, connecting l0 to l1.
syn1	Second layer of weights, Synapse 1 connecting l1 to l2.
l2_error	This is the amount that the neural network "missed".
l2_delta	This is the error of the network scaled by the confidence. It's almost identical to the error except that very confident errors are muted.
l1_error	Weighting l2_delta by the weights in syn1, we can calculate the error in the middle/hidden layer.
l1_delta	This is the l1 error of the network scaled by the confidence. Again, it's almost identical to the l1_error except that confident errors are muted.