# Dynamic Array

**Category:** Data Structures / Vectors

## Problem
Maintain n sequences. Query 1 x y appends y to seq[(x XOR lastAnswer) % n]. Query 2 x y sets lastAnswer = seq[(x XOR lastAnswer) % n][y % size] and records it.

## Approach
List of lists; each query is one XOR, one modulo and one append or index, so every query is constant time.

## Complexity
| Time | Space |
| --- | --- |
| O(N + Q) | O(N + Q) |

## Run
```bash
python solution.py   # reads input in HackerRank format from stdin
```
