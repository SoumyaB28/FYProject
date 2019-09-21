import numpy as np
import sys
import pandas as pd
mu = 0
sigma = 1
n = 16
nBits = 4#subject to change
least = []
phi = []
alpha = []
beta = []
weightMatrix = []

def challengeGen():
    for i in range(n):
        s = bin(i)[2:].zfill(nBits)
        s = s.replace('1','-1')
        s = s.replace('0','1')
        s = s+'1'
        least.append(s)
        
        
def calPhi(): #11111->11111, 111-11->-1-1-111, 11-111->-1-1111
    for i in range(n):
        s = least[i]
        temp=""
        for j in range(nBits+1):
            if(s[j]=='-'):
                j=j+1
            
            if((s.count('-',j,len(s)))%2==0):
                temp=temp+'1'
            else:
                temp=temp+'-1'
        phi.append(temp)
        
        
def generateW():
    for i in range(n):
        p = L[0][i]
        q = L[3][i]
        r = L[2][i]
        s = L[1][i]
        alpha.append((p-q+r-s)/2)
        beta.append((p-q-r+s)/2)
    weightMatrix.append(alpha[0])
    for i in range(1,n-1,1):
        weightMatrix.append(alpha[i]+beta[i-1])
    weightMatrix.append(beta[n-1])


def matMul():
    
        
                
    
L = np.random.normal(mu,sigma,(4,n))
challengeGen()
calPhi() 
generateW()
matMul()





