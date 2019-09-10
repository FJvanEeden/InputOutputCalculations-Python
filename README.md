# InputOutputCalculations-Python
A program to read data from an input file that reads a string and execute calculations based on a marker found in the first part of the String and the number set following the marker.

Calculation types and markers used:

min: (To calculate the mininmum number in the set)
max: (To calculate the maximum number in the set)
avg: (To calculate the average number in the set)
pX: (Where x is a number from 10 to 90 and defines the x percentile of the number set)

Example input:

min:1,2,3,5,6
max:1,2,3,5,6
avg:1,2,3,5,6
p90:1,2,3,4,5,6,7,8,9,10
sum:1,2,3,5,6
min:1,5,6,14,24
max:2,3,9
p70:1,2,3

Example output:

The min of [1, 2, 3, 5, 6] is 1
The max of [1, 2, 3, 5, 6] is 6
The avg of [1, 2, 3, 5, 6] is 3.4
The 90th percentile of ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] is 9
The sum of [1, 2, 3, 5, 6] is 17
The min of [1, 5, 6, 1, 2] is 1
The max of [2, 3, 9] is 9
The 70th percentile of ['1', '2', '3'] is 2
