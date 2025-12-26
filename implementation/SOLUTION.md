# Flatland Space Stations - Solution

[← Back to Problem](./PROBLEM.md) | [← Back to Implementation](../README.md#implementation)

## 🎯 Problem Understanding

Flatland is a country with several cities arranged in a line, each separated by 1 unit of distance. Some cities have space stations, while others don't. The challenge is to find the **maximum distance** between any city and its nearest space station.

**Key Insight**: We need to find the city that is farthest from all space stations, and return that distance.

---

## 🧠 Thought Process

### Initial Approach: Brute Force

My first instinct was to:
1. For each city, calculate the distance to every space station
2. Find the minimum distance for that city
3. Track the maximum of all these minimum distances

This is straightforward but inefficient for large inputs.

### Optimized Approach: Sorted Stations

After analyzing the problem, I realized that:
- Cities at the extremes (0 and n-1) only need to check the nearest station on one side
- Cities between two stations have their nearest station at one of those two positions
- If we sort the stations, we can efficiently find these distances

---

## 📊 Algorithm Breakdown

### Brute Force Solution

```
For each city from 0 to n-1:
    For each space station:
        Calculate distance = |city - station|
    Find minimum distance for this city
Return maximum of all minimum distances
```

**Time Complexity**: O(n × m) where n = number of cities, m = number of stations  
**Space Complexity**: O(n) to store distances

**Implementation**: See [`flatland_solution.py`](./python/flatland_solution.py#L2-L10)

### Optimized Solution

```
1. Sort the array of space stations
2. Calculate distance from first city (0) to first station
3. Calculate distance from last city (n-1) to last station
4. Set max_distance = max of these two values
5. For each pair of consecutive stations:
   - Calculate the gap between them
   - The farthest city in this gap is at the midpoint
   - Distance = gap // 2
   - Update max_distance if this is larger
6. Return max_distance
```

**Time Complexity**: O(m log m) dominated by sorting  
**Space Complexity**: O(1) if sorting in-place, O(m) otherwise

**Implementation**: See [`flatland_solution.py`](./python/flatland_solution.py#L14-L21)

---

## 🔑 Key Insights

1. **Edge Cases Matter**: Cities at positions 0 and n-1 only have stations on one side
2. **Sorting is Powerful**: By sorting stations, we can process gaps between consecutive stations efficiently
3. **Midpoint Logic**: For cities between two stations, the farthest city is at the midpoint of the gap
4. **Integer Division**: Using `//` ensures we get the correct distance for the farthest city in each gap

---

## 📈 Complexity Analysis

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Brute Force | O(n × m) | O(n) | Simple but slow for large inputs |
| Optimized | O(m log m) | O(1) | Much faster, dominated by sorting |

**Why is the optimized approach better?**
- For n = 100,000 and m = 1,000:
  - Brute force: ~100 million operations
  - Optimized: ~10,000 operations (1000 × log 1000)

---

## 💻 Implementation

**Languages**: Python  
**Files**: 
- [flatland_solution.py](./python/flatland_solution.py) - Both implementations
- [test.py](./python/test.py) - Test cases

---

## ✅ Testing

To run the solution:

```bash
cd implementation/Flatland\ Space\ Stations/python
python test.py
```

---

## 📚 What I Learned

1. **Always look for patterns**: Sorting can reveal structure in the problem
2. **Consider edge cases first**: Handling boundaries (first/last cities) simplifies the main logic
3. **Space-time tradeoffs**: The optimized solution trades O(m log m) time for O(1) space
4. **Implementation matters**: Having both brute force and optimized versions helps understand the improvement

---

*Solution implemented on: December 26, 2025*

