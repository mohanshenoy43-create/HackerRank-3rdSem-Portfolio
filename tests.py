"""Sample-case checks for all five solutions. Run: python tests.py"""
import importlib.util
from pathlib import Path


def load(folder):
    spec = importlib.util.spec_from_file_location(folder, Path(__file__).parent / folder / "solution.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


assert load("01-Diagonal-Difference").diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]) == 15

dyn = load("02-Dynamic-Array").dynamicArray
assert dyn(2, [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]) == [7, 3]

tc = load("03-Time-Conversion").timeConversion
assert tc("07:05:45PM") == "19:05:45"
assert tc("12:00:00AM") == "00:00:00"
assert tc("12:45:54PM") == "12:45:54"
assert tc("01:01:01AM") == "01:01:01"

assert load("04-Compare-the-Triplets").compareTriplets([5, 6, 7], [3, 6, 10]) == [1, 1]

assert load("05-Sparse-Arrays").matchingStrings(["aba", "baba", "aba", "xzxb"], ["aba", "xzxb", "ab"]) == [2, 1, 0]

print("All sample tests passed")
