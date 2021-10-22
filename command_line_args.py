# python program to demonstrate command line arguments
import sys
# total arguments
n = len(sys.argv)
print("Total arguments passed: ", n)
# arguments passed
print("\nName of Python script:", sys.argv[0])
print("\nArguments passed:", end=" ")
for i in range(1, n):
    print(sys.argv[i], end=" ")
# Addition of numbers
sum = 0
# using argparse module
for i in range(1, n):
    sum = int(sys.argv[i])
print("\n\nResult:", sum)
