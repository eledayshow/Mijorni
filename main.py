import numpy as np
from defs import *

weights = np.load('weights.npy')

test_input = np.array([1, 0, 1, 0, 8, 4, 9, 9, 2])
output_activation = softmax(np.dot(test_input, weights))

print(np.round(output_activation[1]))

m = 0
i = 0
while m < .9:
    code = []
    for e in range(4): code.append(random.randint(0, 1))
    for e in range(4, 9): code.append(random.randint(0, 9))
    m = softmax(np.dot(np.array(code), weights))[1]
    i += 1
print(m, i)
get_img(code)[0].show()