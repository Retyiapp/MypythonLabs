import csv
import json
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
def task() -> None:
    lines = [line for line in csv.DictReader(open(INPUT_FILENAME))]
    json.dump( lines, open(OUTPUT_FILENAME, "w") , indent=4)
task()
for i in open(OUTPUT_FILENAME):
    print(i,end = "")