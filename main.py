import pandas as pd
from funkcje import get_stat_calories_in_food, load_data
from analiza import analysis

results = get_stat_calories_in_food("menu.csv")
wynik = [res for res in results]
print(wynik) # w postaci krotki (kategoria, liczba produków powyżej 500kcal)

wynik_df = pd.DataFrame(wynik, columns=['Kategoria', 'Liczba'])
print(wynik_df)

data = load_data("menu.csv")

wynik_analizy = analysis(data)
print("\n=== Analiza ===")
for k, v in analysis(data).items():
    print("\n" + k)
    print(v)