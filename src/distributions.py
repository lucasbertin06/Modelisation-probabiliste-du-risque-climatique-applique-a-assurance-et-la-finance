from math import exp, factorial 
import random

cumul = 0

def poisson(k, landa) :
    return (landa**k * exp(-landa)) / factorial(k) # P(N = k)
    
def sim_events(landa) :
    u = random.random() # between 0 and 1
    cumul = 0
    k = 0
    
    while True:
        p = poisson(k, lam)
        cumul += p
        
        if u <= cumul:
            return k
        
        k += 1

# now, if we use a range of a certain number and do print(sim_events(landa)) in the range, we will have a "number" of answers to which the avg will be landa (the purpose of itself)

def lognormal()

def cost_sim(mu, sigma) :
     