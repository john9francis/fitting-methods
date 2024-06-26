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
    
class Lorentz_Normal_Arctan_Creature(Creature):

  save_filename = "save_files/lorentz_normal_arctan.txt"

  def fit_function(self, x: np.ndarray) -> tuple[np.ndarray, int]:
    # 13 params
    p = self.param_list

    n = 12

    norm = p[0] * np.exp(- .5 * (x / p[2] - p[1] / p[2])**2)
    lorentz = (p[3] / np.pi) * (.5 * p[4]) / ((x - p[5]) ** 2 + (.5 * p[4]) ** 2)       
    arctan = p[6] * np.arctan(p[7] * x + p[8])

    return (p[9] * norm + p[10] * lorentz + arctan + p[11], n)

  def set_initial_guesses(self):
    '''
    Function: j * a * N(mean=b, sd=c) + k * d * Lorentzian(alpha=e, x0=f) + g * arctan(hx + i) + L
    '''
    # normal stuff,
    # scale, mean, sd
    self.param_list[0] = 20000
    self.param_list[1] = 512
    self.param_list[2] = 1

    # lorentz stuff,
    # scale, alpha, x0
    self.param_list[3] = 90000
    self.param_list[4] = 3
    self.param_list[5] = 511

    # arctan stuff,
    # scale, x_factor, added value
    self.param_list[6] = -40
    self.param_list[7] = 1
    self.param_list[8] = -511

    # scales and + c
    self.param_list[9] = .5
    self.param_list[10] = .5
    self.param_list[11] = 210
    
    

    
class LorentzianArctanCreature(Creature):
  
  # put the filename where you want to save the best parameters
  save_filename = "save_files/lorentzian_arctan.txt"
  
  # required: implement this fit function
  def fit_function(self, x: np.ndarray) -> np.ndarray:
    a = self.param_list[0]
    b = self.param_list[1]
    c = self.param_list[2]
    d = self.param_list[3]
    e = self.param_list[4]
    f = self.param_list[5]
    g = self.param_list[6]
  
    # write function
    my_function = (c * (1 / np.pi) * (.5 * a) / ((x - b) ** 2 + (.5 * a) ** 2) 
                   + d * np.arctan(e * x + f) + g)
    n_parameters = 7

    # return (function, how many params)
    return (my_function, n_parameters)
  
  def set_initial_guesses(self):
    # Set your initial guesses here:
    self.param_list[0] = 3
    self.param_list[1] = 511
    self.param_list[2] = 90000

    # d * np.arctan(e * x + f) + g 
    self.param_list[3] = -40
    self.param_list[4] = 1
    self.param_list[5] = -511
    self.param_list[6] = 210



class LorentzianCreature(Creature):
  
  # put the filename where you want to save the best parameters
  save_filename = "save_files/lorentzian.txt"
  
  # required: implement this fit function
  def fit_function(self, x: np.ndarray) -> np.ndarray:
    a = self.param_list[0]
    b = self.param_list[1]
    c = self.param_list[2]
  
    # write function
    my_function = c * (1 / np.pi) * (.5 * a) / ((x - b) ** 2 + (.5 * a) ** 2)
    n_parameters = 3

    # return (function, how many params)
    return (my_function, n_parameters)
  
  def set_initial_guesses(self):
    # Set your initial guesses here:
    self.param_list[0] = 3
    self.param_list[1] = 511
    self.param_list[2] = 90000


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
    
    # for the background
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