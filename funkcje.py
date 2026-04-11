import csv
from itertools import groupby
from functools import reduce

columns = ["Category", "Item", "Calories", "Calories from Fat", "Total Fat", "Saturated Fat", "Cholesterol", "Sodium", "Carbohydrates", "Sugars", "Protein"]

# funkcja wczytująca dane (zamienia csv na json)
def load_data(path):
    """Wczytuje dane z pliku csv, bierze pod uwagę tylko niektóre kolumny, zamienia dane na json"""
    data = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({col: row[col] for col in columns}) # wybiera tylko niektore kolumny
    
    return data

# funkcja sprawdzająca
def has_high_calories(item, threshold=500):
    """Sprawdza czy produkt ma więcej niż 500 kcal"""
    return float(item["Calories"]) > threshold

# funkcja filtrująca
def filter_high_calories(data, threshold=500):
    """Filtruje produkty z kaloriami powyżej 500"""
    return filter(lambda x: has_high_calories(x, threshold), data)

# funkcja sortująca
def sort_by_category(data):
    """Sortuje po kategorii"""
    return sorted(data, key=lambda x: x['Category'])

# funkcja grupująca
def group_by_category(data):
    """Grupuje po kategorii"""
    return groupby(data, key=lambda data: data['Category'])

# funkcja zliczająca
def count_per_category(food_groups):
    """Zlicza elementy w kategoriach"""
    return ((category, sum(1 for _ in items)) for category, items in food_groups)

def compose(*funcs):
    return lambda initial: reduce(lambda acc, f: f(acc), reversed(funcs), initial)

get_stat_calories_in_food = compose(
    count_per_category,
    group_by_category,
    sort_by_category,
    filter_high_calories,
    load_data
)
