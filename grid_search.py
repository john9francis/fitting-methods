# Class that performs grid search to find the minimum parameters
import numpy as np
from matplotlib import pyplot as plt

class GridSearch():
  def __init__(self) -> None:
    self.mu1 = 102.1
    self.mu2 = 177.9
    self.gamma1 = 30
    self.gamma2 = 20
    self.a1 = 1826
    self.a2 = 2812

    # since these are pretty good guesses, we will
    # have a small step size
    self.d_a1 = 1
    self.d_a2 = 1

    self.x_data = np.array([i for i in range(50, 241, 10)])
    self.y_data = np.array([
      5, 7, 11, 13, 21, 43, 30, 16, 15, 10,
      13, 42, 90, 75, 29, 13, 8, 4, 6, 3
    ])

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

    return chi_squared



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



