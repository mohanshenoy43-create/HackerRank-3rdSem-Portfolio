# Sparse Arrays

**Category:** Hash Maps / Strings

## Problem
For each query string, report how many times it appears in the list of input strings.

## Approach
Build a frequency map (Counter) once, then answer each query with a dictionary lookup instead of rescanning the list, which avoids O(N x Q).

## Complexity
| Time | Space |
| --- | --- |
| O(N + Q) | O(N) |

## Run
```bash
python solution.py   # reads input in HackerRank format from stdin
```
