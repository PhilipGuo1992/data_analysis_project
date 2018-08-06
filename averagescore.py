import pandas as pd
import numpy
import csv

total_score = 0
total_reTweets = 0
stop_line = 0
previous_line = 0
with open('output.csv', encoding='utf-8') as input_file:
    writer = csv.writer(input_file, lineterminator='\n')
    lines = input_file.readline()
    for row, i in input_file:
        line = lines[i]
        line_next = line[i+1]
        time = row[6]
        total_score = total_score+row[-1]
        total_reTweets = total_reTweets+row[3]+1
        if time != line_next[6]:
            previous_line = stop_line
            stop_line = i
            final_score = total_score/total_reTweets
            total_score = 0
            total_reTweets = 0
            for j in range(previous_line+1, stop_line):
                writer.writerow({'final score': final_score})


input_file.close()