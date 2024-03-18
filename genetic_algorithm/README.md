# Genetic Algorithm Method

# Main Idea:

We have creatures with attributes for the parameters of our function. (e.g.):
```
import random

class Creature:
  def __init__(self):
    self.rand = random.Random()
    self.a = self.rand.uniform(0, 100)
    self.b = self.rand.uniform(0, 100)
    self.mu1 = self.rand.uniform(0, 100)
    self.mu2 = self.rand.uniform(0, 100)
    ...

```

For each creature, we calculate the chi-squared for the function given their parameters and the data. Then we have a creature killer that kills the highest chi-squared creatures.

The surviving creatures are allowed to reproduce. In other words, new creatures are generated inheriting the parameters from the surviving creatures. 

Next, we mutate some creatures. My plan is that half of the creatures mutate by adding or subtracting a value onto one of their parameters. A fourth of them mutate by multiplying or dividing a parameter by a value. This value could be the best chi-squared value of the previous run, that way it gets more and more precise. 

Then, we repeat until the chi-squared is as small as we can get it. 