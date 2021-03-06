from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib

import csv
import random as rd

def makeKaggleSubmition():
    clf = joblib.load('newral_networks/newral_network_probably_under_fitted.pkl')

    # Open the file with the registers
    with open("../../data/matrixtestsummarytextshin2.csv", "r") as csvfile, open("../../data/kaggle_shingle.csv", "w") as kaggle:
        firstValue = True
        for row in csv.reader(csvfile):
            if firstValue:
                firstValue = False
                kaggle.write("Id,Prediction\n")
                continue

            registerId = row[0]

            register = [[float(x) for x in row[1::]]]
            prediction = int(clf.predict(register))

            kaggle.write("{},{}\n".format(registerId, prediction))

def crossValidateWithTest():
    clf = joblib.load('newral_networks/newral_network_without_weight' + '.pkl')

    correctPredictions = 0
    totalPredictions = 0
    # Open the file with the register
    with open("../../data/matrixtrainsummarytext.csv", "r") as csvfile:
        firstValue = True

        for row in csv.reader(csvfile):
            if rd.randrange(10) != 5:
                continue
            if firstValue:
                firstValue = False
                continue

            registerId = row[0]
            correctPrediction = int(row[1])
            register = [[float(x) for x in row[2::]]]
            prediction = int(clf.predict(register))

            correctPredictions += correctPrediction == prediction
            totalPredictions += 1

    print "Net ID " + str(x) + "Correct prediction", correctPredictions, "total predictions", totalPredictions, "ratio", float(correctPredictions)/totalPredictions
    print clf

def main():
    makeKaggleSubmition()
    # crossValidateWithTest()
    return 0

if __name__ == "__main__":
    main()
