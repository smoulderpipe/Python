import numpy as np

#You decide to invest in a series of billboards along interstate 10 to advertise your stylish new chicken restaurant, "Chic-fil-A".
#You buy three billboards evenly spaced starting on mile market 17 and ending on mile marker 28.
#Then you buy another three billboards evenly spaced starting on mile marker 32 and ending on mile marker 36.
#In order, from mile marker 17 to 36, your billboards display these ads: A, B, C, C, B, A.
#Determine how far each "C" ad is from your restaurant which is located at mile marker 30.

bbs_content = np.array(['A', 'B', 'C', 'C', 'B', 'A'])

restaurant_position = 30

bbs_positions = np.array([
    np.linspace(17,28,3),
    np.linspace(32,36,3)
])

print(f"Billboards content: {bbs_content}")
print(f"Billboards positions: {bbs_positions}")
print(f"Each distance between each billboard and the restaurant: {np.abs(bbs_positions - 30)}")
print(f"Each distance between C billboards and the restaurant: {np.abs(bbs_positions - 30)[[0,1], [2,0]]}")