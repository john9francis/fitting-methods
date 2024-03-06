# Class that performs grid search to find the minimum parameters
import numpy as np
from matplotlib import pyplot as plt
import sympy as sp

###########################################################
# A FEW NOTES ON THIS:
#
# NOTE: Also, I havent quite finished the chi squared 
# calculation in the "self.minimize_chi_squared" function.
# to truly finish, I need to fit the 3 points to a parabola. 
###########################################################



class GridSearch():
  def __init__(self, mu1, mu2, gamma1, gamma2, a1, a2) -> None:
    self.mu1 = mu1
    self.mu2 = mu2
    self.gamma1 = gamma1
    self.gamma2 = gamma2
    self.a1 = a1
    self.a2 = a2

    self.step = .01

    self.x_data = np.array([i for i in range(50, 241, 10)])
    self.y_data = np.array([
      5, 7, 11, 13, 21, 43, 30, 16, 15, 10,
      13, 42, 90, 75, 29, 13, 8, 4, 6, 3
    ])

    self.current_chi_2 = 100
    self.desired_chi_2 = 1
    self.error_chi_2 = .5


  def fit_function(self, xi):

    def L(mu, gamma):
      '''Lorentzian distribution'''
      return (gamma/2) / (np.pi * ((xi - mu) ** 2 + (gamma / 2) ** 2))
    
    return self.a1 * L(self.mu1, self.gamma1) + self.a2 * L(self.mu2, self.gamma2)
  

  def calc_chi_squared(self) -> float:
    '''
    Returns a value of the chi squared test
    based on the y data and the fit function
    '''
    chi_squared = 0

    for i in range(len(self.x_data)):

      yi = self.y_data[i]
      xi = self.x_data[i]

      y_func_i = self.fit_function(xi)
      # assuming uncertainty in y is squareroot of yi
      # then sigma squared is just yi
      chi_squared += (yi - y_func_i)**2 / yi

    return chi_squared # to get reduced chi squared
  

  def get_reduced_chi_sq(self):
    '''
    This system returns chi2/degrees of freedom (14)
    '''
    return self.current_chi_2 / 14
  

  def minimize_chi_squared(self):
    '''
    Goes through all the parameters and finds the
    best combination to get an extremely low chi-squared
    '''
    self.find_optimal_param_value("a1", self.a1)
    self.find_optimal_param_value("a2", self.a2)
    #self.find_optimal_param_value("mu1", self.mu1)
    #self.find_optimal_param_value("mu2", self.mu2)
    #self.find_optimal_param_value("gamma1", self.gamma1)
    #self.find_optimal_param_value("gamma2", self.gamma2)

    
  def find_optimal_param_value(self, parameter_name: str, initial_guess: float):
    '''
    Takes in an initial guess and name of a parameter: e.g.
    "a1" "a2" "mu1" "mu2" "gamma1" "gamma2"
    and finds the optimal value to minimize chi-squared
    '''

    param = initial_guess - 1
    step = self.step

    # initialize our before and after chi_squared variables
    old_chi_sq = None
    new_chi_sq = None

    old_param = None
    new_param = None

    can_break = False

    while True:
      # set which parameter we are changing
      if parameter_name == "a1":
        old_param = self.a1 - step
        self.a1 = param
      if parameter_name == "a2":
        old_param = self.a2 - step
        self.a2 = param
      if parameter_name == "mu1":
        old_param = self.mu1 - step
        self.mu1 = param
      if parameter_name == "mu2":
        old_param = self.mu2 - step
        self.mu2 = param
      if parameter_name == "gamma1":
        old_param = self.gamma1 - step
        self.gamma1 = param
      if parameter_name == "gamma2":
        old_param = self.gamma2 - step
        self.gamma2 = param

      new_param = param + step

      new_chi_sq = self.calc_chi_squared()

      # only break if the values have been set
      if old_param != None and new_param != None and old_chi_sq != None and new_chi_sq != None:
        can_break = True

      if new_chi_sq > self.current_chi_2 and can_break:
        break

      old_chi_sq = self.current_chi_2
      self.current_chi_2 = new_chi_sq
      param = new_param


    # after the loop is done, we use the 3 points:
    # old, current, and new chi squareds, and
    # fit them to a parabola, then find the minimum.
      
    a, b, c = self.fit_points_to_parabola((old_param, old_chi_sq),(param, self.current_chi_2),(new_param, new_chi_sq))
    p, chi = self.find_min_of_parabola(a, b, c)

    # don't forget to set our parameters to their
    # optimal values
    self.set_parameter_to_value(parameter_name, p)
    self.current_chi_2 = chi

    print(f"The optimal value of {parameter_name} is {p} with a chi squared value of: {chi}")
      
  def set_parameter_to_value(self, parameter_name:str, param:float):
    if parameter_name == "a1":
      self.a1 = param
    elif parameter_name == "a2":
      self.a2 = param
    elif parameter_name == "mu1":
      self.mu1 = param
    elif parameter_name == "mu2":
      self.mu2 = param
    elif parameter_name == "gamma1":
      self.gamma1 = param
    elif parameter_name == "gamma2":
      self.gamma2 = param
    else:
      print("Parameter name not recognized in\
            the set_parameter_to_value function")

  def get_parameter_by_name(self, parameter_name) -> float:
    if parameter_name == "a1":
      return self.a1
    elif parameter_name == "a2":
      return self.a2
    elif parameter_name == "mu1":
      return self.mu1
    elif parameter_name == "mu2":
      return self.mu2
    elif parameter_name == "gamma1":
      return self.gamma1
    elif parameter_name == "gamma2":
      return self.gamma2
    else:
      print("Parameter name not recognized in\
            the set_parameter_to_value function")
      return 0.0

  def fit_points_to_parabola(self, point1:tuple, point2:tuple, point3:tuple) -> tuple:
    '''Takes in 3 points (x,y) and fits them to a parabola.
    returns the parameters of an ax^2+bx+c parabola (a,b,c)'''
    # Step 1: put the points into a matrix of the form:
    # x1^2  x1  1  |  y1
    # x2^2  x2  1  |  y2
    # x3^2  x3  1  |  y3

    # first, sort from smallest x to largest
    tuples = sorted([point1, point2, point3])
    x1, y1 = tuples[0]
    x2, y2 = tuples[1]
    x3, y3 = tuples[2]

    matrix = sp.Matrix([
      [x1**2, x1, 1, y1],
      [x2**2, x2, 1, y2],
      [x3**2, x3, 1, y3]])
    
    matrix = matrix.rref()

    # "matrix" variable is a tuple. first entry is the matrix,
    # second entry is a tuple of which columns have pivots.
    # so here I am accessing the matrix, and then the last column 
    # of the matrix. 
    last_column = matrix[0][:, -1]
    a, b, c = tuple(last_column)

    return a,b,c
  

  def find_min_of_parabola(self, a, b, c) -> tuple:
    '''Finds the min x,y of a parabola'''
    min_y = c - b**2 / (4*a)
    min_x = -b / (2 * a)
    return min_x, min_y 




  ################################
  # PLOTS
  ################################

  def plot_data_and_fit(self):
    plt.plot(self.x_data, self.y_data, label="Data")
    plt.plot(self.x_data, self.fit_function(self.x_data), label="fit")
    plt.legend()
    plt.show()
    pass


  def plot_chisq_for_varying_a1(self):
    # save a1 to reset later
    save_a1 = self.a1

    a1_vals = np.linspace(1000, 3000, 200)
    chi_sq = []
    for a1 in a1_vals:
      self.a1 = a1
      chi_sq.append(self.calc_chi_squared())

    plt.plot(a1_vals, chi_sq)
    plt.xlabel("a1 values")
    plt.ylabel("Chi squared")
    plt.show()

    # reset a1
    self.a1 = save_a1


  def plot_chisq_for_varying_mu1(self):
    # save mu1 to reset later
    save_mu1 = self.mu1

    mu1_vals = np.linspace(0, 200, 200)
    chi_sq = []
    for mu1 in mu1_vals:
      self.mu1 = mu1
      chi_sq.append(self.calc_chi_squared())

    plt.plot(mu1_vals, chi_sq)
    plt.xlabel("mu1 values")
    plt.ylabel("Chi squared")
    plt.show()

    # reset mu1
    self.mu1 = save_mu1



