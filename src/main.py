import statistics
 
from climat_risk import HAZARDS
from climatic_scenario import SCENARIOS, apply_scenario
from simulation import simulation
from insurance import VaR, expected_Shortfall, ruin_prob, recommended_capital

def choose_hazard(name) :
    if name == "all" : # if name = all, we run every hazards together, else, only one
        return HAZARDS

    for hazards in HAZARDS :
        if hazards["name"] == name :
            return [hazards]
    
    raise ValueError(f"Unknown hazard {name}")

def choose_scenario(name):
    for scenario in SCENARIOS:
        if scenario["name"] == name:
            return scenario
    
    raise ValueError(f"Unknown scenario: {name}")