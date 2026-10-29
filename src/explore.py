import pandas as pd

df = pd.read_csv('./data/raw/streaming.csv')
f_and_c = df.shape
c_names = df.columns

print(df.head())
print("\n")
print(f"Total de reproducciones registradas: {f_and_c[0]}")
print("\n")
print(f"Total de columnas: {f_and_c[1]}")
for i, col in enumerate(df.columns):
    print(f"{i+1}. {col}")