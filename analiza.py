from math import sqrt
import random

def to_float(x):
    try:
        return float(x)
    except:
        return 0.0


# ---------- 1. średnia kalorii ----------
def avg_calories(data):
    values = [to_float(d["Calories"]) for d in data]
    return sum(values) / len(values) if values else 0


# ---------- 2. średnia kalorii per kategoria ----------
def avg_calories_per_category(data):
    groups = {}

    for d in data:
        cat = d["Category"]
        cal = to_float(d["Calories"])

        groups.setdefault(cat, []).append(cal)

    return [
        (cat, sum(vals) / len(vals))
        for cat, vals in groups.items()
    ]


# ---------- 3. korelacja ----------
def correlation_calories_fat(data):
    x = [to_float(d["Total Fat"]) for d in data]
    y = [to_float(d["Calories"]) for d in data]

    n = len(x)
    if n == 0:
        return 0

    mx = sum(x) / n
    my = sum(y) / n

    num = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    den = sqrt(
        sum((xi - mx) ** 2 for xi in x) *
        sum((yi - my) ** 2 for yi in y)
    )

    return num / den if den else 0


# ---------- 4. regresja ----------
def regression_calories_fat(data):
    x = [to_float(d["Total Fat"]) for d in data]
    y = [to_float(d["Calories"]) for d in data]

    n = len(x)
    if n == 0:
        return {"slope": 0, "intercept": 0}

    mx = sum(x) / n
    my = sum(y) / n

    num = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    den = sum((xi - mx) ** 2 for xi in x)

    slope = num / den if den else 0
    intercept = my - slope * mx

    return {"slope": slope, "intercept": intercept}


# ---------- 5. clustering ----------
def clustering_calories_fat(data, k=3, iterations=10):
    points = [
        (to_float(d["Calories"]), to_float(d["Total Fat"]))
        for d in data
    ]

    if not points:
        return {"centers": [], "clusters": []}

    if len(points) < k:
        k = len(points)

    centers = random.sample(points, k)

    for _ in range(iterations):
        clusters = [[] for _ in range(k)]

        for p in points:
            distances = [
                sqrt((p[0] - c[0]) ** 2 + (p[1] - c[1]) ** 2)
                for c in centers
            ]
            idx = distances.index(min(distances))
            clusters[idx].append(p)

        new_centers = []
        for c in clusters:
            if c:
                new_centers.append((
                    sum(p[0] for p in c) / len(c),
                    sum(p[1] for p in c) / len(c)
                ))
            else:
                new_centers.append(random.choice(points))

        centers = new_centers

    return {"centers": centers, "clusters": clusters}


# ---------- 6. MDS ----------
def mds_projection(data):
    points = [
        (to_float(d["Calories"]), to_float(d["Total Fat"]))
        for d in data
    ]

    if not points:
        return []

    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)

    return [
        {
            "x": p[0] / max_x if max_x else 0,
            "y": p[1] / max_y if max_y else 0
        }
        for p in points
    ]

def analysis(data):
    return {
        "ŚREDNIA KALORII": avg_calories(data),

        "ŚREDNIA KALORII DLA KATEGORII": [
            f"{cat}: {val:.2f}"
            for cat, val in avg_calories_per_category(data)
        ],

        "KORELACJA (zawartość tłuszczu vs kalorie)": correlation_calories_fat(data),

        "REGRESJA LINIOWA": {
            "slope": regression_calories_fat(data)["slope"],
            "intercept": regression_calories_fat(data)["intercept"]
        },

        "CLUSTERING": [
            f"center {i}: {c}"
            for i, c in enumerate(clustering_calories_fat(data)["centers"])
        ],

        "MDS": [
            f"({p['x']:.3f}, {p['y']:.3f})"
            for p in mds_projection(data)[:10]
        ]
    }