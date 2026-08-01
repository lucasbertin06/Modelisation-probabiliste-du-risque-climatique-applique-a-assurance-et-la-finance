from math import exp, factorial, log
import random

def poisson(k, landa) :
    return (landa**k * exp(-landa)) / factorial(k) # P(N = k)
    
def sim_events(landa) :
    u = random.random() # between 0 and 1
    cumul = 0
    k = 0
    
    while True:
        p = poisson(k, landa)
        cumul += p
        
        if u <= cumul:
            return k
        
        k += 1

# now, if we use a range of a certain number and do print(sim_events(landa)) in the range, we will have a "number" of answers to which the avg will be landa (the purpose of itself)

def lognormal(mu, sigma):
    # Draws a cost according to a log-normal distribution (always positive, skewed, can simulate an occasionally very large loss)
    return random.lognormvariate(mu, sigma)
 
 
def cost_sim(mu, sigma):
    mu = log(mu) - sigma**2 / 2 # as we know : E(X) = exp(mu + sigma² / 2)

    return lognormal(mu, sigma) # simulate the cost of a sinister

