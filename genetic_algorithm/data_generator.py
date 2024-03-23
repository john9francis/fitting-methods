# This class is specifically for reading the "copper data one" file.
# Eventually it should be adjusted to be able to take in any data file 

import pandas as pd
import numpy as np

class DataGenerator():
  def __init__(self) -> None:
      
    df = pd.read_csv("copper data one.csv", header=6)

    energy_col_name = " Energy (keV)"
    counts_col_name = " Counts"

    # zoom in
    start_point = 4900
    end_point = 5300
    zoomed = df[start_point:end_point]
    self.energy = zoomed[energy_col_name]
    self.counts = zoomed[counts_col_name]


  def get_data(self):
    '''Returns a tuple: x_array, y_array'''
    energy_array = np.array(self.energy)
    counts_array = np.array(self.counts)
    return (energy_array, counts_array)

