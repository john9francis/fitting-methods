import random
import copy
import numpy as np
from matplotlib import pyplot as plt

class Creature:
  '''
  A creature holds parameters for a fit function.
  this creature can hold up to 7 parameters.
  '''

  save_filename = "save_files/base_creature_save_file.txt"

  def __init__(self, param_list:list = []) -> None:

    self.rand = random.Random()

    # parameters
    self.n_params = 13
    self.param_list = [0 for _ in range(self.n_params)]

    # Degrees of freedom = n_data points - n_params
    self.degrees_of_freedom = 0

    # Either set the params or set them to be random
    if len(param_list) == 0:
      self.set_random_params(min=0, max=300)
    else:
      self.param_list = param_list


    # initialize the arrays for data
    self.x_data = np.array([])
    self.y_data = np.array([])
    self.y_uncertainties = np.array([])
    # Assuming the x_uncertainties are much less than y_uncertainties.
    self.y_fit = np.array([])

    self.chi_sq = 0


  def set_initial_guesses(self):
    '''
    For the child classes to implement. This function gets 
    automatically called if there are no initial guesses in a file.
    The way to write this function is as follows:
  
    self.param_list[0] = <guess1>
    self.param_list[1] = <guess2>
    ...
    '''
    return None


  def set_random_params(self, min, max):
    for i in range(len(self.param_list)):
      self.param_list[i] = self.rand.uniform(min, max)

    # set any guesses that 
    self.set_initial_guesses()



  def set_params(self, param_list):
    '''
    Takes in array:
    [a,b,c,d,e,f,g]
    and sets this creature's params to them
    '''
    self.param_list = copy.deepcopy(param_list)


  def get_params(self):
    '''
    returns a copy of the parameters
    '''
    return copy.deepcopy(self.param_list)
  

  def mutate(self):
    '''
    Adds to or subtracts from a random parameter following a normal
    distribution N(0,5)
    '''
    
    change_amount = np.random.normal(0, 5)
    indx_to_change = np.random.randint(0, len(self.param_list) - 1)

    # mutate
    self.param_list[indx_to_change] += change_amount
  


  def legacy___mutate(self, amount:float, indx_to_change=-1):
    '''
    Takes in an amount for how much to mutate a param, then
    changes one random param by either + or - that amount.

    Optional index to change variable, so we can mutate a
    specific parameter instead of a random one.
    '''

    if indx_to_change < 0:
      indx_to_change = self.rand.randint(0, len(self.param_list) - 1)
    param_to_change = self.param_list[indx_to_change]

    # get a 0 or 1 to decide if we're adding or subtracting
    t_or_f = self.rand.randint(0, 1)

    # Very small chance of a crazy huge mutation
    if self.rand.uniform(0, 1) > .7:
      amount += self.rand.uniform(0, 10000)

    if t_or_f == 0:
      param_to_change += amount
    else:
      param_to_change -= amount
      
    # finally, mutate the parameter
    self.param_list[indx_to_change] = param_to_change



  def set_data(self, y_data:np.ndarray, x_data:np.ndarray = np.array([])):
    '''
    Sets y and x data to the creature. This function also calculates the 
    fit function and chi-squared for the function and the data
    '''
    if x_data.size == 0:
      x_data = np.arange(0, len(y_data), 1.)
    self.x_data = x_data
    self.y_data = y_data

    self.y_uncertainties = np.sqrt(y_data)
    self.y_fit, self.n_params = self.fit_function(x_data)

    self.degrees_of_freedom = len(y_data) - self.n_params

    self.chi_sq = self.calculate_chi_squared()



  def get_chi_sq(self):
    # make sure the data has been set
    if self.y_data.size == 0:
      raise AttributeError("Data has not yet been set to this creature, so the chi-squared can not be calculated!")
    
    return self.chi_sq



  def fit_function(self, x:np.ndarray) -> tuple[np.ndarray, int]:
    '''
    Each child creature class must provide a fit function for x.
    This takes in an array for x values and returns a tuple:
    (array for the y fit, int for how many parameters used.)
    '''
    raise NotImplementedError("The base creature has no fit function. Please use a derived creature that has a valid fit function.")
    
  

  def calculate_chi_squared(self):
    chi_sq = 0.
    for i in range(len(self.x_data)):
      chi_sq += (self.y_data[i] - self.y_fit[i]) ** 2 / (self.y_uncertainties[i] ** 2)

    return chi_sq / self.degrees_of_freedom

  

  def plot_fit(self):

    plt.style.use('seaborn-v0_8-bright')
    plt.plot(self.x_data, self.y_data, label="Original Data")
    plt.plot(self.x_data, self.y_fit, label="Fit")
    plt.xlabel("Energy KeV")
    plt.ylabel("Counts")
    plt.title("Curve fit")
    plt.legend()

    print(f"The chi-squared value of this fit is: {self.chi_sq}.")
    print("Parameters:")
    print(f"a: {self.param_list[0]}")
    print(f"b: {self.param_list[1]}")
    print(f"c: {self.param_list[2]}")
    print(f"d: {self.param_list[3]}")
    print(f"e: {self.param_list[4]}")
    print(f"f: {self.param_list[5]}")
    print(f"g: {self.param_list[6]}")

    plt.show()
