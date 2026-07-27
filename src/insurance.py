def VaR(losses, prob = 0.99) : # exemple : if VaR 99% = 1 000 000 means -> in 99% of simulated years, the loss stayed below 1,000,000.
    sorted_losses = sorted(losses) # we are going to search the 1% where we go the worst happens
    in_VaR_index = int(prob * (len(sorted_losses)-1)) # from [0] to [index], we are in the 99% VaR, after this index, we are in the 1% worst case
    return sorted_losses[index] 

