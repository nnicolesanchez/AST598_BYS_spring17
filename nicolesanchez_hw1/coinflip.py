# Coin flip
# p : probability of getting "heads"
# N : number of coin-flips
# h : number of heads
# M : number of times you ran N coin-flips

# 1. plot histogram of h
# 2. print mean of h
# 3. print variance of h
# 4: What is the name of the probability distribution of heads?
import matplotlib.pyplot as plt
import scipy as sci
import numpy as np
#%matplotlib inline

prob = 0.3
N = 8,16,32,64,128
M = 100

h_array = []
for k in range(0,len(N)):
    for j in range(0,M):
        h = 0
        for i in range(0,N[k]):
            h_mask = np.random.choice(['True','False'],p=[1-prob,prob])
            #print(h_mask)
            if h_mask == 'False':
                h = h + 1
        #print(h)
        h_array.append(h)

    #print(h_array)

    h_mean = np.mean(h_array)
    h_var  = sci.var(h_array)
    
    print('The mean of heads',round(h_mean,3))
    print('The variance of heads',round(h_var,3))
    
    plt.hist(h_array)
    plt.title('Number of tosses = '+str(N[k]))
    plt.ylabel('Number of Occurences in M(N flips)')
    plt.xlabel('Occurences of "heads" per N flips')
    plt.savefig('h_hist'+str(N[k])+'.ps')
    plt.show()
