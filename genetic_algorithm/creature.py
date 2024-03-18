import random
import numpy as np

class Creature:
  def __init__(self) -> None:

    self.rand = random.Random()

    pass


  def fit_function(self):
    '''
    The fit function is a gamma multiplied by an arctan.
    '''
    return np.pi