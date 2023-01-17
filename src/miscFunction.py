import math
Seed = 937162211

def rand(low, high):
    low, high = low or 0, high or 1
    Seed = (16807 * Seed) % 2147483647
    return low + (high - low) * Seed / 2147483647 

def rint(low, high):
    return math.floor(0.5 + rand(low, high))

def rnd(n, nPlaces):
    mult = 10 ^ (nPlaces or 3)
    return math.floor(n * mult + 0.5) / mult


