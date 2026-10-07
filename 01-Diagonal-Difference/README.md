# Diagonal Difference

**Category:** 2D Arrays / Matrices

## Problem
Given an n x n matrix, return the absolute difference between the sums of its two diagonals.

## Approach
Single pass over i: add arr[i][i] to the primary sum and arr[i][n-1-i] to the secondary sum, then take abs of the difference.

## Complexity
| Time | Space |
| --- | --- |
| O(N) | O(1) |

## Run
```bash
python solution.py   # reads input in HackerRank format from stdin
```
