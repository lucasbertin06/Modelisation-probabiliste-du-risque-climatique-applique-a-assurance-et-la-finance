def VaR(losses, prob = 0.99) : # exemple : if VaR 99% = 1 000 000 means -> in 99% of simulated years, the loss stayed below 1,000,000.
    sorted_losses = sorted(losses) # we are going to search the 1% where we go the worst happens
    in_VaR_index = int(prob * (len(sorted_losses)-1)) # from [0] to [index], we are in the 99% VaR, after this index, we are in the 1% worst case
    return sorted_losses[in_VaR_index] 

def expected_Shortfall(losses, prob = 0.99) :
    # ES is Conditionnal VaR / Tail VaR -> the avg loss in the worst (1 - prob)  % of the year -> ES tells how bad it gets on avg once we cross the threshold
    sorted_losses = sorted(losses)
    es_index = int(prob * (len(sorted_losses)-1))
    tail = sorted_losses[es_index:]

    if not tail : # to avoid ZeroDivisionError for instance
        return sorted_losses[-1]

    return sum(tail) / len(tail) # with this, when we are already in the worst %, we find the avg loss

def ruin_prob(losses, capital) : # this function is to estimate that the capital that we have won't be enough to absorb the losses
    # we will compare the capital to EACH losses, so the capital is for ONE loss
    n_ruin = sum(1 for loss in losses if loss > capital)
    return n_ruin / len(losses)    

def recommended_capital(losses, prob=0.99, margin=0.05) :
    capital = expected_shortfall(losses, prob)
    return capital * (1 + margin) # Now, we estimate the minimum amount to have with the expected Shortfall, and we add 5% of this amount to be sure to have enough, in case of possible variation