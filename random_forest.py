import numpy as np 
import csv
import pandas as pd 
import string
import sys
 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

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
    return str(time)

def main():
    x = sys.argv[1]
    df = pd.read_csv(x)
    df3 = df.iloc[np.where(df.method.values=='Submission')]
    df3 = df3.copy()
      # mean = df3["time"].mean()
    print df3["time"][0]
    for i in range(0,df3["time"].count()):
        a = df3.iloc[i]["time"]
        temp = convert_seconds(a)
        df3.set_value(i,"time",temp)
  
    print df3["time"][0]
    #cancer = load_breast_cancer()
    #print cancer
  #  X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)

   # forest = RandomForestClassifier(n_estimators=100, random_state=0)
    #forest.fit(X_train,y_train)

    #print ("Accuracy on the training subset: {:.3f}")
   # print (forest.score(X_train, y_train))
   # print ("Accuracy on the test subset: {:.3f}")
   # print (forest.score(X_test, y_test))


		
if __name__ == "__main__":
	main()

#
