# Time Conversion

**Category:** Strings & Logic

## Problem
Convert a 12-hour AM/PM time to 24-hour format.

## Approach
Take hour % 12 so 12 becomes 0, add 12 for PM, and keep the minutes and seconds slice unchanged. Handles 12:xx:xxAM -> 00 and 12:xx:xxPM -> 12.

## Complexity
| Time | Space |
| --- | --- |
| O(1) | O(1) |

## Run
```bash
python solution.py   # reads input in HackerRank format from stdin
```
