# We will use this .py to create differents level of severity of thr event

CURRENT = {
    "name" : "Current climate",
    "frequency" : 1,
    "severity" : 1
}

MODERATE = {
    "name" : "Moderate warning",
    "frequency" : 1.3,
    "severity" : 1.25
}

EXTREME = {
    "name" : "Extreme warning",
    "frequency" : 1.8,
    "severity" : 1.6
}

SCENARIOS = [CURRENT, MODERATE, EXTREME]

def apply_scenario(risk, scenario):
    new_risk = risk.copy() # we copy the dictionnary
    new_risk["frequency"] *= scenario["frequency"] # then multiply by the frequency and severity from above
    new_risk["avg_cost"] *= scenario["severity"]

    return new_risk