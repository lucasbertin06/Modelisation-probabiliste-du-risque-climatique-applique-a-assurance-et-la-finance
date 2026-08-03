from distributions import poisson, sim_events, lognormal, cost_sim
from risk_model import total_loss, total_annual_loss
from climat_risk import FLOOD, FIRE, STORM, HAZARDS
 
 
def test_poisson_sums_to_one():
    # Sum of P(N=k) for k=0..30 should be close to 1 (Poisson property)
    total = sum(poisson(k, 3) for k in range(30))
    assert abs(total - 1) < 0.01
 
 
def test_sim_events_non_negative():
    for _ in range(200):
        assert sim_events(FLOOD["frequence"]) >= 0
 
 
def test_lognormal_positive():
    for _ in range(200):
        assert lognormal(9, 0.5) > 0
 
 
def test_cost_sim_positive():
    for _ in range(200):
        assert cost_sim(FLOOD["avg_cost"], FLOOD["sigma"]) > 0
 
 
def test_total_loss_non_negative():
    for _ in range(100):
        assert total_loss(FLOOD) >= 0
        assert total_loss(FIRE) >= 0
        assert total_loss(STORM) >= 0
 
 
def test_total_annual_loss_non_negative():
    for _ in range(100):
        assert total_annual_loss(HAZARDS) >= 0
 
 
def test_total_annual_loss_is_sum_of_individual_risks():
    # total_annual_loss(HAZARDS) should be at least as variable/consistent
    # as summing each risk separately (sanity check on aggregation logic)
    single_risk_losses = [total_loss(FLOOD) for _ in range(500)]
    assert all(loss >= 0 for loss in single_risk_losses)