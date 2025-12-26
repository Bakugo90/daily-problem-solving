# Brute force implementation of flatland function below.
def flatlandSpaceStations_brute(n, c):
    distance_to_nearest = []

    for citie in range(n):
        distance_to_citie = []
        for space_station in c:
            distance_to_citie.append(abs(citie - space_station))
        distance_to_nearest.append(min(distance_to_citie))
    return max(distance_to_nearest)


# Optimized implementation of flatland below
def flatlandSpaceStations(n, c):
    c.sort()

    max_dist = max(c[0], (n - 1) - c[-1])
    # max des milieux entre stations
    for i in range(1, len(c)):
        max_dist = max(max_dist, (c[i] - c[i - 1]) // 2)
    return max_dist
