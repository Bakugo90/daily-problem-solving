# Flatland Space Stations

[← Back to Implementation Problems](../README.md#implementation) | [View Solution →](./SOLUTION.md)

## Problem Source

**Platform**: HackerRank  
**Difficulty**: Easy  
**Category**: Implementation  
**Link**: [Flatland Space Stations](https://www.hackerrank.com/challenges/flatland-space-stations/problem)

---

## Problem Description

Flatland is a country with a number of cities, some of which have space stations. Cities are numbered consecutively and each has a road of length 1 connecting it to the next city. It is not a circular route, so the first city doesn't connect with the last city. Determine the maximum distance from any city to its nearest space station.

## Example

`n = 3`
`c = [1]`

There are n = 3  cities and 1 city  has a space station. They occur consecutively along a route. City 0 is 1 - 0 unit away and city 2  is 2 -1  units away. City 1 is 0 units from its nearest space station as one is located there. The maximum distance is 1.

## Function Description

Complete the `flatlandSpaceStations` function in the editor below.

`flatlandSpaceStations` has the following parameter(s):

- `int n`: the number of cities
- `int c[m]`: the indices of cities with a space station

Returns
- int: the maximum distance any city is from a space station

### Input Format

The first line consists of two space-separated integers,  and .
The second line contains  space-separated integers, the indices of each city that has a space-station. These values are unordered and distinct.

### Constraints
- 1 <= n  <= 10 ^ 5
- 1 <= m  <= n
- 
- There will be at least  city with a space station.
- No city has more than one space station.

### Output Format

Sample Input 0

STDIN   Function
-----   --------
`5 2     n = 5, c[] size m = 2`
`0 4     c = [0, 4]`

Sample Output 0
2

### Explanation 0

This sample corresponds to following graphic:

![[Pasted image 20251226081607.png]]

The distance to the nearest space station for each city is listed below:


Sample Input 1

`6 6`
`0 1 2 4 3 5`

Sample Output 1
`0`

Explanation 1

In this sample,  so every city has space station and we print  as our answer.