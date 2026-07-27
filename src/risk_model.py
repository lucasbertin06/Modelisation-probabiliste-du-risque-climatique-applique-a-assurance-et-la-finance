from math import log
from distributions import sim_events, cost_sim

# We will use this .py to do a ONE year simulation before doing this for a bigger number

def mu_from_avg_cost(avg_cost, sigma):
    """ 
    For a lognormal distribution, E(X) = exp(mu + sigma^2 / 2).
    So mu = ln(avg_cost) - sigma^2 / 2.
 
    This lets us define risks by their intuitive 'average cost' in
    climat_risk.py
    """
    return log(avg_cost) - (sigma ** 2) / 2

def total_loss() :
    N = sim_events(landa)
    loss = 0
    for i in range(0, N) :
        cost = 