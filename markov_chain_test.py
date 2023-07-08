import numpy as np

a = np.zeros((2,2))
b = np.zeros(2)

print("a nd b")
print(a, "shape ", a.shape)
print(b, "shape" , b.shape)



a[0,0]= 0.75
a[0,1]= 0.4
a[1,0]= 0.25
a[1,1]= 0.6



b[0] = 1
b[1] = 0

print("a nd b")
print(a)
print(b)

path_vec = [0] * 5
for i in range(5):
    print("\n\n ")
    print(i)
    multi_mat = np.dot(a,b)
    path_vec[i] = np.argmax(multi_mat)
    print("multi_mat", multi_mat)
    print("shape",multi_mat.shape)
    b=multi_mat

print("path_vec", path_vec)

transpose_multi_mat= multi_mat.transpose()

print(transpose_multi_mat)
print(transpose_multi_mat.shape)