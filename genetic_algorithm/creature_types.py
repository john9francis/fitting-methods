# A derived creature with a normal distribution
# each creature must implement the "fit_function" method
# it's recommended that the creature redefine the "save_filename",
# and for any initial parameter guesses, they can either put the initial
# guesses in the save file or in their own implementation of "set_random_params."

import numpy as np

from creature import Creature

class GammaArctanCreature(Creature):

  save_filename = "save_files/gamma_arctan_best_params.txt"

  def fit_function(self, _x: np.ndarray) -> np.ndarray:
    a = self.param_list[0]
    b = self.param_list[1]
    c = self.param_list[2]
    d = self.param_list[3]
    e = self.param_list[4]
    f = self.param_list[5]
    g = self.param_list[6]

    # Add a small epsilon value to x to avoid division by zero
    epsilon = 1e-10
    x = _x + epsilon

    return a * x ** (b - 1) * np.exp( -x / c) + d * np.arctan(e * x + f) + g

  

class LorentzianCreature(Creature):

  save_filename = "save_files/lorentzian_best_params.txt"

  def fit_function(self, x: np.ndarray) -> np.ndarray:
    pass



class NormalCreature(Creature):

  save_filename = "save_files/normal_best_params.txt"


  def fit_function(self, _x:np.ndarray) -> np.ndarray:
    a = self.param_list[0]
    b = self.param_list[1]
    c = self.param_list[2]
    d = self.param_list[3]

    # Add a small epsilon value to x to avoid division by zero
    epsilon = 1e-10
    x = _x + epsilon

    return a * np.exp(-.5*(x/c-b/c)**2) + d
  

  def set_random_params(self, min, max):
    # initial guesses.
    # Note: 
    # param list 0 is a scaling factor
    # param list 1 is the mean
    # param list 2 is the standard deviation
    # param list 3 is the + constant at the end
    self.param_list[0] = 20000
    self.param_list[1] = 512
    self.param_list[2] = 1
    self.param_list[3] = 1
    pass