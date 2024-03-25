# Creatures derived from the base "creature" class
#
# each creature must implement the "fit_function" method
# it's recommended that the creature redefine the "save_filename",
# and for any initial parameter guesses, they can either put the initial
# guesses in the save file or in their own implementation of "set_initial_guesses."
# NOTE: Creatures have a maximum of 7 parameters.

import numpy as np

from creature import Creature

# ======================================================
# Create your own creature:
# ======================================================

class MyCreature(Creature):
  
  # put the filename where you want to save the best parameters
  save_filename = "myfunction.txt"


  # required: implement this fit function
  def fit_function(self, x):
    a = self.param_list[0]
    b = self.param_list[1]
    c = self.param_list[2]
    d = self.param_list[3]
    e = self.param_list[4]
    f = self.param_list[5]
    g = self.param_list[6]

    # write function
    my_function = a * x + b
    n_parameters = 2

    # return (function, how many params)
    return (my_function, n_parameters)
  

  def set_initial_guesses(self):
    # Set your initial guesses here:
    self.param_list[0] = 20000
    self.param_list[1] = 512
    self.param_list[2] = 1


  # now, go to main.py and after CreatureList(... put in ctypes.MyCreature
# =====================================================================


class NormalArctanCreature(Creature):

  save_filename = "save_files/normal_arctan_best_params.txt"

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

    return (a * np.exp(-.5*(x/c-b/c)**2) + d * np.arctan(e * x + f) + g , 7)
  

  
  def set_initial_guesses(self):
    # initial guesses.
    # Note: 
    # param list 0 is a scaling factor for the normal
    # param list 1 is the mean
    # param list 2 is the standard deviation
    self.param_list[0] = 20000
    self.param_list[1] = 512
    self.param_list[2] = 1
    
    # for the gamma
    # d * np.arctan(e * x + f) + g 
    self.param_list[3] = -40
    self.param_list[4] = 1
    self.param_list[5] = -511
    self.param_list[6] = 210

    pass




class GammaArctanCreature(Creature):

  save_filename = "save_files/gamma_arctan_best_params.txt"

  def fit_function(self, _x: np.ndarray) -> np.ndarray:
    a = self.param_list[0]

    # since I know the mean is 511 = alpha * beta:
    alpha = self.param_list[1]
    beta = 511 / alpha
    #beta = self.param_list[2]
    d = self.param_list[3]
    e = self.param_list[4]
    f = self.param_list[5]
    g = self.param_list[6]

    # Add a small epsilon value to x to avoid division by zero
    epsilon = 1e-10
    x = _x + epsilon

    return (a * x ** (alpha - 1) * np.exp( -x / beta) + d * np.arctan(e * x + f) + g, 7)
  
  # TODO: implement the initial guesses

  

class LorentzianCreature(Creature):

  save_filename = "save_files/lorentzian_best_params.txt"

  def fit_function(self, x: np.ndarray) -> tuple[np.ndarray, int]:
    # to be implemented
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

    return (a * np.exp(-.5*(x/c-b/c)**2) + d, 4)


  def set_initial_guesses(self):
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