import os
import sys

input_path = sys.argv[1]
input_path = os.path.abspath(input_path)

if not os.path.isdir(input_path):
    print("DIRECOTRY NOT FOUND")
    sys.exit()

print("PROJECT DIRECTORY LOADED: ", input_path)
