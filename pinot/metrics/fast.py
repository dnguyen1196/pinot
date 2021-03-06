""" Slow metrics.

"""

# =============================================================================
# IMPORTS
# =============================================================================
import pinot
import torch
import math


# =============================================================================
# MODULE FUNCTIONS
# =============================================================================
def mse(y, y_hat):
    return torch.nn.functional.mse_loss(
            y,
            y_hat)

def mae(y, y_hat):
    return torch.nn.L1Loss()(y, y_hat)



