import numpy as np
import time

def PageRank(m, epsilon, beta=1):
    '''
    Discription:
        Power iteration method to solve the rank vector r
    Param:
        m: stochastic matrix M
        epsilon: Iteration termination condition. By default, epsilon = 0
        beta: Random teleports coefficient. By default, epsilon = 1
    Return:
        Vector r with stable distribution
    '''
    flag = True

    # Initialize A
    mTeleport = np.full(m.shape, 1/m.shape[0])
    a = beta * m + (1 -beta) * mTeleport

    # Initialize r0
    rt = np.array([1/a.shape[0]] * a.shape[0]).reshape((a.shape[0],1))
    rt1 = rt

    while(flag):
        
        rt1 = np.matmul(a, rt)
        print("-------------------------------------------")
        print("Iterating ===> rt1 = ", str(rt1.reshape((1,3))) + "\n")

        delta = np.mean(np.abs(rt - rt1))
        print("Delta = ", delta)
        if delta <= epsilon:
            flag = False
        else:
            rt = rt1
            
    print("-------------------------------------------")
    return rt1

if __name__ == "__main__":

    # Define stochastic matrix M
    m = np.array([[1/2, 1/2, 0],[1/2, 0, 0],[0, 1/2, 1]])

    # Run PageRank
    rStable = PageRank(m, epsilon=1e-16, beta=0.8)