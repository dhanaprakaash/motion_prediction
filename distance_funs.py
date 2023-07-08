import math

""" The file contains many different distance functions """

def euclidean_distance (A, B):
    distance = math.dist(A, B)
    return distance

def manhatten_distance (A,B):
    distance =  abs( round(A[0])-round(B[0])) + abs (round(A[1])-round(B[1]))
    return distance

if __name__ == "__main__":
    a = (1,3)
    b = [(7,6),(7,5),(7,4),(8,6),(8,5),(8,4),(6,6),(6,5),(6,4)]

    s1 = (5, 15)
    s2 = (8,8)

    print(manhatten_distance(s1, s2))
    
    for i in range(len(b)):
        print(a,b[i], euclidean_distance(a,b[i]), manhatten_distance(a,b[i]))
