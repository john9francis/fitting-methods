# A list to take care of mutating, deleting, etc. creatures.

from creature import Creature
import numpy as np
import random

class CreatureList:
  def __init__(self, how_many_creatures:int, data:np.ndarray) -> None:
    self.creature_amount = how_many_creatures
    self.creature_list = [Creature() for _ in range(self.creature_amount)]

    self.data = data

    self.chi_squared_list = []

    self.rand = random.Random()
  


  def create_chi_sq_list(self):
    '''
    Calcultes chi-squared for each creature and puts it in a list
    '''
    new_chi_sq_list = []

    for c in self.creature_list:
      c.set_data(self.data)
      new_chi_sq_list.append(c.get_chi_sq())

    self.chi_squared_list = new_chi_sq_list

  
  def get_best_chi_squared(self):
    return min(self.chi_squared_list)
  
  def get_worst_chi_squared(self):
    return max(self.chi_squared_list)

  def kill_creatures(self):
    '''
    Kills 2/3 of the creatures with the worst chi-squareds
    '''
    original_creature_amount = len(self.creature_list)

    cutoff = .1 * self.get_worst_chi_squared()

    i = 0
    while i < len(self.creature_list):
      if self.creature_list[i].calculate_chi_squared() > cutoff:
        self.creature_list.pop(i)
        print("Removed a creature!")
      else:
        i += 1

    final_creature_amount = len(self.creature_list)
    # if final_creature_amount != original_creature_amount:
    #   print(f"{original_creature_amount - final_creature_amount} creatures were killed, with a survival rate of {final_creature_amount/original_creature_amount}%.")


  def repopulate_creatures(self):
    '''
    make the creature list go back up to the self.creature_amount
    '''
    new_creature_amount = self.creature_amount - len(self.creature_list)
    new_creatures = []

    for i in range(new_creature_amount):
      # get params from an existing creature
      params = self.rand.choice(self.creature_list).get_params()

      c = Creature(params)
      c.mutate(100)
      new_creatures.append(c)

    self.creature_list.extend(new_creatures)


  def run(self, how_many_times:int):
    '''
    Does one single run of killing, repopulating, and mutating creatures
    '''
    self.create_chi_sq_list()
    print(f"Starting chi-squared: {self.get_best_chi_squared()}")
    for _ in range(how_many_times):
      self.kill_creatures()
      self.repopulate_creatures()
      self.create_chi_sq_list()

    print(f"Final chi-squared: {self.get_best_chi_squared()}")

