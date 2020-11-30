# 2.7abcde
import statistics

grades = [9, 7, 7, 10, 3, 9, 6, 6, 2]
print(grades.count(7))
grades[-1] = 4
print(grades)
print(max(grades))
grades.sort()
print(grades)
print(statistics.mean(grades))
print(sum(grades) / len(grades))

