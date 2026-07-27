# We will use a lognormal distribution because this law is : always positive, asymetric, and can simulate an occasionnaly big loss

from risk_model import total_annual_loss

def simulation(risks, years = 1000) :
    # This is now that we the Monte Carlo method to simulate 'total annual loss' -> 1000 times to have a more precise on VaR, expected shortfall...
    losses = []

    for i in range(years) :
        loss = total_annual_loss(risks)
        losses.append(loss)

    return losses