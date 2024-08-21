import pandas as pd

# Read in the csv with pandas
df = pd.read_csv(r".\raw_data\(updatedAugust21)powerdata-August21(Victor).csv").to_numpy()
y = df[:, 0]
dS = df[:, 2]

print(y)
print(dS)