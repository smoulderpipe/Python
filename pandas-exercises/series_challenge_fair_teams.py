import numpy as np
import pandas as pd

coaches = pd.Series(["Aaron", "Donald", "Joshua", "Peter", "Scott", "Stephen"], dtype="string")
players = pd.Series(["Asher", "Connor", "Elizabeth", "Emily", "Ethan", "Hannah", "Isabella", "Isaiah",
                     "James", "Joshua", "Julian", "Layla", "Leo", "Madison", "Mia", "Oliver", "Ryan", "Scarlett",
                     "William", "Wyatt"], dtype="string")

# Determine randomly and fairly the teams, assigning players to coaches.
# Keep in mind that some teams will have 3 players and some teams will have 4 players.
# Given a Series of coaches and a series of players, create a Series of random coach-to-player mappings.
# The resulting Series should have coach names in its index and player names in its values.


# generator = np.random.default_rng(20)
# players_shuffled = players.sample(frac=1, random_state=generator)
# assignments = np.repeat(coaches, [4, 4, 3, 3, 3, 3])
# players_assigned = pd.Series(
#     data = players_shuffled.values,
#     index = assignments
# )
# print(players_assigned)

#Or (more flexible)

coaches = coaches.sample(frac=1, random_state=2357)
players = players.sample(frac=1, random_state=7532)
repeats = np.ceil(len(players) / len(coaches)).astype('int64')
coaches_repeated = pd.concat([coaches] * repeats).head(len(players))
result = players.copy()
result.index = pd.Index(coaches_repeated, name="coach")
print(result)
