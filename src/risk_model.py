from math import log
from distributions import sim_events, cost_sim

# We will use this .py to do a ONE year simulation before doing this for a bigger number

def total_loss(risk) :
    N = sim_events(risk["frequence"])

    total = 0

    for i in range(N) :
        total += cost_sim(risk["avg_cost"], risk["sigma"])

    return total

def total_annual_loss(risks) : # we sum the cost of all hazards
    total = 0

    for risk in risks : # risks would here be HAZARDS from climat_risk.py 
        total += total_loss(risk)

    return total 