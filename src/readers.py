# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

# taken from https://web.stanford.edu/~hastie/ElemStatLearn/datasets/ozone.data

import csv

FNAME = './assets/ozone.data'

with open(FNAME, 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:        
        print(row['radiation'], row['temperature'])

from pandas import read_csv
df = read_csv(FNAME, sep='\t')
print(df.head())
