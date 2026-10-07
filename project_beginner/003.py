import statistics

def pearson_correlation(x, y):

    return statistics.correlation(x, y)
assets = ['A', 'B', 'C']
returns_data = {
    'A': [0.01, -0.005, 0.02, -0.01],
    'B': [0.008, -0.002, 0.015, -0.008],
    'C': [-0.01, 0.02, -0.015, 0.005]
}

correlation_matrix = {
    (a1, a2): pearson_correlation(returns_data[a1], returns_data[a2])
    for a1 in assets for a2 in assets
    
    
}

for (a1, a2), s in correlation_matrix.items():

    if a1 != a2:
        if s > 0.50:
            print(f"to much correlation {a1} and {a2}: {s:.2f}")
        else:
            print(f"they have good diversification {a1} and {a2}: {s:.2f} ")