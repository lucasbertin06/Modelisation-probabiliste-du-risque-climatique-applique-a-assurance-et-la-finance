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
    
    raise ValueError(f"Unknown hazard : {name}")

def choose_scenario(name):
    for scenario in SCENARIOS:
        if scenario["name"] == name:
            return scenario
    
    raise ValueError(f"Unknown scenario : {name}")

def apply_scenario_all(risks, scenario) :
    for risk in risks :
        return [apply_scenario(risk, scenario)]

def run(hazard_name, scenario_name, years, capital):
    risks = choose_hazard(hazard_name)
    scenario = choose_scenario(scenario_name)
    adjusted_risks = apply_scenario_to_all(risks, scenario)
 
    losses = simulation(adjusted_risks, years=years)
 
    avg_loss = statistics.mean(losses)
    variance = statistics.variance(losses)
    var_99 = VaR(losses, 0.99)
    es_99 = expected_Shortfall(losses, 0.99)
    ruin = ruin_prob(losses, capital)
    capital_reco = recommended_capital(losses, 0.99)
 
    print(f"Hazard(s): {hazard_name}")
    print(f"Scenario: {scenario['name']}")
    print(f"Simulated years: {years}")
    print(f"Average loss: {avg_loss :.2f}")
    print(f"Variance: {variance :.2f}")
    print(f"VaR 99%: {var_99 :.2f}")
    print(f"Expected Shortfall 99%: {es_99 :.2f}")
    print(f"Ruin probability (capital={capital}): {ruin :.4f}")
    print(f"Recommended capital: {capital_reco :.2f}")
    print()
 
    return losses
 
 
def compare_scenarios(hazard_name="all", years=1000, capital=100000):
    # README asks the user to compare different scenarios against each other
    for scenario in SCENARIOS:
        run(hazard_name = hazard_name, scenario_name = scenario["name"], years = years, capital = capital)
 
 
def ask_hazard():
    choices = ["all"] + [hazard["name"] for hazard in HAZARDS]
    print("Available hazards:", ", ".join(choices))
    answer = input("Choose a hazard: ").strip()
    return answer
 
 
def ask_scenario():
    choices = [scenario["name"] for scenario in SCENARIOS]
    print("Available scenarios:", ", ".join(choices))
    answer = input("Choose a scenario: ").strip()
    return answer
 
 
def ask_years():
    answer = input("Number of years to simulate: ").strip()
    return int(answer)
 
 
def ask_capital():
    answer = input("Available capital: ").strip()
    return float(answer)
 
 
if __name__ == "__main__":
    hazard_name = ask_hazard()
    scenario_name = ask_scenario()
    years = ask_years()
    capital = ask_capital()
    run(hazard_name, scenario_name, years, capital)