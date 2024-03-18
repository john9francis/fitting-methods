from creature import Creature
from creature_list import CreatureList
import numpy as np
from matplotlib import pyplot as plt

def main():
  # get data
  data = [.1,1.,2.,3.,2.,5.,2.,2.,2.,1.,.1]

  # get a creature and test the fit
  cl = CreatureList(100, data)
  cl.run(300)


if __name__ == "__main__":
  main()