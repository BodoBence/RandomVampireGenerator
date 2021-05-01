
import csv
from csv import reader
import random

with open('derengements_curated.csv') as chosen_file:
    reader = csv.reader(chosen_file)
    chosen_row = random.choice(list(reader))

print(chosen_row)

# # open file in read mode
# with open('Derengements.csv', 'r') as read_obj:
#     # pass the file object to reader() to get the reader object
#     csv_reader = reader(read_obj)
#     # Iterate over each row in the csv using reader object
#     for row in csv_reader:
#         # row variable is a list that represents a row in csv
#         print(row)
