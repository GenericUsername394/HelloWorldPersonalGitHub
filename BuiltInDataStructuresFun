from dataclasses import replace
import math

# Task 1
points = [13.1, 1.7, 1.8, 7.8, 1.2, 12.9, 10.6, 5.8, 3.0, 9.7, 18.6, 0.5, 7.6, 0.1]
points.sort(reverse = True)
print(points)

# Task 2
# Count
number_count = len(points)
print("There are", str(number_count), "elements")
# Mean
def Average(points):
    return sum(points) / len(points)
Mean = Average(points)
print("The mean is", str(round(Mean, 2)))
# Median
points.sort()
mid = len(points) // 2
median = (points[mid] + points[~mid]) / 2
print("The median is", str(round(median, 2)))
# Min
print("The min is", str(min(points)))
# Max
print("The max is", str(max(points)))

#Task 3
n = int(input("Choose position: "))
v = int(input("Enter new value: "))
points[n] = v
print(str(points))