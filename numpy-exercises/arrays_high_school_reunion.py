import numpy as np

#With your high school reunion fast approaching, you decide to get in shape and lose some weight.
#You record your weight every day for five weeks starting on a Monday. Given these daily weights, build and array with your average weight per weekend.

daily_weights = 185 - np.arange(5*7)/5
print(daily_weights)

print((daily_weights[5::7] + daily_weights[6::7])/2)
