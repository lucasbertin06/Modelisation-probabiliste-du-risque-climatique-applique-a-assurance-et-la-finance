from climat_risk import HAZARDS, FLOOD
from climatic_scenario import SCENARIOS, apply_scenario
from simulation import simulation
from insurance import VaR, expected_Shortfall, ruin_prob, recommended_capital
 
 
def test_simulation_length():
    losses = simulation(HAZARDS, years=200)
    assert len(losses) == 200
 
 
def test_simulation_non_negative():
    losses = simulation(HAZARDS, years=200)
    assert all(loss >= 0 for loss in losses)
 
 
def test_apply_scenario_does_not_mutate_original():
    original_frequence = FLOOD["frequence"]
    scenario = SCENARIOS[-1]  # most severe scenario
    apply_scenario(FLOOD, scenario)
    assert FLOOD["frequence"] == original_frequence
 
 
def test_apply_scenario_increases_frequence_and_cost():
    scenario = SCENARIOS[-1]  # most severe scenario
    adjusted = apply_scenario(FLOOD, scenario)
    assert adjusted["frequence"] >= FLOOD["frequence"]
    assert adjusted["avg_cost"] >= FLOOD["avg_cost"]
 
 
def test_severe_scenario_increases_average_loss():
    baseline_scenario = SCENARIOS[0]
    severe_scenario = SCENARIOS[-1]
 
    baseline_risks = [apply_scenario(risk, baseline_scenario) for risk in HAZARDS]
    severe_risks = [apply_scenario(risk, severe_scenario) for risk in HAZARDS]
 
    baseline_losses = simulation(baseline_risks, years=2000)
    severe_losses = simulation(severe_risks, years=2000)
 
    avg_baseline = sum(baseline_losses) / len(baseline_losses)
    avg_severe = sum(severe_losses) / len(severe_losses)
 
    assert avg_severe > avg_baseline
 
 
def test_var_less_than_or_equal_expected_shortfall():
    losses = simulation(HAZARDS, years=2000)
    var_99 = VaR(losses, 0.99)
    es_99 = expected_Shortfall(losses, 0.99)
    assert es_99 >= var_99
 
 
def test_ruin_prob_between_0_and_1():
    losses = simulation(HAZARDS, years=2000)
    prob = ruin_prob(losses, capital=100000)
    assert 0 <= prob <= 1
 
 
def test_recommended_capital_above_expected_shortfall():
    # recommended_capital adds a 5% margin on top of Expected Shortfall
    losses = simulation(HAZARDS, years=2000)
    es_99 = expected_Shortfall(losses, 0.99)
    capital_reco = recommended_capital(losses, 0.99)
    assert capital_reco > es_99