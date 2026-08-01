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

def total_loss(risk) :
    N = sim_events(risk["frequence"])
    sigma = risk["sigma"]
    mu = mu_from_avg_cost(risk["avg_cost"], sigma)

    total = 0
    for i in range(0, N) :
        total += cost_sim(mu, sigma)

    return total

def total_annual_loss(risks) : # we sum the cost of all hazards
    total = 0

    for risk in risks : # risks would here be HAZARDS from climat_risk.py 
        total += total_loss(risk)

    return total 