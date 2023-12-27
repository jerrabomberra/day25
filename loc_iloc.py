# loc()  label based - need to specify rows and columns based on index/row and column lables

# iloc is inbteger based so need to specify rows and columns by interger postion

import pandas as pd


names = ["L. Messi", "Cristiano Ronaldo", "Neymar Jr", "J. Oblak", "E. Hazard"]
age = [32, 34, 27, 26, 28]
height_cm = [170, 187, 175, 188, 175]
nationality = ["Argentina", "Portugal", "Brazil", "Slovenia", "Belgium"]
club = [
    "Paris Saint-Germain",
    "Manchester United",
    "Paris Saint-Germain",
    "Atlético Madrid",
    "Real Madrid",
]

df = pd.DataFrame(
    index=names,
    data={"age": age, "height_cm": height_cm, "nationality": nationality, "club": club},
)
# get the height of L.Messi
# loc
print(df.loc["L. Messi", "height_cm"])
# iloc
print(df.iloc[0, 1])

print(df)
# # get the height of Cristiano Ronaldo
# # loc
# df.loc["Cristiano Ronaldo", "height_cm"]
# # iloc
# df.iloc[1, 1]

# # get all the data about L.Messi
# # loc
# df.loc["L. Messi", :]
# # iloc
# df.iloc[0, :]

# # get all data about L.Messi and Cristiano Ronaldo
# # loc
# df.loc[["L. Messi", "Cristiano Ronaldo"]]
# # iloc
# df.iloc[[0, 1]]

# # get the height of L.Messi and Cristiano Ronaldo
# df.loc[["L. Messi", "Cristiano Ronaldo"], "height_cm"]

# # get the height of L.Messi and Cristiano Ronaldo
# df.iloc[[0, 1], 1]

# # slice column labels: from age to nationality
# # loc
# players = ['L. Messi', 'Cristiano Ronaldo']
# df.loc[players, 'age':'nationality']

# # iloc
# players = [0, 1]

# df.iloc[players, 0:3] # age:nationality+1
# age	height_cm	nationality
# L. Messi	32	170	Argentina
# Cristiano Ronaldo	34	187	Portugal
# Selecting with conditions
# # one condition: select player with height above 180cm
# # loc
# columns = ['age', 'height_cm', 'club']
# df.loc[df['height_cm']>180, columns]

# # iloc
# columns = [0,1,3]
# df.iloc[list(df['height_cm']>180), columns]
# age	height_cm	club
# Cristiano Ronaldo	34	187	Manchester United
# J. Oblak	26	188	Atlético Madrid
# # multiple conditions: select player with height above 180cm that played in PSG
# # loc
# df.loc[(df['height_cm']>170) & (df['club']=='Paris Saint-Germain'), :]

# # iloc
# df.iloc[list((df['height_cm']>170) & (df['club']=='Paris Saint-Germain')), :]
