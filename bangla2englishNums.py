# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:18:08 2020

@author: Acer
"""

############### BENGALI TO ENGLISH NUMBER CONVERTER ##################
"""
This function takes in a list of integers in the Bengali language and returns a list 
containing the numbers in the english number system.


"""

######################################################################

def bengali_to_english(numList):
    bengaliNums= ["১", "২", "৩", "৪", "৫", "৬", "৭", "৮", "৯", "০"]
    engNums= ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    convertedNums=[]
    for j in numList:
        englishNum=''
        for a in j:
            if a in bengaliNums:
                i=bengaliNums.index(a)
                englishNum+=''.join(engNums[i])
        convertedNums.append(int(englishNum))
    return convertedNums


def main():
    exampleList=["১২২", "২৩", "৩২", "৪৬", "৫", "৬", "৭৬৬৬৮৯০", "০৮০", "৯৮৯", "০"]
    convertedList=bengali_to_english(exampleList)
    print(convertedList) ##This prints the converted list consisting of the translations of the numbers from the example list##
    
if __name__=="__main__":
    main()
    