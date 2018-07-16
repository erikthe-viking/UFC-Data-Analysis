#import numpy as np 
import csv
#import pandas as pd 
import string
import sys
 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer




def main():
	x = sys.argv[1]
	df = pd.read_csv(x)
    df3 = df.iloc[np.where(df.ref.values=='Mark Smith')]
    print df3
 #   cancer = load_breast_cancer()

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
