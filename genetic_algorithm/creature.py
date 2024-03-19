import random
import copy
import numpy as np
from matplotlib import pyplot as plt

class Creature:
  def __init__(self, param_list:list = []) -> None:

    self.rand = random.Random()

    # parameters
    # (a - g) is of length 7
    self.param_list = [0, 0, 0, 0, 0, 0, 0]

    if len(param_list) == 0:
      self.set_random_params(-10, 10)
    else:
      self.param_list = param_list


    self.x_data = np.array([])
    self.y_data = np.array([])
    self.y_uncertainties = np.array([])
    # Assuming the x_uncertainties are much less than y_uncertainties.
    self.y_fit = np.array([])

    self.chi_sq = 0


  def set_random_params(self, min, max):
    for i in range(len(self.param_list)):
      self.param_list[i] = self.rand.uniform(min, max)


  def set_params(self, param_list):
    '''
    Takes in array:
    [a,b,c,d,e,f,g]
    and sets this creature's params to them
    '''
    for i in range(len(self.param_list)):
      self.param_list[i] = param_list[i]


  def get_params(self):
    '''
    returns a copy of the parameters
    '''
    return copy.deepcopy(self.param_list)
  


  def mutate(self, amount:float):
    '''
    Takes in an amount for how much to mutate a param, then
    changes one random param by either + or - that amount.
    '''
    indx_to_change = self.rand.randint(0, len(self.param_list) - 1)
    param_to_change = self.param_list[indx_to_change]

    t_or_f = self.rand.randint(0, 1)

    if t_or_f == 0:
      param_to_change += amount
    else:
      param_to_change -= amount
      
    self.param_list[indx_to_change] = param_to_change




  def set_data(self, y_data:np.ndarray, x_data:np.ndarray = np.array([])):
    if x_data.size == 0:
      x_data = np.arange(0, len(y_data), 1.)
    self.x_data = x_data
    self.y_data = y_data

    self.y_uncertainties = np.sqrt(y_data)
    self.y_fit = self.fit_function(x_data)

    self.chi_sq = self.calculate_chi_squared()

  def get_chi_sq(self):
    return self.chi_sq


  def fit_function(self, x:np.ndarray) -> np.ndarray:
    '''
    Takes in an array of x_values
    The fit function is a gamma added to an arctan:
    f(x) = a * x^(b-1)*exp(-x/c) + d*arctan(e*x+f) + g
    Returns an array of the fit values
    '''
    a = self.param_list[0]
    b = self.param_list[1]
    if b == 1:
      b = 1.1
    c = self.param_list[2]
    if c == 0:
      c = .1
    d = self.param_list[3]
    e = self.param_list[4]
    f = self.param_list[5]
    g = self.param_list[6]

    # Add a small epsilon value to x to avoid division by zero
    epsilon = 1e-10
    x += epsilon


    fit = a * x ** (b - 1) * np.exp( -x / c) + d * np.arctan(e * x + f) + g
    # for testing purposes, I will first fit it to only a gamma
    # fit = a * x ** (b - 1) * np.exp(-x / c)
    
    return fit
  

  def calculate_chi_squared(self):
    chi_sq = 0.
    for i in range(len(self.x_data)):
      chi_sq += (self.y_data[i] - self.y_fit[i]) ** 2 / (self.y_uncertainties[i] ** 2)

    return chi_sq
  

  def plot_fit(self):
    plt.plot(self.x_data, self.y_data, label="original data")
    plt.plot(self.x_data, self.y_fit, label="fit")
    plt.title("Curve fit")
    plt.legend()

    print(f"The chi-squared value of this fit is: {self.chi_sq}.")

    plt.show()