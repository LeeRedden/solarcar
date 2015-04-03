# -*- coding: utf-8 -*-
"""
A script that uses a genetic algorithm to find the
best distribution of solar cells on a solar car. 
This example is a bit of a toy problem, but shows how
clustering over time would work. 

Lee Redden
April 2, 2015

"""

import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

def profits( profit, assignment, numClasses ):
    cash = 0
    for i in xrange(numClasses):
        if sum(assignment==i) == 0:
            print "zero assignment" 
            return 0
        else:
            cash += min(profit[assignment==i]) * sum(assignment==i)
    return cash
    

def main():
    numClasses = 10
    
    numExamples = 100
    np.random.seed(1)

    profit = np.random.rand(numExamples,1)
    assignment =  np.floor(np.random.rand(numExamples)*numClasses)

    numIterations = 100000
    history = np.zeros(numIterations)
    for i in xrange(numIterations):
        newAssignment = deepcopy(assignment)
               
        for j in xrange(5):
            index = int(np.random.rand(1)*numExamples)
            newAssignment[index] = int(np.random.rand(1)*numClasses)
        
        if profits( profit, assignment, numClasses ) < profits( profit, newAssignment, numClasses ):
            assignment = newAssignment
            
        #print str( profits( profit, assignment )) + " at " + str(i)
        history[i] = profits( profit, assignment, numClasses )


    plt.figure()
    plt.plot(history)
    plt.ylabel('some numbers')
    plt.show()
    
    plt.figure()
    for j in xrange(numClasses):
        temp = profit[assignment==j]
        print "values in " + str(j) + " with min " + str(min(temp)) +":"
        print temp
        plt.plot(temp)
    plt.show()
        
if __name__ == "__main__":
    main()
    
    
    