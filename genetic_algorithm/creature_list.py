# A list to take care of mutating, deleting, etc. creatures.

from creature_types import Creature
import numpy as np
import random

class CreatureList:
  def __init__(self, 
               how_many_creatures:int, 
               creature_class:Creature, 
               x_data:np.ndarray, 
               y_data:np.ndarray) -> None:
    
    self.type_of_creature = creature_class
    
    self.creature_amount = how_many_creatures
    self.set_random_creatures(how_many_creatures)

    self.x_data = x_data
    self.y_data = y_data

    self.chi_squared_list = []

    self.rand = random.Random()

    # How much to mutate creatures by initially
    self.mutate_rate = 100 

    self.save_filename = creature_class.save_filename


  def set_random_creatures(self, amount):
    '''
    Creates random creatures of whatever type was specified
    '''
    self.creature_list = [self.type_of_creature() for _ in range(amount)]


  def create_chi_sq_list(self):
    '''
    Calcultes chi-squared for each creature and puts it in a list
    '''
    new_chi_sq_list = []

    for c in self.creature_list:
      c.set_data(self.y_data, self.x_data)
      new_chi_sq_list.append(c.get_chi_sq())

    self.chi_squared_list = new_chi_sq_list

  
  def get_best_chi_squared(self):
    return min(self.chi_squared_list)
  
  def get_worst_chi_squared(self):
    return max(self.chi_squared_list)
  
  def get_median_chi_squared(self):
    return np.median(self.chi_squared_list)
  

  def get_best_creature(self):
    '''
    Returns a reference to the creature with the
    lowest chi-squared value.
    '''
    best_val = self.get_best_chi_squared()

    for c in self.creature_list:
      if c.get_chi_sq() == best_val:
        return c
      
    print("Best creature not found..?")


  def kill_creatures(self):
    '''
    Kills the creatures with the worst chi-squareds
    '''
    original_creature_amount = len(self.creature_list)
    
    # reset if the chi-squared is just too darn high
    if self.get_best_chi_squared() > 1000:
      self.creature_list = []
      return
    
    # set a cutoff value and kill all creatures with
    # a chi-squared greater than this cutoff
    cutoff = self.get_best_chi_squared() + 1

    i = 0
    while i < len(self.creature_list):
      if self.creature_list[i].calculate_chi_squared() >= cutoff:
        self.creature_list.pop(i)
        # print("Removed a creature!")
      else:
        i += 1


    final_creature_amount = len(self.creature_list)


    # if no creatures were killed, it means they all had very similar
    # chi-squared values. so we kill a few off to make room for 
    # some new mutated ones.
    if final_creature_amount == original_creature_amount:
      for i in range(len(self.creature_list ) // 10):
        if self.creature_list[i] != self.get_best_creature():
          self.creature_list.pop(i)



  def repopulate_creatures(self):
    '''
    creates new creatures for the creature_list until it's 
    length is back up to the self.creature_amount
    '''

    # if the list is empty, populate it with random creatures
    if len(self.creature_list) == 0:
      self.set_random_creatures(self.creature_amount)
      return

    new_creature_amount = self.creature_amount - len(self.creature_list)
    new_creatures = []

    for _ in range(new_creature_amount):
      # get params from an existing creature
      params = self.rand.choice(self.creature_list).get_params()

      c = self.type_of_creature(params)
      c.mutate(self.rand.uniform(0, self.mutate_rate))
      new_creatures.append(c)

    # add the new creatures in with the old
    self.creature_list.extend(new_creatures)


  def load_best_params(self):
    '''
    Takes the params saved to the save file and adds
    10 creatures with these best params to the creature_list.
    '''
    try:
      params_array = np.loadtxt(self.save_filename)
    except FileNotFoundError:
      print("File not found. Generating random creatures.")
      return
    
    params_list = list(params_array)
    self.creature_list = [self.type_of_creature(params_list) for _ in range(10)]



  def save_best_params(self):
    '''
    Gets the best creature's parameters and saves them
    to a file.
    '''
    with open(self.save_filename, "w") as file:
      for i in self.get_best_creature().get_params():
        file.write(str(i) + '\n')



  def run(self, how_many_times:int):
    '''
    Does run(s) of killing, repopulating, and mutating creatures
    '''

    # start off loading from a file:
    self.load_best_params()

    # display our initial best chi_squared
    self.create_chi_sq_list()
    print(f"Starting chi-squared: {self.get_best_chi_squared()}")

    # counter variable
    how_many_same_chis = 0

    for _ in range(how_many_times):

      old_chi_squared = self.get_best_chi_squared()

      self.kill_creatures()
      self.repopulate_creatures()
      self.create_chi_sq_list()

      new_chi_squared = self.get_best_chi_squared()

      # adjust the mutation rate if the best chi-squared isn't improving
      if new_chi_squared == old_chi_squared:
        how_many_same_chis += 1

      if how_many_same_chis > 10:
        how_many_same_chis = 0
        self.mutate_rate *= .8

      # print statement so we know how it's progressing.
      print(f"Best creature's chi squared: {self.get_best_chi_squared()}")

    print(f"Final chi-squared: {self.get_best_chi_squared()}")

    # save the best one
    self.save_best_params()

    # print and plot the best one
    self.get_best_creature().plot_fit()

    
    

