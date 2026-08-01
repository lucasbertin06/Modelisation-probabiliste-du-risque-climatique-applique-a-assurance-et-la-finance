FLOOD = {
    "name" : "flood",
    "frequence" : 4,
    "avg_cost" : 10000,
    "sigma" : 0.4
}

FIRE = {
    "name" : "fire",
    "frequence" : 3,
    "avg_cost" : 30000,
    "sigma" : 0.65
}

STORM = {
    "name" : "storm",
    "frequence" : 1,
    "avg_cost" : 50000,
    "sigma" : 0.8
}

HAZARDS = [FLOOD, FIRE, STORM]

# frequence = avg numbers of events per year = lambda in Poisson law
# avg cost = avg cost of one event = use of lognormal distrib
# sigma = volatility of the cost (high sigma = variable cost +++)