import numpy as np 
import csv
import pandas as pd 
import string
import sys
 

# Converts the Time format into seconds with integer values
def convert_seconds(input_time): 
    temp = ""
    temp2 = ""
    switch = False
    for i in range(0,len(input_time)):
        number = 0
         
        if input_time[i] == ":":
            switch = True
        if switch == False and input_time[i] != ":":
            temp = temp + input_time[i]    
        elif switch == True and input_time[i] != ":":
            temp2 = temp2 + input_time[i]
    num1 = int(temp) * 60  # Converts time in minutes to seconds
    num2 = int(temp2)      # time in seconds
    time = num1 + num2

    return time
    

def main():
    x = sys.argv[1]
    df = pd.read_csv(x)
    df3 = df.iloc[np.where(df.method.values=='Submission')]
    df3 = df3.copy()
    sum = 0
      # mean = df3["time"].mean()
    
    for i in range(0,df3["time"].count()):
        a = df3.iloc[i]["time"]
        temp = convert_seconds(a)
        sum = temp + sum
    mean = sum / df3["time"].count()
    print "Mean Submission Time", mean
  #  print df3.time[1200]
   # df4.time = df3.time.astype(np.int64)
  #  mean = df4["time"].mean()
   # print df4
if __name__ == "__main__":
	main()

#
