# Class that performs grid search to find the minimum parameters
import numpy as np

class GridSearch():
  def __init__(self) -> None:
    self.mu1 = 102.1
    self.mu2 = 177.9
    self.gamma1 = 30
    self.gamma2 = 20
    self.a1 = 6000
    self.a2 = 60000

    # since these are pretty good guesses, we will
    # have a small step size
    self.d_a1 = 1
    self.d_a2 = 1

    self.x_data = np.array([i for i in range(50, 241, 10)])
    self.y_data = np.array([
      5, 7, 11, 13, 21, 43, 30, 16, 15, 10,
      13, 42, 90, 75, 29, 13, 8, 4, 6, 3
    ])


  def fit_function(self):
    return 
  
  def calc_chi_squared(self):
    return 

