myFile = open('input.txt', 'r', encoding='utf-8-sig')                                                       # Opens text file for reading
lines = myFile.readlines()                                                                                  # Reads all lines from the text file into a variable
myFile.close()                                                                                              # Closes opened text file to free up resources
myOutput = open('output.txt', 'w', encoding='utf-8-sig')                                                    # Creates text file for writing 

import math

for item in lines:                                                                                          # Starts for loop to run through the lines variable
    if item.find("min:") != -1:                                                                             # Starts if loop to identify text and execute if true
        minList = item.strip('[').replace(':', ',').split(',')                                              # Reads variable to list and modifies the list
        minStat = minList.pop(0)                                                                            # Removes the first item in the list and saves it to a variable
        minLineINT = [int(l[0]) for l in minList]                                                           # Casts list items to integer and saves to variable
        minStr = ''.join(map(str, minList)).strip()                                                         # Joins integers to a single string
        minInt = int(min(minStr))                                                                           # Calculates minimum value within string
        myOutput.write ("The " + str(minStat) + " of " + str(minLineINT) + " is " + str(minInt) + "\n")     # Writes variable data to text file
        
    elif item.find("max:") != -1:                                                                           # Starts if loop to identify text and execute if true
        maxList = item.strip('[').replace(':', ',').split(',')                                              # Reads variable to list and modifies the list
        maxStat = maxList.pop(0)                                                                            # Removes the first item in the list and saves it to a variable
        maxLineINT = [int(l[0]) for l in maxList]                                                           # Casts list items to integer and saves to variable
        maxStr = ''.join(map(str, maxList)).strip()                                                         # Joins integers to a single string
        maxInt = int(max(maxStr))                                                                           # Calculates maximum value within string
        myOutput.write ("The " + str(maxStat) + " of " + str(maxLineINT) + " is " + str(maxInt) + "\n")     # Writes variable data to text file

    elif item.find("avg:") != -1:                                                                           # Starts if loop to identify text and execute if true
        avgList = item.strip('[').replace(':', ',').split(',')                                              # Reads variable to list and modifies the list
        avgStat = avgList.pop(0)                                                                            # Removes the first item in the list and saves it to a variable
        avgLineINT = [int(l[0]) for l in avgList]                                                           # Casts list items to integer and saves to variable
        avgStr = ''.join(map(str, avgList)).strip()                                                         # Joins integers to a single string
        avg = sum(avgLineINT) / float(len(avgLineINT))                                                      # Calculates the average value within string    
        myOutput.write ("The " + str(avgStat) + " of " + str(avgLineINT) + " is " + str(avg) + "\n")        # Writes variable data to text file

    elif item.find("sum:") != -1:                                                                           # Starts if loop to identify text and execute if true
        sumList = item.strip('[').replace(':', ',').split(',')                                              # Reads variable to list and modifies the list
        sumStat = sumList.pop(0)                                                                            # Removes the first item in the list and saves it to a variable
        sumLineINT = [int(l[0]) for l in sumList]                                                           # Casts list items to integer and saves to variable
        sumStr = ''.join(map(str, sumList)).strip()                                                         # Joins integers to a single string
        sum = sum(sumLineINT)                                                                               # Calculates the sum value within string    
        myOutput.write ("The " + str(sumStat) + " of " + str(sumLineINT) + " is " + str(sum) + "\n")        # Writes variable data to text file

    elif item.find("p") != -1:                                                                              # Starts if loop to identify text and execute if true
        pList = item.strip().strip('[').replace(':', ',').split(',')                                        # Reads variable to list and modifies the list
        pStat = pList.pop(0)                                                                                # Removes the first item in the list and saves it to a variable
        pNum = pStat.strip("p")                                                                             # Removed the first letter in the string and saves result to a variable
        pStr = ''.join(map(str, pList)).strip()                                                             # Joins integers to a single string                               
        pPer = int(pNum) / 100                                                                              # Creates percentile from integer
        
        def percentile(N, P):                                                                               # Defines a function to read in a list of data and a percentile 
            n = max(int(round(P * len(N) + 0.5)), 2)                                                        # calculates the percentile of all list items
            return N[n-2]                                                                                   # returns percentile value

        pX = percentile(pList, pPer)                                                                        # calls function
        
        myOutput.write ("The " + str(pNum) + "th percentile of " + str(pList) + " is " + str(pX) + "\n")   # Writes variable data to text file
        
    else:                                                                                                   # Else if loop fails, prints
        print ("Something went wrong! Please try again.")   

myOutput.close()                                                                                            # Closes opened text file to free up resource
